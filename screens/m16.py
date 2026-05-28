from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from status import status_data, sos_data

Builder.load_file("kv/m16.kv")


class M16Screen(Screen):

    strip1 = StringProperty("")
    strip2 = StringProperty("")
    strip3 = StringProperty("")
    grid = StringProperty("")

    def on_pre_enter(self):
        self.refresh()

    def set_status(self, task, value):

        status_data["M16"][task] = value

        self.refresh()

    def set_grid(self):

        status_data["M16"]["Grid"] = self.ids.grid_input.text

        self.refresh()

    def refresh(self):

        self.strip1 = status_data["M16"]["Strip 1"]
        self.strip2 = status_data["M16"]["Strip 2"]
        self.strip3 = status_data["M16"]["Strip 3"]

        self.grid = status_data["M16"]["Grid"]

    def send_sos(self):

        sos_data["active"] = True
        sos_data["party"] = "M16"

    def logout(self):
        self.manager.current = "login"