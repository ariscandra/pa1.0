from prettytable import PrettyTable
from datetime import datetime
import json, pwinput, os, time
os.system ("cls")

rujukan = os.path.abspath(os.curdir)

# DORA = DO(DOni), R(Rafly), A(Aris) EAAA
current_user = None
# IDENTITAS PROGRAM
teks_dekor = "dora"
panjang = 100
frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
print(frame)
print('|{:^100}|'.format('+        DORA FOTO         +'))
print('+' + '-'*100 + '+')
print('|{:^100}|'.format('RENTAL ALAT FOTOGRAFI'))
print(frame)
print()

# JSON untuk login
json_regs = f"{rujukan}/regs_pa.json"
# JSON untuk Produk
json_brg = f"{rujukan}/produk_pa.json"
# JSON untuk Keranjang
json_co = f"{rujukan}/checkout_pa.json"
# JSON untuk TopUp
json_bling = f"{rujukan}/emoney_pa.json"
# txt untuk S&K
txt_sk = f"{rujukan}/sk_rental.txt"

def load_dtMember():
    try:
        with open(json_regs, "r") as dtMember:
            data_login = json.loads(dtMember.read())
        return data_login
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
        
def save_dtMember(data_login):
    with open(json_regs, "w") as dtMember:
        dtMember.write(json.dumps(data_login, indent=4))

def load_dtProduk():
    try:
        with open(json_brg, "r") as dtProduk:
            data = json.load(dtProduk)
        return data
    except  (FileNotFoundError, json.JSONDecodeError):
        return[]
        
def save_dtProduk(data):
    with open(json_brg, "w") as dtProduk:
        json.dump(data, dtProduk, indent=4)

def load_dtKeranjang():
    try:
        with open(json_co, "r") as dtKeranjang:
            data = json.load(dtKeranjang)
        return data
    except  (FileNotFoundError, json.JSONDecodeError):
        return[]
        
def save_dtKeranjang(keranjang):
    with open(json_co, "w") as dtKeranjang:
        json.dump(keranjang, dtKeranjang, indent=4)

def load_riwayat():
    try:
        with open(json_bling, "r") as riwayat:
            data = json.load(riwayat)
        return data
    except  (FileNotFoundError, json.JSONDecodeError):
        return[]

# Data Administrator
dtAdmin = {
    'aris': 'abelia',
    'doni': 'doniaja',
    'rafly': 'wibuakut'
}

# Fungsi Login Admin
def login_admin():
    os.system("cls")
    
    teks_dekor = "login admin"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^99}|'.format('        PASTIKAN ANDA ADALAH ADMIN!        '))
    print(frame)
    print()
    
    sisa_coba = 3
    
    while sisa_coba > 0:
        try:
            username = input("Masukkan username anda: ")
            password = pwinput.pwinput("Masukkan password anda: ")
            
            if username in dtAdmin and dtAdmin[username] == password:
                print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('----LOGIN BERHASIL----', 100, f'Halo, Selamat Datang Bang {username}', 100) + '=' * 100 + '+')
                menu_admin()  # Call your admin menu function
                break
            else:
                sisa_coba -= 1
                pesan_error('LOGIN GAGAL, USERNAME ATAU PASSWORD ANDA SALAH. SILAKAN COBA LAGI!', sisa_coba)
            
            if sisa_coba == 0:
                kunci_akun()
                menu_utama()  # Redirect to main menu
                break
            
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None)

def pesan_error(pesan, sisa_coba=None, lebar=100):
    # Prepare the main error message
    error_message = pesan.rstrip('.')  # Menghapus titik di akhir
    remaining_attempts_message = f'SISA PERCOBAAN: {sisa_coba}' if sisa_coba is not None else ''
    
    print()
    print('+' + '=' * lebar + '+')
    print(f'| {error_message:^{lebar - 2}} |')
    if remaining_attempts_message:  
        print(f'| {remaining_attempts_message:^{lebar - 2}} |')
    print('+' + '=' * lebar + '+')

def kunci_akun():
    print('+' + '=' * 100 + '+\n|{:^{}}|\n+'.format('AKUN ANDA DIKUNCI. MOHON MENUNGGU SEBENTAR UNTUK MENCOBA LAGI!', 100) + '=' * 100 + '+')
    for x in range(3, 0, -1):
        time.sleep(1)
        print(f'Mencoba lagi dalam {x} detik...')

