## Judul Soal
callback

## Deskripsi Soal

> I'm willing to call you back, but I can't find your address

---
## Proof of Concept

- Diberikan berkas `python-compiled` chall.cpython-38.pyc yang kemudian kita dekompilasi menggunakan bantuan `uncompyle6`.
- Setelah mendapatkan `decompiled code`, kita mengetahui bahwa `service` memiliki fitur `add`, `list`, `view`, dan `edit note`.
- Selain itu, terdapat fungsi menarik yaitu `get_shell` yang berfungsi untuk mendapatkan akses RCE. Sayangnya fungsi ini tidak pernah `dipanggil`.
- Analisis pada fungsi `view_note` menunjukkan bahwa terdapat dua buah percabangan, yaitu ketika nilai `instance` merupakan `string` atau `function`.

    ```py
    def view_note():
        try:
            address = int(input('Address: '))
        except ValueError:
            return

        instance = ctypes.cast(address, ctypes.py_object)

        stdout.write('Content: ')
        if hasattr(instance.value, '__call__'):
            return stdout.writelines(instance.value())

        value = user_notes[instance.value]
        stdout.writelines(value)
    ```
- Hal tersebut memungkinkan kita dapat memanggil variable/fungsi apa saja `jika dan hanya jika` kita mengetahui `memory address` dari instance yang akan dipanggil.
- Selanjutnya, kita mendapati `vulnerability` lainnya pada fungsi `edit_note` dimana variable `content` akan dikenai fungsi `eval()`. Namun kita perlu memodifikasi payload yang ada untuk menghindari `blacklisting`.

    ```py
    def edit_note():
        try:
            address = int(input('Address: '))
        except ValueError:
            return

        content = input('Content: ')

        if sanitize_input(content):
            instance = ctypes.cast(address, ctypes.py_object)   
            user_notes[instance.value] = eval(f"'{content}'")

            stdout.write('Successfully edited a note')
        else:
            stdout.write("Get away. Those characters are not allowed")
    ```
- Modifikasi payload dapat kita lakukan dengan tujuan untuk memperoleh `memory address` dari fungsi `get_shell`

    ```
    '+str(id(get_shell))+'
    ```
- Kemudian kita gunakan fungsi `view_note` untuk melihat content dari `note` yang barusan kita ubah. Di sinilah kita mendapatkan `long_int` yang merupakan `memory address` dari fungsi `get_shell()`
- Terakhir kita gunakan fungsi `view_note` sekali lagi dengan memasukkan `memory address` dari step sebelumnya
- Hasilnya fungsi `get_shell()` berhasil dieksekusi

## Flag

LKS2021{thanks_for_calling_me_back}