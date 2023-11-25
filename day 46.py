# READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)

# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'w')
# f.write('Hello, World')
# f.close()

# APPENDING TO A FILE

with open('myfile.txt', 'a') as f:
    f.write("Hey i am inside with\n")