# Fungsi User
def pil_user():
    os.system("cls")
    judul = 'APAKAH ANDA MEMBER DORA FOTO?'
    panjang = 50
    frame = '+' + '=' * panjang + '+'
    # judul
    print(frame)
    print('|{:^{}}|'.format(judul, panjang))
    print('+' + '-' * panjang + '+')
    #  menu
    print('|{:^5}|{:^{}}|'.format('1', 'Ya (Login)', panjang - 6))
    print('|{:^5}|{:^{}}|'.format('2', 'Tidak (Registrasi)', panjang - 6))
    print('|{:^5}|{:^{}}|'.format('3', 'Kembali', panjang - 6))
    print(frame)

    while True:
        try:
            pilihan = input("Masukkan Pilihan Anda (1-3): ")
            if pilihan == '1':
                login_member()
                break
            elif pilihan == '2':
                regs_member()
                break
            elif pilihan == '3':
                menu_utama()
            else:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-3', sisa_coba=None, lebar=50)
        except  (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK  VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)

        except  Exception as e:
            print(f'Error: {e}')

# Fungsi Registrasi Member
def regs_member():
    os.system("cls")
    data_login = load_dtMember()
    teks_dekor = "registrasi member"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^99}|'.format('        REGISTRASI MEMBER DORA FOTO        '))
    print(frame)
    print()
    
    while True:
        try:
            nama = str(input("Masukkan Nama Lengkap Anda: "))
            email = input("Masukkan Email Anda: ")
            no_hp = input("Masukkan No. HP Anda: ")
            if  not no_hp.isdigit() or len(no_hp) < 10:
                print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('NO. TELEPON HANYA BOLEH BERUPA ANGKA DAN MINIMAL BERJUMLAH 10 ANGKA', 100, 'SILAKAN COBA LAGI.', 100) + '=' * 100 + '+')
                continue

            username = input("Masukkan Username Anda (maks. 10 karakter): ")
            if not username.isalnum() or len(username) > 10:                    
                print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('USERNAME HARUS TERDIRI DARI HURUF ATAU ANGKA', 100, 'DAN TIDAK BOLEH MELEBIHI 10 KARAKTER.', 100) + '=' * 100 + '+')
                continue
            elif any(member["Nama Member"] == username for member in data_login):
                print('+' + '=' * 100 + '+\n|{:^{}}|\n+'.format('USERNAME SUDAH DIGUNAKAN. SILAKAN MASUKKAN USERNAME LAIN.', 100) + '=' * 100 + '+')
                continue

            password1 = pwinput.pwinput("Masukkan Password Anda (maks. 8 karakter): ")
            password2 = pwinput.pwinput("Masukkan Password Anda Lagi: ")
            if password1 != password2:
                print('+' + '=' * 100 + '+\n|{:^{}}|\n+'.format('PASSWORD TIDAK COCOK, SILAKAN MASUKKAN LAGI.', 100) + '=' * 100 + '+')
                continue
            elif not password1.isalnum() or password2.isalnum() or len(password1, password2) > 8:                
                print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('PASSWORD HARUS TERDIRI DARI HURUF ATAU ANGKA', 100, 'DAN TIDAK BOLEH MELEBIHI 8 KARAKTER.', 100) + '=' * 100 + '+')
            else:
                akun = {
                    "ID": len(data_login) + 1,
                    "Nama Lengkap":  str(nama),
                    "Email": str(email),
                    "No. HP": str(no_hp),
                    "Username": str(username),
                    "Password": str(password1),
                    "Tanggal Registrasi": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Saldo": 0
                }
            data_login.append(akun)
            save_dtMember(data_login)
            print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('----REGISTRASI BERHASIL----', 100, f'Selamat Kak {nama}! Anda telah menjadi member Dora Foto.', 100) + '=' * 100 + '+')
            login_member()
            break
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL+C!', sisa_coba=None)

def login_member():
    global username
    data_login = load_dtMember()
    teks_dekor = "login member"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^99}|'.format('        PASTIKAN ANDA SUDAH MELAKUKAN REGISTRASI!        '))
    print(frame)
    print()

    sisa_coba = 3
    sdh_login = False

    while sisa_coba > 0 and not sdh_login:
        try:
            username = input("Masukkan Username Anda: ")
            password = pwinput.pwinput("Masukkan Password Anda: ")

            akun_terdaftar = False
            for member in data_login:
                if member["Username"] == username:
                    akun_terdaftar = True
                    if password == member["Password"]:
                        print('+' + '=' * 100 + '+\n|{:^{}}|\n|{:^{}}|\n+'.format('----LOGIN BERHASIL----', 100, f'Halo, Selamat Datang Kak {username}', 100) + '=' * 100 + '+')
                        sdh_login = True
                        break
                    else:
                        sisa_coba -= 1
                        pesan_error('LOGIN GAGAL, PASSWORD ANDA SALAH. SILAKAN COBA LAGI', sisa_coba)
                        continue
            
            if not akun_terdaftar:
                sisa_coba -= 1
                pesan_error('LOGIN GAGAL, MEMBER TIDAK TERDAFTAR. SILAKAN COBA LAGI.', sisa_coba)
                continue

        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL+C!', sisa_coba=None)
        except Exception as e:
            print(f'Error: {e}')

    if sisa_coba == 0:
        kunci_akun()
        sisa_coba = 3
        menu_utama()

    if sdh_login:
        menu_member()

