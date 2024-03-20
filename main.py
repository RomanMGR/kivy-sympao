from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from View.screens import screens
from kivymd.app import MDApp
from asyncio import AbstractEventLoop
from asyncio import get_event_loop
from asyncio import Task
from typing import Optional
from services.screen_transition import ScreenTransitionService


class LoginAppMVC(MDApp):
    def __init__(self, loop:AbstractEventLoop) -> None:
        super().__init__()
        self._loop: AbstractEventLoop = loop
        self._task: Optional[Task] = None
        self.load_all_kv_files(self.directory)
        self.manager_screens = ScreenManager()
        Window.bind(on_keyboard=self.android_back_click)

    def build(self) -> ScreenManager:
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        self.generate_application_screens()
        return self.manager_screens

    def android_back_click(self, window, key, *largs):
        if key == 27:
            self.manager_screens.current = 'start_screen'
            return True

    def generate_application_screens(self):
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.
        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """
        s = ScreenTransitionService(self.manager_screens)
        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](s, self._loop)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            print(name_screen)
            self.manager_screens.add_widget(view)
            s.add_model(name_screen, model)
            s.add_view(name_screen, view)


def main():
    loop: AbstractEventLoop = get_event_loop()
    loop.run_until_complete(LoginAppMVC(loop).async_run(async_lib='asyncio'))
    loop.close()


if __name__ == '__main__':
    main()
