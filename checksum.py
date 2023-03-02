import hashlib
stop = False
HASHLIST = ('md5', 'sha1', 'sha256', 'sha512')
while not stop:
    hashname = input("Enter the method of checking: ")
    if hashname.lower() in HASHLIST:
        stop = True
    else:
        print("Type right method of checking")
stop = False
while not stop:
    name_of_file = input("Enter the path and the name of file: ")
    try:
        file_to_sum = open(name_of_file, 'rb')
    except:
        print("Type correct file path and name")
        continue
    stop = True

returned_hash = ''
hashname = hashname.lower()
if hashname == HASHLIST[0]:
    returned_hash = hashlib.md5(file_to_sum.read()).hexdigest()
elif hashname == HASHLIST[1]:
    returned_hash = hashlib.sha1(file_to_sum.read()).hexdigest()
elif hashname == HASHLIST[2]:
    returned_hash = hashlib.sha256(file_to_sum.read()).hexdigest()
elif hashname == HASHLIST[3]:
    returned_hash = hashlib.sha512(file_to_sum.read()).hexdigest()
print("Returned hash")
print(returned_hash)
if input('Save to a file?(Y/n): ').lower() == 'y':
    n_file = open(hashname+'_return.txt', 'w')
    n_file.write(returned_hash)
