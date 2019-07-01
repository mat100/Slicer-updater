import os, sys
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup as KivyPopup
from kivy.uix.button import Button
from kivy.properties import StringProperty

from updaters.kisslicer_1_6_3 import perform_update_kisslicer_163

from kivy.config import Config
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')
Config.set('kivy','window_icon','resources/icons/trilab.ico')

class Popup(KivyPopup):
    pass

class Updater(Screen):
    slicer = StringProperty("KISSlicer 1.6.3")
    printer = StringProperty("DeltiQ")

    def on_slicer_change(self, value):
        self.slicer = value

    def on_printer_change(self, value):
        self.printer = value

    def perform_update(self):
        if self.slicer == "KISSlicer 1.6.3" and self.printer == "DeltiQ":
            print("test")
            #perform_update_kisslicer_163()
            content = Button(text='Close me!')
            popup = Popup(content=content, auto_dismiss=False)

            # bind the on_press event of the button to the dismiss function
            content.bind(on_press=popup.dismiss)
            popup.open()


class UpdaterApp(App):
    def build(self):
        return Updater()

# FIX issue with resources when compiled --onefile
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/7675014#7675014
# https://stackoverflow.com/questions/54154373/pyinstalled-kivy-app-fails-to-run-on-second-machine
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    kivy.resources.resource_add_path(resource_path(".")) # add this line
    UpdaterApp().run()