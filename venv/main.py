"""program for translating arabic characters into roman arabic script"""

import os

#importing pydub for audio
from pydub import AudioSegment
from pydub.playback import play

#importing lebanese module stuff
from lebanese import breakdown_lebanese
from breakdown_lebanese import arabic_break_down
from lebanese import lebanese_to_roman
from lebanese_to_roman import arabic_to_roman_replace

#importing kivy stuff
import kivy
kivy.require('1.11.1') # replace with your current kivy version !
#from kivy.config import Config
#Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

import kivy

kivy.require('1.11.1')  # replace with your current kivy version !
# from kivy.config import Config
# Config.set('modules', 'screen', 'phone_samsung_galaxy_s5')
from kivy.app import App

class TranslatorWidget(Widget):
    lebanese_arabic_text_input = ObjectProperty()

    #test_word = StringProperty("")
    #value = StringProperty("")

class MyApp(App):
    pass
   # def build(self):
     #   return TranslatorWidget()

if __name__ == '__main__':
    MyApp().run()
