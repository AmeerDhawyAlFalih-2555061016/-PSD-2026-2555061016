Tugas Akhir Judul 3

Judul Program: Pencarian Level Player dalam Game

Program ini digunakan untuk mencari level player dalam sebuah game. Pengguna memasukkan level yang ingin dicari, lalu program akan memeriksa data satu per satu menggunakan metode Sequential Search dan menampilkan berapa kali level tersebut ditemukan, serta mendeskripsikan kategori level player.

Source Code:
<img width="1648" height="2724" alt="codesnap Tugas_Akhir_Judul3" src="https://github.com/user-attachments/assets/c7a98eaa-1a90-45c2-9ad2-46448e7e3d08" />

Penjelasan:
1. Mendefinisikan fungsi sequential search untuk mencari jumlah data yang sesuai dengan target.
2. Membuat variabel indeks awal dimulai dari 0.
3. Membuat variabel penghitung jumlah data yang ditemukan.
4. 
5. Melakukan perulangan selama indeks masih kurang dari jumlah data.
6. Mengecek apakah data pada indeks saat ini sama dengan target.
7. Jika data sama dengan target, maka counter ditambah 1.
8. Indeks berpindah ke data berikutnya.
9. 
10. Mengembalikan nilai counter.
11. 
12. 
13. Mendefinisikan fungsi main().
14. Membuat list data level player.
15. Menghitung jumlah data menggunakan len().
16. 
17. Menampilkan data level player.
18. 
19. 
20. Membuat perulangan menu utama agar program terus berjalan.
21. Menampilkan teks pilihan menu.
22. Menampilkan opsi mencari level.
23. Menampilkan opsi keluar program.
24. 
25. Meminta pengguna memasukkan pilihan menu.
26. 
27. Mengecek apakah pengguna memilih opsi 1.
28. Membuat perulangan untuk validasi input level.
29. Mencoba menjalankan kode yang berpotensi error.
30. Meminta pengguna memasukkan level yang ingin dicari lalu mengubahnya menjadi integer.
31. Menghentikan perulangan jika input valid.
32. Menangani error jika input bukan angka.
33. Menampilkan pesan agar memasukkan angka.
34. 
35. 
36. Memanggil fungsi sequential search untuk mencari target pada data.
37. 
38. Mengecek apakah target ditemukan.
39. Menampilkan jumlah level yang ditemukan.
40. 
41. Mengecek apakah level termasuk kategori Beginner.
42. Menampilkan kategori Beginner.
43. 
44. Mengecek apakah level termasuk kategori Veteran.
45. Menampilkan kategori Veteran.
46. 
47. Mengecek apakah level termasuk kategori Elite.
48. Menampilkan kategori Elite.
49. 
50. Menjalankan kondisi selain kategori sebelumnya.
51. Menampilkan kategori Legend.
52. Menjalankan kondisi jika target tidak ditemukan.
53. Menampilkan pesan bahwa level tidak ditemukan.
54. 
55. Mengecek apakah pengguna memilih opsi 2.
56. Menampilkan pesan penutup program.
57. Menghentikan program menggunakan break.
58. 
59. Menjalankan kondisi jika pilihan menu tidak valid.
60. Menampilkan pesan bahwa pilihan tidak valid.
61. 
62. 
63. Mengecek apakah file dijalankan langsung sebagai program utama.
64. Memanggil fungsi main().


Output 1: Jika input pengguna tidak ada dalam opsi menu

<img width="359" height="148" alt="image" src="https://github.com/user-attachments/assets/456bf4a7-8fd0-4ad1-b034-874f32302c2b" />


Output 2: Ketika level yang diinput tidak ada pada list

<img width="445" height="178" alt="image" src="https://github.com/user-attachments/assets/0f12a48e-e9e7-40dd-988d-2d8a3975d896" />


Output 3: Ketika level yang diinput ada pada list serta deskripsi setiap kategori

<img width="678" height="837" alt="image" src="https://github.com/user-attachments/assets/b691d249-be87-445a-9ab5-c1b170000c9f" />


Output 4: Opsi keluar pada menu

<img width="568" height="146" alt="image" src="https://github.com/user-attachments/assets/30744154-0c8a-451b-a0b2-25fc3761c29f" />



Link Youtube: https://youtu.be/EiUI21oc5oc
