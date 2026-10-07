# SISTEM PENGELOLAAN PAKET, PELANGGAN, DAN TRANSAKSI PADA LAYANAN PHOTOBOX

**Nama:** Meyssa Reguel Sitompul
**NIM:** 2509106108
**Mata Kuliah:** Pemrograman Berorientasi Objek

---

# 1. Deskripsi Program

Program ini merupakan sistem sederhana untuk mengelola layanan Photobox yang meliputi pengelolaan data pelanggan, paket Photobox, dan transaksi.

Program dibuat menggunakan bahasa pemrograman Python dengan menerapkan konsep Pemrograman Berorientasi Objek (PBO).

Konsep yang diterapkan dalam program ini meliputi:

* Class dan Object
* Atribut dan Method
* Class Attribute
* Instance Attribute
* Encapsulation
* Protected Attribute
* Private Attribute
* Relasi UML
* Asosiasi
* Agregasi
* Komposisi
* Inheritance
* Superclass dan Subclass
* Penggunaan `super()`
* Method Overriding

---

# 2. Tujuan Program

Tujuan dari pembuatan program ini adalah:

1. Membuat sistem sederhana untuk mengelola layanan Photobox.
2. Menerapkan konsep Pemrograman Berorientasi Objek menggunakan Python.
3. Menerapkan konsep Relasi UML pada program.
4. Menerapkan hubungan Asosiasi, Agregasi, dan Komposisi.
5. Menerapkan konsep Inheritance.
6. Membuat superclass dan minimal dua subclass.
7. Menerapkan penggunaan `super().__init__()`.
8. Menerapkan atribut Protected dan Private.
9. Menerapkan Method Overriding.
10. Menghubungkan data pelanggan, paket, dan transaksi dalam satu sistem.

---

# 3. Fitur Program

Program memiliki beberapa fitur utama, yaitu:

1. Menambahkan pelanggan.
2. Menampilkan data pelanggan.
3. Menambahkan paket Photobox.
4. Menampilkan daftar paket Photobox.
5. Membuat transaksi.
6. Menampilkan daftar transaksi.
7. Menghitung total pembayaran.
8. Memberikan diskon khusus kepada pelanggan VIP.
9. Menyediakan paket Photobox Silver, Gold, Platinum, dan Diamond.

---

# 4. Struktur Program

Program dibuat dalam satu file yaitu `main.py`.

Seluruh class, atribut, method, fungsi, dan menu program terdapat dalam satu file tersebut.

Program terdiri dari beberapa class utama.

## 4.1 Class DataKontak

Class `DataKontak` digunakan untuk menyimpan informasi kontak pelanggan.

Atribut yang digunakan:

* `no_hp`
* `alamat`

Class ini memiliki method `tampilkan_kontak()` yang digunakan untuk menampilkan nomor HP dan alamat pelanggan.

Class `DataKontak` digunakan sebagai bagian dari object `Pelanggan` sehingga menerapkan konsep Komposisi.

---

## 4.2 Class Pelanggan

Class `Pelanggan` merupakan superclass atau parent class dalam program.

Class ini digunakan untuk menyimpan data umum pelanggan.

Atribut yang digunakan:

* `__id_pelanggan`
* `_nama`
* `kontak`

Atribut `__id_pelanggan` merupakan atribut Private.

Atribut `_nama` merupakan atribut Protected.

Class `Pelanggan` memiliki method:

```python
tampilkan_info()
```

yang digunakan untuk menampilkan informasi pelanggan.

Class ini juga memiliki method:

```python
get_id()
```

yang digunakan untuk mendapatkan ID pelanggan karena atribut ID bersifat Private.

---

## 4.3 Class PelangganVIP

Class `PelangganVIP` merupakan subclass dari class `Pelanggan`.

Class ini digunakan untuk pelanggan yang mendapatkan fasilitas VIP.

Atribut tambahan yang dimiliki adalah:

```text
diskon_khusus
```

Atribut tersebut digunakan untuk menentukan persentase diskon yang diberikan kepada pelanggan VIP.

Class `PelangganVIP` menggunakan:

```python
super().__init__()
```

