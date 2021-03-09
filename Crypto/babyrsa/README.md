## Judul Soal
babyrsa

## Deskripsi Soal

> 

---
## Proof of Concept

- Diberikan dua buah berkas, yaitu `pub.key` dan `flag.enc`.
- Dari `public key` kita peroleh informasi mengenai nilai modulus `n` dan exponent `e`
- Hasilnya diketahui bahwa nilai modulus merupakan hasil kuadrat dari suatu bilangan prima `p`.
- Karena nilai `e` cukup besar, kita dapat menghitung nilai `totient` sebagaimana berikut ini:

    ```
    totient = p * (p - 1)
    ```
- Terakhir hitung private exponent `d` dan gunakan hasilnya untuk mendekripsi ciphertext `flag.enc`.


## Flag

LKS2021{ez_square_number_modulus}