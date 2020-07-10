import sys
from PyQt5 import QtWidgets,QtGui
def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Burası bir butondur.")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")
    etiket.move(200,30)
    buton.move(190,80)
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket1.setText("Burası bir yazıdır.")
    etiket1.move(200,50)
    pencere.setGeometry(100,100,500,500)
    etiket2.move(70,100)
    pencere.show()
    sys.exit(app.exec_())
Pencere()
