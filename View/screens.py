# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.start_screen_model import StartScreenModel
from Model.DeviceScreenModel import DeviceScreenModel
from Model.NbackScreenModel import NbackScreenModel
from Model.ResultsScreenModel import ResultsScreenModel
from Controller.start_screen_controller import StartScreenController
from Controller.DeviceScreenController import DeviceScreenController
from Controller.NbackScreenController import NbackScreenController
from Controller.ResultsScreenController import ResultsScreenController

print('screens')
screens = {
    "start_screen": {
        "model": StartScreenModel,
        "controller": StartScreenController,
    },
    "device_screen":{
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
    }
}
