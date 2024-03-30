import asyncio
import numpy as np
from asyncio import Task
from asyncio import AbstractEventLoop
from typing import Optional
from kivy.core.audio import SoundLoader
from services.export_data import ExportData
from datetime import datetime


class NbackScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.screen_transition_service = screen_transition_service
        self.export_data = ExportData()
        self.n = 1
        self.n_pos_last = '-'
        self.n_pos_cur = ''
        self.n_sound_last = '-'
        self.n_sound_c = ''
        self.Flag = False
        self.Flag_s = False
        self.button = [0, 0]
        self.result = 0
        self.result_pos = 0
        self.result_s = 0
        self.len_step = 20

    def show_menu(self):
        self.screen_transition_service.show_menu()

    def test(self):
        self._task = asyncio.create_task(self.task_test())

    def restart(self):
        self.screen_transition_service.restart()

    async def task_test(self):
        self.result = 0
        self.result_pos = 0
        self.result_s = 0
        self.n_pos_last = '-'
        self.n_pos_cur = ''
        self.n_sound_last = '-'
        self.n_sound_c = ''
        letters_n = np.random.randint(1, 9, self.len_step)
        letters = []
        list_n = np.random.randint(1, 10, self.len_step)
        list_pos = []
        correct_list = np.random.randint(0, 3, self.len_step)
        correct_list2 = np.random.randint(0, 3, self.len_step)
        print(letters_n)
        print(list_n)
        print(correct_list)
        for i in range(len(correct_list)):
            if i >= self.n:
                if correct_list[i] == 0:
                    letters.append(letters_n[i-self.n])
                else:
                    letters.append((letters_n[i]))
                if correct_list2[i] == 0:
                    list_pos.append(list_n[i - self.n])
                else:
                    list_pos.append((list_n[i]))
            else:
                letters.append((letters_n[i]))
                list_pos.append((list_n[i]))
        print(letters)
        print(list_pos)
        for i in range(len(list_n)):
            self.Flag = False
            self.Flag_s = False
            self.screen_transition_service.nback1(list_pos, i)
            self.export_data.time(i)
            if i-self.n >= 0:
                self.n_pos_last = list_pos[i-self.n]
                self.n_sound_last = letters[i-self.n]
            self.n_pos_cur = list_pos[i]
            self.n_sound_c = letters[i]
            self.play_letter(letters[i])
            await asyncio.sleep(0.5)
            self.screen_transition_service.nback2()
            await asyncio.sleep(2.5)
            try:
                self.button[0].disabled = False
            except:
                pass
            try:
                self.button[1].disabled = False
            except:
                pass
            self.total_res()
            self.calculate_miss()
        print(self.result)
        export_n = self.n
        result = self.screen_transition_service.result()
        uuid = self.screen_transition_service.get_uuid()
        self.export_data.diff_time(result, export_n, uuid)

    def total_res(self):
        if self.n_pos_cur == self.n_pos_last:
            self.result += 1
            self.result_pos += 1
        if self.n_sound_c == self.n_sound_last:
            self.result += 1
            self.result_s += 1
        self.screen_transition_service.add_step()

    def calculate_miss(self):
        if not self.Flag:
            if self.n_pos_cur == self.n_pos_last:
                self.export_data.react_time_pos('pos_miss_error')
            else:
                self.export_data.react_time_pos('pos_miss_corr')
        if not self.Flag_s:
            if self.n_sound_c == self.n_sound_last:
                self.export_data.react_time_sound('sound_miss_error')
            else:
                self.export_data.react_time_sound('sound_miss_corr')

    def pos_match(self, btn):
        if self.n_pos_cur == self.n_pos_last:
            count = 1
            self.export_data.react_time_pos('pos-right')
        else:
            count = -1
            self.export_data.react_time_pos('pos-wrong')
        self.Flag = True
        self.button[0] = btn
        self.screen_transition_service.pos_match(count)

    def sound_match(self, btn):
        if self.n_sound_c == self.n_sound_last:
            count = 1
            self.export_data.react_time_sound('sound-right')
        else:
            count = -1
            self.export_data.react_time_sound('sound-wrong')
        self.Flag_s = True
        self.button[1] = btn
        self.screen_transition_service.sound_match(count)

    def play_letter(self, letter):
        if letter == 1:
            SoundLoader.load('music/c.wav').play()
        if letter == 2:
            SoundLoader.load('music/h.wav').play()
        if letter == 3:
            SoundLoader.load('music/k.wav').play()
        if letter == 4:
            SoundLoader.load('music/l.wav').play()
        if letter == 5:
            SoundLoader.load('music/q.wav').play()
        if letter == 6:
            SoundLoader.load('music/r.wav').play()
        if letter == 7:
            SoundLoader.load('music/s.wav').play()
        if letter == 8:
            SoundLoader.load('music/t.wav').play()

    def cancel(self):
        self._task.cancel()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
