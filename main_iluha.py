# Импортируем системый модуль для корректного закрытия программы
import sys
# Импортируем минимальный набор виджетов
from PyQt5 import QtGui
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QSettings, QRegExp
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
# Импортируем созданный нами класс со слотами
from test_concept_1 import *
from data_server import *
from JaCarta import *
from settings import *
import os

SETTINGS_KSC = 'settings/ksc'
SETTINGS_BACULA = 'settings/bacula'
SETTINGS_SIEM = 'settings/siem'
SETTINGS_ZABBIX = 'settings/zabbix'
SETTINGS_DRWEB = 'settings/drweb'

class MainDialog(Ui_Form):
    def __init__(self, Form):
        self.setupUi(Form)
        self.pushButton_2.clicked.connect(MainDialog.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(MainDialog.on_pushButton_3_clicked)
        #dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
        # Regulare expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self.lineEdit)
        self.lineEdit.setValidator(ipValidator)
        settings = QSettings()
        if self.lineEdit.objectName() == "lineEdit_KSC":
            self.lineEdit.setText(QSettings.value(settings,SETTINGS_KSC))
        if self.lineEdit.objectName() == "lineEdit_Bacula":
            self.lineEdit.setText(QSettings.value(settings,SETTINGS_BACULA))
        if self.lineEdit.objectName() == "lineEdit_SIEM":
            self.lineEdit.setText(QSettings.value(settings,SETTINGS_SIEM))
        if self.lineEdit.objectName() == "lineEdit_Zabbix":
            self.lineEdit.setText(QSettings.value(settings,SETTINGS_ZABBIX))
        if self.lineEdit.objectName() == "lineEdit_DrWeb":
            self.lineEdit.setText(QSettings.value(settings,SETTINGS_DRWEB))
        settings.sync()
    def on_pushButton_2_clicked(self):
        dialog.close()

    def on_pushButton_3_clicked(self):
        settings = QSettings()
        if dialog_ui.lineEdit.objectName() == "lineEdit_KSC":
            settings.setValue(SETTINGS_KSC, dialog_ui.lineEdit.text())
        if dialog_ui.lineEdit.objectName() == "lineEdit_Bacula":
            settings.setValue(SETTINGS_BACULA, dialog_ui.lineEdit.text())
        if dialog_ui.lineEdit.objectName() == "lineEdit_SIEM":
            settings.setValue(SETTINGS_SIEM, dialog_ui.lineEdit.text())
        if dialog_ui.lineEdit.objectName() == "lineEdit_Zabbix":
            settings.setValue(SETTINGS_ZABBIX, dialog_ui.lineEdit.text())
        if dialog_ui.lineEdit.objectName() == "lineEdit_DrWeb":
            settings.setValue(SETTINGS_DRWEB, dialog_ui.lineEdit.text())
        settings.sync()
        ui.label_2.setText(QSettings.value(settings,SETTINGS_KSC))
        ui.label_3.setText(QSettings.value(settings,SETTINGS_SIEM))
        ui.label_5.setText(QSettings.value(settings,SETTINGS_ZABBIX))
        ui.label_7.setText(QSettings.value(settings,SETTINGS_BACULA))
        ui.label_9.setText(QSettings.value(settings,SETTINGS_DRWEB))
        dialog.close()
        os.system('/usr/lib/firefox/firefox ' + dialog_ui.lineEdit.text())
 
class DialogSettings(Ui_Dialog):
    def __init__(self, Set):
        self.setupUi(Set)
        #settingsWin.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
        # Regulare expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self.lineEdit)
        self.lineEdit.setValidator(ipValidator)
        self.pushButton_2.clicked.connect(DialogSettings.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(DialogSettings.on_pushButton_3_clicked)
        
    def on_pushButton_2_clicked(self):
        settingsWin.close()
        
    def on_pushButton_3_clicked(self):
        settings = QSettings()
        if settings_ui.lineEdit.objectName() == "lineEdit_KSC":
            settings.setValue(SETTINGS_KSC, settings_ui.lineEdit.text())
        if settings_ui.lineEdit.objectName() == "lineEdit_Bacula":
            settings.setValue(SETTINGS_BACULA, settings_ui.lineEdit.text())
        if settings_ui.lineEdit.objectName() == "lineEdit_SIEM":
            settings.setValue(SETTINGS_SIEM, settings_ui.lineEdit.text())
        if settings_ui.lineEdit.objectName() == "lineEdit_Zabbix":
            settings.setValue(SETTINGS_ZABBIX, settings_ui.lineEdit.text())
        if settings_ui.lineEdit.objectName() == "lineEdit_DrWeb":
            settings.setValue(SETTINGS_DRWEB, settings_ui.lineEdit.text())
        settings.sync()
        settingsWin.close()
        ui.label_2.setText(QSettings.value(settings,SETTINGS_KSC))
        ui.label_3.setText(QSettings.value(settings,SETTINGS_SIEM))
        ui.label_5.setText(QSettings.value(settings,SETTINGS_ZABBIX))
        ui.label_7.setText(QSettings.value(settings,SETTINGS_BACULA))
        ui.label_9.setText(QSettings.value(settings,SETTINGS_DRWEB))
        
class DialogJa(Ui_DialogJa):
    def __init__(self, Ja):
        self.setupUi(Ja)
        self.pushButton_5.clicked.connect(DialogJa.on_pushButton_5_clicked)
        self.pushButton_2.clicked.connect(DialogJa.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(DialogJa.on_pushButton_3_clicked)
        self.pushButton_4.clicked.connect(DialogJa.on_pushButton_4_clicked)
        self.pushButton.clicked.connect(DialogJa.on_pushButton_clicked)
        
    def on_pushButton_5_clicked(self):
        jacarta.close()
        
    def on_pushButton_2_clicked(self):
        p = QtCore.QProcess()
        p.startDetached('sudo /opt/JaCartaSFGOSTSuite/jcsfkeyadmin')
        #os.system('sudo /opt/JaCartaSFGOSTSuite/jcsfkeyadmin')
        jacarta.close()
        
    def on_pushButton_3_clicked(self):
        p = QtCore.QProcess()
        p.startDetached('sudo /opt/JaCartaSFGOSTSuite/jcsfadmin')
        #os.system('sudo /opt/JaCartaSFGOSTSuite/jcsfadmin')
        jacarta.close()
        
    def on_pushButton_4_clicked(self):
        p = QtCore.QProcess()
        p.startDetached('sudo /opt/JaCartaSFGOSTSuite/jcsfuser')
        #os.system('sudo /opt/JaCartaSFGOSTSuite/jcsfuser')
        jacarta.close()
        
    def on_pushButton_clicked(self):
        p = QtCore.QProcess()
        p.startDetached('sudo /opt/JaCartaSFGOSTSuite/jcsfdiag')
        #os.system('sudo /opt/JaCartaSFGOSTSuite/jcsfdiag')
        jacarta.close()
# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(Ui_MainWindow):
        # При инициализации класса нам необходимо выпонить некоторые операции
    def __init__(self, form):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(form)
        settings = QSettings()
        self.label_2.setText(QSettings.value(settings,SETTINGS_KSC))
        self.label_3.setText(QSettings.value(settings,SETTINGS_SIEM))
        self.label_5.setText(QSettings.value(settings,SETTINGS_ZABBIX))
        self.label_7.setText(QSettings.value(settings,SETTINGS_BACULA))
        self.label_9.setText(QSettings.value(settings,SETTINGS_DRWEB))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_4.clicked.connect(self.on_pushButton_4_clicked)
        self.pushButton_7.clicked.connect(self.on_pushButton_7_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.pushButton_9.clicked.connect(self.on_pushButton_9_clicked)
        self.pushButton_10.clicked.connect(self.on_pushButton_10_clicked)
        self.pushButton_11.clicked.connect(self.on_pushButton_11_clicked)
        self.pushButton_17.clicked.connect(self.on_pushButton_17_clicked)
        self.pushButton_18.clicked.connect(self.on_pushButton_18_clicked)
        self.pushButton_19.clicked.connect(self.on_pushButton_19_clicked)
        self.pushButton_33.clicked.connect(self.on_pushButton_33_clicked)
        self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)        
        self.pushButton_34.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.pushButton_13.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        
    def on_pushButton_5_clicked(self):
        p = QtCore.QProcess()
        p.startDetached('sudo /usr/bin/fly-admin-ald-server')
        #os.system('sudo /usr/bin/fly-admin-ald-server')
        
    def on_pushButton_clicked(self):
        jacarta_ui = DialogJa(jacarta)
        jacarta.show()
        
    def on_pushButton_2_clicked(self):
        settings = QSettings()
        settings_button = " KSC"
        settings_lineEdit = "lineEdit_KSC"
        settings_ui.lineEdit.setObjectName(settings_lineEdit)
        settings_ui.label.setText("Введите IP-адрес сервера KSC:")
        settings_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_KSC))
        settingsWin.show()
        
    def on_pushButton_3_clicked(self):
        settings = QSettings()
        settings_button = " SIEM"
        settings_lineEdit = "lineEdit_SIEM"
        settings_ui.lineEdit.setObjectName(settings_lineEdit)
        settings_ui.label.setText("Введите IP-адрес сервера SIEM:")
        settings_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_SIEM))
        settingsWin.show()
        
    def on_pushButton_9_clicked(self):
        settings = QSettings()
        settings_button = " Zabbix"
        settings_lineEdit = "lineEdit_Zabbix"
        settings_ui.lineEdit.setObjectName(settings_lineEdit)
        settings_ui.label.setText("Введите IP-адрес сервера Zabbix:")
        settings_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_ZABBIX))
        settingsWin.show()
        
    def on_pushButton_10_clicked(self):
        settings = QSettings()
        settings_button = " Bacula"
        settings_lineEdit = "lineEdit_Bacula"
        settings_ui.lineEdit.setObjectName(settings_lineEdit)
        settings_ui.label.setText("Введите IP-адрес сервера Bacula:")
        settings_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_BACULA))
        settingsWin.show()
    
    def on_pushButton_11_clicked(self):
        settings = QSettings()
        settings_button = " DrWeb"
        settings_lineEdit = "lineEdit_DrWeb"
        settings_ui.lineEdit.setObjectName(settings_lineEdit)
        settings_ui.label.setText("Введите IP-адрес сервера Dr.Web:")
        settings_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_DRWEB))
        settingsWin.show()
        
    def on_pushButton_4_clicked(self):
        settings = QSettings()
        name_button = " SIEM"
        name_lineEdit = "lineEdit_SIEM"
        dialog_ui.lineEdit.setObjectName(name_lineEdit)
        dialog_ui.label.setText("Введите IP-адрес сервера SIEM:")
        if (QSettings.value(settings,SETTINGS_SIEM) == "0.0.0.0" or QSettings.value(settings,SETTINGS_SIEM) == "" or QSettings.value(settings,SETTINGS_SIEM) == None):
            dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_SIEM))
            dialog.show()
        else:
            #os.system('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_SIEM))
            p = QtCore.QProcess()
            p.startDetached('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_SIEM))
        #dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_SIEM))
        #dialog.show()
        
    def on_pushButton_18_clicked(self):
        settings = QSettings()
        name_button = " KSC"
        name_lineEdit = "lineEdit_KSC"
        dialog_ui.lineEdit.setObjectName(name_lineEdit)
        dialog_ui.label.setText("Введите IP-адрес сервера KSC:")
        settings = QSettings()
        if (QSettings.value(settings,SETTINGS_KSC) == "0.0.0.0" or QSettings.value(settings,SETTINGS_KSC) == "" or QSettings.value(settings,SETTINGS_KSC) == None):
            dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_KSC))
            dialog.show()
        else:
            p = QtCore.QProcess()
            p.startDetached('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_KSC))
            #os.system('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_KSC))
        
    def on_pushButton_7_clicked(self):
        settings = QSettings()
        name_button = " Zabbix"
        name_lineEdit = "lineEdit_Zabbix"
        dialog_ui.lineEdit.setObjectName(name_lineEdit)
        dialog_ui.label.setText("Введите IP-адрес сервера Zabbix:")
        if (QSettings.value(settings,SETTINGS_ZABBIX) == "0.0.0.0" or QSettings.value(settings,SETTINGS_ZABBIX) == "" or QSettings.value(settings,SETTINGS_ZABBIX) == None):
            dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_ZABBIX))
            dialog.show()
        else:
            p = QtCore.QProcess()
            p.startDetached('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_ZABBIX))
            #os.system('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_ZABBIX))
        
    def on_pushButton_19_clicked(self):
        settings = QSettings()
        name_button = " Bacula"
        name_lineEdit = "lineEdit_Bacula"
        dialog_ui.lineEdit.setObjectName(name_lineEdit)
        dialog_ui.label.setText("Введите IP-адрес сервера Bacula:")
        if (QSettings.value(settings,SETTINGS_BACULA) == "0.0.0.0" or QSettings.value(settings,SETTINGS_BACULA) == "" or QSettings.value(settings,SETTINGS_BACULA) == None):
            dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_BACULA))
            dialog.show()
        else:
            p = QtCore.QProcess()
            p.startDetached('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_BACULA))
            #os.system('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_BACULA))
        
    def on_pushButton_17_clicked(self):
        settings = QSettings()
        name_button = " DrWeb"
        name_lineEdit = "lineEdit_DrWeb"
        dialog_ui.lineEdit.setObjectName(name_lineEdit)
        dialog_ui.label.setText("Введите IP-адрес сервера Dr.Web:")
        if (QSettings.value(settings,SETTINGS_DRWEB) == "0.0.0.0" or QSettings.value(settings,SETTINGS_DRWEB) == "" or QSettings.value(settings,SETTINGS_DRWEB) == None):
            dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_DRWEB))
            dialog.show()
        else:
            p = QtCore.QProcess()
            p.startDetached('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_DRWEB))
            #os.system('/usr/lib/firefox/firefox ' + QSettings.value(settings,SETTINGS_DRWEB))
        #dialog_ui.lineEdit.setText(QSettings.value(settings,SETTINGS_DRWEB))
        #dialog.show()
        
    def on_pushButton_33_clicked(self):
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    # Создаём экземпляр приложения
    app = QApplication(sys.argv)
    settings_button = ""
    settings_lineEdit = ""
    name_button = ""
    name_lineEdit = ""    
    # Создаём базовое окно, в котором будет отображаться наш UI
    window = QMainWindow()
    dialog = QDialog()
    jacarta = QDialog()
    settingsWin = QDialog()
    # Создаём экземпляр нашего UI
    ui = MainWindow(window)
    settings_ui = DialogSettings(settingsWin)
    dialog_ui = MainDialog(dialog)
    # Отображаем окно
    window.show()
    # Обрабатываем нажатие на кнопку окна "Закрыть"
    sys.exit(app.exec_())
