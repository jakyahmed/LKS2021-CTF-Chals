## Judul Soal
Old Fragile Box

## Deskripsi Soal

> nc ip_server 20001

---
## Proof of Concept

- Diberikan berkas berupa `service.py` yang menjalankan TCP service dengan fitur `read_file`
- Berkas yang akan diproses oleh fungsi `read_file` sebelumnya akan dienkripsi menggunakan `AES OFB` dengan key & IV tertentu
- Sebagaimana diketahui, Output Feedback (OFB) encryption memiliki vulnerability, dimana dapat dilakukan dekripsi terhadap suatu cipher apabila telah dimiliki pasangan `plaintext-ciphertext` yang telah dienkripsi menggunakan key dan IV yang sama tanpa perlu mengetahui key dan IV-nya dengan cara melakukan operasi XOR pada pasangan tersebut, dan hasil XOR kemudian di-XOR-kan kembali dengan ciphertext yang ingin didekripsi
- Dalam hal ini pasangan `plaintext-ciphertext` kita peroleh dari source code `service.py` & hasil enkripsi `service.py` pada service. Sedangkan `ciphertext` yang ingin kita dekripsi adalah `/proc/self/environ` yang secara `default` menyimpan nilai dari `environment variable`.

## Flag

LKS2021{ofb_goes_brrrrrrruh}