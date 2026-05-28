from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from status import status_data, sos_data

Builder.load_file("kv/dumping.kv")


class DumpingScreen(Screen):

    dumping = StringProperty("")
    grid = StringProperty("")

    def on_pre_enter(self):
        self.refresh()

    def set_status(self, value):

        status_data["DUMPING"]["Dumping"] = value

        self.refresh()

    def set_grid(self):

        status_data["DUMPING"]["Grid"] = self.ids.grid_input.text

        self.refresh()

    def refresh(self):

        self.dumping = status_data["DUMPING"]["Dumping"]

        self.grid = status_data["DUMPING"]["Grid"]

    def send_sos(self):

        sos_data["active"] = True
        sos_data["party"] = "DUMPING"

    def logout(self):

        self.manager.current = "login"