untuk memanggil constructor dari superclass `Pelanggan`.

Class ini juga melakukan Method Overriding terhadap method:

```python
tampilkan_info()
```

Informasi yang ditampilkan oleh pelanggan VIP memiliki tambahan jenis pelanggan dan diskon khusus.

---

## 4.4 Class PelangganBiasa

Class `PelangganBiasa` merupakan subclass dari class `Pelanggan`.

Class ini digunakan untuk pelanggan biasa.

Atribut tambahan yang dimiliki adalah:

```text
status_member
```

Atribut tersebut digunakan untuk menyimpan status membership pelanggan.

Class `PelangganBiasa` juga menggunakan:

```python
super().__init__()
```

untuk memanggil constructor dari superclass `Pelanggan`.

Class ini melakukan Method Overriding terhadap method:

```python
tampilkan_info()
```

Informasi yang ditampilkan berbeda dengan pelanggan VIP karena menampilkan status member pelanggan biasa.

---

## 4.5 Class Paket

Class `Paket` digunakan untuk mengelola paket layanan Photobox.

Atribut yang digunakan antara lain:

* `nama_layanan`
* `total_paket`
* `status_layanan`
* `nama_paket`
* `durasi`
* `harga`

Program menyediakan empat paket awal, yaitu:

| Paket    |    Durasi |     Harga |
| -------- | --------: | --------: |
| Silver   |  30 menit |  Rp50.000 |
| Gold     |  60 menit |  Rp90.000 |
| Platinum |  90 menit | Rp130.000 |
| Diamond  | 120 menit | Rp170.000 |

Class `Paket` memiliki method:

```python
tampilkan_paket()
```

untuk menampilkan informasi paket.

Class ini juga memiliki class method:

```python
ubah_status_layanan()
```

dan static method:

```python
cek_harga()
```

---

## 4.6 Class Transaksi

Class `Transaksi` digunakan untuk mengelola transaksi Photobox.

Atribut yang digunakan:

* `id_transaksi`
* `pelanggan`
* `paket`

Class `Transaksi` memiliki method:

```python
hitung_total()
```

yang digunakan untuk menghitung total pembayaran.

Jika pelanggan merupakan pelanggan VIP, maka sistem akan menghitung diskon khusus.

Class ini juga memiliki method:

```python
tampilkan_transaksi()
```

untuk menampilkan detail transaksi.

---

# 5. Relasi UML

Program menerapkan tiga jenis Relasi UML sesuai dengan ketentuan posttest, yaitu Asosiasi, Agregasi, dan Komposisi.

---

## 5.1 Asosiasi

Asosiasi diterapkan antara class `Pelanggan` dan class `Transaksi`.

Pelanggan memiliki hubungan dengan transaksi karena seorang pelanggan dapat melakukan transaksi Photobox.

Pada class `Transaksi` terdapat atribut:

```python
self.pelanggan = pelanggan
```

Atribut tersebut menyimpan object pelanggan yang melakukan transaksi.

Hubungan ini merupakan Asosiasi karena object `Pelanggan` dan object `Transaksi` dapat berdiri secara terpisah.

---

## 5.2 Agregasi

Agregasi diterapkan antara class `Transaksi` dan class `Paket`.

Sebuah transaksi menggunakan sebuah paket Photobox.

Pada class `Transaksi` terdapat:

```python
self.paket = paket
```

Object `Paket` diberikan kepada object `Transaksi`.

Hubungan tersebut termasuk Agregasi karena paket dapat tetap digunakan walaupun sebuah transaksi sudah tidak digunakan.

Satu paket juga dapat digunakan oleh transaksi lainnya.

---

## 5.3 Komposisi

Komposisi diterapkan antara class `Pelanggan` dan class `DataKontak`.

Pada class `Pelanggan` terdapat:

```python
self.kontak = DataKontak(no_hp, alamat)
```

Object `DataKontak` dibuat sebagai bagian dari object `Pelanggan`.

Data kontak digunakan untuk menyimpan nomor HP dan alamat pelanggan.

Hubungan tersebut digunakan sebagai penerapan Komposisi karena `DataKontak` merupakan bagian dari object `Pelanggan`.

