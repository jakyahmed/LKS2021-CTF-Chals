## Judul Soal
tebak_angka

## Deskripsi Soal

---
## Proof of Concept

- Diberikan sebuah `executable binary` tebak_angka yang menerima sembarang input bilangan
- Diberikan pula sebuah libc binary
- Analisis lebih lanjut menggunakan IDA PRO menunjukkan bahwa digunakan `srand(time(NULL))` untuk mengatur seed dari RNG
- Berbekal libc yang diberikan, kita dapat me-reproduce flow program C menggunakan fungsi `ctypes.CDLL()` pada Python

## Flag

LKS2021{tebak_tebak_berhadiah_flag_f84de2}