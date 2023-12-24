def app():
    file_dir='Text Files/208.txt'
    text=['Enter a number and I check if it is in the list: ','Would you like to leave? Enter y to exit ','Exit successful']
    with open(file_dir) as file_handler:
        file_handler_int= [int(i) for i in file_handler]
        leave='n'
        while leave!='y':
            user_i=(input(text[0]))
            # verfication
            if user_i.isnumeric():
                num=int(user_i)
                if num not in file_handler_int:
                    print(f'{num} is not in the file. Sorry 😥')

                    if leave=='y':
                        break
                else:
                    print(f'{num} is in the list. Matter of fact, it appeared {file_handler_int.count(num)} times!')
            else:
                continue
            leave=input(text[1])
        print(text[2])

app()
