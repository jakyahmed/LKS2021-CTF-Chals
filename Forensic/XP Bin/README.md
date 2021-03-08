## Judul Soal
XP Bin

## Deskripsi Soal

> I opened my old hard-drive & got a bunch of deleted file. Unfortunately, I don't know how to recover it
---

## Hint
- There're a bunch of tools that helps you parse an `INFO2` file

---
## Proof of Concept

- Diberikan `disk.tar.gz` yang kemudian didekompresi menggunakan `tar -xzf disk.tar.gz` sehingga diperoleh `disk.img`
- Analisis menggunakan `testdisk` menunjukkan bahwa terdapat `deleted file` bernama `Recycler` yang notabene merupakan Folder `Recycle.Bin` pada `Windows XP`
- Selain itu terdapat `INFO2` file yang kurang lebih memiliki sistematika sebagai berikut

    ```
    ❯ rifiuti INFO2
    Recycle bin path: 'INFO2'
    Version: 5
    OS Guess: Windows XP or 2003
    Time zone: UTC [+0000]

    Index	Deleted Time	Gone?	Size	Path
    0	2021-03-08 09:20:42	No	4096	C:\repository
    1	2021-03-08 09:20:42	No	4096	C:\repository\.git
    2	2021-03-08 09:20:42	No	41	C:\repository\.git\HEAD
    3	2021-03-08 09:20:42	No	4096	C:\repository\.git\branches
    4	2021-03-08 09:20:42	No	92	C:\repository\.git\config
    5	2021-03-08 09:20:42	No	73	C:\repository\.git\description
    6	2021-03-08 09:20:42	No	4096	C:\repository\.git\hooks
    ```

- Terdapat beberapa opsi yang bisa digunakan, diantaranya:

  a. Melakukan recovery file menggunakan `FTK imager` 

  b. Menjalankan Windows XP kemudian memindahkan isi dari Folder `Recyler/SID` ke drive tertentu, kemudian melakukan file recovery langsung dari `Recycle.Bin`

  c. Membuat parser dengan acuan `INFO2` file

## Flag

LKS2021{revisiting_old_fashioned_recycle_bin}