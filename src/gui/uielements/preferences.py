# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/elias/PycharmProjects/mpvQC/gui/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyKF5.KWidgetsAddons import KEditListWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 668, 502))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.authorLabel = QtWidgets.QLabel(self.widget)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.widget)
        self.authorLineEdit.setPlaceholderText("")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.kCommentTypes = KEditListWidget(self.widget)
        self.kCommentTypes.setToolTip("")
        self.kCommentTypes.setCheckAtEntering(True)
        self.kCommentTypes.setObjectName("kCommentTypes")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.kCommentTypes)
        self.verticalLayout_2.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.autoSaveEnabledCheckBox_4 = QtWidgets.QCheckBox(self.tab)
        self.autoSaveEnabledCheckBox_4.setChecked(True)
        self.autoSaveEnabledCheckBox_4.setObjectName("autoSaveEnabledCheckBox_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.autoSaveEnabledCheckBox_4)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.autosaveSpinBox_4 = QtWidgets.QSpinBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autosaveSpinBox_4.sizePolicy().hasHeightForWidth())
        self.autosaveSpinBox_4.setSizePolicy(sizePolicy)
        self.autosaveSpinBox_4.setMaximum(1000)
        self.autosaveSpinBox_4.setObjectName("autosaveSpinBox_4")
        self.horizontalLayout_5.addWidget(self.autosaveSpinBox_4)
        self.autosaveTimeUnit_4 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autosaveTimeUnit_4.sizePolicy().hasHeightForWidth())
        self.autosaveTimeUnit_4.setSizePolicy(sizePolicy)
        self.autosaveTimeUnit_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.autosaveTimeUnit_4.setObjectName("autosaveTimeUnit_4")
        self.horizontalLayout_5.addWidget(self.autosaveTimeUnit_4)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget_2)
        self.saveNickNameCheckBox = QtWidgets.QCheckBox(self.tab)
        self.saveNickNameCheckBox.setObjectName("saveNickNameCheckBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.saveNickNameCheckBox)
        self.saveVideoPathCheckBox = QtWidgets.QCheckBox(self.tab)
        self.saveVideoPathCheckBox.setObjectName("saveVideoPathCheckBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.saveVideoPathCheckBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mpv_conf_plain_text_edit = QtWidgets.QPlainTextEdit(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.mpv_conf_plain_text_edit.setFont(font)
        self.mpv_conf_plain_text_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mpv_conf_plain_text_edit.setObjectName("mpv_conf_plain_text_edit")
        self.horizontalLayout_2.addWidget(self.mpv_conf_plain_text_edit)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_conf_plain_text_edit = QtWidgets.QPlainTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.input_conf_plain_text_edit.setFont(font)
        self.input_conf_plain_text_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.input_conf_plain_text_edit.setObjectName("input_conf_plain_text_edit")
        self.horizontalLayout_3.addWidget(self.input_conf_plain_text_edit)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setKerning(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Apply | QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.autoSaveEnabledCheckBox_4.toggled['bool'].connect(self.widget_2.setEnabled)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Language"))
        self.comboBox.setItemText(0, _translate("Dialog", "English"))
        self.comboBox.setItemText(1, _translate("Dialog", "German"))
        self.authorLabel.setText(_translate("Dialog", "Nick name"))
        self.label.setText(_translate("Dialog", "Comment types"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "MPV QC"))
        self.autoSaveEnabledCheckBox_4.setText(_translate("Dialog", "Auto save enabled"))
        self.label_6.setText(_translate("Dialog", "each"))
        self.autosaveTimeUnit_4.setText(_translate("Dialog", "seconds"))
        self.saveNickNameCheckBox.setText(_translate("Dialog", "Save nick name to QC document"))
        self.saveVideoPathCheckBox.setText(_translate("Dialog", "Save video path to QC document"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "QC Document"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "mpv.conf"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "input.conf"))
