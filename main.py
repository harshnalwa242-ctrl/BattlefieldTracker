from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.commander import CommanderScreen
from screens.m14 import M14Screen
from screens.m16 import M16Screen
from screens.marking import MarkingScreen
from screens.dumping import DumpingScreen


class BattlefieldTracker(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(CommanderScreen(name="commander"))
        sm.add_widget(M14Screen(name="m14"))
        sm.add_widget(M16Screen(name="m16"))
        sm.add_widget(MarkingScreen(name="marking"))
        sm.add_widget(DumpingScreen(name="dumping"))

        sm.current = "login"

        return sm


if __name__ == "__main__":
    BattlefieldTracker().run()