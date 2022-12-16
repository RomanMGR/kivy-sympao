import asyncio
import bleak
from kivy.app import App
from typing import Optional
from asyncio import AbstractEventLoop
from asyncio import Task
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from bleak import BleakScanner
from bleak import BleakClient
from kivy.clock import Clock
from functools import partial


def obr(read_ch):
    if len(read_ch) > 2:
        read_ch = int(read_ch[1:], 16)
    else:
        read_ch = int(read_ch)
    return read_ch


def test(mac: str, sm) -> None:
    def inner(btn) -> None:
        print('Called!', mac)
        sm.current = mac
    return inner


class MainApp(App):
    def __init__(self, loop:AbstractEventLoop) -> None:
        super().__init__()
        self._loop: AbstractEventLoop = loop
        self._task: Optional[Task] = None

    def build(self):
        global lyt, bts
        sm = ScreenManager()
        screen1 = Screen(name='main')
        lyt = GridLayout(cols=1, spacing=10, size_hint_y=None)
        lyt.bind(minimum_height=lyt.setter('height'))
        bts = Button(text='SCAN', size_hint_y=None, height=150, size_hint_x=1,
                     color=(0, 2, 0, 1), background_color=(0, 0, 205, 1))
        bts_b = lambda bts, sm=sm: self.scan(bts, sm)
        bts.bind(on_release = bts_b)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), bar_width=8,
                          bar_color=[100, 0, 0, 0.9], bar_inactive_color=[0, 100, 0, 0.9])
        root.add_widget(lyt)
        screen1.add_widget(root)
        screen1.add_widget(bts)
        sm.add_widget(screen1)
        print(sm.screen_names)
        return sm

    def scan(self, bts: Button, sm) -> None:
        bts.text = 'SCANNING ...'
        self._task = self._loop.create_task(self.task_scan(sm))

    async def task_scan(self, sm):
        scanned_devices = await BleakScanner.discover()
        print('Scanned devices: ', scanned_devices)
        if len(scanned_devices) == 0:
            dev = Button(text='Устройства не обнаружены', size_hint_y=None, height=160, size_hint_x=1)
            lyt.add_widget(dev)
        else:
            for device in scanned_devices:
                name = str(device.name)
                MAC = str(device.address)
                Btb = Button(text='Back', size_hint_y=None, height=200, size_hint_x=1)
                Btb_b = lambda sm=sm: self.back(sm)
                Btb.on_release = Btb_b
                lb1 = Label(text=('[size=60]' + '[b]' + name + '[/size]' + '\n' + 'MAC:  ' + '[/b]' + MAC),
                            markup=True)
                Bt1 = Button(text='Connect', size_hint_y=None, height=300, size_hint_x=1)
                knop = lambda sm=sm: self.char(sm)
                Bt1.bind(on_press=knop)
                screen2 = Screen(name=MAC)
                Bxl = BoxLayout(orientation='vertical')
                dev = Button(text=('[size=60]' + '[b]' + name + '[/size]' + '\n' + 'MAC:  ' + '[/b]' + MAC),
                             markup=True, size_hint_y=None, height=300, size_hint_x=1,
                             on_press=test(MAC, sm))
                Bxl.add_widget(Btb)
                Bxl.add_widget(lb1)
                Bxl.add_widget(Bt1)
                screen2.add_widget(Bxl)
                sm.add_widget(screen2)
                lyt.add_widget(dev)
        bts.text = 'SCAN'
        return lyt, sm

    def back(self, sm):
        sm.current = 'main'
        return sm

    def char(self, sm):
        self._task = self._loop.create_task(self.task_char(sm))
        self._task = self._loop.create_task(self.task_volt(sm))


    async def task_char(self, sm):
        global event1, lb_battery_voltage
        MAC = sm.current
        screen3 = Screen(name=MAC + '1')
        Btb = Button(text='Back', size_hint_y=None, height=200, size_hint_x=1)
        Btb.on_release = self.back
        Bxl = BoxLayout(orientation='vertical')
        Bxl.add_widget(Btb)
        try:
            async with BleakClient(MAC) as client:
                for service in client.services:
                    print(f"  service {service.uuid}")
                    for characteristic in service.characteristics:
                        print(f"  characteristic {characteristic.uuid} {hex(characteristic.handle)}"
                              f" ({len(characteristic.descriptors)} descriptors)")
                print(
                    f'xgatt_battery_voltage:{obr(await client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))}')
                print(
                    f'xgatt_packet_width_r:{obr(await client.read_gatt_char("dc210dd3-c32c-4ea6-a874-1b3c706d7a6e"))}')
                print(f'xgatt_battery_state:{obr(await client.read_gatt_char("de479aae-4248-4fb0-95fe-a36527747b6a"))}')
                print(f'xgatt_power_state:{obr(await client.read_gatt_char("45462078-e7d5-4604-b376-4d855f949e77"))}')
                print(
                    f'xgatt_impulse_width_r:{obr(await client.read_gatt_char("93fb864e-0c35-4a3b-8dcd-59fa47c6d11b"))}')
                print(
                    f'xgatt_impulse current:{obr(await client.read_gatt_char("e8a139f3-47e9-4b5a-ba3b-f7e1e73a3fed"))}')
        except bleak.exc.BleakError as e:
            print('error char')
        lb_battery_voltage = Label(text='battery_voltage')
        Bxl.add_widget(lb_battery_voltage)
        screen3.add_widget(Bxl)
        sm.add_widget(screen3)
        sm.current = MAC + '1'

    async def task_volt(self, sm):
        print('I am started')
        await asyncio.sleep(5)
        print('finish')
        mac = sm.current[:-1]
        while True:
            try:
                async with BleakClient(mac) as client:
                    print(str(obr(await client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))))
                    await asyncio.sleep(5)
            except bleak.exc.BleakError as e:
                print('error')


def main():
    loop: AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(MainApp(loop).async_run(async_lib='asyncio'))
    loop.close()


if __name__ == '__main__':
    main()

