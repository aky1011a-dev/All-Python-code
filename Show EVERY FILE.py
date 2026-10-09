import os 
 
for dirpath, dirnames, filenames in os.walk("c:\\"): 
    for filename in filenames: 
        print(os.path.join(dirpath, filename))

