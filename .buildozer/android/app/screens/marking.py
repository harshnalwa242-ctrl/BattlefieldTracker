from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from status import status_data, sos_data

Builder.load_file("kv/marking.kv")


class MarkingScreen(Screen):

    frontage = StringProperty("")
    perimeter = StringProperty("")
    grid = StringProperty("")

    def on_pre_enter(self):
        self.refresh()

    def set_status(self, task, value):

        status_data["MARKING"][task] = value

        self.refresh()

    def set_grid(self):

        status_data["MARKING"]["Grid"] = self.ids.grid_input.text

        self.refresh()

    def refresh(self):

        self.frontage = status_data["MARKING"]["Frontage"]

        self.perimeter = status_data["MARKING"]["Marking"]

        self.grid = status_data["MARKING"]["Grid"]

    def send_sos(self):

        sos_data["active"] = True
        sos_data["party"] = "MARKING"

    def logout(self):

        self.manager.current = "login"