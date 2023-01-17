from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QProcess
import sys
import numpy as np
import main
import shutil

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()
        self.plainTextEdit.setReadOnly(True)
        self.pushButton_2.clicked.connect(self.zapisz)
        self.pushButton_3.clicked.connect(self.wczytaj)
        self.pushButton.clicked.connect(self.start)
        self.p = None

    def message(self, s):
        self.plainTextEdit.appendPlainText(s)

    def zapisz(self):
        if self.textEdit.toPlainText() != "" and self.textEdit_2.toPlainText() != "" and self.textEdit_3.toPlainText() != "":
            self.pushButton.setEnabled(True)
            file = open("data/hard_matrix.txt", "w")
            file.write(self.textEdit.toPlainText())
            file.close
            file = open("data/cable_vector.txt", "w")
            file.write(self.textEdit_2.toPlainText())
            file.close
            file = open("data/cost_tuples.txt", "w")
            file.write(self.textEdit_3.toPlainText())
            file.close
            file = open("data/tabu.txt", "w")
            file.write(self.textEdit_4.toPlainText())
            file.close
            file = open("data/mid_mem.txt", "w")
            file.write(self.textEdit_5.toPlainText())
            file.close
            file = open("data/iteration.txt", "w")
            file.write(self.textEdit_6.toPlainText())
            file.close
        else:
            self.pushButton.setEnabled(False)

    def wczytaj(self):
        self.pushButton.setEnabled(True)
        shutil.copyfile('data/hard_matrix_to_read.txt','data/hard_matrix.txt')
        shutil.copyfile('data/cable_vector_to_read.txt', 'data/cable_vector.txt')
        shutil.copyfile('data/cost_tuples_to_read.txt', 'data/cost_tuples.txt')
        shutil.copyfile('data/tabu_to_read.txt', 'data/tabu.txt')
        shutil.copyfile('data/mid_mem_to_read.txt', 'data/mid_mem.txt')
        shutil.copyfile('data/iteration_to_read.txt', 'data/iteration.txt')



    def start(self):
        if self.p is None:
            self.message("Działanie w toku")
            self.p = QProcess()
            self.p.finished.connect(self.finish)
            self.p.start("python3", ['main.py'])

    def finish(self):
        main.fun()
        file = open("res.txt", "r")
        result = file.read()
        file.close
        self.message(f"Result is:{result}")
        self.photo.setPixmap(QtGui.QPixmap("plot.png"))
        self.message("Koniec działania")
        self.p = None

def window():
    app = QApplication([])
    win = MyWindow()
    app.exec_()

window()