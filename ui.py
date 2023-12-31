# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '01.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1444, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 171, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stylus = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.stylus.setObjectName("stylus")
        self.tools = QtWidgets.QButtonGroup(MainWindow)
        self.tools.setObjectName("tools")
        self.tools.addButton(self.stylus)
        self.verticalLayout.addWidget(self.stylus)
        self.brush = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.brush.setObjectName("brush")
        self.tools.addButton(self.brush)
        self.verticalLayout.addWidget(self.brush)
        self.ruber = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ruber.setObjectName("ruber")
        self.tools.addButton(self.ruber)
        self.verticalLayout.addWidget(self.ruber)
        self.sprayButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.sprayButton.setObjectName("sprayButton")
        self.tools.addButton(self.sprayButton)
        self.verticalLayout.addWidget(self.sprayButton)
        self.lineButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.lineButton.setObjectName("lineButton")
        self.tools.addButton(self.lineButton)
        self.verticalLayout.addWidget(self.lineButton)
        self.rectButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rectButton.setObjectName("rectButton")
        self.tools.addButton(self.rectButton)
        self.verticalLayout.addWidget(self.rectButton)
        self.fillCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fillCheckBox.setObjectName("fillCheckBox")
        self.verticalLayout.addWidget(self.fillCheckBox)
        self.colorButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.colorButton.setObjectName("colorButton")
        self.verticalLayout.addWidget(self.colorButton)
        self.widthButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.widthButton.setObjectName("widthButton")
        self.verticalLayout.addWidget(self.widthButton)
        self.choicePhotos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.choicePhotos.setObjectName("choicePhotos")
        self.verticalLayout.addWidget(self.choicePhotos)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 161, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.saveButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.saveButton)
        self.clearButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.clearButton)
        self.fillColorButton = QtWidgets.QPushButton(self.centralwidget)
        self.fillColorButton.setGeometry(QtCore.QRect(130, 350, 61, 23))
        self.fillColorButton.setObjectName("fillColorButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1444, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PaintAnalog"))
        self.stylus.setText(_translate("MainWindow", "Ручка"))
        self.brush.setText(_translate("MainWindow", "Кисть"))
        self.ruber.setText(_translate("MainWindow", "Стёрка"))
        self.sprayButton.setText(_translate("MainWindow", "Спрей"))
        self.lineButton.setText(_translate("MainWindow", "Линия"))
        self.rectButton.setText(_translate("MainWindow", "Прямоугольник"))
        self.fillCheckBox.setText(_translate("MainWindow", "Заливка фигуры"))
        self.colorButton.setText(_translate("MainWindow", "Выбор цвета"))
        self.widthButton.setText(_translate("MainWindow", "Выбор толщины"))
        self.choicePhotos.setText(_translate("MainWindow", "Загрузить фото"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.clearButton.setText(_translate("MainWindow", "Очистить"))
        self.fillColorButton.setText(_translate("MainWindow", "Заливка"))
