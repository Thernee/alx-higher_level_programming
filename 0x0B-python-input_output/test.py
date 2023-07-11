

def append_write(filename="", text=""):
    with open(filename, 'a') as a_file:
        print(a_file.tell())
        a_file.write(text)
        return a_file.tell()




nb_characters_added = append_write("file.txt", "This School is so cool!\n")
print(nb_characters_added)
