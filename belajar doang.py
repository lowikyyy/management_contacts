## Program Management Kontak
class Kontak:
    def __init__(self):
        self.kontak = []

    def liat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["NO"]}, {item["Email"]})')
        else:
            print("lohe kontaknya uda kosong :(((")
            return 1

    def tambah_kontak(self):
        nama = input("masukkan nama = ")
        no = input("masukkan no.hp = ")
        email = input("masukkan email = ")
        kontak_baru = {"nama": nama, "NO": no, "Email": email}
        self.kontak.append(kontak_baru)
        print("uda berhasil ditambah nih")

    def hapus_kontak(self):
        if self.liat_kontak() == 1:
            return
        else:
            i_hapus = int(input("mau delete yang mana nihh = "))
            del self.kontak[i_hapus - 1]
            print("kontak sudah terhapus :(((")


kontak_keluarga = Kontak()
kontak_kantor = Kontak()

while True :
    print("\n Menu kontak")
    print("1. pgn liat kontak nih")
    print("2. nambahin kontak bisa ga")
    print("3. ada yang mau dihapus :(((")
    print("4. pgn keluar kontak.....")

    pilihan = int(input("kamu pilih menu ke = "))

    if pilihan == 1:
        kontak_kantor.liat_kontak()

    elif pilihan == 2:
        kontak_kantor.tambah_kontak()

    elif pilihan == 3:
       kontak_kantor.hapus_kontak()

    elif pilihan == 4:
        break
    else:
        print("masukin yang bener ege")