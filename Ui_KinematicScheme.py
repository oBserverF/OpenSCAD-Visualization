# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KinematicScheme.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_KinematicScheme(object):
    def setupUi(self, KinematicScheme):
        if not KinematicScheme.objectName():
            KinematicScheme.setObjectName(u"KinematicScheme")
        KinematicScheme.resize(640, 480)
        self.centralWidget = QWidget(KinematicScheme)
        self.centralWidget.setObjectName(u"centralWidget")
        KinematicScheme.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(KinematicScheme)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        KinematicScheme.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(KinematicScheme)
        self.statusbar.setObjectName(u"statusbar")
        KinematicScheme.setStatusBar(self.statusbar)
        self.rotationsWidget = QDockWidget(KinematicScheme)
        self.rotationsWidget.setObjectName(u"rotationsWidget")
        self.rotationsWidget.setMinimumSize(QSize(200, 56))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rotationsLayout = QGridLayout()
        self.rotationsLayout.setObjectName(u"rotationsLayout")

        self.verticalLayout_2.addLayout(self.rotationsLayout)

        self.verticalSpacer = QSpacerItem(20, 386, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.rotationsWidget.setWidget(self.dockWidgetContents)
        KinematicScheme.addDockWidget(Qt.LeftDockWidgetArea, self.rotationsWidget)

        self.retranslateUi(KinematicScheme)

        QMetaObject.connectSlotsByName(KinematicScheme)
    # setupUi

    def retranslateUi(self, KinematicScheme):
        KinematicScheme.setWindowTitle(QCoreApplication.translate("KinematicScheme", u"\u041a\u0438\u043d\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0445\u0435\u043c\u0430", None))
        self.rotationsWidget.setWindowTitle(QCoreApplication.translate("KinematicScheme", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442\u044b", None))
    # retranslateUi

