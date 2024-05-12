from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui
from giris_ui import Ui_MainWindow
from kayit import KayitSayfa
from veritabani import Veritabani
from ana import AnaSayfa
from onlinekitap import Kullanici

class arayuz(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtprogram = Ui_MainWindow()
        self.qtprogram.setupUi(self)
        self.qtprogram.girisButon.clicked.connect(self.girisyap)
        kayitsayfa = KayitSayfa()
        
        self.qtprogram.kayitButon.clicked.connect(lambda: kayitsayfa.show())

    def girisyap(self):
        kullaniciadi = self.qtprogram.kullaniciAdiLine.text()
        sifre = self.qtprogram.sifreLine.text()
        Veritabani.query('SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?', (kullaniciadi, sifre))
        uyesql = Veritabani.fetchone()

        if uyesql is None:
            
            msg = QMessageBox()
            msg.setText("Kullanıcı adı veya şifre yanlış.")
            msg.setWindowTitle("Giriş")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()
            return
        
        uye = Kullanici(*uyesql)

        self.anasayfa = AnaSayfa(uye)
        self.anasayfa.show()
        self.close()


app = QApplication([])
pencere = arayuz()
pencere.show()
app.exec_()