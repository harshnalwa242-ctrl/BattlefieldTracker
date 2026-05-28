from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty

from kivy.clock import Clock

from status import status_data, sos_data

Builder.load_file("kv/commander.kv")


class CommanderScreen(Screen):

# ================= M14 =================

    m14_s1 = StringProperty("")
    m14_s2 = StringProperty("")
    m14_s3 = StringProperty("")

# ================= M16 =================

    m16_s1 = StringProperty("")
    m16_s2 = StringProperty("")
    m16_s3 = StringProperty("")

# ================= MARKING =================

    mark_front = StringProperty("")
    mark_peri = StringProperty("")

# ================= DUMPING =================

    dumping = StringProperty("")

# ================= SOS =================

    sos_party = StringProperty("NONE")

    flash_state = BooleanProperty(False)

# ================= GRID =================

    m14_grid = StringProperty("")
    m16_grid = StringProperty("")
    marking_grid = StringProperty("")
    dumping_grid = StringProperty("")

# ================= ENTER =================

    def on_pre_enter(self):

        self.refresh()

        Clock.schedule_interval(self.flash_sos, 0.5)

        Clock.schedule_interval(self.auto_refresh, 2)

# ================= EXIT =================

    def on_leave(self):

        Clock.unschedule(self.flash_sos)

        Clock.unschedule(self.auto_refresh)

# ================= AUTO REFRESH =================

    def auto_refresh(self, dt):

        self.refresh()

# ================= FLASH SOS =================

    def flash_sos(self, dt):

        if sos_data["active"]:

            self.flash_state = not self.flash_state

        else:

            self.flash_state = False

# ================= REFRESH =================

    def refresh(self):

# -------- M14 --------

        self.m14_s1 = status_data["M14"]["Strip 1"]
        self.m14_s2 = status_data["M14"]["Strip 2"]
        self.m14_s3 = status_data["M14"]["Strip 3"]

# -------- M16 --------

        self.m16_s1 = status_data["M16"]["Strip 1"]
        self.m16_s2 = status_data["M16"]["Strip 2"]
        self.m16_s3 = status_data["M16"]["Strip 3"]

# -------- MARKING --------

        self.mark_front = status_data["MARKING"]["Frontage"]

        self.mark_peri = status_data["MARKING"]["Marking"]

# -------- DUMPING --------

        self.dumping = status_data["DUMPING"]["Dumping"]

# -------- GRID --------

        self.m14_grid = status_data["M14"]["Grid"]

        self.m16_grid = status_data["M16"]["Grid"]

        self.marking_grid = status_data["MARKING"]["Grid"]

        self.dumping_grid = status_data["DUMPING"]["Grid"]

# -------- SOS --------

        if sos_data["active"]:

            self.sos_party = sos_data["party"]

        else:

            self.sos_party = "NONE"

# ================= CLEAR SOS =================

    def clear_sos(self):

        sos_data["active"] = False

        sos_data["party"] = "NONE"

        self.refresh()

# ================= M14 CONTROL =================

    def set_m14(self, task, value):

        status_data["M14"][task] = value

        self.refresh()

# ================= M16 CONTROL =================

    def set_m16(self, task, value):

        status_data["M16"][task] = value

        self.refresh()

# ================= MARKING CONTROL =================

    def set_marking(self, task, value):

        status_data["MARKING"][task] = value

        self.refresh()

# ================= DUMPING CONTROL =================

    def set_dumping(self, value):

        status_data["DUMPING"]["Dumping"] = value

        self.refresh()

# ================= LOGOUT =================

    def logout(self):

        self.manager.current = "login"