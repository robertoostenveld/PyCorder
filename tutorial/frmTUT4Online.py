# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmTUT4Online.ui'
#
# Created: Tue Feb 01 09:09:18 2011
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmTUT4Online(object):
    def setupUi(self, frmTUT4Online):
        frmTUT4Online.setObjectName("frmTUT4Online")
        frmTUT4Online.resize(400, 142)
        frmTUT4Online.setFrameShape(QtGui.QFrame.Panel)
        frmTUT4Online.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(frmTUT4Online)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(frmTUT4Online)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ResetAll = QtGui.QPushButton(self.groupBox)
        self.pushButton_ResetAll.setObjectName("pushButton_ResetAll")
        self.horizontalLayout.addWidget(self.pushButton_ResetAll)
        self.pushButton_SetAll = QtGui.QPushButton(self.groupBox)
        self.pushButton_SetAll.setObjectName("pushButton_SetAll")
        self.horizontalLayout.addWidget(self.pushButton_SetAll)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox7 = QtGui.QCheckBox(self.groupBox)
        self.checkBox7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox7.setObjectName("checkBox7")
        self.horizontalLayout_2.addWidget(self.checkBox7)
        self.checkBox6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox6.setObjectName("checkBox6")
        self.horizontalLayout_2.addWidget(self.checkBox6)
        self.checkBox5 = QtGui.QCheckBox(self.groupBox)
        self.checkBox5.setObjectName("checkBox5")
        self.horizontalLayout_2.addWidget(self.checkBox5)
        self.checkBox4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox4.setObjectName("checkBox4")
        self.horizontalLayout_2.addWidget(self.checkBox4)
        self.checkBox3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox3.setObjectName("checkBox3")
        self.horizontalLayout_2.addWidget(self.checkBox3)
        self.checkBox2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox2.setObjectName("checkBox2")
        self.horizontalLayout_2.addWidget(self.checkBox2)
        self.checkBox1 = QtGui.QCheckBox(self.groupBox)
        self.checkBox1.setObjectName("checkBox1")
        self.horizontalLayout_2.addWidget(self.checkBox1)
        self.checkBox0 = QtGui.QCheckBox(self.groupBox)
        self.checkBox0.setObjectName("checkBox0")
        self.horizontalLayout_2.addWidget(self.checkBox0)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.MyButton = QtGui.QRadioButton(self.groupBox)
        self.MyButton.setEnabled(True)
        self.MyButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MyButton.setCheckable(True)
        self.MyButton.setChecked(False)
        self.MyButton.setObjectName("MyButton")
        self.gridLayout.addWidget(self.MyButton, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(frmTUT4Online)
        QtCore.QMetaObject.connectSlotsByName(frmTUT4Online)

    def retranslateUi(self, frmTUT4Online):
        frmTUT4Online.setWindowTitle(QtGui.QApplication.translate("frmTUT4Online", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmTUT4Online", "Trigger Out / My Button", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ResetAll.setText(QtGui.QApplication.translate("frmTUT4Online", "Reset All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SetAll.setText(QtGui.QApplication.translate("frmTUT4Online", "Set All", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox7.setText(QtGui.QApplication.translate("frmTUT4Online", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox6.setText(QtGui.QApplication.translate("frmTUT4Online", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox5.setText(QtGui.QApplication.translate("frmTUT4Online", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox4.setText(QtGui.QApplication.translate("frmTUT4Online", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox3.setText(QtGui.QApplication.translate("frmTUT4Online", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox2.setText(QtGui.QApplication.translate("frmTUT4Online", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox1.setText(QtGui.QApplication.translate("frmTUT4Online", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox0.setText(QtGui.QApplication.translate("frmTUT4Online", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.MyButton.setText(QtGui.QApplication.translate("frmTUT4Online", "\"My Button\" Indicator", None, QtGui.QApplication.UnicodeUTF8))