def menu_admin():
    judul = 'MENU ADMINISTRATOR'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while  True:
        # judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        #  menu
        print('|{:^5}|{:^{}}|'.format('1', 'Cari Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lihat Katalog', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Tambah Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Update Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Hapus Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('6', 'Logout', panjang - 6))
        print(frame)

        try:
            pilihan = input("Masukkan Pilihan Anda (1-6): ")
            if pilihan == '1':
                pencarian()
            elif pilihan == '2':
                katalog_admin()
            elif pilihan == '3':
                add_produk()
            elif pilihan == '4':
                update_produk()
            elif pilihan == '5':
                delete_produk()
            elif pilihan == '6':
                keluar(pesan1='ANDA TELAH LOGOUT SEBAGAI ADMINISTRATOR.', pesan2='TERIMAKASIH.', panjang=50)
                menu_utama()
                break
            else:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-6', sisa_coba=None, lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
        except Exception as e:
            print(f'Error: {e}')

def pencarian():
    data_produk = load_dtProduk()
    input_cari = input("Masukkan kata kunci untuk pencarian (Nama Produk, Harga, atau Kategori):\n").strip()
    
    hasil_pencarian = {}

    for kategori in data_produk["Kategori"]:
        for produk in kategori["Produk"]:
            nama_cocok = input_cari.lower() in produk["Nama Produk"].lower()
            harga_cocok = str(produk["Harga /hari"]) == input_cari or str(produk["Harga /3 hari"]) == input_cari
            kategori_cocok = kategori["Nama Kategori"].lower() == input_cari.lower()

            if nama_cocok or harga_cocok or kategori_cocok:
                if kategori["Nama Kategori"] not in hasil_pencarian:
                    hasil_pencarian[kategori["Nama Kategori"]] = []
                hasil_pencarian[kategori["Nama Kategori"]].append(produk)

    if hasil_pencarian:
        print("Hasil Pencarian:")
        for nama_kategori, list_produk in hasil_pencarian.items():
            print(f"\nKategori: {nama_kategori}")

            table = PrettyTable()
            table.field_names = ["ID", "Nama Produk", "Harga /hari", "Harga /3 hari"]
            table.title = "DORA FOTO"

            for produk in list_produk:
                table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga /hari"], produk["Harga /3 hari"]])

            print(table)

    else:
        pesan_error('--Produk yang Anda Cari Tidak Ditemukan--', sisa_coba=None, lebar=50)
    
    return hasil_pencarian

def sorting_admin(dt):
    judul = 'MENU SORTING KATALOG'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while True:
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        print('|{:^5}|{:^{}}|'.format('1', 'Urutkan Berdasarkan ID', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Urutkan Berdasarkan Harga per Hari', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Urutkan Berdasarkan Harga per 3 Hari', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Kembali', panjang - 6))
        print(frame)

        pilihan = input("Masukkan Pilihan Anda (1-4): ")
        if pilihan == '1':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["ID"])
            print("Katalog telah diurutkan berdasarkan ID")
            tampilkan_katalog()
        elif pilihan == '2':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["Harga /hari"])
            print("Katalog telah diurutkan berdasarkan Harga per Hari")
            tampilkan_katalog()
        elif pilihan == '3':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["Harga /3 hari"])
            print("Katalog telah diurutkan berdasarkan Harga per 3 Hari")
            tampilkan_katalog()
        elif pilihan == '4':
            break
        else:
            print("Tolong masukkan angka yang valid.")

def sorting_member(dt):
    judul = 'MENU SORTING KATALOG'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while True:
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        print('|{:^5}|{:^{}}|'.format('1', 'Urutkan Berdasarkan ID', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Urutkan Berdasarkan Harga per Hari', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Urutkan Berdasarkan Harga per 3 Hari', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Kembali', panjang - 6))
        print(frame)

        pilihan = input("Masukkan Pilihan Anda (1-4): ")
        if pilihan == '1':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["ID"])
            print("Katalog telah diurutkan berdasarkan ID")
            tampilkan_katalog()
        elif pilihan == '2':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["Harga /hari"])
            print("Katalog telah diurutkan berdasarkan Harga per Hari")
            tampilkan_katalog()
        elif pilihan == '3':
            for kategori in dt["Kategori"]:
                kategori["Produk"].sort(key=lambda x: x["Harga /3 hari"])
            print("Katalog telah diurutkan berdasarkan Harga per 3 Hari")
            tampilkan_katalog()
        elif pilihan == '4':
            break
        else:
            print("Tolong masukkan angka yang valid.")

def katalog_admin():
    dt = load_dtProduk()
    tampilkan_katalog(dt)

    while True:
        sorting_input = input("Apakah anda ingin mengurutkan katalog? (y/n): ").lower()
        if sorting_input == 'y':
            sorting_admin()
            tampilkan_katalog()
            break
        elif sorting_input == 'n':
            break
        else:
            print("Tolong masukkan y atau n.")

