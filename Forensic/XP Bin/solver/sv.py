import struct
import os

rootdir = 'Recycler/S-1-5-21-4120123742-20034575120-115436213-1001/'
entry_offset = 20

with open(rootdir + 'INFO2', 'rb') as f:
    content = f.read()


def lists(path, mode, exclude=['INFO2', 'desktop.ini']):
    result = []

    for r, d, f in os.walk(path):
        for _ in eval(mode):
            if _ not in exclude:
                abspath = os.path.join(r, _)
                result.append(abspath)

    return result


entries = list()
while entry_offset < len(content):
    entry = content[entry_offset : entry_offset + 800]
    entries.append(entry)
    entry_offset += 800

entries_catalog = dict()
for entry in entries:
    record_id = struct.unpack('<I', entry[260:264])[0]
    basedir = entry[3:260].strip('\x00')
    basedir = basedir.replace('\\', '/')
    
    ext = os.path.splitext(basedir)[1]
    key_path = 'DC%s%s' % (record_id, ext)
    entries_catalog[key_path] = basedir

dir_files = lists(rootdir, 'd') + lists(rootdir, 'f')
for deleted_path in dir_files:
    path = os.path.basename(deleted_path)
    original_path = entries_catalog[path]

    basename = os.path.basename(deleted_path)
    dirname = os.path.dirname(deleted_path)
    for p in deleted_path.split('/')[2:-1]:
        b1 = os.path.basename(p)
        b2 = os.path.basename(entries_catalog[p])
        dirname = dirname.replace(b1, b2)

    deleted_path = os.path.join(dirname, basename)
    original_path = os.path.join(rootdir, original_path)

    os.rename(deleted_path, original_path)