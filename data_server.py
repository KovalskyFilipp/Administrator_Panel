# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_server.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(400, 201)
        MainDialog.setMinimumSize(400, 201);
        self.label_35 = QtWidgets.QLabel(MainDialog)
        self.label_35.setGeometry(QtCore.QRect(10, 80, 341, 81))
        self.label_35.setObjectName("label_35")
        self.label = QtWidgets.QLabel(MainDialog)
        self.label.setGeometry(QtCore.QRect(10, 33, 220, 18))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(MainDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 160, 88, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon.fromTheme("applications-internet"))
        self.pushButton_2 = QtWidgets.QPushButton(MainDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 160, 88, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon.fromTheme("edit-undo"))
        self.lineEdit = QtWidgets.QLineEdit(MainDialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 29, 141, 31))
        #self.lineEdit.setObjectName(name_lineEdit)
        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Данные Сервера"))
        self.label_35.setText(_translate("MainDialog", "Дальнейшее изменение IP-адреса  можно произвести \n"
"в разделе \"Настройки\""))
        #self.label.setText(_translate("MainDialog", "Введите IP-адрес сервера" + name_button + ":"))
        self.pushButton_3.setText(_translate("MainDialog", "Перейти"))
        self.pushButton_2.setText(_translate("MainDialog", "Назад"))
        #self.lineEdit.setText(_translate("MainDialog", "0.0.0.0"))

