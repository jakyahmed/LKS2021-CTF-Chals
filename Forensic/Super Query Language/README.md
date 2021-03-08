## Judul Soal
Super Query Language

## Deskripsi Soal

> Our API service was attacked last night. Fortunately, we managed to log those activity
---

## Hint
- The attackers were likely trying to reveal `secret` table using `Blind SQLi` technique

---
## Proof of Concept

- Diberikan `access.tar.gz` yang kemudian didekompresi menggunakan `tar -xzf access.tar.gz` sehingga diperoleh `access.log`
- Analisis pada `access.log` menunjukkan bahwa terdapat upaya `SQL injection` pada DB Engine `SQLITE` dengan tujuan melakukan leak pada tabel `secret`.
- Dari jenis payload yang digunakan, `attacker` menggunakan fungsi `randomblob(2000000)` untuk memberikan delay selama `2 detik` untuk setiap query yang bernilai `True`
- Berdasarkan analisis di atas, skema penyelesaian soal dapat dilakukan dengan mencari `time_delta` atau selisih waktu request yang lebih dari `2 detik`. Kemudian dilanjutkan dengan memetakan `indeks` dan `char` yang diperoleh

## Flag

LKS2021{you_can_always_read_sqli_logs_even_with_time_response}