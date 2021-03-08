## Judul Soal
Wangy Wangy Generator

## Deskripsi Soal
Wangy wangy wangy wangy wangy <br>

---

## Penjelasan Penyelesaian Soal
- Terdapat vuln pada parse_str dan eval
- Pertama bypass filter dengan melakukan overwrite menggunakan parse_str
- Setelah itu kita bisa lakukan rce, namun karena string dibatasi, kita perlu memasukan payload menggunakan variabel baru dengan melakukan chaining
- Kita bisa membuat variabel baru menggunakan parse_str, sehingga payload akan kita masukan di query string
- Hasil payload:
  ```
  http://localhost:3000/?name='.`$a`;'&filter=%2F.%2A%2F&a=id
  ```