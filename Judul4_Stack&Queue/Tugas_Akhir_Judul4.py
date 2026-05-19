class StackPortal:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.portal = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def masuk_portal(self, nama_portal):
        if self.is_full():
            print("Portal history penuh!")
            return
        self.top_idx += 1
        self.portal[self.top_idx] = nama_portal
        print(f"Berhasil masuk ke portal {nama_portal}")

    def kembali_portal(self):
        if self.is_empty():
            print("Tidak ada portal untuk kembali!")
            return
        print(f"Keluar dari portal {self.portal[self.top_idx]}")
        self.top_idx -= 1

    def lihat_portal_terakhir(self):
        if self.is_empty():
            print("Belum ada portal yang dimasuki")
            return
        print(f"Portal terakhir: {self.portal[self.top_idx]}")

    def tampilkan_riwayat(self):
        if self.is_empty():
            print("Riwayat portal kosong")
            return
        print("Riwayat Portal (terakhir ke awal):")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.portal[i]}")
        print(f"Total portal yang dimasuki: {self.top_idx + 1}")


def main():
    game = StackPortal()
    pilih = 0

    while pilih != 5:
        print("\nAnomali Journey - Portal Management:")
        print("1. Masuk Portal")
        print("2. Kembali dari Portal")
        print("3. Lihat Portal Terakhir")
        print("4. Tampilkan Riwayat Portal")
        print("5. Tinggalkan Portal dan Selesai")

        try:
            pilih = int(input("Ayo Pilih!:"))
        except ValueError:
            print("harus berupa angka!")
            continue

        if pilih == 1:
            nama = input("Masukkan nama portal: ")
            game.masuk_portal(nama)

        elif pilih == 2:
            game.kembali_portal()

        elif pilih == 3:
            game.lihat_portal_terakhir()

        elif pilih == 4:
            game.tampilkan_riwayat()

        elif pilih == 5:
            print("Selamat tinggal.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()