def katalog_member():
    dt = load_dtProduk()
    tampilkan_katalog()

    while True:
        sorting_input = input("Apakah anda ingin mengurutkan katalog? (y/n): ").lower()
        if sorting_input == 'y':
            sorting_admin(dt)
            tampilkan_katalog(dt)
            break
        elif sorting_input == 'n':
            break
        else:
            print("Tolong masukkan y atau n.")
    add_keranjang()

def tampilkan_katalog():
    dt = load_dtProduk()
    for kategori in dt["Kategori"]:
        print(f"\nKategori: {kategori['Nama Kategori']}")

        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Harga /hari", "Harga /3 hari"]
        table.title = "Dora Foto"

        for produk in kategori["Produk"]:
            table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga /hari"], produk["Harga /3 hari"]])

        print(table)

def add_keranjang(dt):
    keranjang_items = []
    while True:
        try:
            produk_id = input("Masukkan ID produk yang ingin ditambahkan ke keranjang (atau ketik 'selesai' untuk mengakhiri): ")
            if produk_id.lower() == 'selesai':
                break
            produk = next((p for p in dt["Produk"] if p["ID"] == produk_id), None)
            if produk:
                keranjang_items.append(produk)
                print(f'Produk {produk["Nama Produk"]} telah ditambahkan ke keranjang.')
            else:
                print("ID produk tidak ditemukan. Silakan coba lagi.")
        except Exception as e:
            print(f'Error: {e}')
    print("Keranjang Anda:", keranjang_items)

def keranjang():
    global keranjang_items  # Menggunakan variabel global untuk menyimpan item keranjang
    
    if not keranjang_items:
        print("\nKeranjang Anda kosong.")
        return
    
    print("\n=== ISI KERANJANG ANDA ===")
    print("-" * 80)
    
    total_harga_per_hari = 0
    total_harga_tiga_hari = 0
    
    # Menggunakan PrettyTable untuk tampilan yang lebih rapi
    table = PrettyTable()
    table.field_names = ["No", "Kategori", "Nama Produk", "Harga /hari", "Harga /3 hari"]
    
    for index, item in enumerate(keranjang_items, 1):
        table.add_row([
            index,
            item.get('Kategori', '-'),  # Mengambil kategori jika ada
            item['Nama Produk'],
            f"Rp {item['Harga /hari']:,}",
            f"Rp {item['Harga /3 hari']:,}"
        ])
        
        total_harga_per_hari += item['Harga /hari']
        total_harga_tiga_hari += item['Harga /3 hari']
    
    print(table)
    print("-" * 80)
    print(f"Total Harga /hari    : Rp {total_harga_per_hari:,}")
    print(f"Total Harga /3 hari  : Rp {total_harga_tiga_hari:,}")
    
    # Jika ada diskon (sesuai dengan konteks JSON)
    diskon = 20  # Mengambil nilai diskon dari JSON
    if diskon > 0:
        harga_setelah_diskon_per_hari = total_harga_per_hari - (total_harga_per_hari * diskon / 100)
        harga_setelah_diskon_tiga_hari = total_harga_tiga_hari - (total_harga_tiga_hari * diskon / 100)
        
        print(f"\nDiskon {diskon}%")
        print(f"Harga Setelah Diskon /hari   : Rp {harga_setelah_diskon_per_hari:,}")
        print(f"Harga Setelah Diskon /3 hari : Rp {harga_setelah_diskon_tiga_hari:,}")
    
    print("-" * 80)
    
    # Menampilkan opsi untuk pengguna
    print("\nOpsi:")
    print("1. Hapus item dari keranjang")
    print("2. Kosongkan keranjang")
    print("3. Lanjut ke checkout")
    print("4. Kembali ke menu utama")
    
    pilihan = input("\nPilih opsi (1-4): ")
    
    if pilihan == "1":
        try:
            nomor_item = int(input("Masukkan nomor item yang ingin dihapus: "))
            if 1 <= nomor_item <= len(keranjang_items):
                item_dihapus = keranjang_items.pop(nomor_item - 1)
                print(f"\nBerhasil menghapus {item_dihapus['Nama Produk']} dari keranjang.")
                keranjang()  # Tampilkan keranjang lagi setelah menghapus
            else:
                print("\nNomor item tidak valid!")
        except ValueError:
            print("\nMasukkan nomor yang valid!")
    
    elif pilihan == "2":
        konfirmasi = input("Anda yakin ingin mengosongkan keranjang? (ya/tidak): ")
        if konfirmasi.lower() == "ya":
            keranjang_items.clear()
            print("\nKeranjang telah dikosongkan.")
    
    elif pilihan == "3":
        # Panggil fungsi checkout (akan diimplementasikan terpisah)
        checkout()
        # checkout()
    
    elif pilihan == "4":
        return
    
    else:
        print("\nPilihan tidak valid!")

