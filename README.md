# SISTEM PENGELOLAAN LAYANAN PHOTOBOX

## 1. Deskripsi Program

Program **Sistem Pengelolaan Layanan Photobox** merupakan program berbasis Python yang dibuat menggunakan pendekatan **Object-Oriented Programming (OOP)**.

Program ini digunakan untuk mengelola data layanan photobox yang terdiri dari:

* Data paket photobox
* Data pelanggan
* Data transaksi

Program dibuat berdasarkan materi yang telah dipelajari, yaitu:

1. **Class & Object**
2. **Atribut & Method**
3. **Encapsulation & Property**

Program memiliki tiga class utama yang saling berinteraksi, yaitu:

* `Paket`
* `Pelanggan`
* `Transaksi`

Class `Transaksi` menggunakan objek dari class `Pelanggan` dan `Paket` sehingga data pelanggan dan paket dapat digunakan dalam suatu transaksi.

---

# 2. Tujuan Program

Tujuan dibuatnya program ini adalah:

1. Menerapkan konsep **Class dan Object** dalam Python.
2. Menerapkan penggunaan **atribut class dan atribut instance**.
3. Menerapkan **instance method, class method, dan static method**.
4. Menerapkan konsep **encapsulation** menggunakan atribut private.
5. Menerapkan `@property` sebagai getter dan setter.
6. Menerapkan validasi data melalui setter.
7. Menunjukkan interaksi antar-object dalam program OOP.

---

# 3. Struktur Class

Program memiliki tiga class utama.

## 3.1 Class Paket

Class `Paket` digunakan untuk menyimpan dan mengelola data paket layanan photobox.

### Atribut Class

```python
nama_layanan = "Photobox"
total_paket = 0
status_layanan = "Aktif"
```

Keterangan:

| Atribut          | Fungsi                            |
| ---------------- | --------------------------------- |
| `nama_layanan`   | Menyimpan nama layanan            |
| `total_paket`    | Menghitung jumlah objek paket     |
| `status_layanan` | Menyimpan status layanan photobox |

### Atribut Instance

```python
self.nama_paket
self.durasi
self.__harga
```

* `nama_paket` merupakan atribut public.
* `durasi` merupakan atribut public.
* `__harga` merupakan atribut private karena menggunakan `__`.

### Method

**Instance method:**

```python
tampilkan_info()
```

Digunakan untuk menampilkan informasi paket.

**Class method:**

```python
ubah_status_layanan()
```

Digunakan untuk mengubah status layanan pada atribut class.

**Static method:**

```python
cek_harga()
```

Digunakan untuk mengecek apakah harga paket valid.

### Property

```python
@property
def harga(self):
```

Digunakan sebagai getter untuk mengakses atribut private `__harga`.

Setter:

```python
@harga.setter
def harga(self, nilai):
```

Digunakan untuk mengubah harga dengan validasi agar harga tidak boleh bernilai negatif.

---

# 4. Class Pelanggan

Class `Pelanggan` digunakan untuk menyimpan data pelanggan photobox.

### Atribut Class

```python
nama_usaha = "Photobox"
total_pelanggan = 0
status_pelanggan = "Aktif"
```

Keterangan:

| Atribut            | Fungsi                      |
| ------------------ | --------------------------- |
| `nama_usaha`       | Menyimpan nama usaha        |
| `total_pelanggan`  | Menghitung jumlah pelanggan |
| `status_pelanggan` | Menyimpan status pelanggan  |

### Atribut Instance

```python
self.nama
self.umur
self.__no_telepon
```

* `nama` merupakan atribut public.
* `umur` merupakan atribut public.
* `__no_telepon` merupakan atribut private karena menggunakan `__`.

### Method

**Instance method:**

```python
tampilkan_info()
```

Digunakan untuk menampilkan data pelanggan.

**Class method:**

```python
ubah_status_pelanggan()
```

Digunakan untuk mengubah status pelanggan.

**Static method:**

```python
cek_umur()
```

Digunakan untuk mengecek apakah umur pelanggan memenuhi ketentuan program.

### Property

Getter:

```python
@property
def no_telepon(self):
```

Digunakan untuk membaca nomor telepon private.

Setter:

```python
@no_telepon.setter
def no_telepon(self, nomor):
```

Digunakan untuk mengubah nomor telepon sekaligus melakukan validasi.

Validasi yang dilakukan:

* Nomor telepon tidak boleh kosong.
* Nomor telepon hanya boleh berisi angka.

---

# 5. Class Transaksi

