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
        self.__view["nback_screen"].ids.step.text = '0/20'
        self.__view["nback_screen"].ids.menu_btn.disabled = False
        self.__view["nback_screen"].show_alert_dialog()

    def restart(self):
        self.nback2()
        self.__view["nback_screen"].step = 0
        self.__view["nback_screen"].ids.step.text = '0/20'
        self.__view["nback_screen"].ids.menu_btn.disabled = False

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
        self.__view["nback_screen"].ids.progress.value += 5

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
        self.__view["nback_screen"].ids.step.text = str(self.__view["nback_screen"].step) + '/20'

    def get_uuid(self):
        return self.__view["results_screen"].savedata.get_uuid()

    def result(self):
        result = round(int(self.__view["nback_screen"].total)/self.__models["nback_screen"].result * 100, 2)
        if result >= 0:
            self.__view["nback_screen"].result = result
        else:
            self.__view["nback_screen"].result = 0
        self.__view["results_screen"].savedata.save_data(self.__view["nback_screen"].result, self.__models["nback_screen"].n)
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


