# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/elias/PycharmProjects/mpvQC/gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainPlayerView(object):
    def setupUi(self, MainPlayerView):
        MainPlayerView.setObjectName("MainPlayerView")
        MainPlayerView.resize(800, 600)
        self.mainWindowContentWidget = QtWidgets.QWidget(MainPlayerView)
        self.mainWindowContentWidget.setObjectName("mainWindowContentWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindowContentWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainWindowContentSplitter = QtWidgets.QSplitter(self.mainWindowContentWidget)
        self.mainWindowContentSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mainWindowContentSplitter.setObjectName("mainWindowContentSplitter")
        self.verticalLayout.addWidget(self.mainWindowContentSplitter)
        MainPlayerView.setCentralWidget(self.mainWindowContentWidget)
        self.mainWindowMenuBar = QtWidgets.QMenuBar(MainPlayerView)
        self.mainWindowMenuBar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.mainWindowMenuBar.setObjectName("mainWindowMenuBar")
        self.mainWindowFileMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowFileMenu.setObjectName("mainWindowFileMenu")
        self.mainWindowVideoMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowVideoMenu.setObjectName("mainWindowVideoMenu")
        self.mainWindowSettingsMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowSettingsMenu.setObjectName("mainWindowSettingsMenu")
        self.mainWindowAboutMenu = QtWidgets.QMenu(self.mainWindowMenuBar)
        self.mainWindowAboutMenu.setObjectName("mainWindowAboutMenu")
        MainPlayerView.setMenuBar(self.mainWindowMenuBar)
        self.actionNewQcDocument = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("add")
        self.actionNewQcDocument.setIcon(icon)
        self.actionNewQcDocument.setObjectName("actionNewQcDocument")
        self.actionOpenQcDocuments = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("open-for-editing")
        self.actionOpenQcDocuments.setIcon(icon)
        self.actionOpenQcDocuments.setObjectName("actionOpenQcDocuments")
        self.actionSaveQcDocument = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("filesave")
        self.actionSaveQcDocument.setIcon(icon)
        self.actionSaveQcDocument.setObjectName("actionSaveQcDocument")
        self.actionSaveQcDocumentAs = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("filesaveas")
        self.actionSaveQcDocumentAs.setIcon(icon)
        self.actionSaveQcDocumentAs.setObjectName("actionSaveQcDocumentAs")
        self.actionExitMpvQc = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("exit")
        self.actionExitMpvQc.setIcon(icon)
        self.actionExitMpvQc.setObjectName("actionExitMpvQc")
        self.actionOpenVideoFile = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("mpv")
        self.actionOpenVideoFile.setIcon(icon)
        self.actionOpenVideoFile.setObjectName("actionOpenVideoFile")
        self.actionOpenNetworkStream = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("network-server")
        self.actionOpenNetworkStream.setIcon(icon)
        self.actionOpenNetworkStream.setObjectName("actionOpenNetworkStream")
        self.actionResizeVideoToOriginalResolution = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("itmages-resize")
        self.actionResizeVideoToOriginalResolution.setIcon(icon)
        self.actionResizeVideoToOriginalResolution.setObjectName("actionResizeVideoToOriginalResolution")
        self.actionCheckForUpdates = QtWidgets.QAction(MainPlayerView)
        self.actionCheckForUpdates.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("arrow-down")
        self.actionCheckForUpdates.setIcon(icon)
        self.actionCheckForUpdates.setObjectName("actionCheckForUpdates")
        self.actionAboutQt = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAboutQt.setIcon(icon)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionAboutMpvQc = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAboutMpvQc.setIcon(icon)
        self.actionAboutMpvQc.setObjectName("actionAboutMpvQc")
        self.actionSettings = QtWidgets.QAction(MainPlayerView)
        icon = QtGui.QIcon.fromTheme("systemsettings")
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionOpenSubtitleFile = QtWidgets.QAction(MainPlayerView)
        self.actionOpenSubtitleFile.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("gnome-subtitles")
        self.actionOpenSubtitleFile.setIcon(icon)
        self.actionOpenSubtitleFile.setObjectName("actionOpenSubtitleFile")
        self.mainWindowFileMenu.addAction(self.actionNewQcDocument)
        self.mainWindowFileMenu.addAction(self.actionOpenQcDocuments)
        self.mainWindowFileMenu.addAction(self.actionSaveQcDocument)
        self.mainWindowFileMenu.addAction(self.actionSaveQcDocumentAs)
        self.mainWindowFileMenu.addSeparator()
        self.mainWindowFileMenu.addAction(self.actionExitMpvQc)
        self.mainWindowVideoMenu.addAction(self.actionOpenVideoFile)
        self.mainWindowVideoMenu.addAction(self.actionOpenSubtitleFile)
        self.mainWindowVideoMenu.addAction(self.actionOpenNetworkStream)
        self.mainWindowVideoMenu.addSeparator()
        self.mainWindowVideoMenu.addAction(self.actionResizeVideoToOriginalResolution)
        self.mainWindowSettingsMenu.addAction(self.actionSettings)
        self.mainWindowAboutMenu.addAction(self.actionAboutQt)
        self.mainWindowAboutMenu.addAction(self.actionAboutMpvQc)
        self.mainWindowMenuBar.addAction(self.mainWindowFileMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowVideoMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowSettingsMenu.menuAction())
        self.mainWindowMenuBar.addAction(self.mainWindowAboutMenu.menuAction())

        self.retranslateUi(MainPlayerView)
        QtCore.QMetaObject.connectSlotsByName(MainPlayerView)

    def retranslateUi(self, MainPlayerView):
        _translate = QtCore.QCoreApplication.translate
        MainPlayerView.setWindowTitle(_translate("MainPlayerView", "MainWindow"))
        self.mainWindowFileMenu.setTitle(_translate("MainPlayerView", "&File"))
        self.mainWindowVideoMenu.setTitle(_translate("MainPlayerView", "Vi&deo"))
        self.mainWindowSettingsMenu.setTitle(_translate("MainPlayerView", "Optio&ns"))
        self.mainWindowAboutMenu.setTitle(_translate("MainPlayerView", "Abo&ut"))
        self.actionNewQcDocument.setText(_translate("MainPlayerView", "&New QC document"))
        self.actionNewQcDocument.setShortcut(_translate("MainPlayerView", "Ctrl+N"))
        self.actionOpenQcDocuments.setText(_translate("MainPlayerView", "&Open QC document(s) ..."))
        self.actionOpenQcDocuments.setShortcut(_translate("MainPlayerView", "Ctrl+O"))
        self.actionSaveQcDocument.setText(_translate("MainPlayerView", "&Save QC document"))
        self.actionSaveQcDocument.setShortcut(_translate("MainPlayerView", "Ctrl+S"))
        self.actionSaveQcDocumentAs.setText(_translate("MainPlayerView", "S&ave QC document as ..."))
        self.actionSaveQcDocumentAs.setShortcut(_translate("MainPlayerView", "Ctrl+Shift+S"))
        self.actionExitMpvQc.setText(_translate("MainPlayerView", "&Exit mpvQC"))
        self.actionExitMpvQc.setShortcut(_translate("MainPlayerView", "Ctrl+Q"))
        self.actionOpenVideoFile.setText(_translate("MainPlayerView", "Open &video ..."))
        self.actionOpenVideoFile.setShortcut(_translate("MainPlayerView", "Ctrl+Shift+O"))
        self.actionOpenNetworkStream.setText(_translate("MainPlayerView", "Open &network stream ..."))
        self.actionOpenNetworkStream.setShortcut(_translate("MainPlayerView", "Ctrl+Alt+Shift+O"))
        self.actionResizeVideoToOriginalResolution.setText(_translate("MainPlayerView", "&Resize video to original resolution"))
        self.actionResizeVideoToOriginalResolution.setShortcut(_translate("MainPlayerView", "Ctrl+R"))
        self.actionCheckForUpdates.setText(_translate("MainPlayerView", "&Check For Updates ..."))
        self.actionAboutQt.setText(_translate("MainPlayerView", "About &Qt"))
        self.actionAboutMpvQc.setText(_translate("MainPlayerView", "About &mpvQC"))
        self.actionSettings.setText(_translate("MainPlayerView", "&Settings"))
        self.actionSettings.setShortcut(_translate("MainPlayerView", "Ctrl+Alt+S"))
        self.actionOpenSubtitleFile.setText(_translate("MainPlayerView", "&Open subtitle ..."))

