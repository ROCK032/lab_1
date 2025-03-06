import os

folder_path = input("Enter the folder path: ")

if os.path.isdir(folder_path):
    directories = []
    files = []

    for i in os.listdir(folder_path):
        item_path = os.path.join(folder_path, i)
        if os.path.isdir(item_path): 
            directories.append(i)
        elif os.path.isfile(item_path):
            files.append(i)

    print('\nDirectories:')
    if directories:
        print("\n".join(directories))
    else:
        print('No directories')

    print('\nFiles:')
    if files:
        print('\n'.join(files))
    else:
        print('No files')

    print('\nContent folders:')
    print('\n'.join(os.listdir(folder_path)))
else:
    print("Incorrect path")
