class Paket:
    nama_layanan = "Photobox"
    total_paket = 0
    status_layanan = "Aktif"

    def __init__(self, nama_paket, durasi, harga):
        self.nama_paket = nama_paket
        self.durasi = durasi
        self.__harga = harga

        Paket.total_paket += 1

    def tampilkan_info(self):
        print("Nama Paket :", self.nama_paket)
        print("Durasi     :", self.durasi, "menit")
        print("Harga      : Rp", self.__harga)

    @property
    def harga(self):
        return self.__harga
    @harga.setter
    def harga(self, nilai):
        if nilai < 0:
            print("Harga tidak boleh negatif!")
        else:
            self.__harga = nilai
            print("Harga berhasil diperbarui.")

    @classmethod
    def ubah_status_layanan(cls, status):
        cls.status_layanan = status
        print("Status layanan :", cls.status_layanan)

    @staticmethod
    def cek_harga(harga):
        if harga > 0:
            return True
        else:
            return False


class Pelanggan:
    nama_usaha = "Photobox"
    total_pelanggan = 0
    status_pelanggan = "Aktif"

    def __init__(self, nama, umur, no_telepon):

        self.nama = nama
        self.umur = umur
        self.__no_telepon = no_telepon

        Pelanggan.total_pelanggan += 1

    def tampilkan_info(self):
        print("Nama       :", self.nama)
        print("Umur       :", self.umur)
        print("No Telepon :", self.__no_telepon)

    @property
    def no_telepon(self):
        return self.__no_telepon

    @no_telepon.setter
    def no_telepon(self, nomor):
        if nomor == "":
            print("Nomor telepon tidak boleh kosong!")
        elif not nomor.isdigit():
            print("Nomor telepon hanya boleh berisi angka!")
        else:
            self.__no_telepon = nomor
            print("Nomor telepon berhasil diperbarui.")

    @classmethod
    def ubah_status_pelanggan(cls, status):
        cls.status_pelanggan = status
        print("Status pelanggan :", cls.status_pelanggan)

    @staticmethod
    def cek_umur(umur):
        if umur >= 10:
            return True
        else:
            return False


class Transaksi:
    nama_layanan = "Photobox"
    total_transaksi = 0
    status_transaksi = "Diproses"

    def __init__(self, kode_transaksi, pelanggan, paket):
        self.kode_transaksi = kode_transaksi
        self.pelanggan = pelanggan
        self.paket = paket
        self.__status = "Diproses"

        Transaksi.total_transaksi += 1

    def tampilkan_transaksi(self):
        print("Kode Transaksi :", self.kode_transaksi)
        print("Pelanggan      :", self.pelanggan.nama)
        print("Paket          :", self.paket.nama_paket)
        print("Harga          : Rp", self.paket.harga)
        print("Status         :", self.__status)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, nilai):
        if nilai == "":
            print("Status tidak boleh kosong!")
        elif nilai not in ["Diproses", "Selesai", "Batal"]:
            print("Status tidak valid!")
        else:
            self.__status = nilai
            print("Status berhasil diperbarui.")

    @classmethod
    def ubah_status_transaksi(cls, status):
        cls.status_transaksi = status
        print("Status transaksi umum :", cls.status_transaksi)

    @staticmethod
    def hitung_diskon(harga, diskon):
        if diskon < 0 or diskon > 100:
            return "Diskon tidak valid"

        hasil = harga - (harga * diskon / 100)
        return hasil

print("==========================================")
print(" SISTEM PENGELOLAAN LAYANAN PHOTOBOX")
print("==========================================")

print("\n--- DATA PAKET ---")

paket1 = Paket("Silver", 30, 50000)
paket2 = Paket("Gold", 60, 90000)

paket1.tampilkan_info()
print()

paket2.tampilkan_info()

print("\nHarga paket Silver :", paket1.harga)

print("\n--- SETTER PAKET VALID ---")
paket1.harga = 55000
print("Harga baru :", paket1.harga)

print("\n--- SETTER PAKET TIDAK VALID ---")
paket1.harga = -10000

print("\n--- STATIC METHOD PAKET ---")
print("Apakah harga valid?", Paket.cek_harga(paket1.harga))

print("\n--- CLASS METHOD PAKET ---")
Paket.ubah_status_layanan("Sedang Beroperasi")

print("\n--- DATA PELANGGAN ---")

pelanggan1 = Pelanggan("Meyssa108", 19, "081234567890")
pelanggan2 = Pelanggan("Dirga115", 20, "082345678901")

pelanggan1.tampilkan_info()
print()

pelanggan2.tampilkan_info()

print("\nNomor telepon pelanggan 1 :", pelanggan1.no_telepon)
print("\n--- SETTER PELANGGAN VALID ---")
pelanggan1.no_telepon = "089876543210"
print("Nomor baru :", pelanggan1.no_telepon)

print("\n--- SETTER PELANGGAN TIDAK VALID ---")
pelanggan1.no_telepon = ""

print("\n--- STATIC METHOD PELANGGAN ---")
print("Apakah umur pelanggan valid?", Pelanggan.cek_umur(pelanggan1.umur))

print("\n--- CLASS METHOD PELANGGAN ---")
Pelanggan.ubah_status_pelanggan("Terdaftar")

print("\n--- DATA TRANSAKSI ---")

transaksi1 = Transaksi("TRX001", pelanggan1, paket1)
transaksi2 = Transaksi("TRX002", pelanggan2, paket2)

transaksi1.tampilkan_transaksi()
print()

transaksi2.tampilkan_transaksi()

print("\nStatus transaksi 1 :", transaksi1.status)

print("\n--- SETTER TRANSAKSI VALID ---")
transaksi1.status = "Selesai"
print("Status baru :", transaksi1.status)

print("\n--- SETTER TRANSAKSI TIDAK VALID ---")
transaksi1.status = "Sedang Diproses"

print("\n--- STATIC METHOD TRANSAKSI ---")
harga_setelah_diskon = Transaksi.hitung_diskon(90000, 10)
print("Harga setelah diskon 10% : Rp", harga_setelah_diskon)

print("\n--- CLASS METHOD TRANSAKSI ---")
Transaksi.ubah_status_transaksi("Selesai")

print("\n--- DATA JUMLAH ---")
print("Total paket      :", Paket.total_paket)
print("Total pelanggan  :", Pelanggan.total_pelanggan)
print("Total transaksi  :", Transaksi.total_transaksi)

print("\n==========================================")
print(" PROGRAM SELESAI")
print("==========================================")