---

# 6. Inheritance

Inheritance digunakan untuk membuat hubungan pewarisan antara superclass dan subclass.

Superclass yang digunakan adalah:

```text
Pelanggan
```

Sedangkan subclass yang digunakan adalah:

```text
PelangganVIP
PelangganBiasa
```

Kedua subclass tersebut mewarisi atribut dan method dari class `Pelanggan`.

---

# 7. Superclass dan Subclass

Superclass dalam program adalah:

```python
class Pelanggan:
```

Subclass pertama:

```python
class PelangganVIP(Pelanggan):
```

Subclass kedua:

```python
class PelangganBiasa(Pelanggan):
```

Dengan demikian program telah memenuhi syarat minimal satu superclass dan minimal dua subclass.

---

# 8. Penggunaan super()

Kedua subclass menggunakan `super()` untuk memanggil constructor dari superclass.

Pada `PelangganVIP`:

```python
super().__init__(
    id_pelanggan,
    nama,
    no_hp,
    alamat
)
```

Pada `PelangganBiasa`:

```python
super().__init__(
    id_pelanggan,
    nama,
    no_hp,
    alamat
)
```

Penggunaan `super()` membuat subclass dapat menggunakan atribut yang telah dibuat pada superclass.

---

# 9. Atribut Tambahan pada Subclass

Setiap subclass memiliki atribut tambahan yang berbeda.

## PelangganVIP

Memiliki atribut:

```python
diskon_khusus
```

Atribut tersebut digunakan untuk memberikan diskon kepada pelanggan VIP.

## PelangganBiasa

Memiliki atribut:

```python
status_member
```

Atribut tersebut digunakan untuk menyimpan status membership pelanggan biasa.

Dengan demikian setiap subclass memiliki atribut spesifik yang membedakannya.

---

# 10. Method Overriding

Method Overriding diterapkan pada method:

```python
tampilkan_info()
```

Method tersebut pertama kali dibuat pada superclass `Pelanggan`.

Kemudian method tersebut dibuat kembali pada subclass `PelangganVIP` dan `PelangganBiasa`.

Pada `PelangganVIP`, method menampilkan informasi pelanggan VIP dan diskon khusus.

Pada `PelangganBiasa`, method menampilkan informasi pelanggan biasa dan status member.

Dengan demikian method yang sama memiliki perilaku yang berbeda sesuai dengan subclass yang digunakan.

---

# 11. Encapsulation

Program menerapkan Encapsulation dengan membatasi akses terhadap data tertentu.

Atribut Private yang digunakan adalah:

```python
self.__id_pelanggan
```

Atribut tersebut tidak dapat diakses secara langsung dari luar class `Pelanggan`.

Untuk mendapatkan ID pelanggan digunakan method:

```python
get_id()
```

Dengan demikian data ID pelanggan tetap terlindungi.

---

# 12. Protected Attribute

Program menggunakan atribut Protected:

```python
self._nama
```

Atribut tersebut digunakan untuk menyimpan nama pelanggan.

Atribut `_nama` dapat digunakan oleh subclass seperti `PelangganVIP` dan `PelangganBiasa`.

Contohnya:

```python
self._nama
```

Penggunaan satu garis bawah menunjukkan atribut tersebut bersifat Protected.

---

# 13. Private Attribute

Program menggunakan atribut Private:

```python
self.__id_pelanggan
```

Penggunaan dua garis bawah menunjukkan bahwa atribut tersebut bersifat Private.

Atribut tersebut hanya digunakan secara langsung di dalam class `Pelanggan`.

Untuk mengakses nilainya digunakan method:

```python
get_id()
```

---

# 14. Alur Program

Program dimulai dengan menjalankan fungsi `data_awal()`.

Fungsi tersebut membuat empat paket Photobox yang sudah tersedia, yaitu Silver, Gold, Platinum, dan Diamond.

Setelah data paket dibuat, program menjalankan fungsi `menu()`.

Pada menu utama terdapat tujuh pilihan.

Pilihan pertama adalah **Tambah Pelanggan**. Pengguna memasukkan ID pelanggan, nama, nomor HP, dan alamat. Setelah itu pengguna memilih jenis pelanggan, yaitu pelanggan VIP atau pelanggan biasa.

