import os

ls = os.linesep

while True:
    if os.path.exists(fname):
        print("Error: '%s' already exists" % fname)
    else:
        break

all = []
print("\n Enter lines ('.' by itself to quit).\n")

while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print('DONE!')