#!/usr/bin/env python3

import sys
from math import radians

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, \
    QLabel, QSlider
from Ui_KinematicScheme import Ui_KinematicScheme

from pivy.coin import SbColor, SbVec3f, \
    SoSeparator, SoTransform, \
    SoInput, SoDB
from pivy.gui.soqt import SoQt, SoQtExaminerViewer

import json

def loadFileWrl(filename):
    input = SoInput()
    if not input.openFile(filename):
        print("Ошибка открытия файла: {}".format(filename))
        return None
    graph = SoDB.readAll(input)
    input.closeFile()
    if graph == None:
        print("Ошибка чтения файла: {}".format(filename))
        return None
    return graph

def loadJoint(joint, separator):
    separator.addChild(loadFileWrl("{}.wrl".format(joint)))
    with open("joint.json") as file:
        transform = SoTransform()
        params = json.load(file)["parameterSets"][joint]
        translation = json.loads(params["translation"])
        transform.translation.setValue(translation)
        separator.addChild(transform)
        rotation = json.loads(params["rotation"])
        if rotation[0]:
            transform = SoTransform()
            transform.rotation.setValue(SbVec3f(1.0, 0.0, 0.0), radians(rotation[0]))
            separator.addChild(transform)
        if rotation[1]:
            transform = SoTransform()
            transform.rotation.setValue(SbVec3f(0.0, 1.0, 0.0), radians(rotation[1]))
            separator.addChild(transform)
        if rotation[2]:
            transform = SoTransform()
            transform.rotation.setValue(SbVec3f(0.0, 0.0, 1.0), radians(rotation[2]))
            separator.addChild(transform)
        transform = SoTransform()
        separator.addChild(transform)
        return transform

class KinematicScheme(QMainWindow):
    def __init__(self):
        super(KinematicScheme, self).__init__()
        self.initUi()
        self.initScheme()

    def initUi(self):
        SoQt.init(self)

        self.ui = Ui_KinematicScheme()
        self.ui.setupUi(self)

        self.viewer = SoQtExaminerViewer(self.ui.centralWidget)
        self.viewer.setBackgroundColor(SbColor(0.5, 0.5, 0.6))
        self.viewer.setDecoration(False)

    def initScheme(self):
        self.scene = SoSeparator()
        sceneTransform = SoTransform()
        sceneTransform.rotation.setValue(SbVec3f(1.0, 0.0, 0.0), radians(-90.0))
        self.scene.addChild(sceneTransform)
        self.addJoint(0)
        self.addJoint(1)
        self.addJoint(2)
        self.addJoint(3)
        self.addJoint(4)
        self.addJoint(5)
        self.viewer.setSceneGraph(self.scene)

    def addJoint(self, joint):
        transform = loadJoint("joint{}".format(joint), self.scene)
        def setAngleFor(tansform):
            def angleSetter(angle):
                transform.rotation.setValue(SbVec3f(0.0, 0.0, 1.0), radians(angle))
            return angleSetter;
        label = QLabel("A{}:".format(joint + 1))
        slider = QSlider(Qt.Horizontal)
        slider.setRange(-180, 180)
        slider.setValue(0)
        slider.valueChanged.connect(setAngleFor(transform))
        self.ui.rotationsLayout.addWidget(label, joint, 0)
        self.ui.rotationsLayout.addWidget(slider, joint, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = KinematicScheme()
    window.show()

    sys.exit(app.exec_())
