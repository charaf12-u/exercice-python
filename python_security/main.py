from file_reader import read
from misc_script_1 import hashtext
hash=str(input("the hash"))
wordlist=str(input("the wordlist"))
hash_type=str(input("the hash type"))
rr=read()
redall=rr.readlist(wordlist)
hh=hashtext()
all=[]
for i in redall:
    i=i.rstrip("\n")
    print(hh.hashingtext(i,hash_type))