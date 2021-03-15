## Judul Soal
File carving

## Deskripsi Soal

> Last night, I hid a secret file inside of an image

---
## Proof of Concept
- Diberikan berkas citra `flag.png`
- Secara visual, citra yang diberikan merupakan `QR code` yang memuat string `The password i supersecretpasssworduwu`
- Secara hierarkis, binary citra yang diberikan memuat `ZIP header` yang merupakan penanda adanya `Additional byte` setelah PNG Trailer
- Ekstraksi ZIP file dapat dilakukan dengan beberapa cara (misal: foremost)
- Gunakan password yang diperoleh pada tahap sebelumnya untuk mengekstrak isi dari `flag.zip`

## Flag

LKS2021{simple_file_carving_ae23f54}