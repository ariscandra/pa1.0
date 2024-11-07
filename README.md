<img src="https://github.com/user-attachments/assets/dd22e8db-6073-4cd4-a2e1-b16451933f85" alt="" width="100%">

<p align="center">
    Selamat Datang di Panduan Program Sistem Manajemen Rental Peralatan Fotografi DORA FOTO!  
</p>

## 📚 Daftar Isi
- [👥 Profil](#-profil)
- [🚀 Tentang](#-tentang)
- [📖 Flowchart](#-flowchart)
- [🖥️ Penjelasan Output](#️-penjelasan-output)

## 👥 Profil
**Kelompok 3**

| Aris Candra Muzaffar | Muhammad Romadhoni Alfatih | Muhammad Rafly |
|----------------------|----------------------------|----------------|
| **NIM:** 2409116088 <br> **Kelas:** Sistem Informasi C '24 <br> [![Aris](https://img.shields.io/badge/-Aris-FFFFFF?logo=github&logoColor=black)](https://github.com/ariscandra) &nbsp; &nbsp; | **NIM:** 2409116104 <br> **Kelas:** Sistem Informasi C '24 <br> [![Doni](https://img.shields.io/badge/-Doni-FFFFFF?logo=github&logoColor=black)](https://github.com/Zxrov) &nbsp; &nbsp; | **NIM:** 2409116118 <br> **Kelas:** Sistem Informasi C '24 <br> [![Rafly](https://img.shields.io/badge/-Rafly-FFFFFF?logo=github&logoColor=black)](https://github.com/MuhammadRafly12) |

## 🚀 Tentang
Program ini adalah aplikasi sederhana yang dikembangkan dengan bahasa pemrograman Python untuk layanan rental peralatan fotografi. Berikut ini adalah komponen utamanya:

**1. Library yang Digunakan**
- **`prettytable`**: Menampilkan data dalam bentuk tabel.
- **`os`**: Membersihkan layar terminal.
- **`pwinput`**: Menyamarkan input kata sandi.
- **`time`**: Mengatur jeda proses.
- **`json`**: Menyimpan data pengguna, produk, dan transaksi.
- **`random`** dan **`string`**: Membuat ID transaksi secara acak dan unik.

**2. Variabel Global** <br>
Variabel ini digunakan untuk menyimpan jalur file JSON yang berfungsi sebagai penyimpanan data pengguna, produk, transaksi, keranjang, dan saldo.

**3. Fungsi Utama**
- **Menu Utama dan Login**: Mengelola menu utama, login admin, dan menu member.
- **Penyimpanan Data**: Menyimpan dan memuat data ke dalam file JSON.
- **Pengelolaan Keranjang dan Transaksi**: Mengelola proses pembelian, mulai dari menambah produk ke keranjang hingga menyelesaikan pembayaran.

**4. Fitur di Menu Admin** <br>
Admin memiliki akses ke fitur CRUD (Create, Read, Update, Delete) untuk mengelola produk dalam katalog, memudahkan pengaturan data produk.

**5. Fitur di Menu Member**
- **Penyewaan Produk**: Member dapat memilih produk dari katalog dan mengatur tanggal pengembalian.
- **Pengelolaan Keranjang**: Member dapat melihat isi keranjang dan melakukan checkout.
- **Pengelolaan Saldo**: Member dapat melihat saldo akun dan melakukan top-up.

**6. Penyimpanan Data** <br>
Program ini menyimpan data pengguna, produk, keranjang, dan transaksi dalam file JSON, sehingga data tetap tersimpan meskipun program ditutup.

**7. Kesimpulan** <br>
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

## 🖥️ Penjelasan Output
### Menu Utama
<div align="center">
  <img src="https://github.com/user-attachments/assets/6d97fbaa-ff68-41eb-a34b-67ef45aeb1a6" alt="" width="500px">
</div>

<p align="justify">Gambar di atas adalah tampilan yang akan menyambut pengguna untuk pertama kalinya setiap program dijalankan, yaitu menu utama. Menu utama terdapat 3 pilihan.</p>

**1. Administrator Dora Foto**
<p align="justify">Jika pengguna memilih 1, maka akan diarahkan ke login untuk masuk ke menu administrator.</p>

**2. Member Dora Foto**
<p align="justify">Jika pengguna memilih 2, maka akan di arahkan ke menu yang menanyakan apakah pengguna adalah member atau tidak.</p>

**3. Keluar**
<p align="justify">Jika pengguna memilih 3, maka akan program akan berhenti berjalan.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/bfff8ad4-9dc9-47b3-ad06-c35dd4514e25" alt="" width="300px">
</div> <br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/c2753377-6820-4bfc-9c3f-f6fd03f32e13" alt="" width="300px">
</div>

**4. Pengguna Memasukkan Selain 1-3**
<p align="justify">Jika pengguna memasukkan selain 1-3 dan input mereka tidak valid, maka program akan memberikan pesan error, dan pengguna akan mengulangi input.</p>

### Login Administrator
<div align="center">
  <img src="https://github.com/user-attachments/assets/1d415bb1-47af-4940-9ed1-ed17d4b05a96" alt="" width="500px">
</div>

**1. Jika Validasi Benar**
<p align="justify">Jika pengguna berhasil melakukan login, memasukkan input sesuai dengan data admin di dictionary, maka pengguna akan diberi pesan login berhasil dan dialihkan ke menu admin.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/f57d09fc-9569-44ba-bc8f-0aeb59331d9d" alt="" width="500px">
</div>

**2. Jika Validasi Salah**
<p align="justify">Jika pengguna gagal melakukan login, karena proses validasi gagal. Maka, akan muncul pesan login gagal dan pengguna akan mengulangi proses login, percobaan login berjumlah 3x setiap login dimulai dari awal yaitu melalui menu utama.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/18077183-9cb4-4733-b7bd-52c22bf4ac51" alt="" width="500px">
</div>

**3. Sisa Coba Habis**
<p align="justify">Jika sisa percobaan login pengguna habis atau 0. Maka, akan muncul pesan bahwa akun mereka dikunci, dan pengguna dapat kembali ke program setelah menunggu 3 detik. Kemudian, pengguna akan dialihkan ke menu utama lagi.</p>
