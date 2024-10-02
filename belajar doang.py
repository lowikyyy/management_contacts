## Program Management Kontak

kontak1 = {"nama": "witan", "NO": "082457236812", "Email": 'witan@gmail.com'}
kontak2 = {"nama": "hokky", "NO": "082457237341", "Email": 'hokky@gmail.com'}
kontak = [kontak1, kontak2]

while True :
    print("\n Menu kontak")
    print("1. pgn liat kontak nih")
    print("2. nambahin kontak bisa ga")
    print("3. ada yang mau dihapus :(((")
    print("4. pgn keluar kontak.....")

    pilihan = int(input("kamu pilih menu ke = "))

    if pilihan == 1:
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["NO"]}, {item["Email"]})')
        else:
            print("lohe kontaknya uda kosong :(((")
    elif pilihan == 2:
        nama = input("masukkan nama = ")
        no = input("masukkan no.hp = ")
        email = input("masukkan email = ")
        kontak_baru = {"nama": nama, "NO": no, "Email": email}
        kontak.append(kontak_baru)
        print("uda berhasil ditambah nih")
    elif pilihan == 3:
        print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["NO"]}, {item["Email"]})')
        else:
            print("lohe kontaknya uda kosong :(((")
            continue

        i_hapus = int(input("mau delete yang mana nihh = "))
        del kontak[i_hapus-1]
        print("kontak sudah terhapus :(((")
    elif pilihan == 4:
        break
    else:
        print("masukin yang bener ege")