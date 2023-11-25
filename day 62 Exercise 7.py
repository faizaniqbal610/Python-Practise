import os

def clearClutter(path, format):
    files = os.listdir(path)
    i = 0
    for file in files:
        print(file)
        if file.endswith(format):
            os.rename(f"{path}/{file}", f"{path}/{i}{format}")
            i = i+1

clearClutter("C:\\Users\\faiza\\OneDrive\\Pictures\\new", ".png")