def checkout():
    global keranjang_items
    
    if not keranjang_items:
        print("\nKeranjang Anda kosong. Tidak dapat melakukan checkout.")
        return
    
    print("\n=== CHECKOUT ===")
    print("\nPilih durasi sewa:")
    print("1. 1 Hari")
    print("2. 3 Hari")
    
    try:
        durasi = input("\nMasukkan pilihan (1/2): ")
        if durasi not in ['1', '2']:
            print("\nPilihan tidak valid!")
            return
        
        # Hitung total berdasarkan durasi
        total = 0
        if durasi == '1':
            durasi_text = "1 Hari"
            for item in keranjang_items:
                total += item['Harga /hari']
        else:
            durasi_text = "3 Hari"
            for item in keranjang_items:
                total += item['Harga /3 hari']
        
        # Terapkan diskon
        diskon = 20  # sesuai dengan JSON
        total_setelah_diskon = total - (total * diskon / 100)
        
        # Tampilkan ringkasan pesanan
        print("\n=== RINGKASAN PESANAN ===")
        print(f"Total Harga: Rp {total:,}")
        print(f"Diskon {diskon}%: Rp {(total * diskon / 100):,}")
        print(f"Total Setelah Diskon: Rp {total_setelah_diskon:,}")
        
        # Konfirmasi checkout
        konfirmasi = input("\nLanjutkan ke pembayaran? (ya/tidak): ")
        if konfirmasi.lower() != 'ya':
            print("\nCheckout dibatalkan.")
            return
        
        # Verifikasi password
        username = current_user['Username']  # Diasumsikan ada variabel current_user
        password = input("\nMasukkan password Anda untuk konfirmasi: ")
        
        # Verifikasi dari data JSON
        with open('regs_pa.json', 'r') as file:
            data_login = json.load(file)
        
        user = next((user for user in data_login if 
                    user['Username'] == username and 
                    user['Password'] == password), None)
        
        if not user:
            print("\nPassword salah!")
            return
        
        # Cek saldo
        if user['Saldo'] < total_setelah_diskon:
            print("\nSaldo tidak mencukupi!")
            return
        
        # Kurangi saldo
        user['Saldo'] -= total_setelah_diskon
        
        # Update file JSON
        with open('regs_pa.json', 'w') as file:
            json.dump(data_login, file, indent=4)
        
        # Buat struk
        print("\n" + "="*50)
        print("STRUK PEMBAYARAN".center(50))
        print("="*50)
        
        # Menggunakan PrettyTable untuk struk
        struk = PrettyTable()
        struk.field_names = ["Detail", "Keterangan"]
        
        # Tambahkan informasi ke struk
        waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        struk.add_row(["Tanggal & Waktu", waktu_transaksi])
        struk.add_row(["ID Member", user['ID']])
        struk.add_row(["Nama Member", user['Nama Lengkap']])
        struk.add_row(["Durasi Sewa", durasi_text])
        struk.add_row(["-"*20, "-"*20])
        
        # Tambahkan item-item yang dibeli
        for item in keranjang_items:
            harga = item['Harga /hari'] if durasi == '1' else item['Harga /3 hari']
            struk.add_row([item['Nama Produk'], f"Rp {harga:,}"])
        
        struk.add_row(["-"*20, "-"*20])
        struk.add_row(["Total", f"Rp {total:,}"])
        struk.add_row([f"Diskon {diskon}%", f"Rp {(total * diskon / 100):,}"])
        struk.add_row(["Total Setelah Diskon", f"Rp {total_setelah_diskon:,}"])
        struk.add_row(["Sisa Saldo", f"Rp {user['Saldo']:,}"])
        
        print(struk)
        print("\nTerima kasih telah berbelanja di toko kami!")
        print("Selamat menikmati produk yang Anda sewa.")
        print("="*50)
        
        # Kosongkan keranjang setelah checkout berhasil
        keranjang_items.clear()
        
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
        return

