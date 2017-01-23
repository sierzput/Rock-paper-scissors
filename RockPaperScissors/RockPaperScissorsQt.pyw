#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.Qt import QMessageBox
from RockPaperScissors import Symbol, Result, decide, computerChoice
from RockPaperScissorsQtUi import Ui_MainWindow

def enableButtons(ui):
    ui.rockButton.setEnabled(True)
    ui.paperButton.setEnabled(True)
    ui.scissorsButton.setEnabled(True)

def showDialog(result):
    dialog = QMessageBox()
    if result == Result.win:
        message = u'Wygrałeś!'
        icon = QMessageBox.Information
    elif result == Result.lose:
        message = u'Przegrałeś :('
        icon = QMessageBox.Critical
    else:
        message = u'Remis'
        icon = QMessageBox.Warning
    dialog.setText(message)
    dialog.setIcon(icon)
    dialog.setWindowTitle(' ')
    dialog.exec_()

def showHelp():
    message = """Gra składa się z kolejnych tur. W każdej turze gracze i komputer, wybierają symbol papieru, kamienia lub nożyc. Gracz, który wybrał silniejszy symbol, otrzymuje jeden punkt. W przypadku pokazania dwóch takich samych symboli następuje remis – punktu brak. Oto hierarchia symboli:

–       nożyce są silniejsze od papieru, ponieważ go tną,
–       kamień jest silniejszy od nożyc, ponieważ je tępi,
–       papier jest silniejszy od kamienia, ponieważ go owija.

Gracz, który pierwszy uzyska umówioną wcześniej ilość punktów, wygrywa partię."""

    dialog = QMessageBox()
    dialog.setText(message)
    dialog.setIcon(QMessageBox.Information)
    dialog.setWindowTitle('Zasady gry')
    dialog.exec_()

def choose(ui, symbol):
    hideImages(ui)
    if symbol == Symbol.rock:
        ui.paperButton.setEnabled(False)
        ui.scissorsButton.setEnabled(False)
    elif symbol == Symbol.paper:
        ui.rockButton.setEnabled(False)
        ui.scissorsButton.setEnabled(False)
    elif symbol == Symbol.scissors:
        ui.rockButton.setEnabled(False)
        ui.paperButton.setEnabled(False)

    computer = computerChoice()
    if computer == Symbol.rock:
        ui.rockImage.setVisible(True)
    elif computer == Symbol.paper:
        ui.paperImage.setVisible(True)
    elif computer == Symbol.scissors:
        ui.scissorsImage.setVisible(True)

    result = decide(symbol, computer)
    if result == Result.win:
        score = int(ui.yourScore.text())
        score+=1
        ui.yourScore.setText(str(score))
    elif result == Result.lose:
        score = int(ui.computerScore.text())
        score+=1
        ui.computerScore.setText(str(score))

    showDialog(result)
    enableButtons(ui)

def hideImages(ui):
    ui.rockImage.setVisible(False)
    ui.paperImage.setVisible(False)
    ui.scissorsImage.setVisible(False)

def newGame(ui):
    ui.yourScore.setText('0')
    ui.computerScore.setText('0')
    enableButtons(ui)
    hideImages(ui)

def main():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    hideImages(ui)

    ui.rockButton.clicked.connect(lambda: choose(ui,Symbol.rock))
    ui.paperButton.clicked.connect(lambda: choose(ui,Symbol.paper))
    ui.scissorsButton.clicked.connect(lambda: choose(ui,Symbol.scissors))

    ui.actionNewGame.triggered.connect(lambda: newGame(ui))
    ui.actionExit.triggered.connect(QtGui.qApp.quit)
    ui.actionHelp.triggered.connect(showHelp)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()