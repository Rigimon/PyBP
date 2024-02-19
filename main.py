from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow)
from PySide6 import QtCore
from ui_main import Ui_MainWindow
import sys
import os
import commands as tt

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyBP - Quebrador de Senhas")
        appIcon = QIcon(u"icone.ico")
        self.setWindowIcon(appIcon)

        ## TOGGLE BUTTON ##
        self.btn_toogle.clicked.connect(self.LeftMenu)

        ## OPEN DIR BUTTON ##
        self.btn_open_dir.clicked.connect(self.open_path)

        ## Quebrar Senha Button ##
        self.btn_quebrar_senha.clicked.connect(self.broken_pass)

        ## LeftMenu BUTTONS ##
        ### SENHAS ###
        self.btn_quebrar.clicked.connect(lambda: self.main_pages.setCurrentWidget(self.pg_quebrar))
        self.btn_consultar.clicked.connect(self.consul)#lambda: self.main_pages.setCurrentWidget(self.pg_consultar))
        self.btn_feedback.clicked.connect(self.FeedBack)


    def FeedBack(self):
        tt.feedback("https://forms.office.com/r/NxCnRYPet0")
        
    def consul(self):
        self.main_pages.setCurrentWidget(self.pg_consultar)
        self.list_senha.clear()
        texto = tt.consul()
        for frase in texto:
            self.list_senha.addItem(frase)

    def LeftMenu(self):
        width = self.left_container.width()

        if width == 9:
            newWidht = 200
        else:
            newWidht = 9

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidht)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def open_path(self):
        self.path = QFileDialog.getOpenFileNames(self, str("Open Files"),
                                                     f"C:/Users/{os.environ.get('USERNAME')}/Desktop")#, QFileDialog.ShowDirsOnly
                                                     #| QFileDialog.DontResolveSymlinks)
        #print(self.path[0])
        try:
            self.path_dir.setText(self.path[0][0])
        except IndexError:
            pass
        except Exception:
            print("erro")

    def broken_pass(self):
        PATH_ITEM = self.path_dir.text()
        item = ""
        if PATH_ITEM != "":
            item = tt.pegar_item(PATH_ITEM)
            senha = tt.comparar_itens(item)
            if senha == False:
                tt.descobrir_senha(item)
                senha = tt.consulta(item).replace("\n","").split(":")
                if senha[1] != "sem senha":
                    texto = f"A senha de {senha[0]} é [{senha[1]}]"
                    self.ed_senha.setText(texto)
                    tt.guardar_senha(texto + "\n")
                else:
                    texto = f"{senha[0]} está {senha[1]}"
                    self.ed_senha.setText(texto)
            else:
                self.ed_senha.setText(senha)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