Class `Transaksi` digunakan untuk mengelola transaksi photobox.

Class ini berinteraksi dengan object dari class `Pelanggan` dan `Paket`.

### Atribut Class

```python
nama_layanan = "Photobox"
total_transaksi = 0
status_transaksi = "Diproses"
```

Keterangan:

| Atribut            | Fungsi                                 |
| ------------------ | -------------------------------------- |
| `nama_layanan`     | Menyimpan nama layanan                 |
| `total_transaksi`  | Menghitung jumlah transaksi            |
| `status_transaksi` | Menyimpan status transaksi secara umum |

### Atribut Instance

```python
self.kode_transaksi
self.pelanggan
self.paket
self.__status
```

* `kode_transaksi` merupakan atribut public.
* `pelanggan` menyimpan object dari class `Pelanggan`.
* `paket` menyimpan object dari class `Paket`.
* `__status` merupakan atribut private.

### Method

**Instance method:**

```python
tampilkan_transaksi()
```

Digunakan untuk menampilkan informasi transaksi.

**Class method:**

```python
ubah_status_transaksi()
```

Digunakan untuk mengubah status transaksi secara umum.

**Static method:**

```python
hitung_diskon()
```

Digunakan untuk menghitung harga setelah mendapatkan diskon.

### Property

Getter:

```python
@property
def status(self):
```

Digunakan untuk membaca status transaksi.

Setter:

```python
@status.setter
def status(self, nilai):
```

Digunakan untuk mengubah status transaksi dengan validasi.

Status yang diperbolehkan:

* `Diproses`
* `Selesai`
* `Batal`

---

# 6. Konsep OOP yang Digunakan

## 6.1 Class

Class digunakan sebagai cetakan untuk membuat object.

Contoh:

```python
class Paket:
class Pelanggan:
class Transaksi:
```

---

## 6.2 Object

Object dibuat berdasarkan class yang telah dibuat.

Contoh:

```python
paket1 = Paket("Silver", 30, 50000)
paket2 = Paket("Gold", 60, 90000)
```

Object yang dibuat adalah `paket1` dan `paket2`.

Pada class pelanggan:

```python
pelanggan1 = Pelanggan("Meyssa108", 19, "081234567890")
pelanggan2 = Pelanggan("Dirga115", 20, "082345678901")
```

Pada class transaksi:

```python
transaksi1 = Transaksi("TRX001", pelanggan1, paket1)
transaksi2 = Transaksi("TRX002", pelanggan2, paket2)
```

---

# 7. Atribut Class

Program menggunakan minimal tiga atribut class pada setiap class.

Contoh pada class `Paket`:

```python
nama_layanan = "Photobox"
total_paket = 0
status_layanan = "Aktif"
```

Atribut class digunakan bersama oleh seluruh object dari class yang sama.

Contohnya:

```python
Paket.total_paket
```

digunakan untuk mengetahui jumlah paket yang telah dibuat.

---

# 8. Atribut Instance

Atribut instance dibuat di dalam `__init__()` menggunakan `self`.

Contoh:

```python
def __init__(self, nama_paket, durasi, harga):
    self.nama_paket = nama_paket
    self.durasi = durasi
    self.__harga = harga
```

Nilai atribut instance dapat berbeda untuk setiap object.

Contohnya:

```python
paket1 = Paket("Silver", 30, 50000)
paket2 = Paket("Gold", 60, 90000)
```

Object `paket1` memiliki data yang berbeda dengan `paket2`.

---

# 9. Encapsulation

Encapsulation digunakan untuk membatasi akses langsung terhadap data tertentu.

Dalam program terdapat beberapa atribut private, seperti:

```python
self.__harga
self.__no_telepon
self.__status
```

Atribut tersebut tidak diakses secara langsung dari luar class.

Untuk mengakses dan mengubahnya digunakan `@property` dan setter.

Contoh:

```python
@property
def harga(self):
    return self.__harga
```

---

# 10. Getter dan Setter

Getter digunakan untuk mengambil nilai dari atribut private.

Contoh:

```python
@property
def harga(self):
    return self.__harga
```

Setter digunakan untuk mengubah nilai atribut private dengan validasi.

Contoh:

```python
@harga.setter
def harga(self, nilai):
    if nilai < 0:
        print("Harga tidak boleh negatif!")
    else:
        self.__harga = nilai
        print("Harga berhasil diperbarui.")
```

Dengan setter tersebut, harga negatif tidak dapat dimasukkan ke dalam data.

