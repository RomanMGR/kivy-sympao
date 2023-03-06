import asyncio
from kivy.uix.screenmanager import ScreenManager
from View.screens import screens
from kivymd.app import MDApp
from asyncio import AbstractEventLoop
from asyncio import Task
from typing import Optional



class LoginAppMVC(MDApp):
    def __init__(self, loop:AbstractEventLoop) -> None:
        super().__init__()
        self._loop: AbstractEventLoop = loop
        self._task: Optional[Task] = None
        self.load_all_kv_files(self.directory)
        self.manager_screens = ScreenManager()

    def build(self) -> ScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self):
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.
        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            print(name_screen)
            self.manager_screens.add_widget(view)

def main():
    loop: AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(LoginAppMVC(loop).async_run(async_lib='asyncio'))
    loop.close()

if __name__ == '__main__':
    main()