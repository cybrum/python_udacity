import os
def rename_files():
    # (1)  get file names from a folder
    file_list = os.listdir(r"G:\Python\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working dir is: "+saved_path)
    os.chdir(r"G:\Python\prank")

    # (2) for each file, rename file name
    for file_name in file_list :
        print("old name: "+file_name)
        print("new name: "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
