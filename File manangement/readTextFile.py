fname = input('Enter filename')
print()
try:
    fobj = open(fname,'r')
except IOError:
    print("*** file open error:",e)
else:
    for eachLine in fobj:
        print(eachLine),
        fobj.close()