Jika pengguna memilih pelanggan VIP, sistem meminta diskon khusus. Data tersebut kemudian digunakan untuk membuat object `PelangganVIP`.

Jika pengguna memilih pelanggan biasa, sistem meminta status member. Data tersebut digunakan untuk membuat object `PelangganBiasa`.

Pilihan kedua adalah **Tampilkan Pelanggan**. Sistem akan menampilkan seluruh data pelanggan yang sudah tersimpan.

Pilihan ketiga adalah **Tambah Paket**. Pengguna dapat memasukkan nama paket, durasi, dan harga. Sistem akan memeriksa apakah harga yang dimasukkan valid. Jika harga lebih dari nol, paket akan disimpan.

Pilihan keempat adalah **Tampilkan Paket**. Sistem akan menampilkan seluruh paket Photobox yang tersedia beserta durasi dan harga.

Pilihan kelima adalah **Tambah Transaksi**. Sistem terlebih dahulu memeriksa apakah data pelanggan dan paket sudah tersedia.

Jika data tersedia, pengguna memasukkan ID transaksi kemudian memilih pelanggan dan paket yang digunakan.

Setelah pelanggan dan paket dipilih, sistem membuat object `Transaksi`.

Sistem kemudian menghitung total pembayaran berdasarkan harga paket.

Jika pelanggan merupakan pelanggan VIP, sistem akan memberikan diskon khusus sesuai dengan persentase diskon yang dimiliki pelanggan.

Jika pelanggan merupakan pelanggan biasa, sistem tidak memberikan diskon khusus.

Pilihan keenam adalah **Tampilkan Transaksi**. Sistem akan menampilkan seluruh transaksi yang telah dibuat beserta detail pelanggan, paket, harga, dan total pembayaran.

Pilihan ketujuh adalah **Keluar**. Jika pengguna memilih menu tersebut, perulangan program dihentikan dan program selesai.

Setelah menjalankan setiap proses selain keluar, sistem akan kembali menampilkan menu utama sehingga pengguna dapat melakukan proses lainnya.

---

# 15. Alur Pengelolaan Pelanggan

Proses pengelolaan pelanggan dimulai ketika pengguna memilih menu Tambah Pelanggan.

Pengguna memasukkan data pelanggan berupa ID, nama, nomor HP, dan alamat.

Setelah itu pengguna memilih jenis pelanggan.

Jika memilih VIP, sistem membuat object `PelangganVIP` dan meminta diskon khusus.

Jika memilih Biasa, sistem membuat object `PelangganBiasa` dan meminta status member.

Object pelanggan kemudian dimasukkan ke dalam daftar pelanggan.

Data tersebut dapat ditampilkan kembali melalui menu Tampilkan Pelanggan.

---

# 16. Alur Pengelolaan Paket

Program menyediakan empat paket awal, yaitu Silver, Gold, Platinum, dan Diamond.

Pengguna juga dapat menambahkan paket baru melalui menu Tambah Paket.

Pengguna memasukkan nama paket, durasi, dan harga.

Sistem memeriksa harga menggunakan method:

```python
Paket.cek_harga()
```

Jika harga valid, object paket dibuat dan dimasukkan ke dalam daftar paket.

---

# 17. Alur Transaksi

Proses transaksi dimulai dengan memilih menu Tambah Transaksi.

Sistem memeriksa data pelanggan dan paket.

Jika keduanya tersedia, pengguna memasukkan ID transaksi.

Kemudian pengguna memilih pelanggan yang akan melakukan transaksi.

Setelah itu pengguna memilih paket Photobox yang digunakan.

Sistem membuat object `Transaksi` berdasarkan pelanggan dan paket yang dipilih.

Sistem kemudian menghitung total pembayaran.

Untuk pelanggan VIP, sistem menghitung diskon khusus.

Setelah perhitungan selesai, sistem menampilkan detail transaksi.

Transaksi kemudian disimpan ke dalam daftar transaksi.

---

# 18. Contoh Perhitungan Transaksi

Contoh pelanggan VIP memilih paket Gold.