def add_produk():
    while True:
        data = load_dtProduk()  # Memuat data produk
        judul = 'TAMBAH PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        # Judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('DALAM KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        # Menu kategori
        kategori_map = {
            '1': 'Kamera',
            '2': 'Lensa',
            '3': 'Tripod',
            '4': 'Aksesoris'
        }
        
        for key, value in kategori_map.items():
            print('|{:^5}|{:^{}}|'.format(key, value, panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk Baru (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                break  # Kembali jika pengguna memilih untuk kembali
            
            if pilih_kategori not in kategori_map:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-5.', sisa_coba=None, lebar=50)
                continue
            
            nama_kategori = kategori_map[pilih_kategori]  # Mendapatkan nama kategori dari pilihan
            
            # Memasukkan produk baru
            while True:
                for kategori in data["Kategori"]:
                    if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                        try:
                            nama_produk = input("Masukkan Nama Produk Baru: ")
                            harga_hari = input("Masukkan Tarif Rental Produk per Hari: ")
                            harga_3_hari = input("Masukkan Tarif Rental Produk untuk 3 Hari: ")
                            
                            # Validasi input
                            if not (2 <= len(nama_produk) <= 50):
                                pesan_error('NAMA PRODUK HARUS 2-50 KARAKTER.', sisa_coba=None, lebar=50)
                                continue
                            if not (nama_produk.strip() and harga_hari.isdigit() and harga_3_hari.isdigit()):
                                pesan_error('INPUT TIDAK VALID. PASTIKAN FIELD TIDAK KOSONG!', sisa_coba=None, lebar=50)
                                continue
                            if not (100000000 >= int(harga_hari) >= 100 and 100000000 >= int(harga_3_hari) >= 100):
                                pesan_error('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                continue
                            if any(produk["Nama Produk"].lower() == nama_produk.lower() for produk in kategori["Produk"]):
                                pesan_error('PRODUK SUDAH ADA, MASUKKAN LAINNYA.', sisa_coba=None, lebar=50)
                                continue
                            
                            # Menambahkan produk baru
                            produk_baru = {
                                "ID": len(kategori["Produk"]) + 1,
                                "Nama Produk": str(nama_produk),
                                "Harga /hari": int(harga_hari),
                                "Harga /3 hari": int(harga_3_hari)
                            }
                            
                            kategori["Produk"].append(produk_baru)
                            save_dtProduk(data)
                            pesan_error('Produk Baru Berhasil Ditambahkan.', sisa_coba=None, lebar=50)
                            break  # Keluar dari loop setelah berhasil menambah produk
                        
                        except (ValueError, KeyboardInterrupt):
                            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
                        except Exception as e:
                            print(f"Error, {e}")
                break  # Keluar dari loop kategori setelah selesai
                
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def update_produk():
    while True:
        data = load_dtProduk()
        judul = 'UPDATE PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('DALAM KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        kategori_map = {
            '1': 'Kamera',
            '2': 'Lensa',
            '3': 'Tripod',
            '4': 'Aksesoris'
        }
        
        for key, value in kategori_map.items():
            print('|{:^5}|{:^{}}|'.format(key, value, panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk yang Ingin Diubah (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                break
            
            if pilih_kategori not in kategori_map:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-5.', sisa_coba=None, lebar=50)
                continue
            
            nama_kategori = kategori_map[pilih_kategori]
            
            for kategori in data["Kategori"]:
                if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                    table = PrettyTable()
                    table.field_names = ["ID", "Nama", "Harga /hari", "Harga /3 hari"]
                    
                    for produk in kategori["Produk"]:
                        table.add_row([produk['ID'], produk['Nama Produk'], produk['Harga /hari'], produk['Harga /3 hari']])
                    
                    print(f"\nDaftar Produk dalam Kategori '{nama_kategori}':")
                    print(table)
                    
                    id_produk = input("Masukkan ID Produk yang ingin diubah: ")
                    produk_yang_diubah = next((p for p in kategori["Produk"] if str(p["ID"]) == id_produk), None)
                    
                    if produk_yang_diubah:
                        nama_produk = input(f"Masukkan Nama Produk Baru (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Nama Produk']}): ")
                        harga_hari = input(f"Masukkan Tarif Rental Produk per Hari (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Harga /hari']}): ")
                        harga_3_hari = input(f"Masukkan Tarif Rental Produk untuk 3 Hari (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Harga /3 hari']}): ")
                        
                        if nama_produk.strip():
                            if not (2 <= len(nama_produk) <= 50):
                                pesan_error('NAMA PRODUK HARUS 2-50 KARAKTER.', sisa_coba=None, lebar=50)
                                continue
                            produk_yang_diubah['Nama Produk'] = nama_produk
                        
                        if harga_hari.strip():
                            if not harga_hari.isdigit() or not (100 <= int(harga_hari) <= 100000000):
                                pesan_error('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                continue
                            produk_yang_diubah['Harga /hari'] = int(harga_hari)
                        
                        if harga_3_hari.strip():
                            if not harga_3_hari.isdigit() or not (100 <= int(harga_3_hari) <= 100000000):
                                pesan_error('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                continue
                            produk_yang_diubah['Harga /3 hari'] = int(harga_3_hari)

                        save_dtProduk(data)
                        pesan_error('Produk Berhasil Diperbarui.', sisa_coba=None, lebar=50)
                    else:
                        pesan_error('ID PRODUK TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
                    break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def delete_produk():
    while True:
        data = load_dtProduk()
        judul = 'HAPUS PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('DALAM KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        kategori_map = {
            '1': 'Kamera',
            '2': 'Lensa',
            '3': 'Tripod',
            '4': 'Aksesoris'
        }
        
        for key, value in kategori_map.items():
            print('|{:^5}|{:^{}}|'.format(key, value, panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk yang Ingin Dihapus (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                break
            
            if pilih_kategori not in kategori_map:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-5', sisa_coba=None, lebar=50)
                continue
            
            nama_kategori = kategori_map[pilih_kategori]
            
            for kategori in data["Kategori"]:
                if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                    table = PrettyTable()
                    table.field_names = ["ID", "Nama", "Harga /hari", "Harga /3 hari"]
                    
                    for produk in kategori["Produk"]:
                        table.add_row([produk['ID'], produk['Nama Produk'], produk['Harga /hari'], produk['Harga /3 hari']])
                    
                    print(f"\nDaftar Produk dalam Kategori '{nama_kategori}':")
                    print(table)
                    
                    id_produk = input("Masukkan ID Produk yang ingin dihapus: ")
                    produk_yang_dihapus = next((p for p in kategori["Produk"] if str(p["ID"]) == id_produk), None)
                    
                    if produk_yang_dihapus:
                        kategori["Produk"].remove(produk_yang_dihapus)
                        save_dtProduk(data)
                        pesan_error('Produk Berhasil Dihapus.', sisa_coba=None, lebar=50)
                    else:
                        pesan_error('ID PRODUK TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
                    break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def menu_member():
    judul = 'MENU MEMBER'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while  True:
        # judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        #  menu
        print('|{:^5}|{:^{}}|'.format('1', 'Cari Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lihat Katalog', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Keranjang', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'E-Money', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'S&K Dora Foto', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('6', 'Logout', panjang - 6))
        print('+' + '-' * panjang + '+')
        print('|{:^{}}|'.format('PASTIKAN ANDA MEMAHAMI S&K KAMI.', panjang))
        print('|{:^{}}|'.format('DENGAN MELAKUKAN TRANSAKSI,', panjang))
        print('|{:^{}}|'.format('ANDA BERARTI MENYETUJUI.', panjang))
        print(frame)

        try:
            pilihan = input("Masukkan Pilihan Anda (1-6): ")
            if pilihan == '1':
                pencarian()
            elif pilihan == '2':
                katalog_member()
            elif pilihan == '3':
                keranjang()
            elif pilihan == '4':
                saldo()
            elif pilihan == '5':
                sk()
            elif pilihan == '6':
                keluar(teks_dekor=None, panjang=50, pesan1='Terimakasih Telah Berkunjung di Dora Foto.', pesan2='Kami Menanti Anda untuk Kembali!')
                break
            else:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-6', sisa_coba=None, lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)

        except Exception as e:
            print(f'Error: {e}')

def saldo():
    judul = 'MENU SALDO'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while  True:
        # judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        #  menu
        print('|{:^5}|{:^{}}|'.format('1', 'Lihat Saldo', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Top-Up', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Kembali', panjang - 6))
        print(frame)
        try:
            pilihan = input("Masukkan Pilihan Anda (1-3): ")
            if pilihan == '1': 
                lihat_saldo()
            elif pilihan == '2': 
                topup()
            elif  pilihan == '3':
                break
            else:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-3.', sisa_coba=None, lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
        except  Exception as e:
            print(f"Error, {e}")

def lihat_saldo():
    data_login = load_dtMember()
    pesan_error('Masukkan Password Anda untuk Melihat Saldo', sisa_coba=None, lebar=50)
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Masukkan Password Anda: ")
        akun_terdaftar = False

        for member in data_login:
            if member["Username"].lower() == username.lower():
                if member["Password"] == password:
                    akun_terdaftar = True
                    saldo_member = member["Saldo"]
                    judul = 'SALDO E-MONEY'
                    panjang = 50
                    frame = '+' + '=' * panjang + '+'
                    print(frame)
                    print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
                    print('+' + '-' * panjang + '+')
                    #  menu
                    print('|{:^{}}|'.format(f'Hai Kak {username}', panjang - 6))
                    print('|{:^{}}|'.format(f'Saldo e-money saat ini adalah Rp. {saldo_member}', panjang - 6))
                    print(frame)
                    continue

        if akun_terdaftar:
            break
        else:
            pesan_error('AKUN TIDAK TERDAFTAR ATAU KATA SANDI SALAH. SILAKAN COBA LAGI.', sisa_coba=None, lebar=50)

def topup():
    data_login = load_dtMember()  # Memuat data member
    pesan_error('Masukkan Password Anda untuk Melakukan Top-Up', sisa_coba=None, lebar=50)
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Masukkan Password Anda: ")
        akun_terdaftar = False
        user = None

        for member in data_login:
            if member["Username"].lower() == username.lower():
                if member["Password"] == password:
                    akun_terdaftar = True
                    user = member  # Menyimpan data member yang valid
                    break  # Keluar dari loop jika password benar

        if akun_terdaftar:
            while True:  # Loop untuk menu top-up
                try:
                    # Menampilkan menu top-up
                    judul = 'MENU TOP-UP'
                    panjang = 50
                    frame = '+' + '=' * panjang + '+'
                    print(frame)
                    print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
                    print('+' + '-' * panjang + '+')
                    print('|{:^5}|{:^{}}|'.format('1', 'Rp. 500.000', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('2', 'Rp. 1.000.000', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('3', 'Rp. 2.000.000', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('4', 'Rp. 5.000.000', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('5', 'Rp. 10.000.000', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('6', 'Nominal Lain', panjang - 6))
                    print('|{:^5}|{:^{}}|'.format('7', 'Kembali', panjang - 6))
                    print(frame)

                    pilihan = input('Silakan pilih nominal (1-7): ')
                    if pilihan in ['1', '2', '3', '4', '5']:
                        nominal_dict = {
                            '1': 500000,
                            '2': 1000000,
                            '3': 2000000,
                            '4': 5000000,
                            '5': 10000000
                        }
                        jumlah_topup = nominal_dict[pilihan]
                    elif pilihan == '6':
                        try:
                            jumlah_topup = int(input("Masukkan nominal yang ingin ditambahkan: Rp. "))
                            if jumlah_topup <= 0 or jumlah_topup > 150000000:
                                pesan_error('JUMLAH TOP-UP HARUS LEBIH DARI 0 DAN MAKSIMAL Rp.  150.000.000', sisa_coba=None, lebar=50)
                                continue
                        except ValueError:
                            pesan_error('INPUT TIDAK VALID. HARAP MASUKKAN ANGKA YANG BENAR', sisa_coba=None, lebar=50)
                            continue
                    elif pilihan == '7':
                        break
                    else:
                        pesan_error('PILIHAN TIDAK VALID. SILAKAN COBA LAGI', sisa_coba=None, lebar=50)
                        continue
                    
                    # Proses top-up
                    saldo_sebelum_topup = user['Saldo']  # Simpan saldo sebelum top-up
                    user['Saldo'] += jumlah_topup  # Menambahkan jumlah top-up ke saldo
                    save_dtMember(data_login)  # Menyimpan perubahan ke file JSON

                    # Menyimpan riwayat top-up ke emoney_pa.json
                    riwayat_topup = {
                        "Username": username,
                        "Jumlah": jumlah_topup,
                        "Saldo Sebelum": saldo_sebelum_topup,  # Menambahkan saldo sebelum top-up
                        "Saldo Akhir": user['Saldo']
                    }
                    with open(json_bling, 'w') as f:
                        json.dump(riwayat_topup, f, indent=4)

                    keluar(teks_dekor=None, panjang=50, pesan1='Saldo e-money anda berhasil ditambahkan', pesan2=f'Saldo e-money Anda saat ini adalah Rp. {user["Saldo"]:,}')

                except (ValueError, KeyboardInterrupt):
                    pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C', sisa_coba=None, lebar=50)
                except Exception as e:
                    print(f"Error, {e}")
                    break  # Keluar dari loop kategori setelah selesai
        else:
            pesan_error('AKUN TIDAK TERDAFTAR ATAU KATA SANDI SALAH. SILAKAN COBA LAGI.', sisa_coba=None, lebar=50)

def sk():
    try:
        with open(txt_sk, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        pesan_error('FILE TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
    except Exception as e:
        print(f"An error occurred: {e}")

def keluar(teks_dekor="dora", panjang=100, pesan1="TERIMAKASIH ATAS KUNJUNGAN ANDA!", pesan2="KAMI NANTI KUNJUNGAN ANDA SELANJUTNYA"):
    # Check if panjang is less than the length of teks_dekor
    if panjang < len(teks_dekor):
        print("Error: panjang harus lebih besar dari panjang teks dekor.")
        return
    
    # Menghitung panjang frame
    left_padding = (panjang - len(teks_dekor)) // 2
    frame = '+{}+'.format('=' * left_padding + teks_dekor + '=' * left_padding)

    # Mencetak frame dan pesan
    print(frame)
    print('|{:^{}}|'.format(pesan1, panjang))
    print('|{:^{}}|'.format(pesan2, panjang))
    print(frame)
    print()

def menu_utama():
    judul = 'MENU UTAMA'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while  True:
        # judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-'*50 + '+')
        print('|{:^{}}|'.format( 'PILIHAN ROLE' , panjang))
        print('+' + '-' * panjang + '+')
        #  menu
        print('|{:^5}|{:^{}}|'.format('1', 'Administrator DF', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Member DF', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Keluar', panjang - 6))
        print(frame)
        try:
            pilihan = input("Masukkan Pilihan Anda (1-3): ")
            if pilihan == '1': 
                login_admin()
            elif pilihan == '2': 
                pil_user()
            elif  pilihan == '3':
                keluar()
                exit()
                break
            else:
                pesan_error('TOLONG MASUKKAN BERUPA ANGKA 1-3.', sisa_coba=None, lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan_error('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
        except  Exception as e:
            print(f"Error, {e}")

# MULAI PROGRAM
menu_utama()