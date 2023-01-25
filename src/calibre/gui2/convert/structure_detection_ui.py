# Form implementation generated from reading ui file '/home/mslos/桌面/kovidgoyal/calibre/src/calibre/gui2/convert/structure_detection.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(657, 479)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.opt_remove_fake_margins = QtWidgets.QCheckBox(Form)
        self.opt_remove_fake_margins.setObjectName("opt_remove_fake_margins")
        self.gridLayout.addWidget(self.opt_remove_fake_margins, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 4)
        self.opt_page_breaks_before = XPathEdit(Form)
        self.opt_page_breaks_before.setObjectName("opt_page_breaks_before")
        self.gridLayout.addWidget(self.opt_page_breaks_before, 5, 0, 2, 4)
        self.opt_insert_metadata = QtWidgets.QCheckBox(Form)
        self.opt_insert_metadata.setObjectName("opt_insert_metadata")
        self.gridLayout.addWidget(self.opt_insert_metadata, 3, 0, 1, 4)
        self.opt_start_reading_at = XPathEdit(Form)
        self.opt_start_reading_at.setObjectName("opt_start_reading_at")
        self.gridLayout.addWidget(self.opt_start_reading_at, 7, 0, 1, 4)
        self.opt_chapter = XPathEdit(Form)
        self.opt_chapter.setObjectName("opt_chapter")
        self.gridLayout.addWidget(self.opt_chapter, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.opt_chapter_mark = QtWidgets.QComboBox(Form)
        self.opt_chapter_mark.setMinimumContentsLength(20)
        self.opt_chapter_mark.setObjectName("opt_chapter_mark")
        self.gridLayout.addWidget(self.opt_chapter_mark, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.opt_remove_first_image = QtWidgets.QCheckBox(Form)
        self.opt_remove_first_image.setObjectName("opt_remove_first_image")
        self.gridLayout.addWidget(self.opt_remove_first_image, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.label.setBuddy(self.opt_chapter_mark)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.opt_remove_fake_margins.setText(_("Remove &fake margins"))
        self.label_2.setText(_("The header and footer removal options have been replaced by the Search & replace options. Click the Search & replace category in the bar to the left to use these options. Leave the replace field blank and enter your header/footer removal regexps into the search field."))
        self.opt_insert_metadata.setText(_("Insert &metadata as page at start of book"))
        self.label.setText(_("Chapter &mark:"))
        self.opt_remove_first_image.setText(_("Remove first &image"))
from calibre.gui2.convert.xpath_wizard import XPathEdit
