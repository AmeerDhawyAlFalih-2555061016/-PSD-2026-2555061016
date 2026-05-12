def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i] == target:
            counter += 1
        i += 1

    return counter


def main():
    data = [7, 14, 7, 12, 99, 40, 40, 10, 24]
    n = len(data)

    print(f"Data level player: {data}")


    while True:
        print("\n Dipersilahkan memilih opsi:")
        print("1. Cari level")
        print("2. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            while True:
                try:
                    target = int(input("Masukkan level yang ingin dicari: "))
                    break
                except ValueError:
                    print("masukkan angka!")


            counter = sequential_search(data, n, target)

            if counter > 0:
                print(f"Level {target} ditemukan sebanyak {counter} player.")

                if 1 <= target <= 10:
                    print("Kategori Beginner : Player masih tahap awal permainan.")

                elif 11 <= target <= 25:
                    print("Kategori Veteran : Telah menaklukkan bos dungeon level 10.")

                elif 26 <= target <= 40:
                    print("Kategori Elite : Sudah menyelesaikan banyak misi sulit.")

                else:
                    print("Kategori Legend : Player termasuk rank tertinggi.")
            else:
                print(f"Level {target} tidak ditemukan.")

        elif pilihan == "2":
            print("Terima kasih telah bermain! Sampai jumpa lagi.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()