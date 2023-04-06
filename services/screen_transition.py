class ScreenTransitionService():
    def __init__(self, manager_screens):
        self.__models = {}
        self.__manager_screens = manager_screens

    def add_model(self, key, model):
        self.__models[key] = model

    def connect_to_device(self, device, mac, name):
        self.__manager_screens.current = 'device_screen'
        self.__models['device_screen'].start(device, mac, name)