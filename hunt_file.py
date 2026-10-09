import os 
print("running")
for dirpath, dirnames, filenames in os.walk("c:\\"): 
    for filename in filenames:
        if filename.endswith(""): 
            if filename.startswith == ("Mediaval City"):
                print("File Found")
                print(os.path.join(dirpath, filename))
                break
            else:
                print("no")

print("Finished Searching")