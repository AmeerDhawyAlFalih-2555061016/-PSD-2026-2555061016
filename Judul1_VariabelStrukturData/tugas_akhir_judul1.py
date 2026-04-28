def menu():
    print("\n PLAYLIST LAGU")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Hapus Lagu")
    print("4. Keluar")


class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def tambah_lagu(self, judul):
        baru = Node(judul)

        if self.head is None:
            self.head = baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = baru

    def tampilkan(self):
        if self.head is None:
            print("Playlist kosong")
        else:
            current = self.head
            i = 1
            while current:
                print(f"{i}. {current.judul}")
                current = current.next
                i += 1

    def hapus(self, judul):
        current = self.head
        prev = None

        if current and current.judul == judul:
            self.head = current.next
            print("Lagu berhasil dihapus")
            return

        while current and current.judul != judul:
            prev = current
            current = current.next

        if current is None:
            print("Lagu tidak ditemukan")
            return

        prev.next = current.next
        print("Lagu berhasil dihapus")

def main():
    playlist = Playlist()
    running = True

    while running:
        menu()
        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            judul = input("Masukkan judul lagu: ")
            playlist.tambah_lagu(judul)

        elif pilihan == 2:
            playlist.tampilkan()

        elif pilihan == 3:
            judul = input("Masukkan judul lagu yang ingin dihapus: ")
            playlist.hapus(judul)

        elif pilihan == 4:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()