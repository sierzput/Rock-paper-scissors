#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from RockPaperScissors import Symbol, Result, computerChoice, decide

class MainWindow:
    def __init__(self):
        self.gladefile = "RockPaperScissorsGtk.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("applicationwindow1")
        self.window.connect('delete-event', Gtk.main_quit)

        self.computerChoiceBox = self.builder.get_object('computerChoiceBox')

        self.rockImage = self.builder.get_object('rockImage')
        self.paperImage = self.builder.get_object('paperImage')
        self.scissorsImage = self.builder.get_object('scissorsImage')
        self.rockButton = self.builder.get_object('rockButton')
        self.paperButton = self.builder.get_object('paperButton')
        self.scissorsButton = self.builder.get_object('scissorsButton')
        self.yourScore = self.builder.get_object('yourScore')
        self.computerScore = self.builder.get_object('computerScore')

        self.window.show()
        self.__hideImages__()

    def onExitMenuItem(self, *args):
        Gtk.main_quit(*args)

    def onNewGamePressed(self, button):
        self.__hideImages__()

    def onRockButtonClicked(self, button):
        self.paperButton.set_sensitive(False)
        self.scissorsButton.set_sensitive(False)
        self.__choose__(Symbol.rock)

    def onPaperButtonClicked(self, button):
        self.rockButton.set_sensitive(False)
        self.scissorsButton.set_sensitive(False)
        self.__choose__(Symbol.paper)

    def onScissorsButtonClicked(self, button):
        self.rockButton.set_sensitive(False)
        self.paperButton.set_sensitive(False)
        self.__choose__(Symbol.scissors)

    def __enableButtons__(self):
        self.rockButton.set_sensitive(True)
        self.paperButton.set_sensitive(True)
        self.scissorsButton.set_sensitive(True)

    def __hideImages__(self):
        size = self.computerChoiceBox.get_allocation()
        self.computerChoiceBox.set_size_request(size.width, size.height)

        self.rockImage.hide()
        self.paperImage.hide()
        self.scissorsImage.hide()

    def __showDialog__(self, result):
        if result == Result.win:
            message = u'Wygrałeś!'
            icon = Gtk.MessageType.INFO
        elif result == Result.lose:
            message = u'Przegrałeś :('
            icon = Gtk.MessageType.ERROR
        else:
            message = u'Remis'
            icon = Gtk.MessageType.WARNING

        dialog = Gtk.MessageDialog(self.window, Gtk.DialogFlags.MODAL, icon, Gtk.ButtonsType.OK, message)
        dialog.run()
        dialog.destroy()

    def __choose__(self, symbol):
        self.__hideImages__()
        
        computer = computerChoice()
        if computer == Symbol.rock:
            self.rockImage.show()
        elif computer == Symbol.paper:
            self.paperImage.show()
        elif computer == Symbol.scissors:
            self.scissorsImage.show()

        result = decide(symbol, computer)
        if result == Result.win:
            score = int(self.yourScore.get_text())
            score+=1
            self.yourScore.set_text(str(score))
        elif result == Result.lose:
            score = int(self.computerScore.get_text())
            score+=1
            self.computerScore.set_text(str(score))

        self.__showDialog__(result)
        self.__enableButtons__()

def main():
    window = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()