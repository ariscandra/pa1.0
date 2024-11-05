from datetime import datetime
from prettytable import PrettyTable
import json, os, pwinput, time, random, string

pengguna_sekarang = None
RUJUKAN = os.path.abspath(os.curdir)

JSON_REGS = f"{RUJUKAN}/regs_pa.json"
JSON_BRG = f"{RUJUKAN}/produk_pa.json"
JSON_TRANS = f"{RUJUKAN}/transaksi_pa.json"
JSON_CO = f"{RUJUKAN}/checkout_pa.json"
JSON_BLING = f"{RUJUKAN}/emoney_pa.json"
TXT_SK = f"{RUJUKAN}/sk_rental_pa.txt"

def load_data_member():
    try:
        with open(JSON_REGS, "r") as dtMember:
            data_login = json.loads(dtMember.read())
        return data_login
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
        
def save_data_member(data_login):
    with open(JSON_REGS, "w") as dtMember:
        dtMember.write(json.dumps(data_login, indent=4))

def load_data_produk():
    try:
        with open(JSON_BRG, "r") as dtProduk:
            data = json.load(dtProduk)
        return data
    except  (FileNotFoundError, json.JSONDecodeError):
        return[]
        
def save_data_produk(data):
    with open(JSON_BRG, "w") as dtProduk:
        json.dump(data, dtProduk, indent=4)

def load_keranjang():
    try:
        with open(JSON_CO, "r") as dtKeranjang:
            data = json.load(dtKeranjang)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_keranjang(keranjang):
    with open(JSON_CO, "w") as dtKeranjang:
        json.dump(keranjang, dtKeranjang, indent=4)

