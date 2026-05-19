Tugas Akhir Judul 4

Judul Program: Anomali Journey

Anomali Journey adalah game dengan sistem perjalanan antar dimensi yang memungkinkan pemain berpindah ke berbagai dunia misterius melalui portal. Setiap portal yang dimasuki akan tercatat dalam riwayat perjalanan sehingga pemain dapat kembali ke portal sebelumnya menggunakan konsep struktur data Stack dengan prinsip LIFO (Last In First Out).

source code:

<img width="1294" height="3446" alt="codesnap Tugas_Akhir_Judul4" src="https://github.com/user-attachments/assets/1762be64-f151-4138-818c-20982d8dc119" />




Penjelasan:
1. Membuat class StackPortal sebagai struktur utama program stack.
2. Membuat constructor __init__ untuk menjalankan atribut awal class.
3. Menentukan kapasitas maksimum stack sebesar 100.
4. Membuat array/list portal dengan isi awal None.
5. Mengatur top_idx bernilai -1 sebagai tanda stack masih kosong.
6. 
7. Membuat function is_empty() untuk mengecek apakah stack kosong.
8. Mengembalikan nilai True jika top_idx bernilai -1.
9. 
10. Membuat function is_full() untuk mengecek apakah stack penuh.
11. Mengembalikan nilai True jika top_idx sudah mencapai batas maksimum array.
12. 
13. Membuat function masuk_portal() untuk menambahkan portal ke stack.
14. Mengecek apakah stack penuh.
15. Menampilkan pesan bahwa riwayat portal penuh.
16. Menghentikan function jika stack penuh.
17. Menambahkan posisi top_idx sebanyak satu langkah.
18. Menyimpan nama portal ke posisi paling atas stack.
19. Menampilkan pesan bahwa portal berhasil dimasuki.
20. 
21. Membuat function kembali_portal() untuk menghapus portal terakhir.
22. Mengecek apakah stack kosong.
23. Menampilkan pesan bahwa tidak ada portal untuk kembali.
24. Menghentikan function jika stack kosong.
25. Menampilkan portal terakhir yang keluar dari stack.
26. Mengurangi posisi top_idx satu langkah.
27. 
28. Membuat function lihat_portal_terakhir() untuk melihat portal paling atas.
29. Mengecek apakah stack kosong.
30. Menampilkan pesan bahwa belum ada portal yang dimasuki.
31. Menghentikan function jika stack kosong.
32. Menampilkan portal terakhir pada stack.
33. 
34. Membuat function tampilkan_riwayat() untuk menampilkan seluruh isi stack.
35. Mengecek apakah stack kosong.
36. Menampilkan pesan bahwa riwayat portal kosong.
37. Menghentikan function jika stack kosong.
38. Menampilkan judul riwayat portal.
39. Melakukan perulangan dari portal terakhir hingga portal pertama.
40. Menampilkan setiap nama portal pada stack.
41. Menampilkan total portal yang tersimpan.
42. 
43. 
44. Membuat function main() sebagai program utama.
45. Membuat objek game dari class StackPortal.
46. Membuat variabel pilih dengan nilai awal 0.
47. 
48. Membuat perulangan selama pilihan tidak sama dengan 5.
49. Menampilkan judul menu program.
50. Menampilkan menu masuk portal.
51. Menampilkan menu kembali dari portal.
52. Menampilkan menu melihat portal terakhir.
53. Menampilkan menu menampilkan riwayat portal.
54. Menampilkan menu keluar program.
55. 
56. Membuat blok try untuk menangani error input.
57. Meminta pengguna memilih menu dan mengubah input menjadi integer.
58. Menangani error jika input bukan angka.
59. Menampilkan pesan error input.
60. Melanjutkan perulangan menu.
61. 
62. Mengecek apakah pengguna memilih menu 1.
63. Meminta pengguna memasukkan nama portal.
64. Menjalankan function masuk_portal().
65. 
66. Mengecek apakah pengguna memilih menu 2.
67. Menjalankan function kembali_portal().
68. 
69. Mengecek apakah pengguna memilih menu 3.
70. Menjalankan function lihat_portal_terakhir().
71. 
72. Mengecek apakah pengguna memilih menu 4.
73. Menjalankan function tampilkan_riwayat().
74. 
75. Mengecek apakah pengguna memilih menu 5.
76. Menampilkan pesan bahwa program selesai.
77. 
78. Kondisi selain pilihan menu yang tersedia.
79. Menampilkan pesan bahwa pilihan tidak valid.
80. 
81. 
82. Mengecek apakah file dijalankan langsung sebagai program utama.
83. Menjalankan function main().


Output Masuk Portal (push):

<img width="479" height="509" alt="image" src="https://github.com/user-attachments/assets/fcde00bf-4086-4c25-96d7-5a16a1df76ab" />

Output Kembali dari Portal (pop):

<img width="469" height="235" alt="image" src="https://github.com/user-attachments/assets/377327fe-3fa5-4f32-aeba-028547845f65" />

Output Lihat Portal Terakhir (peek):

<img width="445" height="232" alt="image" src="https://github.com/user-attachments/assets/a5247ef3-1d3e-4dac-a550-64a3676fe0ce" />

Output Tampilkan Riwayat Portal:

<img width="433" height="327" alt="image" src="https://github.com/user-attachments/assets/0a93ba21-e5eb-4404-8abc-3aa0b2bf60c7" />

Output Program Selesai:

<img width="430" height="233" alt="image" src="https://github.com/user-attachments/assets/dea61364-d218-4fc1-9550-87ecb294245d" />

Link Youtube: https://youtu.be/zxJUWV8RTwc
