## Judul Soal
xor

## Deskripsi Soal

---
## Proof of Concept
- Diberikan 2 buah berkas, yaitu binary `chall` dan `flag.enc`
- Analisis menggunakan `IDA PRO` menunjukkan bahwa program menerima `stdin` berupa filename, kemudian melakukan `single-byte xor` untuk setiap karakter yang ada dalam file 
- Mengingat constraint variable `key` berada pada range `1 .. 255`, cukup lakukan bruteforce key dari bilangan 1-255. Kemudian lakukan `single-byte xor` pada `flag.enc`

## Flag

LKS2021{0ne_byt3_x0r}