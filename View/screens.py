# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.start_screen_model import StartScreenModel
from Model.DeviceScreenModel import DeviceScreenModel
from Model.NbackScreenModel import NbackScreenModel
from Model.ResultsScreenModel import ResultsScreenModel
from Model.ScaleBeckScreenModel import ScaleBeckScreenModel
from Model.AnxietyScreenModel import AnxietyScreenModel
from Model.AstheniaScreenModel import AstheniaScreenModel
from Model.CorsiScreenModel import CorsiScreenModel
from Model.ScabScreenModel import ScabScreenModel
from Controller.start_screen_controller import StartScreenController
from Controller.DeviceScreenController import DeviceScreenController
from Controller.NbackScreenController import NbackScreenController
from Controller.ResultsScreenController import ResultsScreenController
from Controller.ScaleBeckScreenController import ScaleBeckScreenController
from Controller.AnxietyScreenController import AnxietyScreenController
from Controller.AstheniaScreenController import AstheniaScreenController
from Controller.CorsiScreenController import CorsiScreenController
from Controller.ScabScreenController import ScabScreenController

print('screens')
screens = {
    "start_screen": {
        "model": StartScreenModel,
        "controller": StartScreenController,
    },
    "device_screen": {
        "model": DeviceScreenModel,
        "controller": DeviceScreenController,
    },
    "nback_screen": {
        "model": NbackScreenModel,
        "controller": NbackScreenController,
    },
    "results_screen": {
        "model": ResultsScreenModel,
        "controller": ResultsScreenController
    },
    "scale_beck_screen": {
        "model": ScaleBeckScreenModel,
        "controller": ScaleBeckScreenController
    },
    "anxiety_screen": {
        "model": AnxietyScreenModel,
        "controller": AnxietyScreenController
    },
    "asthenia_screen": {
        "model": AstheniaScreenModel,
        "controller": AstheniaScreenController
    },
    "corsi_screen": {
        "model": CorsiScreenModel,
        "controller": CorsiScreenController
    },
    "scab_screen": {
        "model": ScabScreenModel,
        "controller": ScabScreenController
    },
}
