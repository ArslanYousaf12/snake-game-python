#only for practice purpose


# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()


# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# writing content

# with open("my_file.txt", mode="w") as file:
#     content = file.write("New Text.")


# Append the content in file
# with open("my_file.txt", mode="a") as file:
#     content = file.write("New Text.")


# Create new file of the file did not exist
with open("my_file_1.txt", mode="w") as file:
    content = file.write("New Text.")
    