<a name="top"></a>
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
<details>
<summary><h3>Menu Utama</h3></summary>

<div align="center">
  <img src="https://github.com/user-attachments/assets/6d97fbaa-ff68-41eb-a34b-67ef45aeb1a6" alt="Menu Utama Image" width="500px">
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
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/c2753377-6820-4bfc-9c3f-f6fd03f32e13" alt="" width="300px">
</div>

**4. Pengguna Memasukkan Selain 1-3**
<p align="justify">Jika pengguna memasukkan selain 1-3 dan input mereka tidak valid, maka program akan memberikan pesan error, dan pengguna akan mengulangi input.</p>

</details>

<details>
<summary><h3>Login Administrator</h3></summary>

<div align="center">
  <img src="https://github.com/user-attachments/assets/1d415bb1-47af-4940-9ed1-ed17d4b05a96" alt="Login Administrator Image" width="500px">
</div>

**1. Berhasil Validasi**
<p align="justify">Jika pengguna berhasil melakukan login, memasukkan input sesuai dengan data admin di dictionary, maka pengguna akan diberi pesan login berhasil dan dialihkan ke menu admin.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/f57d09fc-9569-44ba-bc8f-0aeb59331d9d" alt="" width="500px">
</div>

**2. Gagal Validasi**
<p align="justify">Jika pengguna gagal melakukan login, karena proses validasi gagal. Maka, akan muncul pesan login gagal dan pengguna akan mengulangi proses login, percobaan login berjumlah 3x setiap login dimulai dari awal yaitu melalui menu utama.</p>

<div align="center">
  <img src="https://github.com/user-attachments/assets/18077183-9cb4-4733-b7bd-52c22bf4ac51" alt="" width="500px">
</div>

**3. Sisa Coba Habis**
<p align="justify">Jika sisa percobaan login pengguna habis atau 0. Maka, akan muncul pesan bahwa akun mereka dikunci, dan pengguna dapat kembali ke program setelah menunggu 3 detik. Kemudian, pengguna akan dialihkan ke menu utama lagi.</p>

</details>

<details>
  <summary><h3>Menu Admin</h3></summary>

  <div align="center">
    <img src="https://github.com/user-attachments/assets/d0d8e6ae-108b-4bdd-aa5a-eb5c43b61b2b" alt="" width="500px">
  </div>
  <p align="justify">Dalam menu ini terdapat 6 opsi yang bisa admin pilih, yaitu sebagai berikut penjelasannya:</p>

  **1. Cari Produk**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/0f8ad26d-61a5-4e70-afaa-e6f008efccde" alt="" width="500px">
  </div>
  <p align="justify">Jika admin memilih 1, maka fungsi pencarian akan berjalan, admin diminta memasukkan kata kunci produk yang ingin dicari, bisa dalam bentuk nama produk, harga, atau nama kategorinya. Setelah itu, tabel produk hasil pencarian yang sesuai dengan kata kunci yang dimasukkan akan keluar.</p>

  **2. Lihat Katalog**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/eea591d5-bfcb-4de3-a1f9-48dc977dea3a" alt="" width="500px">
  </div>
  <p align="justify">Jika admin memilih 2, maka program akan memanggil semua daftar produk yang ada dalam bentuk tabel prettytable.</p>

  <div align="center">
    <img src="https://github.com/user-attachments/assets/9946b897-e879-49a9-ab83-e98d6dbba485" alt="" width="500px">
  </div>
  <p align="justify">Setelah katalog ditampilkan, maka admin akan ditanya apakah produk ingin menyorting daftar produk. Jika admin memasukkan y, maka menu sorting akan ditampilkan, dan jika admin memasukkan n, maka akan kembali ke menu sebelumnya.</p>

  <div align="center">
    <img src="https://github.com/user-attachments/assets/6625d4fc-867b-4a30-a195-a37fa52c3c4f" alt="" width="500px">
  </div>
  <p align="justify">Menu sorting terdapat beberapa pilihan, yaitu mengurutkan berdasarkan id, harga per hari, dan harga per 3 hari. Saat admin memilih opsi kembali, maka tabel produk akan otomatis kembali seperti semula.</p>

  **3. Tambah, Update, dan Hapus Produk**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/ee762316-249b-4a56-b6dc-6f50717b5f3c" alt="" width="300px">
  </div>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/f5faa9d1-2dc5-499a-a8ae-6878b4961ef5" alt="" width="300px">
  </div>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/ebd001b3-4840-4f35-9367-79fccfeb20c1" alt="" width="300px">
  </div>
  <p align="justify">Mekanisme penambahan, pengubahan, dan penghapusan produk 11 12 sama. Pertama-tama, program akan menampilkan menu sesuai dengan operasi yang admin pilih. Perbedaan dalam data apa yang diambil melalui input mungkin yang sedikit berbeda, bisa dilihat dalam gambar-gambar di bawah.</p>

  <div align="center">
    <img src="https://github.com/user-attachments/assets/e269c9b0-74d1-4d44-ad86-80c3ca0998a4" alt="" width="300px">
  </div>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/bb85a0cd-235e-4ce7-8e22-3cc1aa8a132b" alt="" width="300px">
  </div>
  <div align="center">
    <img src="https://github.com/user-attachments/assets/397a4eed-2761-4e22-8c90-778f63970a41" alt="" width="300px">
  </div>
  <p align="justify">Jika admin ingin menambahkan produk, maka yang akan diminta masukkan adalah nama produk, harga produk per harinya, dan harga produk per 3 harinya. Jika admin ingin mengupdate produk, maka input yang diminta berupa id produk yang ingin diubah, kemudian nama produk dan kedua harganya yang baru, admin juga bisa mengosongkan field input kalau tidak ingin mengubah data produk. Jika admin ingin menghapus, maka yang hanya diminta adalah id dari produk.</p>
  <p align="justify">Ketika operasi berhasil dijalankan berdasarkan ketentuan yang ada, maka program akan memberi pesan bahwa operasi tersebut berhasil.</p>

  **4. Logout**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/f498e40b-139f-4c98-b3f0-4c67cff98f7e" alt="" width="300px">
  </div>
  <p align="justify">Jika pengguna memilih opsi logout, maka program akan mengalihkan pengguna kembali ke menu utama. Program juga akan memberi ucapan terimakasih untuk administrator.</p>

  **5. Jika Memilih Selain 1-6 atau Tidak Valid**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/4a714a2d-bcb2-467b-b57b-b1078fbf641e" alt="" width="300px">
  </div>
  <p align="justify">Jika pengguna memasukkan selain 1-6 dan input mereka tidak valid, maka program akan memberikan pesan error, dan pengguna akan mengulangi input.</p>