Harga paket Gold:

```text
Rp90.000
```

Diskon pelanggan VIP:

```text
10%
```

Perhitungan diskon:

```text
10% × Rp90.000 = Rp9.000
```

Total pembayaran:

```text
Rp90.000 - Rp9.000 = Rp81.000
```

Jadi pelanggan VIP membayar:

```text
Rp81.000
```

---

# 19. Cara Menjalankan Program

Pastikan Python sudah terpasang pada komputer.

Buka terminal pada folder tempat file `main.py` berada.

Kemudian jalankan perintah:

```bash
python3 main.py
```

Jika menggunakan Windows dan perintah `python3` tidak tersedia, dapat menggunakan:

```bash
python main.py
```

Setelah program berhasil dijalankan, sistem akan menampilkan menu utama.

---

# 20. Menu Program

Menu utama program terdiri dari:

```text
1. Tambah Pelanggan
2. Tampilkan Pelanggan
3. Tambah Paket
4. Tampilkan Paket
5. Tambah Transaksi
6. Tampilkan Transaksi
7. Keluar
```

Pengguna dapat memilih menu sesuai dengan kebutuhan.

---

# 21. Contoh Output

Contoh tampilan menu utama:

```text
======================================
       SISTEM LAYANAN PHOTOBOX
======================================
1. Tambah Pelanggan
2. Tampilkan Pelanggan
3. Tambah Paket
4. Tampilkan Paket
5. Tambah Transaksi
6. Tampilkan Transaksi
7. Keluar
======================================
Pilih menu:
```

Contoh pelanggan VIP:

```text
ID Pelanggan : P001
Nama         : Meyssa
No. HP       : 08123456789
Alamat       : Samarinda

Jenis Pelanggan
1. Pelanggan VIP
2. Pelanggan Biasa

Pilih jenis : 1
Diskon khusus (%): 10
```

Contoh transaksi:

```text
ID Transaksi : TR001

Pelanggan    : Meyssa
Paket        : Gold
Durasi       : 60 menit
Harga        : Rp 90000
Total Bayar  : Rp 81000
```

---

# 22. Pemenuhan Syarat Posttest

Program telah memenuhi persyaratan posttest sebagai berikut:

| No | Syarat                    | Penerapan                     |
| -- | ------------------------- | ----------------------------- |
| 1  | Asosiasi                  | Pelanggan dengan Transaksi    |
| 2  | Agregasi                  | Transaksi dengan Paket        |
| 3  | Komposisi                 | Pelanggan dengan DataKontak   |
| 4  | Superclass                | Pelanggan                     |
| 5  | Subclass                  | PelangganVIP                  |
| 6  | Subclass                  | PelangganBiasa                |
| 7  | Penggunaan `super()`      | Digunakan pada kedua subclass |
| 8  | Atribut tambahan subclass | `diskon_khusus`               |
| 9  | Atribut tambahan subclass | `status_member`               |
| 10 | Method Overriding         | `tampilkan_info()`            |
| 11 | Protected                 | `_nama`                       |
| 12 | Private                   | `__id_pelanggan`              |

---

# 23. Kesimpulan

Program Sistem Pengelolaan Paket, Pelanggan, dan Transaksi pada Layanan Photobox merupakan program yang menerapkan konsep Pemrograman Berorientasi Objek menggunakan Python.

Program menerapkan tiga Relasi UML, yaitu Asosiasi antara pelanggan dan transaksi, Agregasi antara transaksi dan paket, serta Komposisi antara pelanggan dan data kontak.

Program juga menerapkan Inheritance dengan `Pelanggan` sebagai superclass dan `PelangganVIP` serta `PelangganBiasa` sebagai subclass.

Selain itu, program menggunakan `super().__init__()`, atribut Protected `_nama`, atribut Private `__id_pelanggan`, atribut tambahan pada masing-masing subclass, serta Method Overriding pada method `tampilkan_info()`.

Dengan penerapan tersebut, program dapat digunakan sebagai sistem sederhana untuk mengelola pelanggan, paket Photobox, dan transaksi sekaligus memenuhi konsep PBO yang dipersyaratkan pada posttest.
