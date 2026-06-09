Tugas Akhir Judul 6

Judul Program: Leaderboard Arena PVP Legendaris
Dalam game Arena PvP Legendaris, data pemain disimpan menggunakan Hash Map dengan Player ID (int) sebagai key dan jumlah kemenangan sebagai value. Jika terjadi collision, data ditempatkan ke slot berikutnya menggunakan linear probing, sehingga pencarian dan update data tetap cepat dan efisien.

Source Code:

<img width="1308" height="5916" alt="codesnap Tugas_Akhir_Judul6" src="https://github.com/user-attachments/assets/916e8aa3-03e3-49f9-8fc9-1747e0543120" />

penjelasan:
1. mendefinisikan class SlotState
2. mendefinisikan status EMPTY = 0
3. mendefinisikan status OCCUPIED = 1
4. mendefinisikan status DELETED = 2
5. 
6. 
7. mendefinisikan class Entry
8. mendefinisikan constructor __init__
9. membuat self.key = None
10. membuat self.value = None
11. mengatur state awal menjadi SlotState.EMPTY
12. 
13. 
14. mendefinisikan class HashMapOpenAddressing
15. mendefinisikan constructor dengan parameter size=10
16. menyimpan ukuran hash map ke self.SIZE
17. membuat tabel hash berisi object Entry() sebanyak ukuran SIZE
18. 
19. mendefinisikan fungsi hash_function
20. menghitung hash key menggunakan modulus %
21. 
22. mendefinisikan fungsi insert
23. mencari index menggunakan hash function
24. membuat variabel first_deleted = -1
25. 
26. melakukan perulangan sebanyak ukuran hash map
27. menghitung index linear probing (idx + step) % self.SIZE
28. 
29. mengecek apakah slot sedang OCCUPIED
30. mengecek apakah key sama
31. mengubah value jika key ditemukan
32. mengembalikan True
33. 
34. mengecek apakah slot berstatus DELETED
35. mengecek apakah first_deleted masih kosong
36. menyimpan index deleted pertama
37. 
38. menangani slot kosong (EMPTY)
39. mengecek apakah ada slot deleted sebelumnya
40. menggunakan slot deleted pertama
41. 
42. menyimpan key ke tabel
43. menyimpan value ke tabel
44. mengubah state menjadi OCCUPIED
45. mengembalikan True
46. 
47. mengecek apakah ada slot deleted tersimpan
48. menyimpan key pada slot deleted
49. menyimpan value pada slot deleted
50. mengubah state menjadi OCCUPIED
51. mengembalikan True
52. 
53. mengembalikan False jika gagal insert
54. 
55. mendefinisikan fungsi search
56. mencari index menggunakan hash function
57. 
58. melakukan perulangan sebanyak ukuran hash map
59. menghitung index probing
60. 
61. mengecek apakah slot kosong EMPTY
62. mengembalikan None jika data tidak ditemukan
63. 
64. mengecek kondisi pencarian
65. mengecek apakah slot OCCUPIED
66. mengecek apakah key sesuai
67. penutup kondisi if
68. mengembalikan data tabel jika ditemukan
69. 
70. mengembalikan None jika tidak ditemukan
71. 
72. mendefinisikan fungsi remove_key
73. mencari entry berdasarkan key
74. 
75. mengecek apakah entry tidak ditemukan
76. mengembalikan False
77. 
78. mengubah state menjadi DELETED
79. mengembalikan True
80. 
81. mendefinisikan fungsi display
82. menampilkan judul leaderboard
83. 
84. melakukan perulangan seluruh isi tabel
85. menampilkan index tabel
86. 
87. mengecek apakah slot kosong EMPTY
88. menampilkan tulisan "EMPTY"
89. 
90. mengecek apakah slot DELETED
91. menampilkan tulisan "DELETED"
92. 
93. kondisi selain itu (OCCUPIED)
94. menampilkan data player
95. menampilkan Player ID dan key
96. menampilkan jumlah kemenangan/value
97. penutup print
98. 
99.
100. mendefinisikan fungsi main
101. membuat object leaderboard dari class HashMapOpenAddressing
102. 
103. menambahkan data (1001, 25)
104. menambahkan data (1011, 17)
105. menambahkan data (1021, 33)
106. menambahkan data (1002, 12)
107. 
108. menampilkan pesan data berhasil ditambahkan
109. menampilkan isi leaderboard
110. 
111. mencari data dengan key 1011
112. 
113. mengecek apakah hasil ditemukan
114. menampilkan data player ditemukan
115. menampilkan Player ID
116. menampilkan jumlah kemenangan
117. penutup print
118. kondisi jika data tidak ditemukan
119. menampilkan pesan player tidak ditemukan
120. 
121. mencari data dengan key 1021
122. 
123. mengecek apakah hasil ditemukan
124. menampilkan data player ditemukan
125. menampilkan Player ID
126. menampilkan jumlah kemenangan
127. penutup print
128. 
129. menampilkan isi leaderboard
130. 
131. menghapus data dengan key 1011
132. 
133. menampilkan pesan setelah penghapusan
134. menampilkan isi leaderboard
135. 
136. mencari kembali data dengan key 1021
137. 
138. mengecek apakah hasil ditemukan
139. menampilkan pesan player masih ditemukan
140. menampilkan Player ID
141. menampilkan jumlah kemenangan
142. penutup print
143. kondisi jika data tidak ditemukan
144. menampilkan pesan player tidak ditemukan
145. 
146. 
147. mengecek apakah file dijalankan langsung
148. menjalankan fungsi main()

Output:

<img width="473" height="759" alt="image" src="https://github.com/user-attachments/assets/41be16f8-a6e6-49f3-89e1-15967c3b5850" />


Link Youtube: https://youtu.be/dBnyA8lofXc