</details>

<details>
<summary><h3>Menu Apakah Member</h3></summary>

<div align="center">
  <img src="https://github.com/user-attachments/assets/c426c338-be61-4b12-a15b-987cca316e12" alt="Menu Apakah Member Image" width="500px">
</div>

<p align="justify">Pengguna akan ditujukan ke menu ini jika memilih 2 di menu utama. Di Dalam menu ini terdapat 3 opsi, yaitu registrasi member, login member, dan kembali ke menu utama.</p>

**1. Ya (Login)**
<div align="center">
  <img src="https://github.com/user-attachments/assets/8ccbe4d4-e9a1-46ec-a2fd-114a81ae78fc" alt="Login Image" width="300px">
</div>
<p align="justify">Jika pengguna memilih 1, maka akan diarahkan ke login member. Jika login berhasil divalidasi, maka pengguna akan di arahkan ke menu member.</p>

**2. Tidak (Registrasi)**
<div align="center">
  <img src="https://github.com/user-attachments/assets/ff1cd49c-d0e4-4219-be46-19c82c1f6051" alt="Registrasi Image" width="300px">
</div>
<p align="justify">Jika pengguna memilih 2, maka pengguna akan memulai proses registrasi sebagai member. Apabila seluruh field input sudah terisi sesuai dengan ketentuan, maka pengguna berhasil melakukan registrasi dan akan otomatis melakukan login setelahnya</p>

**3. Kembali**
<p align="justify">Jika pengguna memilih opsi 3, maka pengguna akan kembali ke menu sebelumnya, yakni menu utama.</p>

**4. Jika Memilih Selain 1-3 atau Tidak Valid**
<div align="center">
  <img src="https://github.com/user-attachments/assets/b7448b50-3cd0-4845-b85c-8cf631484d3c" alt="Error Message Image" width="300px">
</div>
<p align="justify">Jika pengguna memasukkan angka selain 1-3 atau memasukkan input yang tidak valid, maka program akan memberi pesan error dan pengguna akan diminta mengulangi proses input.</p>

</details>

<details>
<summary><h3>Menu Member</h3></summary>

<div align="center">
  <img src="https://github.com/user-attachments/assets/32820178-4c74-4ee6-9a01-8f76590bbdaf" alt="" width="500px">
</div>

<p align="justify">Pengguna akan masuk ke menu member bila sebelumnya berhasil melakukan login. Dalam menu ini, terdapat 6 pilihan, ada opsi cari produk dan lihat katalog yang mekanismenya sama seperti di menu admin. Kemudian ada pilihan transaksi, e-money, s&k dora foto, dan terakhir, logout.</p>

**1. Transaksi**
<div align="center">
  <img src="https://github.com/user-attachments/assets/ba386dc6-4978-4066-8dd7-3ccfd31ae358" alt="" width="300px">
</div>
<p align="justify">Jika pengguna memilih 3 di menu member, maka akan diarahkan ke menu transaksi. Dalam menu ini, terdapat 5 pilihan yaitu untuk menambahkan produk ke keranjang, melihat keranjang, melanjutkan proses pembayaran, riwayat transaksi, dan kembali ke menu member.</p>

