Tugas Akhir Judul 5

Judul Program: Titan Classification

Titan Classification adalah program yang digunakan untuk menyimpan dan mengelola data Titan berdasarkan kode kekuatannya menggunakan struktur data Binary Search Tree (BST). Program ini dapat menambahkan, mencari, dan menampilkan data Titan secara terurut sehingga pengelolaan data menjadi lebih cepat dan terstruktur.

Souce code:

<img width="1556" height="6220" alt="codesnap Tugas_Akhir_Judul5" src="https://github.com/user-attachments/assets/2cbc0bef-1025-45cb-87c9-bd52e7be990a" />

penjelasan:
1. Membuat class Node untuk menyimpan data node pada Binary Search Tree.
2. Membuat constructor __init__ pada class Node.
3. Menyimpan nilai node ke variabel key.
4. Membuat child kiri dengan nilai awal None.
5. Membuat child kanan dengan nilai awal None.
6. Baris kosong.
7. Baris kosong.
8. Membuat class BSTDasar sebagai class utama BST.
9. Membuat constructor __init__ pada class BSTDasar.
10. Membuat root awal BST dengan nilai None.
11. Baris kosong.
12. Membuat function insert_node() untuk menambahkan node baru.
13. Mengecek apakah root kosong.
14. Membuat node baru jika root kosong.
15. Baris kosong.
16. Mengecek apakah nilai key lebih kecil dari root.
17. Memasukkan node ke subtree kiri secara rekursif.
18. Baris kosong.
19. Mengecek apakah nilai key lebih besar dari root.
20. Memasukkan node ke subtree kanan secara rekursif.
21. Baris kosong.
22. Mengembalikan root BST.
23. Baris kosong.
24. Membuat function insert().
25. Memanggil function insert_node() mulai dari root.
26. Baris kosong.
27. Membuat function search_node() untuk mencari data pada BST.
28. Mengecek apakah root kosong.
29. Mengembalikan nilai False jika data tidak ditemukan.
30. Baris kosong.
31. Mengecek apakah data root sama dengan key yang dicari.
32. Mengembalikan nilai True jika data ditemukan.
33. Baris kosong.
34. Mengecek apakah key lebih kecil dari root.
35. Mencari data pada subtree kiri secara rekursif.
36. Baris kosong.
37. Mencari data pada subtree kanan secara rekursif.
38. Baris kosong.
39. Membuat function search().
40. Memanggil function search_node() mulai dari root.
41. Baris kosong.
42. Membuat function inorder().
43. Mengecek apakah root kosong.
44. Menghentikan function jika root kosong.
45. Baris kosong.
46. Menjalankan traversal inorder pada subtree kiri.
47. Menampilkan data root.
48. Menjalankan traversal inorder pada subtree kanan.
49. Baris kosong.
50. Membuat function find_min() untuk mencari nilai terkecil.
51. Mengecek apakah root kosong.
52. Mengembalikan nilai -1 jika BST kosong.
53. Baris kosong.
54. Membuat variabel current yang menunjuk ke root.
55. Baris kosong.
56. Melakukan perulangan selama child kiri masih ada.
57. Memindahkan posisi current ke child kiri.
58. Baris kosong.
59. Mengembalikan nilai terkecil pada BST.
60. Baris kosong.
61. Membuat function find_max() untuk mencari nilai terbesar.
62. Mengecek apakah root kosong.
63. Mengembalikan nilai -1 jika BST kosong.
64. Baris kosong.
65. Membuat variabel current yang menunjuk ke root.
66. Baris kosong.
67. Melakukan perulangan selama child kanan masih ada.
68. Memindahkan posisi current ke child kanan.
69. Baris kosong.
70. Mengembalikan nilai terbesar pada BST.
71. Baris kosong.
72. Membuat function count_nodes() untuk menghitung jumlah node.
73. Mengecek apakah root kosong.
74. Mengembalikan nilai 0 jika node kosong.
75. Baris kosong.
76. Menghitung jumlah seluruh node menggunakan rekursif.
77. Baris kosong.
78. Membuat function sum_nodes() untuk menghitung total nilai node.
79. Mengecek apakah root kosong.
80. Mengembalikan nilai 0 jika node kosong.
81. Baris kosong.
82. Menjumlahkan seluruh nilai node menggunakan rekursif.
83. Baris kosong.
84. Baris kosong.
85. Membuat function main() sebagai program utama.
86. Membuat object BST bernama bst.
87. Membuat variabel pilih dengan nilai awal 0.
88. Baris kosong.
89. Membuat perulangan selama pilihan tidak sama dengan 8.
90. Menampilkan judul program.
91. Menampilkan menu tambah Titan.
92. Menampilkan menu cari Titan.
93. Menampilkan menu tampilkan Titan terurut.
94. Menampilkan menu Titan terlemah.
95. Menampilkan menu Titan terkuat.
96. Menampilkan menu jumlah Titan.
97. Menampilkan menu total kekuatan Titan.
98. Menampilkan menu keluar.
99. Baris kosong.
100. Membuat blok try.
101. Meminta user memilih menu dan mengubah input menjadi integer.
102. Baris kosong.
103. Menangani error jika input bukan angka menggunakan except ValueError.
104. Menampilkan pesan input tidak valid.
105. Melanjutkan perulangan program menggunakan continue.
106. Baris kosong.
107. Mengecek apakah user memilih menu 1.
108. Membuat blok try untuk input Titan.
109. Meminta user memasukkan kode kekuatan Titan.
110. Menjalankan function insert() untuk menambahkan Titan.
111. Baris kosong
112. Menampilkan pesan bahwa Titan berhasil ditambahkan.
113. Baris kosong.
114. Menangani error jika input bukan angka.
115. Menampilkan pesan input tidak valid.
116. Baris kosong.
117. Mengecek apakah user memilih menu 2.
118. Membuat blok try.
119. Meminta user memasukkan kode Titan yang dicari.
120. Mengecek apakah Titan ditemukan menggunakan function search().
121. Menampilkan pesan bahwa Titan ditemukan.
122. Kondisi jika Titan tidak ditemukan.
123. Menampilkan pesan bahwa Titan tidak ditemukan.
124. Baris kosong.
125. Menangani error jika input bukan angka menggunakan except ValueError.
126. Menampilkan pesan input tidak valid.
127. Baris kosong.
128. Mengecek apakah user memilih menu 3.
129. Menampilkan judul data Titan terurut.
130. Menjalankan traversal inorder.
131. Membuat baris baru.
132. Baris kosong.
133. Mengecek apakah user memilih menu 4.
134. Menampilkan Titan dengan nilai terkecil.
135. Baris kosong.
136. Mengecek apakah user memilih menu 5.
137. Menampilkan Titan dengan nilai terbesar.
138. Baris kosong.
139. Mengecek apakah user memilih menu 6.
140. Menampilkan jumlah seluruh Titan.
141. Baris kosong.
142. Mengecek apakah user memilih menu 7.
143. Menampilkan total kekuatan seluruh Titan.
144. Baris kosong.
145. Mengecek apakah user memilih menu 8.
146. Menampilkan pesan program selesai.
147. Baris kosong.
148. Kondisi jika pilihan menu tidak tersedia.
149. Menampilkan pesan pilihan tidak valid.
150. Baris kosong.
151. Baris kosong.
152. Mengecek apakah file dijalankan langsung sebagai program utama.
153. Menjalankan function main().
154. Baris kosong.
156. Baris akhir program.

Output Insert (1):

<img width="605" height="681" alt="image" src="https://github.com/user-attachments/assets/a519c24e-0ea7-4752-9259-1f0225b5ef10" />

Output Search (2):

<img width="496" height="339" alt="image" src="https://github.com/user-attachments/assets/7e32d66b-045f-411c-9b44-a616861b0f4a" />

Output Inorder (3):

<img width="630" height="314" alt="image" src="https://github.com/user-attachments/assets/f88e8e29-d6b4-4cad-9cc5-e53a0d8c921e" />

Output findmin & findmax (4):

<img width="525" height="632" alt="image" src="https://github.com/user-attachments/assets/149ce723-7005-4a1c-b2e2-436bebadda23" />

Output Count (5):

<img width="429" height="332" alt="image" src="https://github.com/user-attachments/assets/ef4a37ae-dce5-4da1-a7b2-9e9de48f7444" />

Output Sum (6):

<img width="493" height="334" alt="image" src="https://github.com/user-attachments/assets/dbd4e9dc-31ce-45cc-a761-013c35736428" />

Link Youtube: https://youtu.be/633-sw7bPEc
