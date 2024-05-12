from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal
from kitapoku_ui import Ui_Form
from onlinekitap import Icerik
from veritabani import Veritabani

class KitapOkuSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.index = 0
        self.form.sonrakiButon.clicked.connect(self.sonraki)
        self.form.oncekiButon.clicked.connect(self.onceki)

    def goster(self, kitap):
        Veritabani.query("select * from kitapicerik where kitapid=?",(kitap.id,))
        icerikler = Veritabani.fetchall()
        self.icerikler = []
        for icerik in icerikler:
            icerikk = Icerik(*icerik)
            self.icerikler.append(icerikk)
        self.index = 0
        self.icerikguncelle()
        self.show()

    def sonraki(self):
        self.index += 1
        if len(self.icerikler) == self.index:
            self.index = len(self.icerikler)-1
            return
        self.icerikguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = 0
            return
        self.icerikguncelle()

    def icerikguncelle(self):
        icerik = next((icerikk for icerikk in self.icerikler if icerikk.sayfa == (self.index+1)), None)
        self.form.aciklamaLabel.setText(icerik.icerik)
        self.form.sayfa.setText(f"Sayfa: {self.index+1}/{len(self.icerikler)}")