---

# 11. Validasi Data

Program memiliki beberapa validasi.

### Validasi Harga

Harga tidak boleh negatif.

```python
paket1.harga = -10000
```

Program akan menampilkan:

```text
Harga tidak boleh negatif!
```

### Validasi Nomor Telepon

Nomor telepon tidak boleh kosong.

```python
pelanggan1.no_telepon = ""
```

Program akan menampilkan:

```text
Nomor telepon tidak boleh kosong!
```

Nomor telepon juga harus berupa angka.

### Validasi Status Transaksi

Status transaksi hanya dapat menggunakan:

```text
Diproses
Selesai
Batal
```

Jika memasukkan:

```python
transaksi1.status = "Sedang Diproses"
```

maka program menampilkan:

```text
Status tidak valid!
```

---

# 12. Instance Method

Instance method merupakan method yang menggunakan parameter `self`.

Contohnya:

```python
def tampilkan_info(self):
```

dan:

```python
def tampilkan_transaksi(self):
```

Method tersebut digunakan melalui object.

Contoh:

```python
paket1.tampilkan_info()
pelanggan1.tampilkan_info()
transaksi1.tampilkan_transaksi()
```

---

# 13. Class Method

Class method menggunakan decorator:

```python
@classmethod
```

dan parameter `cls`.

Contohnya:

```python
@classmethod
def ubah_status_layanan(cls, status):
    cls.status_layanan = status
```

Class method digunakan untuk mengubah atribut class.

Contoh pemanggilan:

```python
Paket.ubah_status_layanan("Sedang Beroperasi")
```

Class method juga terdapat pada:

* `Paket`
* `Pelanggan`
* `Transaksi`

---

# 14. Static Method

Static method menggunakan decorator:

```python
@staticmethod
```

Static method tidak membutuhkan `self` maupun `cls`.

Contohnya:

```python
@staticmethod
def cek_harga(harga):
    if harga > 0:
        return True
    else:
        return False
```

Static method digunakan sebagai fungsi bantuan.

Static method yang terdapat pada program:

| Class       | Static Method     | Fungsi                          |
| ----------- | ----------------- | ------------------------------- |
| `Paket`     | `cek_harga()`     | Mengecek validitas harga        |
| `Pelanggan` | `cek_umur()`      | Mengecek validitas umur         |
| `Transaksi` | `hitung_diskon()` | Menghitung harga setelah diskon |

---

# 15. Interaksi Antar Class

Class `Transaksi` menggunakan object dari class `Pelanggan` dan `Paket`.

Contoh:

```python
transaksi1 = Transaksi("TRX001", pelanggan1, paket1)
```

Pada kode tersebut:

* `pelanggan1` merupakan object dari class `Pelanggan`.
* `paket1` merupakan object dari class `Paket`.
* Kedua object tersebut digunakan oleh class `Transaksi`.

Sehingga ketika transaksi ditampilkan:

```python
transaksi1.tampilkan_transaksi()
```

program dapat menampilkan nama pelanggan dan nama paket yang digunakan.

Alur sederhananya:

```text
Paket
  ↓
Pelanggan
  ↓
Transaksi
  ↓
Informasi transaksi ditampilkan
```

---

# 16. Pengujian Program

Program melakukan pengujian terhadap seluruh class dan method.

## 16.1 Pengujian Class Paket

Dibuat dua object:

```python
paket1 = Paket("Silver", 30, 50000)
paket2 = Paket("Gold", 60, 90000)
```

Kemudian informasi paket ditampilkan menggunakan:

```python
paket1.tampilkan_info()
paket2.tampilkan_info()
```

---

## 16.2 Pengujian Setter Harga

### Data Valid

```python
paket1.harga = 55000
```

Hasil:

```text
Harga berhasil diperbarui.
Harga baru : 55000
```

### Data Tidak Valid

```python
paket1.harga = -10000
```

Hasil:

```text
Harga tidak boleh negatif!
```

---

## 16.3 Pengujian Static Method Paket

```python
Paket.cek_harga(paket1.harga)
```

Method digunakan untuk mengecek apakah harga paket valid.

---

## 16.4 Pengujian Class Method Paket

```python
Paket.ubah_status_layanan("Sedang Beroperasi")
```

Digunakan untuk mengubah status layanan.

---

# 17. Pengujian Class Pelanggan

Dibuat dua object pelanggan:

```python
pelanggan1 = Pelanggan("Meyssa108", 19, "081234567890")
pelanggan2 = Pelanggan("Dirga115", 20, "082345678901")
```

