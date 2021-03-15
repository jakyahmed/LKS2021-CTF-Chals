## Judul Soal
Rivest Shamir Adleman

## Deskripsi Soal

> https://en.wikipedia.org/wiki/RSA_(cryptosystem)

---
## Proof of Concept
- Cari faktor `p` & `q` yang ternyata merupakan pasangan bilangan prima
- Karena nilai `e` cukup besar, kita dapat menghitung nilai `euler totient` sebagaimana berikut ini:

    ```
    φ(pq) = (p - 1) * (q - 1)
    ```
- Terakhir hitung private exponent `d` dan gunakan hasilnya untuk mendekripsi ciphertext `flag.enc`.


## Flag

LKS2021{rsa_for_fun}