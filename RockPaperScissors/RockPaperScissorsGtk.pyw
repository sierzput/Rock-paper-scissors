#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

def main():
    builder = Gtk.Builder()
    builder.add_from_file("RockPaperScissorsGtk.glade")
    window = builder.get_object('dialog1')
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()