def load_transaksi():
    try:
        with open(JSON_TRANS, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transaksi(transaksi_list):
    with open(JSON_TRANS, "w") as file:
        json.dump(transaksi_list, file, indent=4)

def load_riwayat():
    try:
        with open(JSON_BLING, "r") as riwayat:
            data = json.load(riwayat)
        return data
    except  (FileNotFoundError, json.JSONDecodeError):
        return[]

data_admin = {
    'aris': 'abelia',
    'doni': 'doniaja',
    'rafly': 'wibuakut'
}

def pesan1(pesan, sisa_coba=None, lebar=100):
    pesan = pesan.rstrip('.')  # Menghapus titik di akhir
    pesan_sisa_coba = f'SISA PERCOBAAN: {sisa_coba}' if sisa_coba is not None else ''
    
    print()
    print('+' + '=' * lebar + '+')
    print(f'| {pesan:^{lebar - 2}} |')
    if pesan_sisa_coba:  
        print(f'| {pesan_sisa_coba:^{lebar - 2}} |')
    print('+' + '=' * lebar + '+')

def pesan2(teks_dekor=None, panjang=100, pesan1='TERIMAKASIH ATAS KUNJUNGAN ANDA!', pesan2='KAMI NANTI KUNJUNGAN ANDA SELANJUTNYA'):
    # Jika teks_dekor None, gunakan string kosong
    teks_dekor = teks_dekor if teks_dekor is not None else ''
    
    if panjang < len(teks_dekor):
        print("Error: panjang harus lebih besar dari panjang teks dekor.")
        return
    
    left_padding = (panjang - len(teks_dekor)) // 2
    right_padding = panjang - len(teks_dekor) - left_padding 
    frame = '+{}+'.format('=' * left_padding + teks_dekor + '=' * right_padding)

    print(frame)
    print('|{:^{}}|'.format(pesan1, panjang))
    print('|{:^{}}|'.format(pesan2, panjang))
    print(frame)
    print()

def kunci_akun():
    print('+' + '=' * 100 + '+\n|{:^{}}|\n+'.format('AKUN ANDA DIKUNCI. MOHON MENUNGGU SEBENTAR UNTUK MENCOBA LAGI!', 100) + '=' * 100 + '+')
    for x in range(3, 0, -1):
        time.sleep(1)
        print(f'Mencoba lagi dalam {x} detik...')

def menu_utama():
    while True:
        # Dekorasi header
        teks_dekor = "dora"
        panjang_header = 50
        frame_header = '+{}+'.format('=' * ((panjang_header - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang_header - len(teks_dekor)) // 2))
        
        print(frame_header)
        print('|{:^50}|'.format('+        DORA FOTO         +'))
        print('+' + '-'*50 + '+')
        print('|{:^50}|'.format('RENTAL ALAT FOTOGRAFI SAMARINDA'))
        print(frame_header)
        print()

        # Menu
        judul = 'MENU UTAMA'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-'*50 + '+')
        print('|{:^{}}|'.format('PILIHAN ROLE', panjang))
        print('+' + '-' * panjang + '+')
        print('|{:^5}|{:^{}}|'.format('1', 'Administrator Dora Foto', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Member Dora Foto', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Keluar', panjang - 6))
        print(frame)

        try:
            pilihan = input("Masukkan Pilihan Anda (1-3): ")
            if pilihan == '1':
                login_admin()
                continue  # Balik ke awal loop
            elif pilihan == '2':
                pil_user()
                continue  # Balik ke awal loop
            elif pilihan == '3':
                pesan2()
                return  # Keluar
            else:
                pesan1(pesan='TOLONG MASUKKAN BERUPA ANGKA 1-3.', lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan1(pesan='INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
        except Exception as e:
            print(f"Error: {e}")

def login_admin():
    # Membersihkan
    os.system('cls' if os.name == 'nt' else 'clear')
    global pengguna_sekarang
    teks_dekor = "login admin"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^99}|'.format('        PASTIKAN ANDA ADALAH ADMIN!        '))
    print(frame)
    print()
    
    sisa_coba = 4
    
    while sisa_coba > 0:
        try:
            username = input("Masukkan username anda: ")
            password = pwinput.pwinput("Masukkan password anda: ")
            
            if username in data_admin and data_admin[username] == password:
                nama_kapital = username.capitalize()
                pesan2(pesan1='----LOGIN BERHASIL----', pesan2=f'Halo, Selamat Datang Bang {nama_kapital}')
                pengguna_sekarang = 'admin'
                menu_admin()
                break
            else:
                sisa_coba -= 1
                pesan1(pesan='LOGIN GAGAL, USERNAME ATAU PASSWORD ANDA SALAH. SILAKAN COBA LAGI', sisa_coba=f'{sisa_coba}')
            
            if sisa_coba == 0:
                kunci_akun()
                menu_utama()
                break
            
        except (ValueError, KeyboardInterrupt):
            pesan1(pesan='INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!')

def menu_admin():
    global pengguna_sekarang
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
                katalog()
            elif pilihan == '3':
                add_produk()
            elif pilihan == '4':
                update_produk()
            elif pilihan == '5':
                delete_produk()
            elif pilihan == '6':
                pengguna_sekarang = None
                pesan2(pesan1='ANDA TELAH LOGOUT SEBAGAI ADMINISTRATOR.', pesan2='TERIMAKASIH.', panjang=50)
                menu_utama()
                break
            else:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-6', lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
        except Exception as e:
            print(f'Error: {e}')

def pencarian():
    data_produk = load_data_produk()
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
        pesan1('--Produk yang Anda Cari Tidak Ditemukan--', lebar=50)
    
    return hasil_pencarian

def katalog(tampil_menu=True):
    dt = load_data_produk()
    for kategori in dt["Kategori"]:
        print(f"\nKategori: {kategori['Nama Kategori']}")

        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Harga /hari", "Harga /3 hari"]
        table.title = "Dora Foto"

        for produk in kategori["Produk"]:
            table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga /hari"], produk["Harga /3 hari"]])

        print(table)
    
    if tampil_menu:
        tanya_sort() 

def sort():
    global pengguna_sekarang
    dt = load_data_produk()
    judul = 'MENU SORTING KATALOG'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while True:
        try:
            print(frame)
            print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
            print('+' + '-' * panjang + '+')
            print('|{:^5}|{:^{}}|'.format('1', 'Urutkan Berdasarkan ID', panjang - 6))
            print('|{:^5}|{:^{}}|'.format('2', 'Urutkan Berdasarkan Harga per Hari', panjang - 6))
            print('|{:^5}|{:^{}}|'.format('3', 'Urutkan Berdasarkan Harga per 3 Hari', panjang - 6))
            print('|{:^5}|{:^{}}|'.format('4', 'Kembali', panjang - 6))
            print(frame)

            pilihan = input("Masukkan Pilihan Anda (1-4): ")
            if pilihan in ['1', '2', '3']:
                if pilihan == '1':
                    for kategori in dt["Kategori"]:
                        kategori["Produk"].sort(key=lambda x: x["ID"])
                    print("Katalog telah diurutkan berdasarkan ID")
                elif pilihan == '2':
                    for kategori in dt["Kategori"]:
                        kategori["Produk"].sort(key=lambda x: x["Harga /hari"])
                    print("Katalog telah diurutkan berdasarkan Harga per Hari")
                elif pilihan == '3':
                    for kategori in dt["Kategori"]:
                        kategori["Produk"].sort(key=lambda x: x["Harga /3 hari"])
                    print("Katalog telah diurutkan berdasarkan Harga per 3 Hari")
                
                save_data_produk(dt)
                katalog(tampil_menu=False)
            elif pilihan == '4':
                for kategori in dt["Kategori"]:
                    kategori["Produk"].sort(key=lambda x: x["ID"])
                save_data_produk(dt)
                return
            else:
                pesan1(pesan='TOLONG MASUKKAN BERUPA ANGKA 1-4', lebar=50)

        except KeyboardInterrupt:
            pesan1(pesan='INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
            continue 

def tanya_sort():
    while True:
        try:
            tanya = input("Apakah anda ingin mengurutkan katalog? (y/n): ").lower()
            if tanya == 'y':
                sort()
                katalog()
                break
            elif tanya == 'n':
                break
            else:
                pesan1(pesan='TOLONG MASUKKAN BERUPA y ATAU n', lebar=50)
        
        except KeyboardInterrupt:
            pesan1(pesan='INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
            continue 

def add_produk():
    while True:
        data = load_data_produk()
        judul = 'TAMBAH PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('PILIHAN KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        print('|{:^5}|{:^{}}|'.format('1', 'Kamera', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lensa', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Tripod', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Aksesoris', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk Baru (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                return
            
            if pilih_kategori not in ['1', '2', '3', '4']:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-5.', lebar=50)
                continue
            
            if pilih_kategori == '1':
                nama_kategori = 'Kamera'
            elif pilih_kategori == '2':
                nama_kategori = 'Lensa'
            elif pilih_kategori == '3':
                nama_kategori = 'Tripod'
            elif pilih_kategori == '4':
                nama_kategori = 'Aksesoris'
            
            while True:
                for kategori in data["Kategori"]:
                    if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                        try:
                            nama_produk = input("Masukkan Nama Produk Baru: ")
                            harga_hari = input("Masukkan Tarif Rental Produk per Hari: Rp.")
                            harga_3_hari = input("Masukkan Tarif Rental Produk untuk 3 Hari: Rp.")
                            
                            if not (2 <= len(nama_produk) <= 50):
                                pesan1('NAMA PRODUK HARUS 2-50 KARAKTER.', sisa_coba=None, lebar=50)
                                continue
                            if not (nama_produk.strip() and harga_hari.isdigit() and harga_3_hari.isdigit()):
                                pesan2(pesan1='INPUT TIDAK VALID. PASTIKAN HARGA TIDAK KOSONG!', pesan2='ATAU BERUPA ANGKA',  panjang=50)
                                continue
                            if not (100000000 >= int(harga_hari) >= 100 and 100000000 >= int(harga_3_hari) >= 100):
                                pesan1('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                continue
                            if any(produk["Nama Produk"].lower() == nama_produk.lower() for produk in kategori["Produk"]):
                                pesan1('PRODUK SUDAH ADA, MASUKKAN LAINNYA.', sisa_coba=None, lebar=50)
                                continue
                            
                            produk_baru = {
                                "ID": len(kategori["Produk"]) + 1,
                                "Nama Produk": str(nama_produk),
                                "Harga /hari": int(harga_hari),
                                "Harga /3 hari": int(harga_3_hari)
                            }
                            
                            kategori["Produk"].append(produk_baru)
                            save_data_produk(data)
                            pesan1('Produk Baru Berhasil Ditambahkan.', lebar=50)
                            return
                        
                        except (ValueError, KeyboardInterrupt):
                            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
                            continue
                        except Exception as e:
                            print(f"Error: {e}")
                            continue
                
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue

def update_produk():
    while True:
        data = load_data_produk()
        judul = 'UPDATE PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('PILIHAN KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        print('|{:^5}|{:^{}}|'.format('1', 'Kamera', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lensa', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Tripod', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Aksesoris', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk yang Ingin Diubah (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                return
            
            if pilih_kategori not in ['1', '2', '3', '4']:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-5.', sisa_coba=None, lebar=50)
                continue
            
            if pilih_kategori == '1':
                nama_kategori = 'Kamera'
            elif pilih_kategori == '2':
                nama_kategori = 'Lensa'
            elif pilih_kategori == '3':
                nama_kategori = 'Tripod'
            elif pilih_kategori == '4':
                nama_kategori = 'Aksesoris'
            
            for kategori in data["Kategori"]:
                if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                    table = PrettyTable()
                    table.field_names = ["ID", "Nama", "Harga /hari", "Harga /3 hari"]
                    
                    for produk in kategori["Produk"]:
                        table.add_row([produk['ID'], produk['Nama Produk'], produk['Harga /hari'], produk['Harga /3 hari']])
                    
                    print(f"\nDaftar Produk dalam Kategori '{nama_kategori}':")
                    print(table)
                    
                    while True:
                        try:
                            id_produk = input("Masukkan ID Produk yang ingin diubah: ")
                            produk_yang_diubah = next((p for p in kategori["Produk"] if str(p["ID"]) == id_produk), None)
                            
                            if produk_yang_diubah:
                                nama_produk = input(f"Masukkan Nama Produk Baru (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Nama Produk']}): ")
                                harga_hari = input(f"Masukkan Tarif Rental Produk per Hari (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Harga /hari']}): ")
                                harga_3_hari = input(f"Masukkan Tarif Rental Produk untuk 3 Hari (tekan enter jika tidak ingin mengubah, saat ini: {produk_yang_diubah['Harga /3 hari']}): ")
                                
                                if nama_produk.strip():
                                    if not (2 <= len(nama_produk) <= 50):
                                        pesan1('NAMA PRODUK HARUS 2-50 KARAKTER.', sisa_coba=None, lebar=50)
                                        continue
                                    produk_yang_diubah['Nama Produk'] = nama_produk
                                
                                if harga_hari.strip():
                                    if not harga_hari.isdigit() or not (100 <= int(harga_hari) <= 100000000):
                                        pesan1('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                        continue
                                    produk_yang_diubah['Harga /hari'] = int(harga_hari)
                                
                                if harga_3_hari.strip():
                                    if not harga_3_hari.isdigit() or not (100 <= int(harga_3_hari) <= 100000000):
                                        pesan1('HARGA HARUS Rp. 100-100.000.000.', sisa_coba=None, lebar=50)
                                        continue
                                    produk_yang_diubah['Harga /3 hari'] = int(harga_3_hari)

                                save_data_produk(data)
                                pesan1('Produk Berhasil Diperbarui.', sisa_coba=None, lebar=50)
                                return
                            else:
                                pesan1('ID PRODUK TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
                                continue
                        
                        except (ValueError, KeyboardInterrupt):
                            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
                            continue
                        except Exception as e:
                            print(f"Error: {e}")
                            continue
                    
                    break
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue

def delete_produk():
    while True:
        data = load_data_produk()
        judul = 'HAPUS PRODUK'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * 50 + '+')
        print('|{:^{}}|'.format('PILIHAN KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        print('|{:^5}|{:^{}}|'.format('1', 'Kamera', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lensa', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Tripod', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Aksesoris', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)
        
        try:
            pilih_kategori = input('Pilih dalam Kategori Apakah Produk yang Ingin Dihapus (1-5): ')
            if pilih_kategori == '5':
                menu_admin()
                return
            
            if pilih_kategori not in ['1', '2', '3', '4']:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-5', sisa_coba=None, lebar=50)
                continue
            
            if pilih_kategori == '1':
                nama_kategori = 'Kamera'
            elif pilih_kategori == '2':
                nama_kategori = 'Lensa'
            elif pilih_kategori == '3':
                nama_kategori = 'Tripod'
            elif pilih_kategori == '4':
                nama_kategori = 'Aksesoris'
            
            for kategori in data["Kategori"]:
                if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                    table = PrettyTable()
                    table.field_names = ["ID", "Nama", "Harga /hari", "Harga /3 hari"]
                    
                    for produk in kategori["Produk"]:
                        table.add_row([produk['ID'], produk['Nama Produk'], produk['Harga /hari'], produk['Harga /3 hari']])
                    
                    print(f"\nDaftar Produk dalam Kategori '{nama_kategori}':")
                    print(table)
                    
                    while True:
                        try:
                            id_produk = input("Masukkan ID Produk yang ingin dihapus: ")
                            produk_yang_dihapus = next((p for p in kategori["Produk"] if str(p["ID"]) == id_produk), None)
                            
                            if produk_yang_dihapus:
                                kategori["Produk"].remove(produk_yang_dihapus)
                                save_data_produk(data)
                                pesan1('Produk Berhasil Dihapus.', sisa_coba=None, lebar=50)
                                return
                            else:
                                pesan1('ID PRODUK TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
                                continue
                        
                        except (ValueError, KeyboardInterrupt):
                            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
                            continue
                        except Exception as e:
                            print(f"Error: {e}")
                            continue
                    
                    break
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue

def pil_user():
    os.system('cls' if os.name == 'nt' else 'clear')
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
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-3', sisa_coba=None, lebar=50)
        except  (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK  VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)

        except  Exception as e:
            print(f'Error: {e}')

def regs_member():
    os.system("cls")
    data_login = load_data_member()
    teks_dekor = "registrasi member"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^99}|'.format('        AYO BERGABUNG BERSAMA KAMI        '))
    print(frame)
    print()

    while True:
        nama = input("Masukkan Nama Lengkap Anda: ")
        if 5 < len(nama) <= 50: 
            break
        pesan2(pesan1='NAMA HARUS LEBIH DARI 5 HURUF DAN MAKSIMAL 50 HURUF', pesan2='SILAKAN COBA LAGI')

    while True:
        email = input("Masukkan Email Anda: ")
        if 8 < len(email) <= 100:
            break
        pesan2(pesan1='EMAIL HARUS LEBIH DARI 8 KARAKTER DAN MAKSIMAL 100 KARAKTER', pesan2='SILAKAN COBA LAGI')

    while True:
        no_hp = input("Masukkan No. HP Anda: ")
        if no_hp.isdigit() and 10 <= len(no_hp) <= 20:
            break
        pesan2(pesan1='NO. TELEPON HANYA BOLEH BERUPA ANGKA DAN MINIMAL BERJUMLAH 10-20 ANGKA', pesan2='SILAKAN COBA LAGI')

    while True:
        username = input("Masukkan Username Anda (maks. 10 karakter): ")
        if username.isalnum() and len(username) <= 10:
            if not any(member["Username"] == username for member in data_login):
                break
            pesan1(pesan='USERNAME SUDAH DIGUNAKAN. SILAKAN MASUKKAN USERNAME LAIN',  sisa_coba=None)

        else:
            pesan2(pesan1='USERNAME HARUS TERDIRI DARI HURUF ATAU ANGKA', pesan2='DAN TIDAK BOLEH MELEBIHI 10 KARAKTER')

    while True:
        password1 = pwinput.pwinput("Masukkan Password Anda (maks. 8 karakter): ")
        if password1.isalnum() and len(password1) <= 8:
            password2 = pwinput.pwinput("Masukkan Password Anda Lagi: ")
            if password1 == password2:
                break
            pesan1(pesan='PASSWORD TIDAK COCOK, SILAKAN MASUKKAN LAGI',  sisa_coba=None)
        else:
            pesan2(pesan1='PASSWORD HARUS TERDIRI DARI HURUF ATAU ANGKA', pesan2='DAN TIDAK BOLEH MELEBIHI 8 KARAKTER')

    akun = {
        "ID": len(data_login) + 1,
        "Nama Lengkap": nama,
        "Email": email,
        "No. HP": no_hp,
        "Username": username,
        "Password": password1,
        "Tanggal Registrasi": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Saldo": 0
    }
    data_login.append(akun)
    save_data_member(data_login)
    pesan2(pesan1='----REGISTRASI BERHASIL----', pesan2=f'Selamat Kak {nama}! Anda telah menjadi member Dora Foto')
    login_member()

    try:
        pil_user()
    except KeyboardInterrupt:
        pesan1(pesan='INPUT TIDAK VALID. JANGAN TEKAN CTRL+C!',  sisa_coba=None)
        
def login_member():
    global username, pengguna_sekarang
    data_login = load_data_member()
    teks_dekor = "login member"
    panjang = 100
    frame = '+{}+'.format('=' * ((panjang - len(teks_dekor)) // 2) + teks_dekor + '=' * ((panjang - len(teks_dekor)) // 2))
    print(frame)
    print('|{:^100}|'.format('        PASTIKAN ANDA SUDAH MELAKUKAN REGISTRASI!        '))
    print(frame)
    print()

    sisa_coba = 4
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
                        nama_kapital = username.capitalize()
                        pesan2(pesan1='----LOGIN BERHASIL----', pesan2=f'Halo, Selamat Datang Kak {nama_kapital}')
                        sdh_login = True
                        pengguna_sekarang = 'member'
                        break
                    else:
                        sisa_coba -= 1
                        pesan1(pesan='LOGIN GAGAL, PASSWORD ANDA SALAH. SILAKAN COBA LAGI', sisa_coba=f'{sisa_coba}')
                        continue
            
            if not akun_terdaftar:
                sisa_coba -= 1
                pesan1('LOGIN GAGAL, MEMBER TIDAK TERDAFTAR. SILAKAN COBA LAGI', sisa_coba=f'{sisa_coba}')
                continue

        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL+C!')
        except Exception as e:
            print(f'Error: {e}')

    if sisa_coba == 0:
        kunci_akun()
        sisa_coba = 4
        menu_utama()

    if sdh_login:
        menu_member()

def menu_member():
    global pengguna_sekarang
    judul = 'MENU MEMBER'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while True:
        # judul
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        #  menu
        print('|{:^5}|{:^{}}|'.format('1', 'Cari Produk', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lihat Katalog', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Transaksi', panjang - 6))
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
                katalog(tampil_menu=True)
            elif pilihan == '3':
                menu_transaksi()
            elif pilihan == '4':
                saldo()
            elif pilihan == '5':
                sk()
            elif pilihan == '6':
                pengguna_sekarang = None
                pesan2(panjang=50, pesan1='Terimakasih Telah Berkunjung di Dora Foto.', pesan2='Kami Menanti Anda untuk Kembali!')
                pil_user()
            else:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-6', lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
        except Exception as e:
            print(f'Error: {e}')

def menu_transaksi():
    judul = 'MENU TRANSAKSI'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    while True:
        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('+' + '-' * panjang + '+')
        print('|{:^5}|{:^{}}|'.format('1', 'Tambah ke Keranjang', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lihat Keranjang', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Proses Pembayaran', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Riwayat Transaksi', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)

        try:
            pilihan = input("Masukkan Pilihan Anda (1-5): ")
            if pilihan == '1':
                tambah_ke_keranjang()
            elif pilihan == '2':
                lihat_keranjang()
            elif pilihan == '3':
                checkout()
            elif pilihan == '4':
                riwayat_transaksi()
            elif pilihan == '5':
                return
            else:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-5', lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', lebar=50)
        except Exception as e:
            print(f"Error: {e}")

def tambah_ke_keranjang():
    data = load_data_produk()
    keranjang = load_keranjang()
    
    while True:
        judul = 'TERSEDIA PERALATAN DALAM'
        panjang = 50
        frame = '+' + '=' * panjang + '+'

        print(frame)
        print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
        print('|{:^{}}|'.format('PILIHAN KATEGORI', panjang))
        print('+' + '-' * panjang + '+')
        
        print('|{:^5}|{:^{}}|'.format('1', 'Kamera', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('2', 'Lensa', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('3', 'Tripod', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('4', 'Aksesoris', panjang - 6))
        print('|{:^5}|{:^{}}|'.format('5', 'Kembali', panjang - 6))
        print(frame)

        try:
            pilih_kategori = input('Pilih kategori produk (1-5): ')
            if pilih_kategori == '5':
                return
            
            if pilih_kategori not in ['1', '2', '3', '4']:
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-5', sisa_coba=None, lebar=50)
                continue
            
            kategori = data["Kategori"][int(pilih_kategori)-1]
            
            print(f"\nProduk dalam kategori {kategori['Nama Kategori']}:")
            table = PrettyTable()
            table.field_names = ["ID", "Nama Produk", "Harga /hari", "Harga /3 hari"]
            
            for produk in kategori["Produk"]:
                table.add_row([
                    produk["ID"],
                    produk["Nama Produk"],
                    f"Rp {produk['Harga /hari']:,}",
                    f"Rp {produk['Harga /3 hari']:,}"
                ])
            print(table)
            
            try:
                id_produk = int(input("\nMasukkan ID produk (0 untuk batal): "))
                if id_produk == 0:
                    continue
                
                produk = next((p for p in kategori["Produk"] if p["ID"] == id_produk), None)
                
                if produk:
                    item_keranjang = {
                        "id_produk": produk["ID"],
                        "nama_produk": produk["Nama Produk"],
                        "kategori": kategori["Nama Kategori"],
                        "harga_per_hari": produk["Harga /hari"],
                        "harga_per_3_hari": produk["Harga /3 hari"]
                    }
                    
                    if username not in keranjang:
                        keranjang[username] = []
                    keranjang[username].append(item_keranjang)
                    save_keranjang(keranjang)
                    
                    print(f"\nProduk '{produk['Nama Produk']}' berhasil ditambahkan ke keranjang!")
                else:
                    pesan1('ID PRODUK TIDAK TERDAFTAR / DITEMUKAN', lebar=50)
                    
            except ValueError:
                pesan1('INPUT TIDAK VALID', sisa_coba=None, lebar=50)
                
        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
        except Exception as e:
            print(f"Error: {e}")

def lihat_keranjang():
    keranjang = load_keranjang()

    if username not in keranjang or not keranjang[username]:
        pesan1('KERANJANG ANDA KOSONG', lebar=50)
        return

    items = keranjang[username]
    table = PrettyTable()
    table.title ="KERANJANG"
    table.field_names = ["No", "Nama Produk", "Kategori"]
    
    for idx, item in enumerate(items, 1):
        table.add_row([
            idx,
            item["nama_produk"],
            item["kategori"]
        ])

    print(table)

def checkout():
    keranjang = load_keranjang()
    judul = 'PROSES PEMBAYARAN RENTAL'
    panjang = 50
    frame = '+' + '=' * panjang + '+'

    print(frame)
    print('|{:^{}}|'.format('+ ' + judul + ' +', panjang))
    print(frame)

    if username not in keranjang or not keranjang[username]:
        print('|{:^{}}|'.format('KERANJANG ANDA KOSONG', panjang))
        print(frame)
        return

    lihat_keranjang()
    
    try:
        konfirmasi = input("\nLanjutkan checkout? (y/n): ").lower()
        if konfirmasi != 'y':
            return
            
        # Input tanggal pengembalian
        print(frame)
        print('|{:^{}}|'.format('MASUKKAN TANGGAL PENGEMBALIAN', panjang))
        print(frame)
        
        while True:
            try:
                tanggal_kembali_str = input("Masukkan tanggal (DD-MM-YYYY): ")
                tanggal_kembali = datetime.strptime(tanggal_kembali_str, "%d-%m-%Y")
                waktu_transaksi = datetime.now()
                
                durasi = (tanggal_kembali - waktu_transaksi).days + 1
                if not 1 <= durasi <= 30:
                    pesan1('DURASI SEWA HARUS 1-30 HARI', sisa_coba=None, lebar=50)
                    continue
                break
            except ValueError:
                pesan1('FORMAT TANGGAL TIDAK VALID (DD-MM-YYYY)', sisa_coba=None, lebar=50)

        # Proses hitung harga
        total_harga = 0
        for item in keranjang[username]:
            if durasi >= 3:
                paket_3_hari = durasi // 3
                sisa_hari = durasi % 3
                harga = (paket_3_hari * item["harga_per_3_hari"]) + (sisa_hari * item["harga_per_hari"])
            else:
                harga = durasi * item["harga_per_hari"]
                
            diskon, persen_diskon = hitung_diskon(durasi, harga)
            harga_akhir = harga - diskon
            
            item.update({
                "durasi": durasi,
                "harga_awal": harga,
                "diskon_persen": persen_diskon,
                "diskon_nominal": diskon,
                "harga_akhir": harga_akhir
            })
            total_harga += harga_akhir

        # Cek saldo
        data_member = load_data_member()
        member = next((m for m in data_member if m["Username"] == username), None)
        
        if not member or member["Saldo"] < total_harga:
            pesan1('SALDO ANDA TIDAK MENCUKUPI', sisa_coba=None, lebar=50)
            return

        id_transaksi = buat_kode_struk()
        member["Saldo"] -= total_harga
        save_data_member(data_member)

        # Simpan transaksi
        transaksi_baru = {
            "id_transaksi": id_transaksi,
            "username": username,
            "waktu_transaksi": waktu_transaksi.strftime("%d-%m-%Y %H:%M:%S"),
            "tanggal_kembali": tanggal_kembali.strftime("%d-%m-%Y"),
            "durasi": durasi,
            "total_harga": total_harga,
            "items": keranjang[username]
        }

        transaksi_list = load_transaksi()
        transaksi_list.append(transaksi_baru)
        save_transaksi(transaksi_list)

        # Cetak struk
        print("\n" + "="*70)
        print("{:^70}".format("STRUK TRANSAKSI"))
        print("{:^70}".format("DORA FOTO"))
        print("{:^70}".format("RENTAL PERALATAN FOTOGRAFI"))
        print("{:^70}".format("Jl. Pramuka VI No.12 Blok E, Samarinda"))

        print("{:^70}".format("Telp: 0821 4117 2579"))
        print("="*70)
        print(f"ID Transaksi                                 : {id_transaksi}")
        print(f"Tanggal & Waktu Transaksi                    : {waktu_transaksi.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Penyewa                                      : Kak {username}")
        print(f"Tanggal Pengembalian                         : {tanggal_kembali.strftime('%d-%m-%Y')}")
        print(f"Durasi Rental                                : {durasi} hari")
        print("-"*70)
        print("{:^70}".format("DETAIL PENYEWAAN"))
        print("-"*70)

        for item in transaksi_baru['items']:
            print(f"\nKategori                                     : {item['kategori']}")
            print(f"Produk                                       : {item['nama_produk']}")
            print(f"Tarif Awal (Sebelum Diskon)                  : Rp {item['harga_awal']:,}")
            print(f"Diskon ({item['diskon_persen']}%)                                  : Rp {item['diskon_nominal']:,}")
            print(f"Tarif Akhir (Setelah Diskon)                 : Rp {item['harga_akhir']:,}")
            print("Ketentuan diskon ada di S&K Kami ya kak")

        print("-"*70)
        print(f"Total Pembayaran                             : Rp {total_harga:,}")
        print(f"Saldo Awal                                   : Rp {(member['Saldo'] + total_harga):,}")
        print(f"Saldo Akhir                                  : Rp {member['Saldo']:,}")
        print("="*70)
        print("{:^70}".format("TERIMA KASIH!"))
        print("{:^70}".format("BALIK LAGI YA KAK, SOALNYA PERALATANNYA MAHAL ;)"))
        print("="*70)

        # Kosongkan keranjang
        keranjang[username] = []
        save_keranjang(keranjang)
        
        print("\nCheckout berhasil!")

    except (ValueError, KeyboardInterrupt):
        pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
    except Exception as e:
        print(f"Error: {e}")

def hitung_diskon(durasi, harga):
    if durasi >= 7:
        diskon_persen = 10
    elif durasi >= 3:
        diskon_persen = 5
    else:
        diskon_persen = 0
    
    diskon_nominal = (diskon_persen / 100) * harga
    return diskon_nominal, diskon_persen

def buat_kode_struk():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def riwayat_transaksi():
    try:
        list_transaksi = load_transaksi()

        # Filter transaksi untuk pengguna yang sedang login
        transaksi_member = [t for t in list_transaksi if t.get("username") == username]

        if not transaksi_member:
            pesan1('TESTTT')
            return

        table = PrettyTable()
        table.title= f'RIWAYAT TRANSAKSI KAK {username.upper()}'
        table.field_names = ["ID Transaksi", "Tanggal & Waktu Transaksi", "Tanggal Pengembalian", "Durasi", "Produk", "Total Tarif"]

        table.align = "l" 
        table.max_width = 50

        for transaksi in transaksi_member:
            list_produk = []
            if 'items' in transaksi:
                for item in transaksi['items']:
                    list_produk.append(item['nama_produk'])
            produk_str = '\n'.join(list_produk) 

            durasi = transaksi.get("durasi", "N/A")
            durasi_str  = f"{durasi} hari" if durasi != "N/A" else "N/A"

            table.add_row([
                # N/A itu untuk semisal gada isi
                transaksi.get("id_transaksi", "N/A"), 
                transaksi.get("waktu_transaksi", "N/A"),
                transaksi.get("tanggal_kembali", "N/A"),
                durasi_str,
                produk_str or "N/A",
                f"Rp {transaksi.get('total_harga', 0):,.0f}"
            ])

        print(table)

    except Exception as e:
        print(f"Error: {str(e)}")

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
                pesan1('TOLONG MASUKKAN BERUPA ANGKA 1-3.', sisa_coba=None, lebar=50)
        except (ValueError, KeyboardInterrupt):
            pesan1('INPUT TIDAK VALID. JANGAN TEKAN CTRL + C!', sisa_coba=None, lebar=50)
        except  Exception as e:
            print(f"Error, {e}")

def lihat_saldo():
    data_login = load_data_member()
    pesan1('Masukkan Password Anda untuk Melihat Saldo', sisa_coba=None, lebar=50)
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
                    print('|{:^{}}|'.format(f'Hai Kak {username}', panjang))
                    print('|{:^{}}|'.format(f'Saldo e-money kakak saat ini Rp. {saldo_member}', panjang))
                    print(frame)
                    continue

        if akun_terdaftar:
            break
        else:
            pesan2(pesan1='AKUN TIDAK TERDAFTAR ATAU', pesan2='KATA SANDI SALAH, SILAKAN COBA LAGI', sisa_coba=None, lebar=50)

def topup():
    data_login = load_data_member()
    pesan1('Masukkan Password Anda untuk Melakukan Top-Up', sisa_coba=None, lebar=50)
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Masukkan Password Anda: ")
        user = next((member for member in data_login if member["Username"].lower() == username.lower() and member["Password"] == password), None)

        if user:
            while True:
                try:
                    # Menu
                    print('+' + '=' * 50 + '+')
                    print('|{:^50}|'.format('MENU TOP-UP'))
                    print('+' + '-' * 50 + '+')
                    print('|{:^5}|{:^44}|'.format('1', 'Rp. 500.000'))
                    print('|{:^5}|{:^44}|'.format('2', 'Rp. 1.000.000'))
                    print('|{:^5}|{:^44}|'.format('3', 'Rp. 2.000.000'))
                    print('|{:^5}|{:^44}|'.format('4', 'Rp. 5.000.000'))
                    print('|{:^5}|{:^44}|'.format('5', 'Rp. 10.000.000'))
                    print('|{:^5}|{:^44}|'.format('6', 'Nominal Lain'))
                    print('|{:^5}|{:^44}|'.format('7', 'Kembali'))
                    print('+' + '=' * 50 + '+')

                    pilihan = input('Silakan pilih nominal (1-7): ')
                    if pilihan in ['1', '2', '3', '4', '5']:
                        pil_nominal = {
                            '1': 500000,
                            '2': 1000000,
                            '3': 2000000,
                            '4': 5000000,
                            '5': 10000000
                        }
                        jumlah_topup = pil_nominal[pilihan]
                    elif pilihan == '6':
                        try:
                            jumlah_topup = int(input("Masukkan nominal yang ingin ditambahkan: Rp. "))
                            if jumlah_topup <= 0 or jumlah_topup > 150000000:
                                pesan2(pesan1='JUMLAH TOP-UP HARUS LEBIH DARI 0', pesan2='DAN MAKSIMAL Rp. 150.000.000', panjang=50)
                                continue
                        except ValueError:
                            pesan2(pesan1='INPUT TIDAK VALID', pesan2='HARAP MASUKKAN ANGKA YANG BENAR', panjang=50)
                            continue
                    elif pilihan == '7':
                        return 
                    else:
                        pesan2(pesan1='PILIHAN TIDAK VALID', pesan2='SILAKAN COBA LAGI', panjang=50)
                        continue
                    
                    saldo_sebelum_topup = user['Saldo']
                    user['Saldo'] += jumlah_topup
                    save_data_member(data_login)

                    riwayat_topup = {
                        "Username": username,
                        "Jumlah": jumlah_topup,
                        "Saldo Sebelum": saldo_sebelum_topup,
                        "Saldo Akhir": user['Saldo']
                    }
                    with open(JSON_BLING, 'w') as f:
                        json.dump(riwayat_topup, f, indent=4)

                    pesan2(teks_dekor='berhasil!', panjang=50, pesan1='Saldo e-money anda berhasil ditambahkan', pesan2=f'Saldo e-money Kakak saat ini Rp. {user["Saldo"]:,}')
                    return 

                except ValueError:
                    pesan1('INPUT TIDAK VALID. HARAP MASUKKAN ANGKA YANG BENAR', sisa_coba=None, lebar=50)
                except KeyboardInterrupt:
                    pesan1('OPERASI DIBATALKAN', sisa_coba=None, lebar=50)
                except Exception as e:
                    print(f"Error: {e}")
                    return

        else:
            pesan2(pesan1='AKUN TIDAK TERDAFTAR ATAU', pesan2='KATA SANDI SALAH. SILAKAN COBA LAGI', lebar=50)

def sk():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(TXT_SK, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        pesan1('FILE TIDAK DITEMUKAN.', sisa_coba=None, lebar=50)
    except Exception as e:
        print(f"An error occurred: {e}")

# MULAI PROGRAM
menu_utama()
