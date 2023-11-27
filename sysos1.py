import os
for dirname,dirpath,filename in os.walk("/etc/ssh"):
    print(dirname)
    for file in filename:
            print(os.path.join(dirname,file))