* Tambah ke Keranjang
    <div align="center">
      <img src="https://github.com/user-attachments/assets/6a915944-c2bf-442c-ad6e-c65cc084e29f" alt="" width="300px">
    </div>
    <p align="justify">Ketika pengguna ingin menambahkan produk ke keranjang, pengguna akan diminta memasukkan pilihan kategori produk mana yang ingin mereka taruh di keranjang. Setelah itu, program akan menampilkan daftar produk dalam kategori sesuai dengan yang pengguna pilih. Pengguna diminta untuk memasukkan id produk, 0 jika pengguna mau kembali, setelah pengguna menginput id produk yang diinginkan, program akan memberi pesan bahwa produk tersebut berhasil ditambahkan ke keranjang. Pengguna akan kembali ke menu pilihan kategori</p>

* Lihat Keranjang
    <div align="center">
      <img src="https://github.com/user-attachments/assets/70b5164b-da97-41ae-a0aa-32362f91801e" alt="" width="300px">
    </div>
    <p align="justify">Dalam pilihan ini, program akan langsung menunjukkan isi dari keranjang dalam bentuk tabel menggunakan prettytable.</p>

* Proses Pembayaran
    <div align="center">
      <img src="https://github.com/user-attachments/assets/19257b35-cfd1-47e3-8153-30d8c28eab4b" alt="" width="300px">
    </div>
    <p align="justify">Program akan memastikan apakah pengguna yakin ingin melanjutkan ke proses pembayaran. Jika pengguna memasukkan y, maka program akan lanjut dengan meminta tanggal pengembalian barang yang disewa dalam format (dd-mm-yyyy). Setelah itu, program akan memvalidasi input dari pengguna, jika sesuai ketentuan, maka program akan mengkalkulasi apakah saldo dari pengguna mencukupi biaya transaksi. Kalau tidak, maka program akan memberi pesan bahwa saldo pengguna tidak mencukupi. Jika iya, maka struk transaksi akan dicetak. Pembayaran berhasil.</p>

    <div align="center">
      <img src="https://github.com/user-attachments/assets/a403aac7-7483-49c9-b2e4-c93d5b22f911" alt="" width="300px">
    </div>
    <p align="justify">Jika iya, maka struk transaksi akan dicetak. Pembayaran berhasil.</p>

* Riwayat Transaksi
    <div align="center">
      <img src="https://github.com/user-attachments/assets/9088275f-3fbe-456e-8581-ab863e0717be" alt="" width="300px">
    </div>
    <p align="justify">Program akan menunjukkan secara langsung riwayat transaksi dalam bentuk tabel menggunakan prettytable.</p>

* Kembali
    <p align="justify">Pengguna akan kembali ke menu member jika memilih opsi untuk kembali.</p>

**2. E-Money**
<div align="center">
  <img src="https://github.com/user-attachments/assets/e23c9137-7011-4eb5-a4d3-137eabd2c4f1" alt="" width="300px">
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/55fc189c-f857-4c5e-9080-132ac5fabb99" alt="" width="300px">
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/69cb42b5-9afb-45c7-bed2-e0a850057c8e" alt="" width="300px">
</div>
<p align="justify">Jika pengguna memilih 4 di menu member, maka akan dialihkan ke menu e-emoney, yang isinya opsi pengguna untuk melihat saldo dan melakukan topup. Pengguna akan diminta memasukkan password lagi jika ingin melakukan kedua aksi tersebut. Dalam opsi melakukan topup, program akan menampilkan menu nominal yang bisa dipilih oleh pengguna, jika semua input sesuai dengan ketentuan yang berada, maka nominal topup akan ditambahkan ke saldo pengguna.</p>

**3. S&K Dora Foto**
<div align="center">
  <img src="https://github.com/user-attachments/assets/b6bbc08a-ae91-4016-a0c9-3a8e919fc050" alt="" width="400px">
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/13947d44-2d8b-4dd8-a6a2-308d0c17329b" alt="" width="400px">
</div>
<p align="justify">Jika pengguna memilih 5 di menu member, maka program akan memanggil teks syarat dan ketentuan dari jasa rental kami.</p>

**4. Logout**
<div align="center">
  <img src="https://github.com/user-attachments/assets/d9dcdd05-542f-4137-93e5-d4923957f94c" alt="" width="300px">
</div>
<p align="justify">Jika pengguna memilih 6 di menu member, maka program akan memberi pesan sampai jumpa, dan pengguna akan kembali ke menu apakah member.</p>

**5. Jika Memilih Selain 1-6 atau Tidak Valid**
<div align="center">
  <img src="https://github.com/user-attachments/assets/3f03c497-da14-4abf-ae5c-14618eeb5264" alt="" width="300px">
</div>
<p align="justify">Jika pengguna memasukkan selain 1-6 atau input yang dimasukkan tidak valid, maka program akan memberikan pesan error dan pengguna diminta untuk mengulangi input.</p>

</details>

---
> [!NOTE]
> **🎉 Terimakasih! 🎉**
> Kepada abang, mba, dan rekan semua yang sudah membantu kami dalam menyelesaikan proyek ini 🙏

---
[⬆️ Kembali ke Awal](#top)
<img src="https://github.com/user-attachments/assets/5a226224-062e-447a-8e3e-1c97d76ea9da" alt="" width="100%">