Data pelanggan kemudian ditampilkan menggunakan:

```python
pelanggan1.tampilkan_info()
pelanggan2.tampilkan_info()
```

---

# 18. Pengujian Setter Nomor Telepon

### Data Valid

```python
pelanggan1.no_telepon = "089876543210"
```

Hasil:

```text
Nomor telepon berhasil diperbarui.
```

### Data Tidak Valid

```python
pelanggan1.no_telepon = ""
```

Hasil:

```text
Nomor telepon tidak boleh kosong!
```

---

# 19. Pengujian Static dan Class Method Pelanggan

Static method:

```python
Pelanggan.cek_umur(pelanggan1.umur)
```

digunakan untuk mengecek validitas umur pelanggan.

Class method:

```python
Pelanggan.ubah_status_pelanggan("Terdaftar")
```

digunakan untuk mengubah status pelanggan.

---

# 20. Pengujian Class Transaksi

Dibuat dua object transaksi:

```python
transaksi1 = Transaksi("TRX001", pelanggan1, paket1)
transaksi2 = Transaksi("TRX002", pelanggan2, paket2)
```

Kemudian data transaksi ditampilkan:

```python
transaksi1.tampilkan_transaksi()
transaksi2.tampilkan_transaksi()
```

Informasi yang ditampilkan meliputi:

* Kode transaksi
* Nama pelanggan
* Nama paket
* Harga paket
* Status transaksi

---

# 21. Pengujian Setter Status Transaksi

### Data Valid

```python
transaksi1.status = "Selesai"
```

Hasil:

```text
Status berhasil diperbarui.
Status baru : Selesai
```

### Data Tidak Valid

```python
transaksi1.status = "Sedang Diproses"
```

Hasil:

```text
Status tidak valid!
```

---

# 22. Pengujian Static Method Transaksi

Program menggunakan:

```python
Transaksi.hitung_diskon(90000, 10)
```

Artinya harga awal adalah Rp90.000 dengan diskon 10%.

Hasil:

```text
Harga setelah diskon 10% : Rp 81000.0
```

---

# 23. Pengujian Class Method Transaksi

Program menjalankan:

```python
Transaksi.ubah_status_transaksi("Selesai")
```

Method tersebut digunakan untuk mengubah status transaksi secara umum.

---

# 24. Pengujian Jumlah Object

Program juga menghitung jumlah object yang telah dibuat.

```python
print("Total paket      :", Paket.total_paket)
print("Total pelanggan  :", Pelanggan.total_pelanggan)
print("Total transaksi  :", Transaksi.total_transaksi)
```

Dengan dua object pada setiap class, hasilnya:

```text
Total paket      : 2
Total pelanggan  : 2
Total transaksi  : 2
```

---

# 25. Alur Program

Alur program secara keseluruhan adalah:

```text
Mulai
  ↓
Membuat object Paket
  ↓
Menampilkan informasi paket
  ↓
Menguji getter dan setter harga
  ↓
Menguji validasi harga
  ↓
Menguji static method Paket
  ↓
Menguji class method Paket
  ↓
Membuat object Pelanggan
  ↓
Menampilkan informasi pelanggan
  ↓
Menguji getter dan setter nomor telepon
  ↓
Menguji validasi nomor telepon
  ↓
Menguji static method Pelanggan
  ↓
Menguji class method Pelanggan
  ↓
Membuat object Transaksi
  ↓
Menghubungkan pelanggan dengan paket
  ↓
Menampilkan informasi transaksi
  ↓
Menguji getter dan setter status
  ↓
Menguji validasi status
  ↓
Menguji static method transaksi
  ↓
Menguji class method transaksi
  ↓
Menampilkan jumlah object
  ↓
Program selesai
```

---

# 26. Kesimpulan

Program **Sistem Pengelolaan Layanan Photobox** telah menerapkan konsep dasar Object-Oriented Programming menggunakan Python.

Konsep yang diterapkan meliputi:

* Class dan Object
* Atribut class
* Atribut instance
* Public attribute
* Private attribute
* Instance method
* Class method
* Static method
* Encapsulation
* Getter menggunakan `@property`
* Setter menggunakan `@property.setter`
* Validasi data
* Interaksi antar-object

Dengan adanya tiga class yaitu `Paket`, `Pelanggan`, dan `Transaksi`, program dapat menggambarkan pengelolaan layanan photobox secara sederhana sekaligus memenuhi penerapan materi OOP yang telah dipelajari.
