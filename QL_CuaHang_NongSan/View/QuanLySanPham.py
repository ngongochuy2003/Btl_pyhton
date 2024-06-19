# Form implementation generated from reading ui file 'QuanLySanPham.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

class Ui_Dialog(object):
    def __init__(self, main_window):
      self.main_window = main_window
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 695)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(270, 10, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.tblDuLieu = QtWidgets.QTableView(parent=Dialog)
        self.tblDuLieu.setGeometry(QtCore.QRect(0, 100, 911, 431))
        self.tblDuLieu.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tblDuLieu.setObjectName("tblDuLieu")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 80, 911, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 540, 911, 16))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnThemSanPham = QtWidgets.QPushButton(parent=Dialog)
        self.btnThemSanPham.setGeometry(QtCore.QRect(30, 580, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnThemSanPham.setFont(font)
        self.btnThemSanPham.setObjectName("btnThemSanPham")
        self.btnCapNhatSanPham = QtWidgets.QPushButton(parent=Dialog)
        self.btnCapNhatSanPham.setGeometry(QtCore.QRect(290, 580, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnCapNhatSanPham.setFont(font)
        self.btnCapNhatSanPham.setObjectName("btnCapNhatSanPham")
        self.btnXoaSanPham = QtWidgets.QPushButton(parent=Dialog)
        self.btnXoaSanPham.setGeometry(QtCore.QRect(550, 580, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnXoaSanPham.setFont(font)
        self.btnXoaSanPham.setObjectName("btnXoaSanPham")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(844, 642, 61, 51))
        self.btnQuayVe.setStyleSheet("")
        self.btnQuayVe.setText("")
        self.btnQuayVe.setObjectName("btnQuayVe")
        self.Favicon = QtWidgets.QLabel(parent=Dialog)
        self.Favicon.setGeometry(QtCore.QRect(10, 10, 131, 71))
        self.Favicon.setText("")
        self.Favicon.setObjectName("Favicon")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

#==================================CSS=========================================
        #CSS Label
        self.label.setStyleSheet("""
                    color: #FF4500;
                    font-weight: bold;
                """)

        #CSS Favicon
        pixamp = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixamp)
        self.Favicon.setScaledContents(True)

        #CSS Icon Button

        self.btnThemSanPham.setIcon(QIcon("../Access/Icon/plus.png"))
        self.btnThemSanPham.setIconSize(QSize(40,40))
        self.btnXoaSanPham.setIcon(QIcon("../Access/Icon/delete.png"))
        self.btnXoaSanPham.setIconSize(QSize(40,40))
        self.btnCapNhatSanPham.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnCapNhatSanPham.setIconSize(QSize(40,40))
        self.btnQuayVe.setIcon(QIcon("../Access/Icon/back.png"))
        self.btnQuayVe.setIconSize(QSize(40,40))

        #CSS Button
        self.btnThemSanPham.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                            """)
        self.btnCapNhatSanPham.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                            """)
        self.btnXoaSanPham.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                         """)
        self.btnQuayVe.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 25px;
                                     """)
#==================================Sự Kiện======================================
        self.Dialog = Dialog
        self.btnQuayVe.clicked.connect(self.quayve)

#==================================Hàm==========================================

    def quayve(self):
      from UiAdmin import Ui_MainWindow
      self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
      self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      self.Dialog.hide()
#==============================================================================
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Quản Lý Danh Sách Sản Phẩm"))
        self.btnThemSanPham.setText(_translate("Dialog", "Thêm Sản Phẩm"))
        self.btnCapNhatSanPham.setText(_translate("Dialog", "Cập Nhật Sản Phẩm"))
        self.btnXoaSanPham.setText(_translate("Dialog", "Xoá Sản Phẩm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
