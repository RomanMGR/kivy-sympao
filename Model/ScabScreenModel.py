from random import sample
from asyncio import Task
from typing import Optional
from asyncio import AbstractEventLoop
from datetime import datetime
from Model.data import scab_result
from services.export_data import ExportData


class ScabScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.export_data = ExportData()
        self.screen_transition_service = screen_transition_service
        self.list_sector, self.color_sector = [], []
        self.current_element = 0
        self.total_first = 30
        self.total_second = 30
        self.scab_color = ['red', 'yellow', 'blue', 'black', 'green']
        self.scab_words = ["Красный", "Желтый", "Синий", "Черный", "Зеленый"]
        self.scab_words_2 = {"Красный": 'red', "Желтый": 'yellow', "Синий": 'blue', "Черный": 'black', "Зеленый": 'green'}
        self.time = []

    def start(self):
        self.list_sector = sample(12*["Красный", "Желтый", "Синий", "Черный", "Зеленый"], 60)
        self.color_sector = sample(6 * ['red', 'yellow', 'blue', 'black', 'green'], 30)
        self.screen_transition_service.scab_start(self.list_sector[0])
        self.time.append(datetime.now())
        self.export_data.react_time_pos('start')
        # print(self.list_sector_2)

    def press_btn(self, n):
        answer = 1
        if self.current_element < 29:
            if n != self.list_sector[self.current_element]:
                self.total_first -= 1
                answer = -1
            print('check pos = ', self.current_element, '-----', 'total = ', self.total_first)
            self.current_element += 1
            self.screen_transition_service.scab_add_next(self.list_sector[self.current_element])
        elif self.current_element < 59:
            if self.current_element == 29:
                self.time.append(datetime.now())
                if n != self.list_sector[self.current_element]:
                    self.total_first -= 1
                    answer = -1
            elif self.scab_words_2[n] != self.color_sector[self.current_element - 30]:
                self.total_second -= 1
                answer = -1
            print('check pos = ', self.current_element, '-----', 'total = ', self.total_second)
            self.current_element += 1
            self.screen_transition_service.scab_add_next_2(self.list_sector[self.current_element],
                                                           self.color_sector[self.current_element - 30])
        else:
            if self.scab_words_2[n] != self.color_sector[self.current_element - 30]:
                self.total_second -= 1
                answer = -1
            self.export_data.react_time_pos(answer)
            self.show_result()
        self.export_data.react_time_pos(answer)
        self.notify_observers()

    def show_result(self):
        answer = ''
        self.time.append(datetime.now())
        time_first_part = self.time[1].timestamp() - self.time[0].timestamp()
        time_second_part = self.time[2].timestamp() - self.time[1].timestamp()
        all_time = time_second_part + time_first_part
        averange_first = time_first_part/30
        averange_second = time_second_part/30
        delta_averange = averange_second - averange_first
        percent = (delta_averange/averange_first)*100
        if percent > 100:
            answer = scab_result[0]
        elif percent > 80:
            answer = scab_result[1]
        elif percent > 50:
            answer = scab_result[2]
        elif percent > 20:
            answer = scab_result[3]
        else:
            answer = scab_result[4]
        uuid = self.screen_transition_service.get_uuid()
        self.screen_transition_service.calculate_scab(all_time, averange_first, averange_second, delta_averange,
                                                      percent, self.total_first, self.total_second, answer)
        self.screen_transition_service.save_data_scab(all_time, averange_first, averange_second, delta_averange,
                                                      percent, self.total_first, self.total_second, answer)
        self.export_data.send_scab(all_time, averange_first, averange_second, delta_averange,
                                   percent, self.total_first, self.total_second, answer, uuid)
        self.screen_transition_service.restart_scab()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)