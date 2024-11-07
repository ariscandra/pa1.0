<img src="https://github.com/user-attachments/assets/dd22e8db-6073-4cd4-a2e1-b16451933f85" alt="" width="100%">

<p align="center">
    Selamat datang di Panduan Program Sistem Manajemen Rental Peralatan Fotografi DORA FOTO!  
</p>

## 📚 Daftar Isi
- [👥 Profil](#-profil)
  - [Kelompok 3](#kelompok-3)
- [🚀 Tentang](#-tentang)
- [📖 Flowchart](#-flowchart)

## 👥 Profil
### Kelompok 3
- Aris Candra Muzaffar <br>
  2409116088 <br>
  Sistem Informasi C '24 <br>
  
  [![Contributor1](https://img.shields.io/badge/-Aris-181717?logo=github&logoColor=white)](https://github.com/ariscandra)
  
- Muhammad Romadhoni Alfatih <br>
  2409116104 <br>
  Sistem Informasi C '24 <br>
  
  [![Contributor1](https://img.shields.io/badge/-Doni-181717?logo=github&logoColor=white)](https://github.com/Zxrov)
  
- Muhammad Rafly <br>
  2409116118 <br>
  Sistem Informasi C '24 <br>
  
  [![Contributor1](https://img.shields.io/badge/-Rafly-181717?logo=github&logoColor=white)](https://github.com/MuhammadRafly12)
  
## 🚀 Tentang
Program ini adalah aplikasi sederhana yang dikembangkan dengan bahasa pemrograman Python untuk layanan rental peralatan fotografi. Berikut ini adalah komponen utamanya:

**1. Library yang Digunakan**
- **`prettytable`**: Menampilkan data dalam bentuk tabel.
- **`os`**: Membersihkan layar terminal.
- **`pwinput`**: Menyamarkan input kata sandi.
- **`time`**: Mengatur jeda proses.
- **`json`**: Menyimpan data pengguna, produk, dan transaksi.
- **`random`** dan **`string`**: Membuat ID transaksi secara acak dan unik.

**2. Variabel Global**
Variabel ini digunakan untuk menyimpan jalur file JSON yang berfungsi sebagai penyimpanan data pengguna, produk, transaksi, keranjang, dan saldo.

**3. Fungsi Utama**
- **Menu Utama dan Login**: Mengelola menu utama, login admin, dan menu member.
- **Penyimpanan Data**: Menyimpan dan memuat data ke dalam file JSON.
- **Pengelolaan Keranjang dan Transaksi**: Mengelola proses pembelian, mulai dari menambah produk ke keranjang hingga menyelesaikan pembayaran.

**4. Fitur di Menu Admin**
Admin memiliki akses ke fitur CRUD (Create, Read, Update, Delete) untuk mengelola produk dalam katalog, memudahkan pengaturan data produk.

**5. Fitur di Menu Member**
- **Penyewaan Produk**: Member dapat memilih produk dari katalog dan mengatur tanggal pengembalian.
- **Pengelolaan Keranjang**: Member dapat melihat isi keranjang dan melakukan checkout.
- **Pengelolaan Saldo**: Member dapat melihat saldo akun dan melakukan top-up.

**6. Penyimpanan Data**
Program ini menyimpan data pengguna, produk, keranjang, dan transaksi dalam file JSON, sehingga data tetap tersimpan meskipun program ditutup.

**Kesimpulan**
Program ini mendukung kemudahan dan keamanan bagi pengguna dalam mengakses layanan rental alat fotografi, dengan fitur autentikasi, pengelolaan saldo, pemesanan produk, dan tampilan data dalam bentuk tabel.

## 📖 Flowchart

<details>
  <summary>1. Flowchart Menu Utama</summary>
  <img src="https://github.com/user-attachments/assets/15de16c4-8f34-432b-bce1-97a30a771718" alt="">
</details>

<details>
  <summary>2. Flowchart Menu Admin (Pilihan Pencarian - Lihat Katalog)</summary>
  <img src="https://github.com/user-attachments/assets/2d14828a-77f9-45a3-8a6c-ecf854ca8915" alt="">
</details>

<details>
  <summary>3. Flowchart Menu Admin (Pilihan Tambah Produk - Menu Admin Selesai)</summary>
  <img src="https://github.com/user-attachments/assets/a6e1a5f9-efd6-43c0-87a5-f22f6d7f1696" alt="">
</details>

<details>
  <summary>4. Flowchart Menu Apakah Member? (Registrasi & Login)</summary>
  <img src="https://github.com/user-attachments/assets/cf9d4bda-79e3-44fd-a9b1-0ea6b66514f4" alt="">
</details>

<details>
  <summary>5. Flowchart Menu Member (Pilihan Pencarian - Lihat Katalog)</summary>
  <img src="https://github.com/user-attachments/assets/8fb3e516-efec-478c-aa03-9f7580cef7fd" alt="">
</details>

<details>
  <summary>6. Flowchart Menu Member (Pilihan Transaksi)</summary>
  <img src="https://github.com/user-attachments/assets/6da0501f-fbec-4c1e-869e-09757a57a02f" alt="">
</details>

<details>
  <summary>7. Flowchart Menu Member (Pilihan E-Money - Menu Admin Selesai)</summary>
  <img src="https://github.com/user-attachments/assets/cb1493b0-8b72-4ba5-9144-2f9baccc9077" alt="">
</details>
