from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from kitapekle_ui import Ui_Form
from onlinekitap import Kitap

class KitapEkleSayfa(QWidget):
    ekle_sinyal = pyqtSignal(int)
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ekleButon.clicked.connect(self.ekle)
        
    def ekle(self):
        yanit = QMessageBox.warning(self,"Kitap Oluştur", "Kitap oluşturmak istediğinize emin misiniz?",QMessageBox.Yes,QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        kitapisim = self.form.kitapadi.text()
        aciklama = self.form.aciklama.toPlainText()
        yayinevi = self.form.yayinevi.text()
        yazar = self.form.yazaradi.text()
        tur = self.form.turBox.text()
        Kitap.olustur(kitapisim, yazar, yayinevi, tur, aciklama)
        self.ekle_sinyal.emit(0)
        yanit = QMessageBox.information(self,"Kitap Oluştur", "Kitap oluşturuldu.",QMessageBox.Ok)
        self.close()