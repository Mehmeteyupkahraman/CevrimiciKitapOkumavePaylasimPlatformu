from veritabani import Veritabani

class Kullanici:
    def __init__(self, id, kullaniciadi, sifre, ad, soyad, telefon):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES (?, ?, ?, ?, ?)", (kullaniciadi, sifre, ad, soyad, telefon))

    def kitap_ekle(self, kitap):
        Veritabani.query("INSERT INTO kitaplistem (kullaniciid, kitapid) VALUES (?, ?)", (self.id, kitap.id))

    def kitap_sil(self, kitap):
        Veritabani.query("DELETE FROM kitaplistem WHERE kullaniciid = ? and kitapid = ?", (self.id, kitap.id))

class Kitap:
    def __init__ (self, id, ad, yazar, yayinevi, tur, fotograf, aciklama):
        self.id = id
        self.yazar = yazar
        self.ad = ad
        self.yayinevi = yayinevi
        self.tur = tur
        self.fotograf = fotograf
        self.aciklama = aciklama

    def yorum_yap(self, uye, yorum):
        Veritabani.query("INSERT INTO yorumlar (kullaniciid, kitapid, yorum) VALUES (?, ?, ?)", (uye.id, self.id, yorum))

    @staticmethod
    def olustur(ad, yazar, yayinevi, tur, aciklama):
        Veritabani.query("INSERT INTO kitaplar (ad, yazar, yayinevi, tur, fotograf, aciklama) VALUES (?, ?, ?, ?, ?, ?)", (ad, yazar, yayinevi, tur, 'kitap.jpg', aciklama))
    
class Icerik:
    def __init__(self, id , kitapid, sayfa, icerik):
        self.id = id
        self.kitapid = kitapid
        self.sayfa = sayfa
        self.icerik = icerik