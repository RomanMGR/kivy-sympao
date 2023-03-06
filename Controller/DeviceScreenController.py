import asyncio
from kivy.uix.button import Button
from typing import Optional
from asyncio import AbstractEventLoop
from asyncio import Task
from View.device_screen.device_screen import DeviceScreenView
from Model.DeviceScreenModel import DeviceScreenModel


class DeviceScreenController:
    """
    The `start_screen_controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model) -> None:
        self.model = model
        self.view = DeviceScreenView(controller=self, model=self.model)

    def get_view(self) -> DeviceScreenView:
        return self.view