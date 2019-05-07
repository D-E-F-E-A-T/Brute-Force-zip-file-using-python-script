import zipfile

zFile = zipfile.ZipFile('test.zip')
passFile = open('dictionary.txt')

for line in passFile.readlines():
    try:
        password = line.strip('\n')
        zFile.extractall(pwd=password)
        print('[+] password found '+password+'\n')
    except:
        pass
    
