import asyncio
from random import sample
from asyncio import Task
from asyncio import AbstractEventLoop
from typing import Optional
from services.export_data import ExportData


class CorsiScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._task2: Optional[Task] = None
        self._task3: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self.active_inversion_flag = False
        self._observers = []
        self.list_sector = []
        self.pressed_btn = []
        self.length = ''
        self.check_list = []
        self.export_data = ExportData()
        self.screen_transition_service = screen_transition_service

    def start_test(self):
        self._task = asyncio.create_task(self.start_test_task())

    async def start_test_task(self):
        for i in range(8):
            print('start show sector')
            self._task3 = asyncio.create_task(self.press_btn_task())
            self._task2 = asyncio.create_task(self.show_sector_task(i+2))
            await asyncio.wait([self._task3])
            await asyncio.sleep(1)
            self.screen_transition_service.show_normal_corsi_active()
            print('end show sector')
        print('check list ',self.check_list)
        self.screen_transition_service.corsi_result(self.check_list, self.active_inversion_flag)
        self.screen_transition_service.save_data_corsi(self.active_inversion_flag)

    async def show_sector_task(self, length):
        self.list_sector = sample([1, 2, 3, 4, 5, 6, 7, 8, 9], length)
        print(self.list_sector)
        self.screen_transition_service.corsi_change_text()
        self.screen_transition_service.show_normal_corsi()
        await asyncio.sleep(0.75)
        for i in self.list_sector:
            self.screen_transition_service.show_sector_corsi(i)
            await asyncio.sleep(1)
            self.screen_transition_service.show_normal_corsi()
            await asyncio.sleep(1)
        self.export_data.react_time_pos(length)
        self.screen_transition_service.corsi_active_btn()
        self.length = length

    def press_btn(self, n):
        self.pressed_btn.append(n)
        self.screen_transition_service.corsi_click_btn(n)
        if self.length == len(self.pressed_btn):
            self._task3.cancel()
            self.screen_transition_service.corsi_inactive_btn()
            if not self.active_inversion_flag:
                if self.pressed_btn == self.list_sector:
                    self.check_list.append(1)
                else:
                    self.check_list.append(0)
            else:
                if self.pressed_btn == self.list_sector[::-1]:
                    self.check_list.append(1)
                else:
                    self.check_list.append(0)
            self.export_data.react_time_corsi(self.pressed_btn, self.list_sector)
            self.pressed_btn = []
            self.notify_observers()

    async def press_btn_task(self):
        while True:
            await asyncio.sleep(1)

    def active_inversion(self):
        if not self.active_inversion_flag:
            self.active_inversion_flag = True
        else:
            self.active_inversion_flag = False

    def cancel(self):
        self._task.cancel()
        self._task2.cancel()
        self._task3.cancel()
        self.screen_transition_service.show_normal_corsi()
        self.screen_transition_service.corsi_inactive_btn()
        self.active_inversion_flag = False
        self.list_sector.clear()
        self.pressed_btn.clear()
        self.length = ''
        self.check_list.clear()
        self.export_data.clear()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
