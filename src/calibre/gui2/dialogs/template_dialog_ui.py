# Form implementation generated from reading ui file '/home/mslos/桌面/kovidgoyal/calibre/src/calibre/gui2/dialogs/template_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TemplateDialog(object):
    def setupUi(self, TemplateDialog):
        TemplateDialog.setObjectName("TemplateDialog")
        TemplateDialog.resize(588, 546)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TemplateDialog.sizePolicy().hasHeightForWidth())
        TemplateDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(TemplateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scroll_area = QtWidgets.QScrollArea(TemplateDialog)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.wid1 = QtWidgets.QWidget()
        self.wid1.setObjectName("wid1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.wid1)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.color_layout = QtWidgets.QWidget(self.wid1)
        self.color_layout.setObjectName("color_layout")
        self.gridlayout = QtWidgets.QGridLayout(self.color_layout)
        self.gridlayout.setObjectName("gridlayout")
        self.colored_field_label = QtWidgets.QLabel(self.color_layout)
        self.colored_field_label.setObjectName("colored_field_label")
        self.gridlayout.addWidget(self.colored_field_label, 0, 0, 1, 1)
        self.colored_field = QtWidgets.QComboBox(self.color_layout)
        self.colored_field.setObjectName("colored_field")
        self.gridlayout.addWidget(self.colored_field, 0, 1, 1, 1)
        self.color_chooser_label = QtWidgets.QLabel(self.color_layout)
        self.color_chooser_label.setObjectName("color_chooser_label")
        self.gridlayout.addWidget(self.color_chooser_label, 1, 0, 1, 1)
        self.color_name = ColorButton(self.color_layout)
        self.color_name.setObjectName("color_name")
        self.gridlayout.addWidget(self.color_name, 1, 1, 1, 1)
        self.color_copy_button = QtWidgets.QToolButton(self.color_layout)
        icon = QtGui.QIcon.ic("edit-copy.png")
        self.color_copy_button.setIcon(icon)
        self.color_copy_button.setObjectName("color_copy_button")
        self.gridlayout.addWidget(self.color_copy_button, 1, 2, 1, 1)
        self.verticalLayout1.addWidget(self.color_layout)
        self.icon_layout = QtWidgets.QWidget(self.wid1)
        self.icon_layout.setObjectName("icon_layout")
        self.gridlayout1 = QtWidgets.QGridLayout(self.icon_layout)
        self.gridlayout1.setObjectName("gridlayout1")
        self.icon_kind_layout = QtWidgets.QHBoxLayout()
        self.icon_kind_layout.setObjectName("icon_kind_layout")
        self.icon_kind_label = QtWidgets.QLabel(self.icon_layout)
        self.icon_kind_label.setObjectName("icon_kind_label")
        self.icon_kind_layout.addWidget(self.icon_kind_label)
        self.icon_kind = QtWidgets.QComboBox(self.icon_layout)
        self.icon_kind.setObjectName("icon_kind")
        self.icon_kind_layout.addWidget(self.icon_kind)
        self.gridlayout1.addLayout(self.icon_kind_layout, 0, 0, 1, 2)
        self.icon_chooser_label = QtWidgets.QLabel(self.icon_layout)
        self.icon_chooser_label.setObjectName("icon_chooser_label")
        self.gridlayout1.addWidget(self.icon_chooser_label, 1, 0, 1, 1)
        self.icon_field = QtWidgets.QComboBox(self.icon_layout)
        self.icon_field.setObjectName("icon_field")
        self.gridlayout1.addWidget(self.icon_field, 1, 1, 1, 1)
        self.image_chooser_label = QtWidgets.QLabel(self.icon_layout)
        self.image_chooser_label.setObjectName("image_chooser_label")
        self.gridlayout1.addWidget(self.image_chooser_label, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.icon_layout)
        self.widget.setObjectName("widget")
        self.icon_select_layout = QtWidgets.QHBoxLayout(self.widget)
        self.icon_select_layout.setObjectName("icon_select_layout")
        self.icon_files = QtWidgets.QComboBox(self.widget)
        self.icon_files.setObjectName("icon_files")
        self.icon_select_layout.addWidget(self.icon_files)
        self.icon_copy_button = QtWidgets.QToolButton(self.widget)
        self.icon_copy_button.setIcon(icon)
        self.icon_copy_button.setObjectName("icon_copy_button")
        self.icon_select_layout.addWidget(self.icon_copy_button)
        self.filename_button = QtWidgets.QPushButton(self.widget)
        self.filename_button.setObjectName("filename_button")
        self.icon_select_layout.addWidget(self.filename_button)
        self.gridlayout1.addWidget(self.widget, 2, 1, 1, 1)
        self.verticalLayout1.addWidget(self.icon_layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.template_name_label = QtWidgets.QLabel(self.wid1)
        self.template_name_label.setObjectName("template_name_label")
        self.hboxlayout.addWidget(self.template_name_label)
        self.template_name = QtWidgets.QComboBox(self.wid1)
        self.template_name.setEditable(True)
        self.template_name.setObjectName("template_name")
        self.hboxlayout.addWidget(self.template_name)
        self.gridLayout.addLayout(self.hboxlayout, 0, 0, 1, 1)
        self.lowlayout = FlowLayout()
        self.lowlayout.setObjectName("lowlayout")
        self.label = QtWidgets.QLabel(self.wid1)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.lowlayout.addWidget(self.label)
        self.label1 = QtWidgets.QLabel(self.wid1)
        self.label1.setObjectName("label1")
        self.lowlayout.addWidget(self.label1)
        self.break_box = QtWidgets.QCheckBox(self.wid1)
        self.break_box.setObjectName("break_box")
        self.lowlayout.addWidget(self.break_box)
        self.eparator = Separator(self.wid1)
        self.eparator.setObjectName("eparator")
        self.lowlayout.addWidget(self.eparator)
        self.go_button = QtWidgets.QToolButton(self.wid1)
        icon1 = QtGui.QIcon.ic("sync-right.png")
        self.go_button.setIcon(icon1)
        self.go_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.go_button.setObjectName("go_button")
        self.lowlayout.addWidget(self.go_button)
        self.eparator1 = Separator(self.wid1)
        self.eparator1.setObjectName("eparator1")
        self.lowlayout.addWidget(self.eparator1)
        self.breakpoint_line_box_label = QtWidgets.QLabel(self.wid1)
        self.breakpoint_line_box_label.setObjectName("breakpoint_line_box_label")
        self.lowlayout.addWidget(self.breakpoint_line_box_label)
        self.breakpoint_line_box = QtWidgets.QSpinBox(self.wid1)
        self.breakpoint_line_box.setMinimum(1)
        self.breakpoint_line_box.setMaximum(999)
        self.breakpoint_line_box.setProperty("value", 1)
        self.breakpoint_line_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.breakpoint_line_box.setObjectName("breakpoint_line_box")
        self.lowlayout.addWidget(self.breakpoint_line_box)
        self.toggle_button = QtWidgets.QToolButton(self.wid1)
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        icon2 = QtGui.QIcon.ic("swap.png")
        self.toggle_button.setIcon(icon2)
        self.toggle_button.setObjectName("toggle_button")
        self.lowlayout.addWidget(self.toggle_button)
        self.eparator2 = Separator(self.wid1)
        self.eparator2.setObjectName("eparator2")
        self.lowlayout.addWidget(self.eparator2)
        self.remove_all_button = QtWidgets.QToolButton(self.wid1)
        self.remove_all_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        icon3 = QtGui.QIcon.ic("list_remove.png")
        self.remove_all_button.setIcon(icon3)
        self.remove_all_button.setObjectName("remove_all_button")
        self.lowlayout.addWidget(self.remove_all_button)
        self.set_all_button = QtWidgets.QToolButton(self.wid1)
        self.set_all_button.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        icon4 = QtGui.QIcon.ic("plus.png")
        self.set_all_button.setIcon(icon4)
        self.set_all_button.setObjectName("set_all_button")
        self.lowlayout.addWidget(self.set_all_button)
        self.gridLayout.addLayout(self.lowlayout, 1, 0, 1, 3)
        self.textbox = CodeEditor(self.wid1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy)
        self.textbox.setObjectName("textbox")
        self.gridLayout.addWidget(self.textbox, 2, 0, 1, 3)
        self.new_doc_label = QtWidgets.QLabel(self.wid1)
        self.new_doc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.new_doc_label.setObjectName("new_doc_label")
        self.gridLayout.addWidget(self.new_doc_label, 3, 0, 1, 1)
        self.new_doc = QtWidgets.QTextEdit(self.wid1)
        self.new_doc.setObjectName("new_doc")
        self.gridLayout.addWidget(self.new_doc, 4, 0, 1, 3)
        self.label2 = QtWidgets.QLabel(self.wid1)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 7, 0, 1, 1)
        self.template_value = QtWidgets.QTableWidget(self.wid1)
        self.template_value.setObjectName("template_value")
        self.template_value.setColumnCount(0)
        self.template_value.setRowCount(0)
        self.gridLayout.addWidget(self.template_value, 8, 0, 1, 3)
        self.user_label_1 = QtWidgets.QLabel(self.wid1)
        self.user_label_1.setVisible(False)
        self.user_label_1.setObjectName("user_label_1")
        self.gridLayout.addWidget(self.user_label_1, 11, 0, 1, 1)
        self.user_layout_1 = BoxLayout()
        self.user_layout_1.setObjectName("user_layout_1")
        self.gridLayout.addLayout(self.user_layout_1, 11, 1, 1, 1)
        self.user_label_2 = QtWidgets.QLabel(self.wid1)
        self.user_label_2.setVisible(False)
        self.user_label_2.setObjectName("user_label_2")
        self.gridLayout.addWidget(self.user_label_2, 12, 0, 1, 1)
        self.user_layout_2 = BoxLayout()
        self.user_layout_2.setObjectName("user_layout_2")
        self.gridLayout.addLayout(self.user_layout_2, 12, 1, 1, 1)
        self.user_label_3 = QtWidgets.QLabel(self.wid1)
        self.user_label_3.setVisible(False)
        self.user_label_3.setObjectName("user_label_3")
        self.gridLayout.addWidget(self.user_label_3, 13, 0, 1, 1)
        self.user_layout_3 = BoxLayout()
        self.user_layout_3.setObjectName("user_layout_3")
        self.gridLayout.addLayout(self.user_layout_3, 13, 1, 1, 1)
        self.user_label_4 = QtWidgets.QLabel(self.wid1)
        self.user_label_4.setVisible(False)
        self.user_label_4.setObjectName("user_label_4")
        self.gridLayout.addWidget(self.user_label_4, 14, 0, 1, 1)
        self.user_layout_4 = BoxLayout()
        self.user_layout_4.setObjectName("user_layout_4")
        self.gridLayout.addLayout(self.user_layout_4, 14, 1, 1, 1)
        self.user_label_5 = QtWidgets.QLabel(self.wid1)
        self.user_label_5.setVisible(False)
        self.user_label_5.setObjectName("user_label_5")
        self.gridLayout.addWidget(self.user_label_5, 15, 0, 1, 1)
        self.user_layout_5 = BoxLayout()
        self.user_layout_5.setObjectName("user_layout_5")
        self.gridLayout.addLayout(self.user_layout_5, 15, 1, 1, 1)
        self.user_label_6 = QtWidgets.QLabel(self.wid1)
        self.user_label_6.setVisible(False)
        self.user_label_6.setObjectName("user_label_6")
        self.gridLayout.addWidget(self.user_label_6, 16, 0, 1, 1)
        self.user_layout_6 = BoxLayout()
        self.user_layout_6.setObjectName("user_layout_6")
        self.gridLayout.addLayout(self.user_layout_6, 16, 1, 1, 1)
        self.user_label_7 = QtWidgets.QLabel(self.wid1)
        self.user_label_7.setVisible(False)
        self.user_label_7.setObjectName("user_label_7")
        self.gridLayout.addWidget(self.user_label_7, 17, 0, 1, 1)
        self.user_layout_7 = BoxLayout()
        self.user_layout_7.setObjectName("user_layout_7")
        self.gridLayout.addLayout(self.user_layout_7, 17, 1, 1, 1)
        self.user_label_8 = QtWidgets.QLabel(self.wid1)
        self.user_label_8.setVisible(False)
        self.user_label_8.setObjectName("user_label_8")
        self.gridLayout.addWidget(self.user_label_8, 18, 0, 1, 1)
        self.user_layout_8 = BoxLayout()
        self.user_layout_8.setObjectName("user_layout_8")
        self.gridLayout.addLayout(self.user_layout_8, 18, 1, 1, 1)
        self.user_label_9 = QtWidgets.QLabel(self.wid1)
        self.user_label_9.setVisible(False)
        self.user_label_9.setObjectName("user_label_9")
        self.gridLayout.addWidget(self.user_label_9, 19, 0, 1, 1)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.font_name_label = QtWidgets.QLabel(self.wid1)
        self.font_name_label.setObjectName("font_name_label")
        self.hboxlayout1.addWidget(self.font_name_label)
        self.font_box = QtWidgets.QFontComboBox(self.wid1)
        self.font_box.setObjectName("font_box")
        self.hboxlayout1.addWidget(self.font_box)
        self.font_size_label = QtWidgets.QLabel(self.wid1)
        self.font_size_label.setObjectName("font_size_label")
        self.hboxlayout1.addWidget(self.font_size_label)
        self.font_size_box = QtWidgets.QSpinBox(self.wid1)
        self.font_size_box.setObjectName("font_size_box")
        self.hboxlayout1.addWidget(self.font_size_box)
        self.frame = QtWidgets.QFrame(self.wid1)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.hboxlayout1.addWidget(self.frame)
        self.load_button = QtWidgets.QToolButton(self.wid1)
        self.load_button.setObjectName("load_button")
        self.hboxlayout1.addWidget(self.load_button)
        self.save_button = QtWidgets.QToolButton(self.wid1)
        self.save_button.setObjectName("save_button")
        self.hboxlayout1.addWidget(self.save_button)
        self.frame1 = QtWidgets.QFrame(self.wid1)
        self.frame1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame1.setLineWidth(3)
        self.frame1.setObjectName("frame1")
        self.hboxlayout1.addWidget(self.frame1)
        spacerItem = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.wid1)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hboxlayout1.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.hboxlayout1, 24, 0, 1, 3)
        self.frame2 = QtWidgets.QFrame(self.wid1)
        self.frame2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.frame2.setObjectName("frame2")
        self.gridLayout.addWidget(self.frame2, 25, 0, 1, 3)
        self.gridlayout2 = QtWidgets.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")
        self.label3 = QtWidgets.QLabel(self.wid1)
        self.label3.setObjectName("label3")
        self.gridlayout2.addWidget(self.label3, 0, 0, 1, 2)
        self.label4 = QtWidgets.QLabel(self.wid1)
        self.label4.setObjectName("label4")
        self.gridlayout2.addWidget(self.label4, 1, 0, 1, 1)
        self.function = QtWidgets.QComboBox(self.wid1)
        self.function.setObjectName("function")
        self.gridlayout2.addWidget(self.function, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.wid1)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_22.setObjectName("label_22")
        self.gridlayout2.addWidget(self.label_22, 2, 0, 1, 1)
        self.func_type = QtWidgets.QLineEdit(self.wid1)
        self.func_type.setReadOnly(True)
        self.func_type.setObjectName("func_type")
        self.gridlayout2.addWidget(self.func_type, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.wid1)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2, 3, 0, 1, 1)
        self.documentation = QtWidgets.QPlainTextEdit(self.wid1)
        self.documentation.setMaximumSize(QtCore.QSize(16777215, 75))
        self.documentation.setObjectName("documentation")
        self.gridlayout2.addWidget(self.documentation, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.wid1)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridlayout2.addWidget(self.label_3, 4, 0, 1, 1)
        self.source_code = QtWidgets.QPlainTextEdit(self.wid1)
        self.source_code.setMaximumSize(QtCore.QSize(16777215, 75))
        self.source_code.setObjectName("source_code")
        self.gridlayout2.addWidget(self.source_code, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridlayout2, 30, 0, 1, 3)
        self.template_tutorial = QtWidgets.QLabel(self.wid1)
        self.template_tutorial.setOpenExternalLinks(True)
        self.template_tutorial.setObjectName("template_tutorial")
        self.gridLayout.addWidget(self.template_tutorial, 27, 1, 1, 1)
        self.template_func_reference = QtWidgets.QLabel(self.wid1)
        self.template_func_reference.setOpenExternalLinks(True)
        self.template_func_reference.setObjectName("template_func_reference")
        self.gridLayout.addWidget(self.template_func_reference, 28, 1, 1, 1)
        self.verticalLayout1.addLayout(self.gridLayout)
        self.scroll_area.setWidget(self.wid1)
        self.verticalLayout.addWidget(self.scroll_area)
        self.colored_field_label.setBuddy(self.colored_field)
        self.color_chooser_label.setBuddy(self.color_name)
        self.icon_chooser_label.setBuddy(self.icon_field)
        self.image_chooser_label.setBuddy(self.icon_files)
        self.template_name_label.setBuddy(self.template_name)
        self.label.setBuddy(self.textbox)
        self.eparator.setBuddy(self.go_button)
        self.eparator1.setBuddy(self.go_button)
        self.breakpoint_line_box_label.setBuddy(self.breakpoint_line_box)
        self.eparator2.setBuddy(self.go_button)
        self.new_doc_label.setBuddy(self.new_doc)
        self.label2.setBuddy(self.template_value)
        self.user_label_1.setBuddy(self.template_value)
        self.user_label_2.setBuddy(self.template_value)
        self.user_label_3.setBuddy(self.template_value)
        self.user_label_4.setBuddy(self.template_value)
        self.user_label_5.setBuddy(self.template_value)
        self.user_label_6.setBuddy(self.template_value)
        self.user_label_7.setBuddy(self.template_value)
        self.user_label_8.setBuddy(self.template_value)
        self.user_label_9.setBuddy(self.template_value)
        self.font_name_label.setBuddy(self.font_box)
        self.font_size_label.setBuddy(self.font_size_box)
        self.label4.setBuddy(self.function)
        self.label_22.setBuddy(self.func_type)
        self.label_2.setBuddy(self.documentation)
        self.label_3.setBuddy(self.source_code)

        self.retranslateUi(TemplateDialog)
        self.buttonBox.accepted.connect(TemplateDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(TemplateDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TemplateDialog)

    def retranslateUi(self, TemplateDialog):

        TemplateDialog.setWindowTitle(_("Edit template"))
        self.colored_field_label.setText(_("Set the color of the column:"))
        self.color_chooser_label.setText(_("Copy a color name to the clipboard:"))
        self.color_copy_button.setToolTip(_("Copy the selected color name to the clipboard"))
        self.icon_kind_label.setText(_("Kind:"))
        self.icon_chooser_label.setText(_("Apply the icon to column:"))
        self.image_chooser_label.setText(_("Copy an icon file name to the clipboard:"))
        self.icon_files.setToolTip(_("<p>The template must return the name of the icon file\n"
"                to display. If you wish to display multiple icons, separate the\n"
"                individual icon file names with a \':\' (colon). They will all be\n"
"                displayed in the column</p>"))
        self.icon_copy_button.setToolTip(_("Copy the selected icon file name to the clipboard"))
        self.filename_button.setText(_("Add icon"))
        self.filename_button.setToolTip(_("Add an icon file to the set of choices"))
        self.template_name_label.setText(_("Template &name:"))
        self.template_name.setToolTip(_("The name of the callable template"))
        self.label.setText(_("T&emplate:"))
        self.label.setToolTip(_("The text of the template program goes into the box below"))
        self.label1.setText(_("        "))
        self.break_box.setText(_("Enable &breakpoints"))
        self.break_box.setToolTip(_("<p>If checked, the template evaluator will stop when it\n"
"evaluates an expression on a double-clicked line number, opening a dialog showing\n"
"you the value as well as all the local variables</p>"))
        self.go_button.setText(_("&Go"))
        self.go_button.setToolTip(_("If \'Enable breakpoints\' is checked then click this button to run your template"))
        self.breakpoint_line_box_label.setText(_("&Line:"))
        self.breakpoint_line_box_label.setToolTip(_("Line number to toggle"))
        self.breakpoint_line_box.setToolTip(_("Line number to toggle"))
        self.toggle_button.setText(_("&Toggle"))
        self.toggle_button.setToolTip(_("Toggle the breakpoint on the line number in the box"))
        self.remove_all_button.setText(_("&Remove all"))
        self.remove_all_button.setToolTip(_("Remove all breakpoints"))
        self.set_all_button.setText(_("&Set all"))
        self.set_all_button.setToolTip(_("Set breakpoint on every line"))
        self.textbox.setToolTip(_("<p>The text of the template program goes in this box.\n"
"            A General Program Mode template must begin with the word \"program:\".\n"
"            A Python template must begin with the word \"python:\" followed by a\n"
"            function definition line. There is a context menu item you can use\n"
"            to enter the first lines of a Python template.</p>"))
        self.new_doc_label.setText(_("D&ocumentation:"))
        self.new_doc.setToolTip(_("Documentation for the function being defined or edited"))
        self.label2.setText(_("Template value:"))
        self.label2.setToolTip(_("The value of the template using the current book in the library view"))
        self.user_label_1.setText(_("User label"))
        self.user_label_2.setText(_("User label"))
        self.user_label_3.setText(_("User label"))
        self.user_label_4.setText(_("User label"))
        self.user_label_5.setText(_("User label"))
        self.user_label_6.setText(_("User label"))
        self.user_label_7.setText(_("User label"))
        self.user_label_8.setText(_("User label"))
        self.user_label_9.setText(_("User label"))
        self.font_name_label.setText(_("Font:"))
        self.font_box.setToolTip(_("Select the font for the Template box"))
        self.font_size_label.setText(_("Size:"))
        self.font_size_box.setToolTip(_("Select the font size for the Template box"))
        self.load_button.setText(_("Lo&ad"))
        self.load_button.setToolTip(_("Load the template from a file"))
        self.save_button.setText(_("Sa&ve"))
        self.save_button.setToolTip(_("Save the template in a file"))
        self.label3.setText(_("Template Function Reference"))
        self.label4.setText(_("Function &name:"))
        self.label_22.setText(_("&Function type:"))
        self.label_2.setText(_("&Documentation:"))
        self.label_3.setText(_("&Code:"))
from calibre.gui2.dialogs.template_dialog_box_layout import BoxLayout
from calibre.gui2.dialogs.template_dialog_code_widget import CodeEditor
from calibre.gui2.widgets2 import ColorButton, FlowLayout, Separator
