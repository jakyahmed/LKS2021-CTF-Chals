grep -oP '(?<=2021:)(\d{2}:\d{2}:\d{2})' access.log > timestamp;
grep -oP '(?<=q=).*- ' access.log > payload
python2 sv.py
