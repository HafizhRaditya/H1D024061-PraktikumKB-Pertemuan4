import tkinter as tk
from tkinter import messagebox


# 1. KNOWLEDGE BASE (DATABASE KERUSAKAN)

knowledge_base = {
    "RAM Bermasalah": {
        "gejala": ["layar blank hitam", "terdengar bunyi bip berulang", "sering blue screen (bsod)"],
        "solusi": "Cabut RAM, bersihkan pin kuningannya dengan penghapus karet, lalu pasang kembali."
    },
    "Power Supply (PSU) / Baterai Lemah": {
        "gejala": ["mati total tidak ada indikator nyala", "kipas menyala sebentar lalu mati", "mati mendadak saat aplikasi berat"],
        "solusi": "Cek kabel power/charger. Coba nyalakan tanpa baterai atau tes dengan PSU lain."
    },
    "Overheat (Prosesor Terlalu Panas)": {
        "gejala": ["bodi terasa sangat panas", "suara kipas sangat bising", "mati mendadak setelah digunakan lama", "kinerja sangat lambat"],
        "solusi": "Bersihkan debu pada saluran udara dan kipas. Ganti thermal paste pada prosesor."
    },
    "VGA Rusak (Artefak)": {
        "gejala": ["layar bergaris-garis", "muncul kotak-kotak aneh di layar", "warna tampilan pudar"],
        "solusi": "Hubungkan ke monitor eksternal. Jika di monitor luar juga bergaris, chip VGA rusak."
    },
    "Hardisk / SSD Corrupt": {
        "gejala": ["muncul pesan no bootable device", "loading booting sangat lama", "sering freeze tidak merespon"],
        "solusi": "Segera backup data penting Anda. Cek kesehatan storage dengan aplikasi HDD Sentinel."
    }
}

# Ekstrak semua gejala unik menjadi sebuah list
semua_gejala = set()
for data in knowledge_base.values():
    for g in data["gejala"]:
        semua_gejala.add(g)
daftar_gejala = list(semua_gejala)

# Variabel Global untuk melacak status pertanyaan
current_index = 0
gejala_user = []


# 2. FUNGSI LOGIKA (MESIN INFERENSI)

def mulai_diagnosa():
    global current_index, gejala_user
    current_index = 0
    gejala_user = []
    
    # Atur status tombol
    btn_mulai.config(state=tk.DISABLED)
    btn_ya.config(state=tk.NORMAL)
    btn_tidak.config(state=tk.NORMAL)
    
    # Tampilkan pertanyaan pertama
    tampilkan_pertanyaan()

def tampilkan_pertanyaan():
    if current_index < len(daftar_gejala):
        gejala_sekarang = daftar_gejala[current_index]
        teks_tanya = f"Apakah Anda mengalami:\n{gejala_sekarang}?"
        
        lbl_pertanyaan.config(state=tk.NORMAL)
        lbl_pertanyaan.delete(1.0, tk.END)
        lbl_pertanyaan.insert(tk.END, teks_tanya)
        lbl_pertanyaan.config(state=tk.DISABLED)
    else:
        # Jika semua pertanyaan sudah habis ditanyakan
        proses_diagnosa()

def jawab(jawaban_ya):
    global current_index
    if jawaban_ya:
        gejala_user.append(daftar_gejala[current_index])
        
    current_index += 1
    tampilkan_pertanyaan()

def proses_diagnosa():
    kemungkinan_penyakit = []

    for kerusakan, data in knowledge_base.items():
        gejala_database = set(data["gejala"])
        gejala_cocok = gejala_database.intersection(set(gejala_user))

        if len(gejala_cocok) > 0:
            persentase = (len(gejala_cocok) / len(gejala_database)) * 100
            if persentase >= 33: # Minimal kecocokan
                kemungkinan_penyakit.append({
                    "nama": kerusakan,
                    "solusi": data["solusi"],
                    "persentase": persentase
                })

    # Urutkan berdasarkan persentase tertinggi
    kemungkinan_penyakit = sorted(kemungkinan_penyakit, key=lambda x: x["persentase"], reverse=True)

    # Tampilkan Hasil di Message Box
    if not kemungkinan_penyakit:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi kerusakan yang cocok dengan gejala tersebut.\n\nSaran: Bawa perangkat ke teknisi terdekat.")
    else:
        hasil_tertinggi = kemungkinan_penyakit[0]
        pesan = f"Diagnosa: {hasil_tertinggi['nama']}\n"
        pesan += f"Kecocokan: {hasil_tertinggi['persentase']:.0f}%\n\n"
        pesan += f"Solusi: {hasil_tertinggi['solusi']}"
        messagebox.showinfo("Hasil Diagnosa", pesan)
        
    # Reset UI
    lbl_pertanyaan.config(state=tk.NORMAL)
    lbl_pertanyaan.delete(1.0, tk.END)
    lbl_pertanyaan.insert(tk.END, "Silakan klik 'Mulai Diagnosa' untuk mengulang.")
    lbl_pertanyaan.config(state=tk.DISABLED)
    
    btn_mulai.config(state=tk.NORMAL)
    btn_ya.config(state=tk.DISABLED)
    btn_tidak.config(state=tk.DISABLED)


# 3. MEMBANGUN UI TKINTER (SESUAI CONTOH MODUL)

root = tk.Tk()
root.title("Sistem Pakar Kerusakan Komputer")
root.geometry("400x350")
root.configure(padx=20, pady=20)

# Judul
lbl_judul = tk.Label(root, text="Aplikasi Diagnosa Kerusakan PC", font=("Arial", 14, "bold"))
lbl_judul.pack(pady=10)

lbl_sub = tk.Label(root, text="Kolom Pertanyaan:")
lbl_sub.pack(anchor="w")

# Kotak Teks Pertanyaan (Read Only)
lbl_pertanyaan = tk.Text(root, height=4, width=40, font=("Arial", 11), bg="#f0f0f0", wrap=tk.WORD)
lbl_pertanyaan.pack(pady=10)
lbl_pertanyaan.insert(tk.END, "Klik tombol di bawah untuk memulai.")
lbl_pertanyaan.config(state=tk.DISABLED)

# Frame untuk Tombol Ya/Tidak
frame_tombol = tk.Frame(root)
frame_tombol.pack(pady=10)

btn_tidak = tk.Button(frame_tombol, text="Tidak", width=10, command=lambda: jawab(False), state=tk.DISABLED)
btn_tidak.grid(row=0, column=0, padx=10)

btn_ya = tk.Button(frame_tombol, text="Ya", width=10, command=lambda: jawab(True), state=tk.DISABLED)
btn_ya.grid(row=0, column=1, padx=10)

# Tombol Mulai
btn_mulai = tk.Button(root, text="Mulai Diagnosa", width=20, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=mulai_diagnosa)
btn_mulai.pack(pady=20)

root.mainloop()