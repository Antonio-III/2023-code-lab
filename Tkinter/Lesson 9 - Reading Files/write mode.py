file_dir='text files/206.txt'

with open(file_dir,'w') as file_handler:
    file_handler.write('I love programming')
    file_handler.write('ye')
with open(file_dir,'a') as file_handler:
    file_handler.write('I love datasets\n')
    file_handler.write('oh ye\n')
