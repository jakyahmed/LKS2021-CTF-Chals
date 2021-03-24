## Judul Soal
Waifu Terbaik

## Deskripsi Soal
Dipilih aja gan. <br>

---

## Penjelasan Penyelesaian Soal
- Blind SQLite injection
- Karena spasi difilter, kita bisa gunakan `/**/` sebagai pengganti spasi
- Karena saat melakukan SQLi tidak ada hasilnya, kita bisa melakukan teknik blind boolean based
- Kita akan menggunakan query CASE, jika hasilnya salah maka hasil vote nya 0, jika benar maka lbh dari 1
- Pertama kita harus dump nama table
- Lalu setelah dapat table, kita dump kolomnya
- Setelah menemukan kolom, kita dump data flagnya

## FLAG
LKS2021{waifumu_integral_satu_per_t_dt_mas}