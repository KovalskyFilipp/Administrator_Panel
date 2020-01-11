# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JaCarta.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogJa(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 216)
        Dialog.setMinimumSize(305, 216);
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 30, 131, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 100, 131, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(207, 170, 91, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setIcon(QtGui.QIcon.fromTheme("edit-undo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выбор программного обеспечения JaCarta"))
        self.pushButton.setText(_translate("Dialog", "Программа \n"
"Диагностики"))
        self.pushButton_2.setText(_translate("Dialog", "Программа\n"
" Главного\n"
"Администратора"))
        self.pushButton_3.setText(_translate("Dialog", "Программа\n"
" Администратора"))
        self.pushButton_4.setText(_translate("Dialog", "Программа\n"
"Пользователя"))
        self.pushButton_5.setText(_translate("Dialog", "Назад"))

