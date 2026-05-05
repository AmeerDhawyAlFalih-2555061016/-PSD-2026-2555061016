Tugas Akhir Judul 2

Judul Program: Pengurutan Nilai Mahasiswa

Program ini dibuat untuk mengurutkan nilai mahasiswa menggunakan algoritma Bubble Sort. Data nilai yang dimasukkan pengguna akan diproses dengan cara membandingkan elemen yang bersebelahan dan menukarnya jika tidak sesuai urutan, hingga seluruh data tersusun dari yang terkecil ke terbesar. Program ini bertujuan untuk memahami konsep dasar sorting secara sederhana.

source code:
<img width="1186" height="1964" alt="codesnap Tugas_Akhir_Judul2" src="https://github.com/user-attachments/assets/6d3b0911-0b86-4000-a99a-981d8a2819e5" />

penjelasan:
1. Mendefinisikan fungsi tukar(arr, i, j) untuk menukar posisi dua elemen dalam array.
2. Menyimpan nilai pada indeks i ke dalam variabel sementara temp.
3. Memindahkan nilai pada indeks j ke posisi indeks i.
4. Menempatkan nilai temp ke posisi indeks j (proses pertukaran selesai).
5. Mendefinisikan fungsi bubble_sort(arr, n) untuk mengurutkan array.
6. Membuat perulangan luar (for i) untuk jumlah putaran Bubble Sort.
7. Membuat perulangan dalam (for j) untuk membandingkan elemen bersebelahan.
8. Mengecek apakah elemen kiri lebih besar dari elemen kanan.
9. Memanggil fungsi tukar() untuk menukar posisi jika kondisi terpenuhi.
10. 
11. 
12. Mendefinisikan fungsi utama main().
13. Memulai blok try untuk menangani error input.
14. Mengambil input jumlah mahasiswa dari pengguna.
15. Menangkap error jika input tidak valid.
16. Menampilkan pesan kesalahan input.
17. Menghentikan program jika terjadi error.
18. 
19. Membuat list kosong nilai untuk menyimpan data.
20. 
21. Menampilkan pesan untuk memasukkan nilai mahasiswa.
22. Membuat perulangan untuk input data sesuai jumlah mahasiswa.
23. Membuat loop while True untuk validasi input.
24. Memulai blok try untuk input nilai.
25. Mengambil input nilai dan mengubahnya menjadi integer.
26. Menambahkan nilai ke dalam list nilai.
27. Menghentikan loop jika input valid.
28. Menangkap error jika input bukan angka.
29. Menampilkan pesan bahwa input harus berupa angka.
30. 
31. Menampilkan teks sebelum data ditampilkan.
32. Menampilkan isi list sebelum diurutkan.
33. 
34. #Proses Sorting
35. Memanggil fungsi bubble_sort() untuk mengurutkan data.
36. 
37. Menampilkan teks hasil setelah diurutkan.
38. Membuat perulangan untuk menampilkan setiap nilai.
39. Menampilkan nilai tanpa pindah baris.
40. Membuat baris baru setelah output selesai.
41.
42.
43. Mengecek apakah program dijalankan langsung.
44. Memanggil fungsi main() untuk menjalankan program.

Output 1; User memasukkan jumlah data dan nilai
<img width="328" height="173" alt="image" src="https://github.com/user-attachments/assets/3ba1bd0d-4358-48da-b16a-12d14177e477" />

Output 2; Menampilkan nilai sebelum dan sesudah ascending
<img width="421" height="137" alt="image" src="https://github.com/user-attachments/assets/e6cba722-efb7-49f4-ab7b-91765cb901b0" />

Link youtube: 
