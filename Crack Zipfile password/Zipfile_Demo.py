import zipfile
try:
    with zipfile.ZipFile('1.zip') as zFile:
        zFile.extractall(path='./',pwd=b'1314')
        print('Extract the Zip file successfully!')
except:
    print('Extract the zip file failed')
