import asyncio
import bleak
from asyncio import Task
from asyncio import AbstractEventLoop
from typing import Optional
from services.get_volt_service import GetVoltService
from services.connect_service import ConnectService
from services.get_parameters import GetParametersService
from services.send_parameters_service import SendParametersService

class DeviceScreenModel:

    lb_battery_voltage = 0
    rssi = 0
    ble_client = None
    examp_class_serv = None
    parameters = None

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._task_get_parameters: Optional[Task] = None
        self._task_send: [Optional[Task]] = []
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.screen_transition_service = screen_transition_service
        self.__mac = None
        self.__device = None
        self.__name = None

    def start(self, device, mac, name):
        self.__mac = mac
        self.__device = device
        self.__name = name
        self.screen_transition_service.show_dialog_device()
        self.get_parameters()

    def get_name(self):
        return self.__name

    def check_volt(self):
        self._task = self._loop.create_task(self.task_volt())
        print('check volt task created')

    async def task_volt(self):
        examp_class_volt = GetVoltService()
        while True:
            try:
                await examp_class_volt.get_volt(DeviceScreenModel.ble_client)
                voltage_obr = int(round((int(GetVoltService.battery_voltage) - 3000)/1200 * 100, 0))
                DeviceScreenModel.lb_battery_voltage = voltage_obr
                self.notify_observers()
                await asyncio.sleep(10)
            except bleak.exc.BleakError as e:
                print('error')

    def get_parameters(self):
        self._task_get_parameters = self._loop.create_task(self.task_get_parameters())

    async def task_get_parameters(self):
        DeviceScreenModel.examp_class_serv = ConnectService(self.__device)
        DeviceScreenModel.ble_client = DeviceScreenModel.examp_class_serv.bleak_client()
        print(DeviceScreenModel.ble_client)
        await DeviceScreenModel.examp_class_serv.connect()
        DeviceScreenModel.parameters = await GetParametersService().get_parameters(DeviceScreenModel.ble_client)
        print(DeviceScreenModel.parameters)
        self.check_volt()

    def send_anode(self, n):
        self._task_send.append(self._loop.create_task(self.send_anode_task(n)))

    async def send_anode_task(self, n):
        if str(n) != DeviceScreenModel.parameters[3]:
            DeviceScreenModel.parameters[3] = n
            await SendParametersService().send_anode(DeviceScreenModel.ble_client, n)
            print('send_anode_task finished')

    def send_amp(self, value):
        self._task_send.append(self._loop.create_task(self.send_amp_task(value)))
        print('created task amp!!!!!')

    async def send_amp_task(self, value):
        if str(value) != DeviceScreenModel.parameters[0]:
            DeviceScreenModel.parameters[0] = float(value)
            await SendParametersService().send_amp(DeviceScreenModel.ble_client, value)
            print('finish task amp!!!!')

    def send_dlit(self, value):
        self._task_send.append(self._loop.create_task(self.task_send_dlit(value)))

    async def task_send_dlit(self, value):
        if str(value) != DeviceScreenModel.parameters[1]:
            DeviceScreenModel.parameters[1] = float(value)
            await SendParametersService().send_dlit(DeviceScreenModel.ble_client, value)

    def send_chast(self, value):
        self._task_send.append(self._loop.create_task(self.task_send_chast(value)))

    async def task_send_chast(self, value):
        if str(value) != DeviceScreenModel.parameters[2]:
            DeviceScreenModel.parameters[2] = float(value)
            await SendParametersService().send_chast(DeviceScreenModel.ble_client, value)

    def send_segment(self, n):
        self._task_send.append(self._loop.create_task(self.task_send_segment(n)))

    async def task_send_segment(self, n):
        if str(n) != DeviceScreenModel.parameters[4]:
            DeviceScreenModel.parameters[4] = float(n)
            await SendParametersService().send_segment(DeviceScreenModel.ble_client, n)

    def discon(self):
        try:
            self._task.cancel()
            self._task_get_parameters.cancel()
            for i in self._task_send:
                i.cancel()
        except:
            pass
        self._task = self._loop.create_task(self.task_discon())

    async def task_discon(self):
        await DeviceScreenModel.examp_class_serv.discon()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
