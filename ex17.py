from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} , to {to_file}")

#First Open the file
in_file = open(from_file)
#Then need to read the data and put it in in_data
in_data = in_file.read()
#to_file dosyasini ac
out_file = open(to_file, 'w')
#in_data dosyasini, to_file dosyasina yazmis oluyoruz
out_file.write(in_data)

print("Alright, all done")

out_file.close()
in_file.close()
