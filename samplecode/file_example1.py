
import sys

filename = input("file name:")
fileobj = open(filename, "r+")
readmode = input("openmode (l-line by line/w-whole file)")
if(readmode=='l' or readmode=='L'):
    for line in fileobj:
        sys.stdin.read(1)
        print (line)
else:
    print(fileobj.read())
