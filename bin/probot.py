#!/usr/bin/env python3
import os

os.environ["KIVY_NO_CONSOLELOG"] = "1"
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '770')
from kivy.core.window import Window
Window.hide()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import commands
import nltk

widget_set = {}

class ProBot(App):
    def on_focus(instance, value):
        global widget_set
        instance.foreground_color = 'white'
        instance.text = ""
        if not value:
            instance.foreground_color = 'gray'
            instance.text = "Enter a message..."

    def on_submission(instance):
        global widget_set
        widget_set["activity"].background_color = '#00e846'
        widget_set["log"].text += "You: " + instance.text + "\n"
        commands.command(instance.text, widget_set["log"])

    def init_widgets():
        global widget_set
        widget_set["float"].add_widget(widget_set["entry_line_1"])
        widget_set["entry_line_1"].multiline = False
        widget_set["entry_line_1"].size_hint = (1, 0.01)
        widget_set["entry_line_1"].background_color = '#1c6c91'
        widget_set["entry_line_1"].pos_hint = {'x': 0, 'y': 0.88}

        widget_set["float"].add_widget(widget_set["log"])
        widget_set["log"].text = "Hey \n Here are some things you can do \n"
        widget_set["log"].size_hint = (1, 0.75)
        widget_set["log"].pos_hint = {'x': 0, 'y': 0.12}
        widget_set["log"].background_color = '#0d0d0d'
        widget_set["log"].foreground_color = '#bde4ff'
        widget_set["log"].cursor_color = (0, 0, 0, 1)
        widget_set["log"].font_name = 'DejaVuSans.ttf'
        widget_set["log"].font_size = 18
        widget_set["log"].halign = 'center'
        widget_set["log"].line_spacing = 10

        widget_set["float"].add_widget(widget_set["entry_line_2"])
        widget_set["entry_line_2"].multiline = False
        widget_set["entry_line_2"].size_hint = (1, 0.01)
        widget_set["entry_line_2"].background_color = '#1c6c91'
        widget_set["entry_line_2"].pos_hint = {'x': 0, 'y': 0.11}

        widget_set["float"].add_widget(widget_set["entry"])
        widget_set["entry"].text = "Enter a message..."
        widget_set["entry"].multiline = False
        widget_set["entry"].size_hint = (1, 0.1)
        widget_set["entry"].pos_hint = {'x': 0, 'y':0}
        widget_set["entry"].background_color = '#000000'
        widget_set["entry"].foreground_color = '#FFFFFF'
        widget_set["entry"].cursor_color = (.1, .8, .1, 1)
        widget_set["entry"].bind(on_text_validate = ProBot.on_submission)
        widget_set["entry"].bind(focus = ProBot.on_focus)
        widget_set["entry"].font_size = 16
        widget_set["entry"].focus = False
        widget_set["entry"].foreground_color = 'gray'

        widget_set["float"].add_widget(widget_set["heading"])
        widget_set["heading"].text = "<< " + "ProBot >>"
        widget_set["heading"].size_hint = (1, 0.1)
        widget_set["heading"].pos_hint = {'x': 0.1, 'y': 0.9}
        widget_set["heading"].color = '#0096ff'
        widget_set["heading"].font_size = 36
        widget_set["heading"].halign = 'center'

        widget_set["float"].add_widget(widget_set["logo"])
        widget_set["entry_line_1"].size_hint = (0.1, 0.1)
        widget_set["entry_line_1"].pos_hint = {'x': 0, 'y': 0.9}

        widget_set["float"].add_widget(widget_set["activity"])
        widget_set["activity"].background_color = '#ff0011'
        widget_set["activity"].size_hint = (0.04, 0.01)
        widget_set["activity"].pos_hint = {'x': 0.96, 'y': 0.89}

    def build(self):
        global widget_set
        print("Initializing Bot")
        print("Connecting to dbus interface")
        os.system("xdg-open restart >/dev/null 2>&1")
        print("Connected to dbus interface")
        print("Initializing GUI")
        widget_set["float"] = FloatLayout()
        widget_set["log"] = TextInput()
        widget_set["entry"] = TextInput()
        widget_set["entry_line_1"] = TextInput()
        widget_set["entry_line_2"] = TextInput()
        widget_set["heading"] = Label()
        widget_set["activity"] = TextInput()
        widget_set["logo"] = Image()
        ProBot.init_widgets()
        print("Initialized GUI")
        print("Verifying NLTK libraries")
        nltk.download('stopwords')
        nltk.download('punkt')
        print("Verified NLTK libraries")
        print("Starting")
        Window.show()
        return widget_set["float"]

if __name__ == '__main__':
    try:
        ProBot().run()
    except Exception as ex:
        print("Internal Error Occured.")
