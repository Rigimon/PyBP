# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import a_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 401)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.pg_home.setGeometry(QRect(0, 0, 160, 223))
        self.verticalLayout_4 = QVBoxLayout(self.pg_home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_quebrar = QPushButton(self.pg_home)
        self.btn_quebrar.setObjectName(u"btn_quebrar")

        self.verticalLayout_4.addWidget(self.btn_quebrar)

        self.btn_consultar = QPushButton(self.pg_home)
        self.btn_consultar.setObjectName(u"btn_consultar")

        self.verticalLayout_4.addWidget(self.btn_consultar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.pg_home, u"Senhas")
        self.pg_config = QWidget()
        self.pg_config.setObjectName(u"pg_config")
        self.toolBox.addItem(self.pg_config, u"Page")
        self.pg_suporte = QWidget()
        self.pg_suporte.setObjectName(u"pg_suporte")
        self.pg_suporte.setGeometry(QRect(0, 0, 160, 223))
        self.verticalLayout_5 = QVBoxLayout(self.pg_suporte)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_feedback = QPushButton(self.pg_suporte)
        self.btn_feedback.setObjectName(u"btn_feedback")

        self.verticalLayout_5.addWidget(self.btn_feedback)

        self.lb_contato = QLabel(self.pg_suporte)
        self.lb_contato.setObjectName(u"lb_contato")
        self.lb_contato.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setKerning(True)
        self.lb_contato.setFont(font)
        self.lb_contato.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lb_contato)

        self.frame_6 = QFrame(self.pg_suporte)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(90, 90))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(90, 90))
        self.label_4.setPixmap(QPixmap(u":/a/qrcode.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.lb_version = QLabel(self.pg_suporte)
        self.lb_version.setObjectName(u"lb_version")

        self.verticalLayout_5.addWidget(self.lb_version)

        self.toolBox.addItem(self.pg_suporte, u"Suporte")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toogle = QPushButton(self.top_frame)
        self.btn_toogle.setObjectName(u"btn_toogle")
        self.btn_toogle.setMaximumSize(QSize(15, 16777215))
        self.btn_toogle.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/a/bars-3.png);	\n"
"	border:0px;\n"
"	width:15px;\n"
"	height:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_toogle)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.main_pages = QStackedWidget(self.main_frame)
        self.main_pages.setObjectName(u"main_pages")
        self.pg_quebrar = QWidget()
        self.pg_quebrar.setObjectName(u"pg_quebrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_quebrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.pg_quebrar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.path_dir = QLineEdit(self.frame_3)
        self.path_dir.setObjectName(u"path_dir")
        self.path_dir.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.path_dir)

        self.btn_open_dir = QPushButton(self.frame_3)
        self.btn_open_dir.setObjectName(u"btn_open_dir")
        self.btn_open_dir.setStyleSheet(u"QPushButton{\n"
"	border:0px;\n"
"	border-image: url(:/a/open_dir.png);\n"
"	width:25px;\n"
"	height:25px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_open_dir)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.pg_quebrar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ed_senha = QLabel(self.frame_4)
        self.ed_senha.setObjectName(u"ed_senha")
        self.ed_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ed_senha)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_quebrar_senha = QPushButton(self.frame_5)
        self.btn_quebrar_senha.setObjectName(u"btn_quebrar_senha")

        self.horizontalLayout_6.addWidget(self.btn_quebrar_senha)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.main_pages.addWidget(self.pg_quebrar)
        self.pg_consultar = QWidget()
        self.pg_consultar.setObjectName(u"pg_consultar")
        self.verticalLayout_9 = QVBoxLayout(self.pg_consultar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.list_senha = QListWidget(self.pg_consultar)
        self.list_senha.setObjectName(u"list_senha")

        self.verticalLayout_9.addWidget(self.list_senha)

        self.main_pages.addWidget(self.pg_consultar)

        self.verticalLayout_6.addWidget(self.main_pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(2)
        self.main_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PyBP", None))
        self.btn_quebrar.setText(QCoreApplication.translate("MainWindow", u"Quebrar Senha", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar Senhas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_home), QCoreApplication.translate("MainWindow", u"Senhas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_config), QCoreApplication.translate("MainWindow", u"Page", None))
        self.btn_feedback.setText(QCoreApplication.translate("MainWindow", u"FeedBack", None))
        self.lb_contato.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Email de Contato:</p><p align=\"center\">rigi.dev@hotmail.com</p></body></html>", None))
        self.label_4.setText("")
        self.lb_version.setText(QCoreApplication.translate("MainWindow", u"vers\u00e3o 0.1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pg_suporte), QCoreApplication.translate("MainWindow", u"Suporte", None))
        self.btn_toogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyBrokenPassword", None))
        self.path_dir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seleciona o arquivo que deseja descobrir a senha", None))
#if QT_CONFIG(whatsthis)
        self.btn_open_dir.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_open_dir.setText("")
        self.ed_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_quebrar_senha.setText(QCoreApplication.translate("MainWindow", u"Quebrar Senha", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"@Rigimon", None))
    # retranslateUi

