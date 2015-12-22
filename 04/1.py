import hashlib
import sys

gotKey = False
alpha = sys.argv[1]
num = 0

while not gotKey:
    num += 1
    numStr = str(num)

    h = hashlib.new('md5')
    h.update((alpha+numStr).encode('ascii'))
    if h.hexdigest()[0:5] == '00000':
        key = alpha+numStr
        gotKey = True

print(key)
