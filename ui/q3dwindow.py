# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\ui\q3dwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Q3DWindow(object):
    def setupUi(self, Q3DWindow):
        Q3DWindow.setObjectName("Q3DWindow")
        Q3DWindow.resize(757, 580)
        Q3DWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(Q3DWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = Q3DView(self.centralwidget)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        Q3DWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Q3DWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        self.menuScene = QtWidgets.QMenu(self.menubar)
        self.menuScene.setObjectName("menuScene")
        self.menuCamera = QtWidgets.QMenu(self.menuScene)
        self.menuCamera.setObjectName("menuCamera")
        self.menuControls = QtWidgets.QMenu(self.menuScene)
        self.menuControls.setObjectName("menuControls")
        self.menuDecorations = QtWidgets.QMenu(self.menuScene)
        self.menuDecorations.setObjectName("menuDecorations")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuPanels = QtWidgets.QMenu(self.menuWindow)
        self.menuPanels.setObjectName("menuPanels")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSaveAs = QtWidgets.QMenu(self.menuFile)
        self.menuSaveAs.setObjectName("menuSaveAs")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setToolTipsVisible(True)
        self.menuHelp.setObjectName("menuHelp")
        Q3DWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Q3DWindow)
        self.statusbar.setObjectName("statusbar")
        Q3DWindow.setStatusBar(self.statusbar)
        self.dockWidgetLayers = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetLayers.setObjectName("dockWidgetLayers")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView = Q3DTreeView(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.dockWidgetLayers.setWidget(self.dockWidgetContents)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLayers)
        self.dockWidgetConsole = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetConsole.setFloating(False)
        self.dockWidgetConsole.setObjectName("dockWidgetConsole")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidgetDebugView = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listWidgetDebugView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listWidgetDebugView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidgetDebugView.setObjectName("listWidgetDebugView")
        self.verticalLayout_3.addWidget(self.listWidgetDebugView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditInputBox = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEditInputBox.setObjectName("lineEditInputBox")
        self.horizontalLayout.addWidget(self.lineEditInputBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.dockWidgetConsole.setWidget(self.dockWidgetContents_2)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetConsole)
        self.actionSaveAsSTL = QtWidgets.QAction(Q3DWindow)
        self.actionSaveAsSTL.setEnabled(False)
        self.actionSaveAsSTL.setObjectName("actionSaveAsSTL")
        self.actionSceneSettings = QtWidgets.QAction(Q3DWindow)
        self.actionSceneSettings.setObjectName("actionSceneSettings")
        self.actionPerspective = QtWidgets.QAction(Q3DWindow)
        self.actionPerspective.setCheckable(True)
        self.actionPerspective.setChecked(True)
        self.actionPerspective.setObjectName("actionPerspective")
        self.actionOrthographic = QtWidgets.QAction(Q3DWindow)
        self.actionOrthographic.setCheckable(True)
        self.actionOrthographic.setObjectName("actionOrthographic")
        self.actionReload = QtWidgets.QAction(Q3DWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionAlwaysOnTop = QtWidgets.QAction(Q3DWindow)
        self.actionAlwaysOnTop.setCheckable(True)
        self.actionAlwaysOnTop.setChecked(False)
        self.actionAlwaysOnTop.setObjectName("actionAlwaysOnTop")
        self.actionExportToWeb = QtWidgets.QAction(Q3DWindow)
        self.actionExportToWeb.setEnabled(True)
        self.actionExportToWeb.setObjectName("actionExportToWeb")
        self.actionSaveAsImage = QtWidgets.QAction(Q3DWindow)
        self.actionSaveAsImage.setObjectName("actionSaveAsImage")
        self.actionResetCameraPosition = QtWidgets.QAction(Q3DWindow)
        self.actionResetCameraPosition.setObjectName("actionResetCameraPosition")
        self.actionOrbit = QtWidgets.QAction(Q3DWindow)
        self.actionOrbit.setCheckable(True)
        self.actionOrbit.setChecked(True)
        self.actionOrbit.setEnabled(False)
        self.actionOrbit.setObjectName("actionOrbit")
        self.actionLayer_Panel = QtWidgets.QAction(Q3DWindow)
        self.actionLayer_Panel.setCheckable(True)
        self.actionLayer_Panel.setChecked(True)
        self.actionLayer_Panel.setEnabled(False)
        self.actionLayer_Panel.setObjectName("actionLayer_Panel")
        self.actionCloseExporter = QtWidgets.QAction(Q3DWindow)
        self.actionCloseExporter.setObjectName("actionCloseExporter")
        self.actionPluginSettings = QtWidgets.QAction(Q3DWindow)
        self.actionPluginSettings.setObjectName("actionPluginSettings")
        self.actionHelp = QtWidgets.QAction(Q3DWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHomePage = QtWidgets.QAction(Q3DWindow)
        self.actionHomePage.setObjectName("actionHomePage")
        self.actionSendFeedback = QtWidgets.QAction(Q3DWindow)
        self.actionSendFeedback.setObjectName("actionSendFeedback")
        self.actionAbout = QtWidgets.QAction(Q3DWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSaveAsOBJ = QtWidgets.QAction(Q3DWindow)
        self.actionSaveAsOBJ.setEnabled(False)
        self.actionSaveAsOBJ.setObjectName("actionSaveAsOBJ")
        self.actionSaveAsGLTF = QtWidgets.QAction(Q3DWindow)
        self.actionSaveAsGLTF.setObjectName("actionSaveAsGLTF")
        self.actionClearAllSettings = QtWidgets.QAction(Q3DWindow)
        self.actionClearAllSettings.setObjectName("actionClearAllSettings")
        self.actionConsoleCopy = QtWidgets.QAction(Q3DWindow)
        self.actionConsoleCopy.setObjectName("actionConsoleCopy")
        self.actionConsoleClear = QtWidgets.QAction(Q3DWindow)
        self.actionConsoleClear.setObjectName("actionConsoleClear")
        self.actionNorthArrow = QtWidgets.QAction(Q3DWindow)
        self.actionNorthArrow.setObjectName("actionNorthArrow")
        self.actionFooterLabel = QtWidgets.QAction(Q3DWindow)
        self.actionFooterLabel.setObjectName("actionFooterLabel")
        self.menuCamera.addAction(self.actionPerspective)
        self.menuCamera.addAction(self.actionOrthographic)
        self.menuControls.addAction(self.actionOrbit)
        self.menuDecorations.addAction(self.actionNorthArrow)
        self.menuDecorations.addAction(self.actionFooterLabel)
        self.menuScene.addAction(self.actionSceneSettings)
        self.menuScene.addAction(self.menuCamera.menuAction())
        self.menuScene.addAction(self.menuControls.menuAction())
        self.menuScene.addAction(self.menuDecorations.menuAction())
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.actionClearAllSettings)
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.actionReload)
        self.menuScene.addAction(self.actionResetCameraPosition)
        self.menuWindow.addAction(self.menuPanels.menuAction())
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAlwaysOnTop)
        self.menuSaveAs.addAction(self.actionSaveAsImage)
        self.menuSaveAs.addSeparator()
        self.menuSaveAs.addAction(self.actionSaveAsGLTF)
        self.menuFile.addAction(self.actionExportToWeb)
        self.menuFile.addAction(self.menuSaveAs.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPluginSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCloseExporter)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHomePage)
        self.menuHelp.addAction(self.actionSendFeedback)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScene.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Q3DWindow)
        self.actionCloseExporter.triggered.connect(Q3DWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Q3DWindow)

    def retranslateUi(self, Q3DWindow):
        _translate = QtCore.QCoreApplication.translate
        Q3DWindow.setWindowTitle(_translate("Q3DWindow", "Qgis2threejs Exporter"))
        self.menuScene.setTitle(_translate("Q3DWindow", "&Scene"))
        self.menuCamera.setTitle(_translate("Q3DWindow", "Camera"))
        self.menuControls.setTitle(_translate("Q3DWindow", "Controls"))
        self.menuDecorations.setTitle(_translate("Q3DWindow", "Decorations"))
        self.menuWindow.setTitle(_translate("Q3DWindow", "&Window"))
        self.menuPanels.setTitle(_translate("Q3DWindow", "Panels"))
        self.menuFile.setTitle(_translate("Q3DWindow", "&File"))
        self.menuSaveAs.setTitle(_translate("Q3DWindow", "Save Scene As"))
        self.menuHelp.setTitle(_translate("Q3DWindow", "&Help"))
        self.dockWidgetLayers.setWindowTitle(_translate("Q3DWindow", "Layers"))
        self.dockWidgetConsole.setWindowTitle(_translate("Q3DWindow", "Console"))
        self.label.setText(_translate("Q3DWindow", ">>>"))
        self.actionSaveAsSTL.setText(_translate("Q3DWindow", "STL (.stl)"))
        self.actionSceneSettings.setText(_translate("Q3DWindow", "Scene Settings..."))
        self.actionPerspective.setText(_translate("Q3DWindow", "Perspective"))
        self.actionOrthographic.setText(_translate("Q3DWindow", "Orthographic"))
        self.actionReload.setText(_translate("Q3DWindow", "Reload"))
        self.actionReload.setShortcut(_translate("Q3DWindow", "F5"))
        self.actionAlwaysOnTop.setText(_translate("Q3DWindow", "Always on Top"))
        self.actionExportToWeb.setText(_translate("Q3DWindow", "Export to Web..."))
        self.actionSaveAsImage.setText(_translate("Q3DWindow", "Image (.png)"))
        self.actionResetCameraPosition.setText(_translate("Q3DWindow", "Reset Camera Position"))
        self.actionResetCameraPosition.setShortcut(_translate("Q3DWindow", "Shift+R"))
        self.actionOrbit.setText(_translate("Q3DWindow", "Orbit"))
        self.actionLayer_Panel.setText(_translate("Q3DWindow", "Layer Panel"))
        self.actionCloseExporter.setText(_translate("Q3DWindow", "Close Exporter"))
        self.actionPluginSettings.setText(_translate("Q3DWindow", "Exporter Settings.."))
        self.actionHelp.setText(_translate("Q3DWindow", "&Help"))
        self.actionHelp.setToolTip(_translate("Q3DWindow", "Open plugin document in default browser."))
        self.actionHomePage.setText(_translate("Q3DWindow", "Plugin Home Page"))
        self.actionHomePage.setToolTip(_translate("Q3DWindow", "Open plugin homepage in default browser."))
        self.actionSendFeedback.setText(_translate("Q3DWindow", "Send Feedback"))
        self.actionSendFeedback.setToolTip(_translate("Q3DWindow", "Open plugin issue tracking system in default browser."))
        self.actionAbout.setText(_translate("Q3DWindow", "About Qgis2threejs Plugin"))
        self.actionAbout.setToolTip(_translate("Q3DWindow", "Display this plugin version."))
        self.actionSaveAsOBJ.setText(_translate("Q3DWindow", "Wavefront (.obj)"))
        self.actionSaveAsGLTF.setText(_translate("Q3DWindow", "glTF (.gltf, .glb)"))
        self.actionClearAllSettings.setText(_translate("Q3DWindow", "Clear All Settings"))
        self.actionConsoleCopy.setText(_translate("Q3DWindow", "Copy"))
        self.actionConsoleClear.setText(_translate("Q3DWindow", "Clear"))
        self.actionNorthArrow.setText(_translate("Q3DWindow", "North Arrow"))
        self.actionFooterLabel.setText(_translate("Q3DWindow", "Footer Label"))

from Qgis2threejs.q3dtreeview import Q3DTreeView
from Qgis2threejs.q3dview import Q3DView
