import tkinter as tk                    # Mengimpor modul Tkinter dan memberikan alias 'tk' agar lebih mudah digunakan
import sqlite3                          # Mengimpor modul SQLite3 untuk berinteraksi dengan database SQLite.

# Fungsi untuk membuat tabel jika tabel belum ada
def create_table():             
    connection = sqlite3.connect('Tugastkinter.db')                  # Membuka atau membuat database SQLite
    cursor = connection.cursor()                                    
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (                   
                    id INTEGER PRIMARY KEY,
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER,         
                    inggris INTEGER,
                    prediksi_fakultas TEXT
                    )''')
    connection.commit()                                               # Melakukan commit dan menutup koneksi          
    connection.close()

# Fungsi untuk memasukkan data ke dalam database
def insert_data():
    nama_siswa = entry_nama.get()
    nilai_biologi = int(entry_biologi.get())
    nilai_fisika = int(entry_fisika.get())
    nilai_inggris = int(entry_inggris.get())

    # Mencari nilai tertinggi dan menentukan hasil prediksi fakultas
    max_nilai = max(nilai_biologi, nilai_fisika, nilai_inggris)
    prediksi = ""
    if max_nilai == nilai_biologi:
        prediksi = "Kedokteran"
    elif max_nilai == nilai_fisika:
        prediksi = "Teknik"
    elif max_nilai == nilai_inggris:
        prediksi = "Bahasa"
    hasil.config(text=f"Hasil Prediksi: {prediksi}")

    connection = sqlite3.connect('Tugastkinter.db')                  # Membuka atau membuat database SQLite    
    cursor = connection.cursor()                                                                                                    
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)     
                   VALUES (?, ?, ?, ?, ?)''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi)) # Memasukkan data mata pelajaran kedalam tabel
    connection.commit()                                  # Melakukan commit dan menutup koneksi
    connection.close()

# Fungsi untuk menyimpan data setelah tombol 'Simpan' ditekan
def simpan_data():
    insert_data()
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Membuat tabel jika belum ada
create_table()


# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

button_simpan = tk.Button(root, text="Simpan", command=simpan_data)
button_simpan.pack()


hasil = tk.Label(root, text="Hasil Prediksi:")          # Pada Hasil Prediksi ini akan menampilkan dia masuk dalam kategori fakultas apa, ketika sudah menginpukan nilai siswa.
hasil.pack()


root.mainloop()                                     # Memulai loop utama Tkinter --> untuk menampilkan dan memperbarui jendela secara terus menerus hingga jendela ditutup.