#!/usr/bin/env python3

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class ContactGrid(Widget):
    pass

class MyApp(App):

    def build(self):
        return ContactGrid()





if __name__=="__main__" :
    MyApp().run()
