#types - 1 Binary 2 Text
# modes
#"r" = read = Default value.open file for reading.error if file doesn't exist
#"a" = append = opens file for appending at the end of file.creates file if it doesn't exist
#"w" = write = opens a file for writing,will overwrite existing content,creates file if it doesn't exist
#"x" = create the specified file.returns error if the file exist

#syntax = open(filename,mode)
#In addition we can specify if the file should be handled as the binary or text mode
#"t" = text = default value,text mode
#"b" = binary = binary mode(e.g. image)



#file.read() = to read char

#samplefile = open('sample3.txt')
#print(samplefile.read()) #to read entire file
#print(samplefile.read(10)) #to read first 10 char
#samplefile.close()


#file.readline()
#https://www.w3schools.com/python/ref_file_readlines.asp
#https://www.w3schools.com/python/ref_file_readline.asp
#samplefile = open('sample3.txt')
#print(samplefile.readline()) #to read first line
#print(samplefile.readlines()) #to read lines separately
#samplefile.close()


#looping

#file = open('sample3.txt')
#for line in file:
#	print(file.readlines())
#file.close()



#File write method

#f = open('sample3.txt',"a")

#f.write('Hello,my name is vaishnv=avi')
#f.close()


#creating file
#f = open('sample.txt',"x")

#f.write('Hello,my name is vaishnv=avi')
#f.close()


#deleting file

import os

#remove file
#os.remove('filename')

if os.path.exists("sample.txt"):
	os.remove('sample.txt') 
else:
	print("file doesn't exist")     

#check if file exist
#os.path.exists("filename")

#deleting a folder
#ps.rmdir("foldername")











