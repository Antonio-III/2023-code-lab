spaces = " "

spaces_count = 4

char = "*"

char_count = 1

for x in range(1,9):
  
    if x == 0:
        print(f"{spaces*spaces_count}{char*x}", end = "")
        spaces_count -=1
        char_count +=2
        
    elif x <5:
        print(f"{spaces*spaces_count}{char*x}", end = "")
        spaces_count -=1
        char_count +=2
    else:
        char_count, spaces_count = 3,3
        print(f"{spaces*spaces_count}{char*3}", end = "")        

    print()
