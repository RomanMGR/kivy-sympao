

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

    def show_dialog_device(self):
        self.__view['device_screen'].show_alert_dialog()

    def show_menu(self):
        self.__view['start_screen'].ids.nav_drawer.set_state("open")



