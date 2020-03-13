import os

directory_in_str = "/Users/isaacrowe/Documents/GitHub/tessajewel/img/studio"
directory = os.fsencode(directory_in_str)

count= 0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     os.rename(filename, "familial_code" + str(count))
     coun= count + 1