import asyncio
from kivy.uix.button import Button
from typing import Optional
from asyncio import AbstractEventLoop
from asyncio import Task
from View.start_screen.start_screen import StartScreenView
from Model.start_screen_model import StartScreenModel
from Model.DeviceScreenModel import DeviceScreenModel
from kivy.properties import ObjectProperty, ListProperty, ColorProperty, StringProperty

class StartScreenController:
    """
    The `start_screen_controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model) -> None:
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = StartScreenView(controller=self, model=self.model)

    def scan(self)->None:
        self.model.scanm()
        self.view.ids.bts.text = 'SCANNING ...'

    def change_screen(self, name, mac):
        DeviceScreenModel.MAC = mac
        self.view.manager_screens.current = 'device_screen'

    def get_view(self) -> StartScreenView:
        return self.view
