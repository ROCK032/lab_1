import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)
if __name__ == "__main__":
    path = input("Enter the directory path: ")
    if os.path.exists(path) and os.path.isdir(path):
        print("\nDirectories:", list_directories(path))
        print("\nFiles:", list_files(path))
        print("\nAll Directories and Files:", list_all(path))
    else:
        print("Invalid Directory Path")
