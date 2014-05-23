# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scatterPlot.ui'
#
# Created: Thu Aug 11 10:42:48 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScatterPlotDialog(object):
    def setupUi(self, ScatterPlotDialog):
        ScatterPlotDialog.setObjectName(_fromUtf8("ScatterPlotDialog"))
        ScatterPlotDialog.resize(378, 167)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScatterPlotDialog.sizePolicy().hasHeightForWidth())
        ScatterPlotDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/programIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScatterPlotDialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ScatterPlotDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(ScatterPlotDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName(_fromUtf8("lblFigureWidth"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblFigureWidth)
        self.spinFigWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigWidth.sizePolicy().hasHeightForWidth())
        self.spinFigWidth.setSizePolicy(sizePolicy)
        self.spinFigWidth.setDecimals(2)
        self.spinFigWidth.setMinimum(0.5)
        self.spinFigWidth.setMaximum(20.0)
        self.spinFigWidth.setSingleStep(0.5)
        self.spinFigWidth.setProperty(_fromUtf8("value"), 6.0)
        self.spinFigWidth.setObjectName(_fromUtf8("spinFigWidth"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinFigWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName(_fromUtf8("lblFigureHeight"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblFigureHeight)
        self.spinFigHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigHeight.sizePolicy().hasHeightForWidth())
        self.spinFigHeight.setSizePolicy(sizePolicy)
        self.spinFigHeight.setMinimum(0.5)
        self.spinFigHeight.setMaximum(20.0)
        self.spinFigHeight.setSingleStep(0.05)
        self.spinFigHeight.setProperty(_fromUtf8("value"), 6.0)
        self.spinFigHeight.setObjectName(_fromUtf8("spinFigHeight"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinFigHeight)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(ScatterPlotDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.chkShowHistogram = QtGui.QCheckBox(self.groupBox)
        self.chkShowHistogram.setObjectName(_fromUtf8("chkShowHistogram"))
        self.verticalLayout_4.addWidget(self.chkShowHistogram)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinNumBins = QtGui.QSpinBox(self.groupBox)
        self.spinNumBins.setMaximum(1000)
        self.spinNumBins.setObjectName(_fromUtf8("spinNumBins"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinNumBins)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinHistogramSize = QtGui.QDoubleSpinBox(self.groupBox)
        self.spinHistogramSize.setMaximum(6.0)
        self.spinHistogramSize.setSingleStep(0.25)
        self.spinHistogramSize.setObjectName(_fromUtf8("spinHistogramSize"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinHistogramSize)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chkShowCIs = QtGui.QCheckBox(ScatterPlotDialog)
        self.chkShowCIs.setChecked(True)
        self.chkShowCIs.setObjectName(_fromUtf8("chkShowCIs"))
        self.verticalLayout_3.addWidget(self.chkShowCIs)
        self.chkShowR2 = QtGui.QCheckBox(ScatterPlotDialog)
        self.chkShowR2.setChecked(True)
        self.chkShowR2.setObjectName(_fromUtf8("chkShowR2"))
        self.verticalLayout_3.addWidget(self.chkShowR2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(ScatterPlotDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinMarkerSize = QtGui.QSpinBox(ScatterPlotDialog)
        self.spinMarkerSize.setMinimum(1)
        self.spinMarkerSize.setMaximum(100)
        self.spinMarkerSize.setProperty(_fromUtf8("value"), 20)
        self.spinMarkerSize.setObjectName(_fromUtf8("spinMarkerSize"))
        self.horizontalLayout_2.addWidget(self.spinMarkerSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(ScatterPlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ScatterPlotDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ScatterPlotDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ScatterPlotDialog.reject)
        QtCore.QObject.connect(self.chkShowHistogram, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinNumBins.setEnabled)
        QtCore.QObject.connect(self.chkShowHistogram, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.spinHistogramSize.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ScatterPlotDialog)

    def retranslateUi(self, ScatterPlotDialog):
        ScatterPlotDialog.setWindowTitle(QtGui.QApplication.translate("ScatterPlotDialog", "Scatter plot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ScatterPlotDialog", "Figure size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureWidth.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureHeight.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ScatterPlotDialog", "Histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowHistogram.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Show histograms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Bins:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowCIs.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Show CIs", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowR2.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Show R2 value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScatterPlotDialog", "Marker size:", None, QtGui.QApplication.UnicodeUTF8))
