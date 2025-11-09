f=open('Python','w') # open a file in write mode and returns file object
f.write('''Python:
Python is an interactive programming language.
Simple syntax of the language makes python programs easy-
to read and write.''') # to write into file

f.close() # save and close the open file
# f.write('python was developed in 1991')
f=open('Python','r')
print(f.read())
f.close()
f=open('Python','r')
print(f.tell()) # find current position of the file object
print(f.read(4)) # read a file
print(f.tell())
print(f.read(4))
print(f.tell())
print(f.readline()) # read one line at a time from the current position.
print(f.readline())
print(f.readline())
f.seek(10)
print(f.tell())
print(f.readline())
f.seek(0) # reach desired position in a file
print(f.readlines()) # read and return a list of lines read from a file(from the current position)
f.close()
print()
f1=open('Python','r')
f2=open('PythonCopy','w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()
f2=open('PythonCopy','r')
print(f2.read())
f2.close()
# f=open('Python','a')
# f.write('python was developed in 1991')
# f.close()
# f=open('Python','r')
# print(f.read())
# f.close()
# f=open('Python','r+')
# print("before write ",f.read())
# f.write("BY SATYAM SINGH")
# f.seek(0)
# print("after write operation",f.read())
# f.close()
print()
# Q> writing structures into a file
import pickle
def main():
    '''
    objective:To write and read a list and dictionary to
    and from a file
    Input parametres:none
    Return value:none
    '''
    f=open('file1','wb')
    pickle.dump(['hi','hello'],f)
    pickle.dump({1:'one',2:'two',3:'three'},f)
    f.close()
    f=open('file1','rb')
    value1=pickle.load(f)
    value2=pickle.load(f)
    print(value1,value2)
    f.close()
main()    

