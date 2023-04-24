import English, Vietnamese, French, Italia, Spanish, StringtoPDF

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 502, 101, 31))
        self.label.setObjectName("label")
        self.ngonngu = QtWidgets.QComboBox(self.centralwidget)
        self.ngonngu.setGeometry(QtCore.QRect(100, 500, 81, 31))
        self.ngonngu.setObjectName("ngonngu")
        self.ngonngu.addItem("")
        self.ngonngu.addItem("")
        self.ngonngu.addItem("")
        self.ngonngu.addItem("")
        self.ngonngu.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 531, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(110, 60, 571, 411))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 561, 391))
        self.label_3.setObjectName("label_3")
        self.chonhinhanh = QtWidgets.QPushButton(self.centralwidget)
        self.chonhinhanh.setGeometry(QtCore.QRect(460, 490, 91, 31))
        self.chonhinhanh.setObjectName("chonhinhanh")
        self.image_selected = False
        self.chuyendoi = QtWidgets.QPushButton(self.centralwidget)
        self.chuyendoi.setGeometry(QtCore.QRect(550, 490, 121, 31))
        self.chuyendoi.setObjectName("chuyendoi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.chonhinhanh.clicked.connect(self.openFileDialog)
        self.chuyendoi.clicked.connect(self.convert)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def openFileDialog(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Chọn hình ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            self.pixmap = QPixmap(filename)
            self.label_3.setPixmap(self.pixmap.scaled(self.label_3.width(), self.label_3.height()))
            self.image_selected = True
            self.image_location = filename

    # Hàm chuyển đổi hình ảnh sang PDF
    def convert(self):
        if not self.image_selected:
            # Hiển thị thông báo lỗi
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Lỗi")
            msg_box.setText("Bạn chưa chọn hình ảnh.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            choice = self.ngonngu.currentIndex()
            match choice:
                case 0:
                    self.text = English.convertToString(self.image_location)
                case 1:
                    self.text = Italia.convertToString(self.image_location)
                case 2:
                    self.text = Vietnamese.convertToString(self.image_location)
                case 3:
                    self.text = French.convertToString(self.image_location)
                case 4:
                    self.text = Spanish.convertToString(self.image_location)
            
            succeed = StringtoPDF.convertToPdf(self)
            if succeed:
                # Hiển thị thông báo thành công
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Thông tin")
                msg_box.setText("Lưu PDF thành công.")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chọn Ngôn Ngữ"))
        self.ngonngu.setItemText(0, _translate("MainWindow", "Tiếng Anh"))
        self.ngonngu.setItemText(1, _translate("MainWindow", "Tiếng Ý"))
        self.ngonngu.setItemText(2, _translate("MainWindow", "Tiếng Việt"))
        self.ngonngu.setItemText(3, _translate("MainWindow", "Tiếng Pháp"))
        self.ngonngu.setItemText(4, _translate("MainWindow", "Tây Ban Nha"))
        self.label_2.setText(_translate("MainWindow", "Chuyển đổi chữ viết tay sang text và lưu vào file PDF"))
        self.groupBox.setTitle(_translate("MainWindow", "hình ảnh"))
        
        self.chonhinhanh.setText(_translate("MainWindow", "Chọn hình ảnh"))
        self.chuyendoi.setText(_translate("MainWindow", "Chuyển đổi sang pdf"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
