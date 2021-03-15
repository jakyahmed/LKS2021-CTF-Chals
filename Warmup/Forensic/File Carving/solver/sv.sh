zbarimg ../peserta/flag.png | cut -d' ' -f4 > password
foremost flag.png
7z x -p$(cat password) output/zip/00000000.zip
cat flag.txt
