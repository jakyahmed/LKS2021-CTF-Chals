## Judul Soal
crack_me

## Deskripsi Soal

> Crack me if you can

---
## Proof of Concept

- Diberikan sebuah `executable binary` crack_me yang menerima `user input` berupa kata sandi.
- Analisis lebih lanjut pada kode hasil dekompilasi menunjukkan bahwa terdapat fungsi `validate_code()` yang mendeklarasikan beberapa `constraints` dari setiap `char` yang dimasukkan.
- Untuk mempermudah proses pengerjaan, cukup masukkan list `constraint` yang ada menggunakan `python-z3`.


## Flag

LKS2021{simpl3_p4sscrack_us1ng_z3}