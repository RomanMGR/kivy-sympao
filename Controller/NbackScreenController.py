from View.nback_screen.nback_screen import NbackScreenView


class NbackScreenController:

    def __init__(self, model) -> None:
        self.model = model
        self.view = NbackScreenView(controller=self, model=self.model)

    def show_menu(self):
        self.model.show_menu()

    def get_view(self) -> NbackScreenView:
        return self.view