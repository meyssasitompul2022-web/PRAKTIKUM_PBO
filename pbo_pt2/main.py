class DataKontak:
    def __init__(self, no_hp, alamat):
        self.no_hp = no_hp
        self.alamat = alamat

    def tampilkan_kontak(self):
        print("No. HP       :", self.no_hp)
        print("Alamat       :", self.alamat)


class Pelanggan:
    jumlah_pelanggan = 0

    def __init__(self, id_pelanggan, nama, no_hp, alamat):
        self.__id_pelanggan = id_pelanggan
        self._nama = nama
        self.kontak = DataKontak(no_hp, alamat)

        Pelanggan.jumlah_pelanggan += 1

    def tampilkan_info(self):
        print("ID Pelanggan :", self.__id_pelanggan)
        print("Nama         :", self._nama)
        self.kontak.tampilkan_kontak()

    def get_id(self):
        return self.__id_pelanggan


class PelangganVIP(Pelanggan):

    def __init__(
        self,
        id_pelanggan,
        nama,
        no_hp,
        alamat,
        diskon_khusus
    ):
        super().__init__(
            id_pelanggan,
            nama,
            no_hp,
            alamat
        )

        self.diskon_khusus = diskon_khusus

    def tampilkan_info(self):
        print("ID Pelanggan :", self.get_id())
        print("Nama         :", self._nama)
        print("Jenis        : VIP")
        print("Diskon       :", self.diskon_khusus, "%")
        self.kontak.tampilkan_kontak()


class PelangganBiasa(Pelanggan):

    def __init__(
        self,
        id_pelanggan,
        nama,
        no_hp,
        alamat,
        status_member
    ):
        super().__init__(
            id_pelanggan,
            nama,
            no_hp,
            alamat
        )

        self.status_member = status_member

    def tampilkan_info(self):
        print("ID Pelanggan :", self.get_id())
        print("Nama         :", self._nama)
        print("Jenis        : Biasa")
        print("Status       :", self.status_member)
        self.kontak.tampilkan_kontak()


class Paket:
    nama_layanan = "Photobox"
    total_paket = 0
    status_layanan = "Aktif"

    def __init__(self, nama_paket, durasi, harga):
        self.nama_paket = nama_paket
        self.durasi = durasi
        self.harga = harga

        Paket.total_paket += 1

    def tampilkan_paket(self):
        print("Paket        :", self.nama_paket)
        print("Durasi       :", self.durasi, "menit")
        print("Harga        : Rp", self.harga)

    @classmethod
    def ubah_status_layanan(cls, status):
        cls.status_layanan = status

    @staticmethod
    def cek_harga(harga):
        if harga > 0:
            return True
        else:
            return False


class Transaksi:
    jumlah_transaksi = 0

    def __init__(self, id_transaksi, pelanggan, paket):
        self.id_transaksi = id_transaksi
        self.pelanggan = pelanggan
        self.paket = paket

        Transaksi.jumlah_transaksi += 1

    def hitung_total(self):
        total = self.paket.harga

        if hasattr(self.pelanggan, "diskon_khusus"):
            diskon = (
                total
                * self.pelanggan.diskon_khusus
                / 100
            )

            total = total - diskon

        return total

    def tampilkan_transaksi(self):
        print("ID Transaksi :", self.id_transaksi)
        print("Pelanggan    :", self.pelanggan._nama)
        print("Paket        :", self.paket.nama_paket)
        print("Durasi       :", self.paket.durasi, "menit")
        print("Harga        : Rp", self.paket.harga)
        print("Total Bayar  : Rp", self.hitung_total())



pelanggan1 = PelangganVIP(
    "P001",
    "Meyssa",
    "08123456789",
    "Samarinda",
    10
)

pelanggan2 = PelangganBiasa(
    "P002",
    "Reguel",
    "08234567890",
    "Samarinda",
    "Aktif"
)


paket1 = Paket(
    "Silver",
    30,
    50000
)

paket2 = Paket(
    "Gold",
    60,
    90000
)

paket3 = Paket(
    "Platinum",
    90,
    130000
)

paket4 = Paket(
    "Diamond",
    120,
    170000
)


transaksi1 = Transaksi(
    "TR001",
    pelanggan1,
    paket2
)

transaksi2 = Transaksi(
    "TR002",
    pelanggan2,
    paket1
)


print("==============================================")
print("       SISTEM LAYANAN PHOTOBOX")
print("==============================================")


print("\nDATA PELANGGAN")
print("----------------------------------------------")

print("\nPelanggan 1")
print("----------------------------------------------")
pelanggan1.tampilkan_info()

print("\nPelanggan 2")
print("----------------------------------------------")
pelanggan2.tampilkan_info()

print("\nDATA PAKET PHOTOBOX")
print("----------------------------------------------")

print("\nPaket 1")
print("----------------------------------------------")
paket1.tampilkan_paket()

print("\nPaket 2")
print("----------------------------------------------")
paket2.tampilkan_paket()

print("\nPaket 3")
print("----------------------------------------------")
paket3.tampilkan_paket()

print("\nPaket 4")
print("----------------------------------------------")
paket4.tampilkan_paket()

print("\nDATA TRANSAKSI")
print("----------------------------------------------")

print("\nTransaksi 1")
print("----------------------------------------------")
transaksi1.tampilkan_transaksi()

print("\nTransaksi 2")
print("----------------------------------------------")
transaksi2.tampilkan_transaksi()

print("\n==============================================")
print("              INFORMASI SISTEM")
print("==============================================")

print("Nama Layanan     :", Paket.nama_layanan)
print("Total Paket      :", Paket.total_paket)
print("Status Layanan   :", Paket.status_layanan)
print("Jumlah Pelanggan :", Pelanggan.jumlah_pelanggan)
print("Jumlah Transaksi :", Transaksi.jumlah_transaksi)

print("\n==============================================")
print("             PROGRAM SELESAI")
print("==============================================")