from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("kv/login.kv")

USERS = {

    "CMDR": {
        "password": "Hitman",
        "screen": "commander"
    },

    "M14": {
        "password": "Apple",
        "screen": "m14"
    },

    "M16": {
        "password": "Mango",
        "screen": "m16"
    },

    "MARKING": {
        "password": "Mike",
        "screen": "marking"
    },

    "DUMPING": {
        "password": "Delta",
        "screen": "dumping"
    }
}


class LoginScreen(Screen):

    def login(self):

        username = self.ids.username.text.upper()
        password = self.ids.password.text

        if username in USERS:

            if USERS[username]["password"] == password:

                self.manager.current = USERS[username]["screen"]

            else:
                self.ids.message.text = "Wrong Password"

        else:
            self.ids.message.text = "Wrong Username"