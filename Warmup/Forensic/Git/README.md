## Judul Soal
Git

## Deskripsi Soal

> I made a Git Repository. Unfortunately, I often made some mistakes, so that I've undone some minor commits

---
## Proof of Concept
- Diberikan berkas `src.zip` berisikan Git repository
- Analisis menggunakan `git log` menunjukkan bahwa terdapat 2 buah commit yang sayangnya tidak memuat informasi yang berkaitan dengan flag

    ```sh
    $ git log

    commit 1064d4fa9c11c1e01b52ca70b0f6c430415d50f3 (HEAD)
    Author: hanasuru <faqih.insani@ymail.com>
    Date:   Tue Mar 16 12:14:28 2021 +0700

        Cleanup

    commit 91ac79532551c2649d49bc8992ded5e64eb500cd
    Author: hanasuru <faqih.insani@ymail.com>
    Date:   Tue Mar 16 12:10:04 2021 +0700

        Initial commit
    ```
- Berdasarkan hasil temuan tersebut, kita lakukan pengecekan terhadap isi dari `.git/objects`

    ```
    $ tree .git/object

    .git/objects
    ├── 10
    │   └── 64d4fa9c11c1e01b52ca70b0f6c430415d50f3
    ├── 15
    │   └── 763c863454cdbb1017d3071ab9c79ed9db57f0
    ├── 4b
    │   └── 825dc642cb6eb9a060e54bf8d69288fbee4904
    ├── 6a
    │   └── d85a054018d71adc2fae676a175e6ae237ae6c
    ├── 76
    │   └── d4cb70ce391e1ee9535dc766b3240576a56650
    ├── 91
    │   └── ac79532551c2649d49bc8992ded5e64eb500cd
    ├── a2
    │   └── 32ee9ddad8ac1c700971215fef4d1983ab24ee
    ├── aa
    │   └── e7c81ccd19ebcc40922b9fd490305fde92c0b4
    ├── c0
    │   └── bf535106e9bdfa7fac300b898f3c3541fda5d2
    ├── info
    └── pack
    ```
- Hasilnya kita mendapatkan 9 buah object yang masing-masing merupakan representasi dari `blob`, `tree`, dan `commit-msg`
- Apabila kita telaah lebih lanjut, sebuah git commit akan menggenerate paling tidak 3 buah `object` yakni 1 blob, 1 tree, dan 1 commit-msg.
- Hal ini menunjukkan apabila terdapat 2 buah commit, otomatis terdapat 6 buah object. Sedangkan pada proses sebelumnya kita menemukan 9 buah object, yang mana menunjukkan bahwa pernah terjadi perubahan `referrence logs`
- Untuk membuktikan dugaan tersebut, kita lakukan operasi berikut

    ```
    $ git reflog

    1064d4f (HEAD) HEAD@{0}: commit: Cleanup
    91ac795 HEAD@{1}: checkout: moving from master to 91ac79532551c2649d49bc8992ded5e64eb500cd
    6ad85a0 (master) HEAD@{2}: commit: Remove flag.txt
    76d4cb7 HEAD@{3}: commit: Add flag.txt
    91ac795 HEAD@{4}: commit (initial): Initial commit
    ```
- Hasilnya kita dapat melihat `commit` lain yang menunjukkan aktivitas penambahan `flag.txt`
- Dari sini, cukup lakukan `git diff` untuk mendapatkan perubahan dari commit

## Flag

LKS2021{secret_within_dangled_commit}