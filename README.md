
Nama: Hafizh Naufal Raditya
NIM: H1D024061


---

Fitur Utama & Pemenuhan Kriteria Tugas

1. Knowledge Base Terstruktur (Dictionary)
   Sistem ini menyimpan basis pengetahuan (gejala dan solusi) menggunakan struktur data `Dictionary`, bukan menggunakan deretan `if-else` yang panjang dan kaku. Terdapat 5 jenis kerusakan yang dideteksi:
   * RAM Bermasalah
   * Power Supply (PSU) / Baterai Lemah
   * Overheat (Prosesor Terlalu Panas)
   * VGA Rusak (Artefak)
   * Hardisk / SSD Corrupt

2. Mesin Inferensi Cerdas (Set Intersection)
   Untuk menentukan hasil diagnosa, mesin inferensi membaca himpunan gejala yang dialami pengguna dan membandingkannya dengan gejala di database menggunakan metode irisan himpunan matematis (`set.intersection()`). Sistem juga menghitung **persentase kecocokan**.

3. Penanganan Kasus Tidak Dikenal (Error Handling)
   Jika pengguna memasukkan kombinasi gejala yang tidak mencapai batas minimal kecocokan (33%) atau tidak ada di database sama sekali, sistem akan menampilkan pop-up khusus yang menyatakan kerusakan tidak terdeteksi.

4. Antarmuka Interaktif (GUI)
   Dibangun menggunakan murni library bawaan `tkinter`, antarmuka didesain interaktif dengan kotak teks dinamis dan tombol pilihan (Ya/Tidak) layaknya berkonsultasi dengan teknisi sungguhan.


---

Pembahasan Kode

**1. Basis Pengetahuan (Knowledge Base) & Persiapan Data**
Sesuai dengan kriteria tugas, program tidak menggunakan deretan `if-else` untuk menyimpan aturan, melainkan menggunakan struktur data **Dictionary**.
* Variabel `knowledge_base` adalah sebuah *dictionary* bersarang yang berisi 5 jenis kerusakan utama. Setiap kerusakan memiliki *key* `"gejala"` (berisi *list* gejala) dan `"solusi"` (berisi teks solusi singkat).
* **Ekstraksi Gejala Unik:** Agar sistem tidak menanyakan gejala yang sama berulang kali, program melakukan *looping* untuk mengambil semua gejala dari setiap kerusakan dan memasukkannya ke dalam sebuah `set()`. Tipe data `set` secara otomatis membuang duplikasi. Kumpulan gejala unik ini kemudian diubah kembali menjadi `list` pada variabel `daftar_gejala` untuk ditanyakan secara berurutan.

**2. Alur Interaksi dan Pengumpulan Fakta (Tanya Jawab)**
Program menggunakan tiga fungsi utama untuk menangani interaksi pengguna:
* `mulai_diagnosa()`: Berfungsi untuk mereset *array* `gejala_user` menjadi kosong dan mengembalikan indeks pertanyaan ke angka 0.
* `tampilkan_pertanyaan()`: Berfungsi mengambil teks gejala dari `daftar_gejala` berdasarkan urutan `current_index`, lalu menampilkannya ke layar GUI.
* `jawab(jawaban_ya)`: Fungsi ini dieksekusi ketika pengguna menekan tombol "Ya" atau "Tidak". Jika pengguna menekan "Ya" (`True`), gejala tersebut akan direkam (di-*append*) ke dalam *array* `gejala_user` (sebagai fakta baru). Indeks kemudian ditambah 1 untuk memanggil pertanyaan selanjutnya.

**3. Mesin Inferensi (Penarikan Kesimpulan)**
Ini adalah inti kecerdasan dari program, yang terletak di dalam fungsi `proses_diagnosa()`. Alih-alih mencocokkan gejala dengan logika kondisi berantai, sistem menggunakan operasi **Irisan Himpunan (Set Intersection)** matematis:
* Program akan melakukan *looping* untuk setiap kerusakan di `knowledge_base`.
* Sistem membandingkan himpunan gejala yang dimiliki kerusakan di database (`gejala_database`) dengan himpunan gejala yang dijawab "Ya" oleh pengguna (`gejala_user`).
* Perintah `gejala_database.intersection(set(gejala_user))` akan menghasilkan daftar gejala yang **cocok (beririsan)**.
* **Pembobotan/Persentase:** Sistem menghitung persentase kecocokan dengan membagi jumlah gejala yang cocok dengan total gejala pada kerusakan tersebut. Jika kecocokan $\ge 33\%$, maka penyakit tersebut dimasukkan ke dalam daftar kemungkinan.
* Daftar kemungkinan tersebut kemudian diurutkan (*sorting*) secara menurun (dari persentase tertinggi ke terendah).

**4. Output dan Penanganan Error (GUI & Messagebox)**
* Hasil akhir dengan nilai kecocokan tertinggi akan ditampilkan menggunakan *pop-up* peringatan standar Windows/Sistem Operasi melalui fungsi `messagebox.showinfo()`. Teks yang ditampilkan memuat Nama Kerusakan, Persentase, dan Solusinya.
* **Penanganan Kasus Kosong:** Sesuai kriteria tugas, jika variabel daftar kemungkinan penyakit kosong (tidak ada gejala yang beririsan atau persentase di bawah 33%), blok `if not kemungkinan_penyakit:` akan dieksekusi, lalu menampilkan pesan bahwa "Tidak terdeteksi kerusakan yang cocok".



