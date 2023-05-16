from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
from Model.DeviceScreenModel import DeviceScreenModel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from kivymd.color_definitions import colors


class Content(BoxLayout):
    pass


class DeviceScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    name = 'not load'
    voltage = 'not refresh'
    voltage_icon = 'battery-unknown'
    slider_amp_text = int(0)
    slider_dlit_text = int(0)
    slider_chast_text = int(0)
    dialog = None

    def __init__(self, **kwargs):
        super(DeviceScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        print('init device_screen', self)

    def back(self):
        self.manager_screens.current = 'start_screen'
        self.model.discon()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(title="Подключение к устройству", type="custom",content_cls=Content())
        self.dialog.open()

    def on_text_reaction(self):
        if 0 < float(self.ids.text_field_id.text) <= 25:
            self.ids.slider_amp_id.value = self.ids.text_field_id.text
        elif float(self.ids.text_field_id.text) <= 0:
            self.ids.slider_amp_id.value = 0
            self.ids.text_field_id.text = str(0)
        else:
            self.ids.slider_amp_id.value = 25
            self.ids.text_field_id.text = str(25)

    def on_text_reaction_dlit(self):
        if 15 < float(self.ids.text_field_dlit_id.text) <= 60:
            self.ids.slider_dlit_id.value = self.ids.text_field_id.text
        elif float(self.ids.text_field_dlit_id.text) <= 15:
            self.ids.slider_dlit_id.value = 15
            self.ids.text_field_dlit_id.text = str(15)
        else:
            self.ids.slider_dlit_id.value = 60
            self.ids.text_field_dlit_id.text = str(60)

    def on_text_reaction_chast(self):
        if 5 < float(self.ids.text_field_chast_id.text) <= 150:
            self.ids.slider_chast_id.value = self.ids.text_field_chast_id.text
        elif float(self.ids.text_field_chast_id.text) <= 5:
            self.ids.slider_chast_id.value = 5
            self.ids.text_field_chast_id.text = str(5)
        else:
            self.ids.slider_chast_id.value = 150
            self.ids.text_field_chast_id.text = str(150)

    def refresh_voltage(self):
        self.ids.voltage_id.text = str(DeviceScreenModel.lb_battery_voltage) + '%'
        if DeviceScreenModel.lb_battery_voltage < 10:
            self.ids.voltage_icon_id.icon = 'battery-alert-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 20:
            self.ids.voltage_icon_id.icon = 'battery-10-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 30:
            self.ids.voltage_icon_id.icon = 'battery-20-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 40:
            self.ids.voltage_icon_id.icon = 'battery-30-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 50:
            self.ids.voltage_icon_id.icon = 'battery-40-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 60:
            self.ids.voltage_icon_id.icon = 'battery-50-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 70:
            self.ids.voltage_icon_id.icon = 'battery-60-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 80:
            self.ids.voltage_icon_id.icon = 'battery-70-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 90:
            self.ids.voltage_icon_id.icon = 'battery-80-bluetooth'
        elif DeviceScreenModel.lb_battery_voltage < 100:
            self.ids.voltage_icon_id.icon = 'battery-90-bluetooth'
        else:
            self.ids.voltage_icon_id.icon = 'battery-bluetooth'

    def refresh_parameters(self):
        self.ids.slider_amp_id.value = str(self.model.parameters[0])
        self.ids.slider_dlit_id.value = str(self.model.parameters[1])
        self.ids.slider_chast_id.value = str(self.model.parameters[2])
        if int(self.model.parameters[3]) == 0:
            self.ids.a0.active = True
        elif int(self.model.parameters[3]) == 1:
            self.ids.a1.active = True
        elif int(self.model.parameters[3]) == 2:
            self.ids.a2.active = True
        elif int(self.model.parameters[3]) == 3:
            self.ids.a3.active = True
        elif int(self.model.parameters[3]) == 4:
            self.ids.a4.active = True
        elif int(self.model.parameters[3]) == 5:
            self.ids.a5.active = True
        elif int(self.model.parameters[3]) == 6:
            self.ids.a6.active = True
        elif int(self.model.parameters[3]) == 7:
            self.ids.a7.active = True
        elif int(self.model.parameters[3]) == 8:
            self.ids.a8.active = True
        elif int(self.model.parameters[3]) == 9:
            self.ids.a9.active = True
        elif int(self.model.parameters[3]) == 10:
            self.ids.a10.active = True
        elif int(self.model.parameters[3]) == 11:
            self.ids.a11.active = True
        elif int(self.model.parameters[3]) == 12:
            self.ids.a12.active = True
        if int(self.model.parameters[4]) == 0:
            self.ids.btn_off.md_bg_color = colors['Red']['700']
            self.ids.btn_l.md_bg_color = colors['Blue']['700']
            self.ids.btn_r.md_bg_color = colors['Blue']['700']
        elif int(self.model.parameters[4]) == 1:
            self.ids.btn_l.md_bg_color = colors['Red']['700']
            self.ids.btn_off.md_bg_color = colors['Blue']['700']
            self.ids.btn_r.md_bg_color = colors['Blue']['700']
        elif int(self.model.parameters[4]) == 2:
            self.ids.btn_r.md_bg_color = colors['Red']['700']
            self.ids.btn_off.md_bg_color = colors['Blue']['700']
            self.ids.btn_l.md_bg_color = colors['Blue']['700']

    def model_is_changed(self):
        name = self.model.get_name()
        self.refresh_voltage()
        self.refresh_parameters()
        self.dialog.dismiss()
        self.ids.named.text = ' '+name
