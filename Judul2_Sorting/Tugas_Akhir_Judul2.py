def bubble_sort(arr, n):
    # Proses Bubble Sort (ascending)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    nilai = []

    print("Masukkan nilai mahasiswa:")
    for i in range(n):
        while True:
            try:
                n_input = int(input(f"Nilai ke-{i+1}: "))
                nilai.append(n_input)
                break
            except ValueError:
                print("Input harus berupa angka!")

    print("\nNilai sebelum diurutkan:")
    print(nilai)

    # Proses sorting
    bubble_sort(nilai, n)

    print("\nNilai setelah diurutkan (Ascending):")
    for i in range(n):
        print(nilai[i], end=" ")
    print()


if __name__ == "__main__":
    main()