## Judul Soal
buffow

## Deskripsi Soal

---
## Proof of Concept
- Diberikan executable binary `buf` yang menerima input berupa `secret number`
- Analisis pada binary menunjukkan bahwa digunakan fungsi `gets()` untuk menerima `stdin`
- Selain itu kita ketahui pula bahwa binary tidak memiliki proteksi `canary` sehingga kita memiliki kontrol untuk mengubah isi dari `stack`
    ```sh
    ❯ checksec buf
        Arch:     amd64-64-little
        RELRO:    Full RELRO
        Stack:    No canary found
        NX:       NX enabled
        PIE:      PIE enabled
    ```
- Eksploitasi dapat dilakukan dengan memasukkan sembarang karakter dengan size `25 + 4` byte, dengan tujuan untuk mengubah isi dari variable `hack_me`


## Flag

LKS2021{buffer_0verflow_ftw}