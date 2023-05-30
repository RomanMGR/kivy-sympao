from View.results_screen.results_screen import ResultsScreenView


class ResultsScreenController:
    """
    The `start_screen_controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model) -> None:
        self.model = model
        self.view = ResultsScreenView(controller=self, model=self.model)

    def get_view(self) -> ResultsScreenView:
        return self.view
