Tugas Akhir Judul 1

Judul Program: Playlist Lagu

Program yang akan dibuat adalah sebuah sistem sederhana untuk mengelola playlist lagu menggunakan Python. Di dalam program ini, setiap lagu akan disimpan sebagai bagian dari sebuah rangkaian data yang saling terhubung (Singly Linked List), sehingga playlist bisa bertambah atau berkurang dengan mudah. Pengguna nantinya bisa menambahkan lagu baru, menghapus lagu tertentu, dan melihat daftar lagu yang ada secara berurutan. Konsep ini mirip seperti playlist musik pada umumnya, di mana lagu diputar satu per satu sesuai urutan. Dengan cara ini, pengelolaan data menjadi lebih fleksibel dibandingkan menggunakan metode biasa seperti array, karena tidak perlu menggeser data saat ada perubahan.

souce code:
<img width="1372" height="3826" alt="codesnap Tugas_Akhir_Judul1" src="https://github.com/user-attachments/assets/0a5f6cad-cd92-45c6-94bf-eac7916bc55e" />
1. Mendefinisikan fungsi menu() untuk menampilkan daftar pilihan.
2. Mencetak judul "PLAYLIST LAGU" dengan baris baru di awal.
3. Mencetak opsi menu untuk menambah lagu. 
4. Mencetak opsi menu untuk menampilkan playlist. 
5. Mencetak opsi menu untuk menghapus lagu. 
6. Mencetak opsi menu untuk keluar dari program.
7.
8.
9. Mendefinisikan class Node sebagai struktur data untuk satu lagu.
10. Membuat constructor __init__ dengan parameter judul.
11. Menyimpan nilai judul lagu ke atribut self.judul. 
12. Menginisialisasi pointer next dengan None. 
13.
14.
15. Mendefinisikan class Playlist sebagai Linked List. 
16. Membuat constructor __init__ untuk playlist. 
17. Mengatur head sebagai None (playlist kosong). 
18.
19. Mendefinisikan method tambah_lagu(). 
20. Membuat node baru dengan judul lagu. 
21.
22. Mengecek apakah playlist kosong. 
23. Jika kosong, node baru dijadikan head. 
24. Jika tidak kosong, masuk ke blok else. 
25. Menginisialisasi pointer current ke head. 
26. Melakukan loop selama masih ada node berikutnya. 
27. Memindahkan current ke node berikutnya. 
28. Menyambungkan node terakhir dengan node baru. 
29.
30. Mendefinisikan method tampilkan(). 
31. Mengecek apakah playlist kosong. 
32. Jika kosong, menampilkan pesan "Playlist kosong". 
33. Jika tidak kosong, masuk ke blok else. 
34. Menginisialisasi current ke head. 
35. Menginisialisasi nomor urut i = 1. 
36. Loop selama masih ada node. 
37. Menampilkan nomor dan judul lagu. 
38. Pindah ke node berikutnya. 
39. Menambah nomor urut. 
40.
41. Mendefinisikan method hapus(). 
42. Menginisialisasi current ke head. 
43. Menginisialisasi prev sebagai None. 
44.
45. Mengecek apakah lagu yang dihapus ada di head. 
46. Jika iya, head digeser ke node berikutnya. 
47. Menampilkan pesan berhasil dihapus. 
48. Menghentikan fungsi dengan return. 
49.
50. Loop untuk mencari lagu yang ingin dihapus. 
51. Memindahkan prev ke posisi current. 
52. Memindahkan current ke node berikutnya. 
53.
54. Mengecek apakah lagu tidak ditemukan.
55. Menampilkan pesan "Lagu tidak ditemukan". 
56. Menghentikan fungsi. 
57.
58. Menghubungkan prev.next ke current.next (menghapus node). 
59. Menampilkan pesan lagu berhasil dihapus. 
60.
61. Mendefinisikan fungsi main(). 
62. Membuat objek playlist. 
63. Menginisialisasi variabel running = True. 
64.
65. Memulai loop selama program berjalan. 
66. Memanggil fungsi menu(). 
67. Mengambil input dari user. 
68. Menggunakan try untuk validasi input. 
69. Menangkap error jika input bukan angka. 
70. Menampilkan pesan error. 
71. Mengulang ke menu dengan continue. 
72.
73. Jika user memilih menu 1. 
74. Meminta input judul lagu. 
75. Menambahkan lagu ke playlist. 
76.
77. Jika user memilih menu 2. 
78. Menampilkan playlist. 
79.
80. Jika user memilih menu 3. 
81. Meminta judul lagu yang ingin dihapus. 
82. Menghapus lagu dari playlist. 
83.
84. Jika user memilih menu 4. 
85. Menghentikan loop (running = False). 
86. Menampilkan pesan program selesai. 
87.
88. Jika pilihan tidak valid. 
89. Menampilkan pesan error pilihan. 
90.
91.
92. Mengecek apakah file dijalankan langsung. 
93. Menjalankan fungsi main().

Output menambahkan lagu (1)
<img width="596" height="578" alt="image" src="https://github.com/user-attachments/assets/6751c277-ea8d-40d4-b90e-7fb5d17146ed" />

Output menampilkan playlist (2)
<img width="400" height="325" alt="image" src="https://github.com/user-attachments/assets/86de2073-5322-4b35-b0ee-8bc01e119331" />

Output menghapus lagu (3)
<img width="853" height="323" alt="image" src="https://github.com/user-attachments/assets/d5f68030-56c8-481a-b9a4-e53476756e0a" />

Output jika pilihan tidak valid
<img width="471" height="289" alt="image" src="https://github.com/user-attachments/assets/0640a84c-a7c8-4b62-acf3-8dbd47cf1a7c" />

Output ketika program selesai
<img width="402" height="285" alt="image" src="https://github.com/user-attachments/assets/de827dbb-cefa-4fa3-9402-d0a4e28035a0" />

Link Youtube: https://youtu.be/6xUcmRx7QMM
