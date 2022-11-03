import asyncio
import bleak

from kivy.app import App

# from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy import clock
from kivy.app import runTouchApp
from bleak import BleakScanner


class MainApp(App):
    def build(self):
        global lyt
        lyt = GridLayout(cols = 1, spacing = 10 , size_hint_y = None)
        lyt.bind(minimum_height=lyt.setter('height'))
        bt1 = Button(text = 'Check', size_hint_y = None, height = 400, size_hint_x = 1)
        bt1.on_release = lambda: asyncio.run(self.scan())
        lyt.add_widget(bt1)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(lyt)
        runTouchApp(root)
        return lyt
    async def scan(self):
        scanned_devices = await BleakScanner.discover()
        print('Scanned devices: ', scanned_devices)
        if len(scanned_devices) == 0:
            dev = Label(text = 'Устройства не обнаружены')
            lyt.add_widget(dev)
        else:
            for device in scanned_devices:
                dev = Button(text = str(device), size_hint_y = None, height = 560, size_hint_x = 1)
                lyt.add_widget(dev)
        return lyt



app = MainApp()
app.run()
