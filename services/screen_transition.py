from kivymd.color_definitions import colors
import random


class ScreenTransitionService():

    def __init__(self, manager_screens):
        self.__models = {}
        self.__view = {}
        self.__manager_screens = manager_screens

    def add_model(self, key, model):
        self.__models[key] = model

    def add_view(self, key, view):
        self.__view[key] = view

    def connect_to_device(self, device, mac, name):
        self.__manager_screens.current = 'device_screen'
        self.__models['device_screen'].start(device, mac, name)

    def start_n(self):
        self.nback2()
        self.__view["nback_screen"].step = 0
        self.__view["nback_screen"].ids.menu_btn.disabled = False
        self.__view["nback_screen"].ids.menu2_btn.disabled = False
        self.__view["nback_screen"].show_alert_dialog()

    def start_corsi(self):
        self.__view["corsi_screen"].show_alert_dialog()

    def restart(self):
        self.nback2()
        self.__view["nback_screen"].step = 0
        self.__view["nback_screen"].ids.menu_btn.disabled = False
        self.__view["nback_screen"].ids.menu2_btn.disabled = False

    def start_results(self):
        self.__view["results_screen"].start()

    def nback1(self, list, i):
        if list[i] == 1:
            self.__view["nback_screen"].ids.bt_1.disabled = False
        elif list[i] == 2:
            self.__view["nback_screen"].ids.bt_2.disabled = False
        elif list[i] == 3:
            self.__view["nback_screen"].ids.bt_3.disabled = False
        elif list[i] == 4:
            self.__view["nback_screen"].ids.bt_4.disabled = False
        elif list[i] == 5:
            self.__view["nback_screen"].ids.bt_5.disabled = False
        elif list[i] == 6:
            self.__view["nback_screen"].ids.bt_6.disabled = False
        elif list[i] == 7:
            self.__view["nback_screen"].ids.bt_7.disabled = False
        elif list[i] == 8:
            self.__view["nback_screen"].ids.bt_8.disabled = False
        elif list[i] == 9:
            self.__view["nback_screen"].ids.bt_9.disabled = False
        self.__view["nback_screen"].ids.progress.value += float(100/self.__models['nback_screen'].len_step)

    def nback2(self):
        self.__view["nback_screen"].ids.bt_1.disabled = True
        self.__view["nback_screen"].ids.bt_2.disabled = True
        self.__view["nback_screen"].ids.bt_3.disabled = True
        self.__view["nback_screen"].ids.bt_4.disabled = True
        self.__view["nback_screen"].ids.bt_5.disabled = True
        self.__view["nback_screen"].ids.bt_6.disabled = True
        self.__view["nback_screen"].ids.bt_7.disabled = True
        self.__view["nback_screen"].ids.bt_8.disabled = True
        self.__view["nback_screen"].ids.bt_9.disabled = True

    def pos_match(self, count):
        self.__view["nback_screen"].total = int(self.__view["nback_screen"].total) + count
        self.__view["nback_screen"].total_pos = int(self.__view["nback_screen"].total_pos) + count

    def sound_match(self, count):
        self.__view["nback_screen"].total = int(self.__view["nback_screen"].total) + count
        self.__view["nback_screen"].total_s = int(self.__view["nback_screen"].total_s) + count

    def show_dialog_device(self):
        self.__view['device_screen'].show_alert_dialog()

    def show_menu(self):
        self.__view['start_screen'].ids.nav_drawer.set_state("open")

    def add_step(self):
        self.__view["nback_screen"].step = int(self.__view["nback_screen"].step) + 1
        self.__view["nback_screen"].ids.menu2_btn.text = str(self.__view["nback_screen"].step) + \
                                                         '/' +str(self.__models['nback_screen'].len_step)

    def get_uuid(self):
        return self.__view["results_screen"].savedata.get_uuid()

    def result(self):
        result = round(int(self.__view["nback_screen"].total)/self.__models["nback_screen"].result * 100, 2)
        if result >= 0:
            self.__view["nback_screen"].result = result
        else:
            self.__view["nback_screen"].result = 0
        self.__view["results_screen"].savedata.save_data('N-back', 'Результат: '+str(self.__view["nback_screen"].result)
                                                         + '%', "n = "+str(self.__models["nback_screen"].n))
        text_result = str("Суммарный: " + str(self.__view["nback_screen"].total) + '/' + str(self.__models["nback_screen"].result) +
                      '\n' + 'Позициональный: ' + str(self.__view["nback_screen"].total_pos) + '/' + str(
                      self.__models["nback_screen"].result_pos) + '\n' + 'Звуковой: ' + str(self.__view["nback_screen"].total_s) +
                      '/' + str(self.__models["nback_screen"].result_s))
        self.__view["nback_screen"].show_result_dialog()
        self.__view["nback_screen"].total = str(0)
        self.__view["nback_screen"].total_pos = str(0)
        self.__view["nback_screen"].total_s = str(0)
        self.__view["nback_screen"].result = 0
        return text_result

    def show_snackbar_nback(self):
        self.__view["nback_screen"].show_snackbar()

    def close_snackbar_nback(self):
        self.__view["nback_screen"].close_snackbar()

    def counter(self, n, current_screen):
        self.__view[current_screen].count += n
        if current_screen == "asthenia_screen":
            self.__view[current_screen].answer_list.append(n)
        print(self.__view[current_screen].count)

    def count_asthenia(self, n, current_screen):
        if len(self.__view[current_screen].answer_list) in (2, 5, 9, 10, 13, 14, 16, 17, 18, 19):
            self.__view[current_screen].count += 6 - n
            self.__view[current_screen].answer_list.append(6 - n)
            print(self.__view[current_screen].answer_list[-1])
        else:
            self.__view[current_screen].count += n
            self.__view[current_screen].answer_list.append(n)
            print(self.__view[current_screen].answer_list[-1])

    def show_sector_corsi(self, i):
        if i == 1:
            self.__view["corsi_screen"].ids.corsi_btn_1.md_bg_color_disabled = 'green'
        elif i == 2:
            self.__view["corsi_screen"].ids.corsi_btn_2.md_bg_color_disabled = 'green'
        elif i == 3:
            self.__view["corsi_screen"].ids.corsi_btn_3.md_bg_color_disabled = 'green'
        elif i == 4:
            self.__view["corsi_screen"].ids.corsi_btn_4.md_bg_color_disabled = 'green'
        elif i == 5:
            self.__view["corsi_screen"].ids.corsi_btn_5.md_bg_color_disabled = 'green'
        elif i == 6:
            self.__view["corsi_screen"].ids.corsi_btn_6.md_bg_color_disabled = 'green'
        elif i == 7:
            self.__view["corsi_screen"].ids.corsi_btn_7.md_bg_color_disabled = 'green'
        elif i == 8:
            self.__view["corsi_screen"].ids.corsi_btn_8.md_bg_color_disabled = 'green'
        elif i == 9:
            self.__view["corsi_screen"].ids.corsi_btn_9.md_bg_color_disabled = 'green'

    def show_normal_corsi(self):
        self.__view["corsi_screen"].ids.corsi_btn_1.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_2.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_3.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_4.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_5.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_6.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_7.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_8.md_bg_color_disabled = colors['Gray']['500']
        self.__view["corsi_screen"].ids.corsi_btn_9.md_bg_color_disabled = colors['Gray']['500']

    def corsi_active_btn(self):
        self.__view["corsi_screen"].ids.corsi_btn_1.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_2.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_3.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_4.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_5.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_6.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_7.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_8.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_9.disabled = False
        self.__view["corsi_screen"].ids.corsi_btn_start.text = 'Ожидание ответа'

    def corsi_inactive_btn(self):
        self.__view["corsi_screen"].ids.corsi_btn_1.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_2.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_3.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_4.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_5.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_6.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_7.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_8.disabled = True
        self.__view["corsi_screen"].ids.corsi_btn_9.disabled = True

    def corsi_click_btn(self, i):
        if i == 1:
            self.__view["corsi_screen"].ids.corsi_btn_1.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_1.disabled = True
        elif i == 2:
            self.__view["corsi_screen"].ids.corsi_btn_2.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_2.disabled = True
        elif i == 3:
            self.__view["corsi_screen"].ids.corsi_btn_3.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_3.disabled = True
        elif i == 4:
            self.__view["corsi_screen"].ids.corsi_btn_4.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_4.disabled = True
        elif i == 5:
            self.__view["corsi_screen"].ids.corsi_btn_5.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_5.disabled = True
        elif i == 6:
            self.__view["corsi_screen"].ids.corsi_btn_6.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_6.disabled = True
        elif i == 7:
            self.__view["corsi_screen"].ids.corsi_btn_7.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_7.disabled = True
        elif i == 8:
            self.__view["corsi_screen"].ids.corsi_btn_8.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_8.disabled = True
        elif i == 9:
            self.__view["corsi_screen"].ids.corsi_btn_9.md_bg_color_disabled = 'red'
            self.__view["corsi_screen"].ids.corsi_btn_9.disabled = True

    def show_normal_corsi_active(self):
        self.__view["corsi_screen"].ids.corsi_btn_1.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_2.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_3.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_4.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_5.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_6.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_7.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_8.md_bg_color = 'blue'
        self.__view["corsi_screen"].ids.corsi_btn_9.md_bg_color = 'blue'

    def corsi_change_text(self):
        self.__view["corsi_screen"].ids.corsi_btn_start.text = 'Показ последовательности'

    def corsi_result(self, check_list, flag):
        for i in range(len(check_list)):
            if check_list[i] == 1:
                self.__view["corsi_screen"].result += str(2+i)+". Верно" + "\n"
            else:
                self.__view["corsi_screen"].result += str(2+i) + ". Неверно" + "\n"
        self.__view["corsi_screen"].show_result_dialog()
        uuid = self.get_uuid()
        self.__models["corsi_screen"].export_data.export_corsi(self.__view["corsi_screen"].result, uuid, flag)
        print('end')

    def scab_start(self, n):
        self.__view["scab_screen"].lbl_txt.text = n

    def scab_add_next(self, n):
        if self.__models["scab_screen"].list_sector[self.__models["scab_screen"].current_element - 1] == n:
            for i in self.__models["scab_screen"].scab_words:
                if i != n:
                    self.__models["scab_screen"].list_sector[self.__models["scab_screen"].current_element] = i
                    print(n, ' change on ', i)
                    n = i
                    break
            self.__models["scab_screen"].scab_words.clear()
            self.__models["scab_screen"].scab_words = random.sample(["Красный", "Желтый", "Синий", "Черный", "Зеленый"],
                                                                    5)
        self.__view["scab_screen"].lbl_txt.text = n
        return n

    def scab_add_next_2(self, n, color):
        n = self.scab_add_next(n)
        if n == 'Красный' and color == 'red' or n == 'Желтый' and color == 'yellow' or \
            n == 'Синий' and color == 'blue' or n == 'Черный' and color == 'black' or n == 'Зеленый' and color == 'green':
            for i in self.__models["scab_screen"].scab_color:
                if i != color:
                    print(color, ' change on ', i)
                    color = i
                    break
            self.__models["scab_screen"].scab_color.clear()
            self.__models["scab_screen"].scab_color = random.sample(['red', 'yellow', 'blue', 'black', 'green'], 5)
        self.__view["scab_screen"].lbl_txt.text_color = color
        self.__models["scab_screen"].color_sector[self.__models["scab_screen"].current_element - 30] = color
        self.__view["scab_screen"].btn_1.md_bg_color = 'white'
        self.__view["scab_screen"].btn_2.md_bg_color = 'white'
        self.__view["scab_screen"].btn_3.md_bg_color = 'white'
        self.__view["scab_screen"].btn_4.md_bg_color = 'white'
        self.__view["scab_screen"].btn_5.md_bg_color = 'white'
        self.__view["scab_screen"].btn_1.text = "Красный"
        self.__view["scab_screen"].btn_2.text = "Желтый"
        self.__view["scab_screen"].btn_3.text = "Синий"
        self.__view["scab_screen"].btn_4.text = "Черный"
        self.__view["scab_screen"].btn_5.text = "Зеленый"



    def calculate_scab(self, all_time, averange_first, averange_second, delta_averange, percent, total_first,
                       total_second, answer):
        self.__view["scab_screen"].result = 'Общее время выполнения теста: ' + str(round(all_time, 2)) + " сек"\
            + "\n" + 'Среднее время ответа в первом этапе: ' + str(round(averange_first, 2)) + " сек" + "\n" \
            + 'Среднее время ответа во втором этапе: ' + str(round(averange_second, 2)) + " сек" + "\n" \
            + 'Среднее время задержки: ' + str(round(delta_averange, 2)) + " сек" + "\n" \
            + 'Процент от среднего времени реакции в первой очереди эксперимента: ' + str(round(percent, 2)) + " %" + "\n" \
            + "Количество ошибок в первой части теста: " + str(30-total_first) + "\n" \
            + "Количество ошибок во второй части теста: " + str(30-total_second)
        self.__view["scab_screen"].show_result_dialog()

    def restart_scab(self):
        self.__view["scab_screen"].restart()

    def save_data_anxiety(self, count, export):
        self.__view["results_screen"].savedata.save_data('Anxiety Scale', "Количество баллов: " + str(count),
                                                         "Комментарий: " + str(export))

    def save_data_asthenia(self, export):
        self.__view["results_screen"].savedata.save_data('Asthenia scale', export)

    def save_data_corsi(self, active_inversion_flag):
        if active_inversion_flag == True:
            active_inversion_flag = 'Да'
        else:
            active_inversion_flag = 'Нет'
        self.__view["results_screen"].savedata.save_data('Corsi', 'Ответы на шагах: '+ '\n' + self.__view["corsi_screen"].result,
                                                         'Обратный порядок шагов: ' + str(active_inversion_flag))

    def save_data_scab(self, all_time, averange_first, averange_second, delta_averange, percent, total_first,
                       total_second, answer):
        self.__view["results_screen"].savedata.save_data('Scab', "Количество ошибок: " + str((30-total_first) +
                                                         (30-total_second)), "Эффект Струпа, сек: " + str(round(delta_averange, 1)))

    def save_data_Beck(self, count, comment):
        self.__view["results_screen"].savedata.save_data('Beck', 'Счет: ' + str(count), comment)




