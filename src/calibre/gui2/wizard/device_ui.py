# Form implementation generated from reading ui file '/home/mslos/桌面/kovidgoyal/calibre/src/calibre/gui2/wizard/device.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(400, 300)
        icon = QtGui.QIcon.ic("wizard.png")
        WizardPage.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(WizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(WizardPage)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(WizardPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manufacturer_view = QtWidgets.QListView(self.groupBox)
        self.manufacturer_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.manufacturer_view.setObjectName("manufacturer_view")
        self.verticalLayout.addWidget(self.manufacturer_view)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(WizardPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.device_view = QtWidgets.QListView(self.groupBox_2)
        self.device_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.device_view.setObjectName("device_view")
        self.verticalLayout_2.addWidget(self.device_view)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):

        WizardPage.setWindowTitle(_("Welcome to calibre"))
        WizardPage.setTitle(_("Welcome to calibre"))
        WizardPage.setSubTitle(_("The one stop solution to all your e-book needs."))
        self.groupBox.setTitle(_("&Manufacturers"))
        self.groupBox_2.setTitle(_("&Devices"))
