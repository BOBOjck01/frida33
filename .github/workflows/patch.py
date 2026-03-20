import sys

path = sys.argv[1]
offset = int(sys.argv[2])
size = int(sys.argv[3])

data = bytearray(open(path, "rb").read())
seg = data[offset:offset+size]

def replace(old, new):
    if len(old) != len(new):
        raise SystemExit("len mismatch")
    i = 0
    count = 0
    while True:
        j = seg.find(old, i)
        if j == -1:
            break
        seg[j:j+len(old)] = new
        i = j + len(old)
        count += 1
    print(old, "->", new, "count:", count)

replace(b"frida-server", b"sysmond____")
replace(b"re.frida.server", b"re.core.server_")

data[offset:offset+size] = seg
open(path, "wb").write(data)

print("patch done")
