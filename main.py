from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    """Interface for the kivy project"""

    def handleSubmit(self):
        ids = self.ids
        usernameInput = ids.usernameInput.text
        ids.usernameLabel.text = usernameInput


class ProjectApp(App):
    """build interface class"""
    pass

ProjectApp().run()