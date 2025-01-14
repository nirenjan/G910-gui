# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bene/Programmierkram/GitHub/G910-gui/src/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 627)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/input-keyboard-virtual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel#asd {\n"
"    image: url(:/icons/MEMORY_1.png);\n"
"    border: 4px solid black;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QLabel#asd:hover {\n"
"    border-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QLabel#asd:pressed {\n"
"    border-color: red;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.supportedDevice = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.supportedDevice.setFont(font)
        self.supportedDevice.setAlignment(QtCore.Qt.AlignCenter)
        self.supportedDevice.setObjectName("supportedDevice")
        self.horizontalLayout_7.addWidget(self.supportedDevice)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.memoryKeySlots = QtWidgets.QHBoxLayout()
        self.memoryKeySlots.setObjectName("memoryKeySlots")
        self.horizontalLayout_6.addLayout(self.memoryKeySlots)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.macroKeys = QtWidgets.QWidget()
        self.macroKeys.setGeometry(QtCore.QRect(0, 0, 83, 465))
        self.macroKeys.setObjectName("macroKeys")
        self.scrollArea.setWidget(self.macroKeys)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.macroNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.macroNameEdit.setObjectName("macroNameEdit")
        self.horizontalLayout_4.addWidget(self.macroNameEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.addKey = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("input-keyboard")
        self.addKey.setIcon(icon)
        self.addKey.setObjectName("addKey")
        self.horizontalLayout_4.addWidget(self.addKey)
        self.addDelay = QtWidgets.QPushButton(self.centralwidget)
        self.addDelay.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.addDelay.setIcon(icon)
        self.addDelay.setObjectName("addDelay")
        self.horizontalLayout_4.addWidget(self.addDelay)
        self.clearAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearAllButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clearAllButton.setText("")
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.clearAllButton.setIcon(icon)
        self.clearAllButton.setObjectName("clearAllButton")
        self.horizontalLayout_4.addWidget(self.clearAllButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.keyListWidget = QtWidgets.QScrollArea(self.centralwidget)
        self.keyListWidget.setWidgetResizable(True)
        self.keyListWidget.setObjectName("keyListWidget")
        self.keyListWidgetContents = CListWidgetContent()
        self.keyListWidgetContents.setGeometry(QtCore.QRect(0, 0, 797, 413))
        self.keyListWidgetContents.setObjectName("keyListWidgetContents")
        self.keyListWidget.setWidget(self.keyListWidgetContents)
        self.verticalLayout_3.addWidget(self.keyListWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("edit-undo")
        self.resetButton.setIcon(icon)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_3.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 34))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.bottomStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.bottomStatusBar.setObjectName("bottomStatusBar")
        MainWindow.setStatusBar(self.bottomStatusBar)
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("system-help")
        self.actionGitHub.setIcon(icon)
        self.actionGitHub.setObjectName("actionGitHub")
        self.actionReport_issue = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("mail-send")
        self.actionReport_issue.setIcon(icon)
        self.actionReport_issue.setObjectName("actionReport_issue")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExport_config = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionExport_config.setIcon(icon)
        self.actionExport_config.setObjectName("actionExport_config")
        self.actionImport_config = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.actionImport_config.setIcon(icon)
        self.actionImport_config.setObjectName("actionImport_config")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionImport_config)
        self.menuFile.addAction(self.actionExport_config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionGitHub)
        self.menuAbout.addAction(self.actionReport_issue)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Keyboard Center"))
        self.supportedDevice.setText(_translate("MainWindow", "no supported device found :("))
        self.label.setText(_translate("MainWindow", "Profile:"))
        self.macroNameEdit.setPlaceholderText(_translate("MainWindow", "name"))
        self.addKey.setText(_translate("MainWindow", "Add Key"))
        self.addDelay.setText(_translate("MainWindow", "Add Delay (soon)"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        self.actionReport_issue.setText(_translate("MainWindow", "Report issue"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExport_config.setText(_translate("MainWindow", "Export config...(soon)"))
        self.actionImport_config.setText(_translate("MainWindow", "Import config...(soon)"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
from gui.customwidgets import CListWidgetContent
from . import ressources_rc
