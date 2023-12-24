with open('text files/textfile.txt') as file_object:
    print(file_object.readline().rstrip())
    print(file_object.readline())
    # iterates through a list object. each call of readline will move calls 1 element (line) of the list (notepad)
