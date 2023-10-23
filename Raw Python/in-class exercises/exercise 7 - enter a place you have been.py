#Input places visited using loop statements and call "break" as soon as the user enters "quit"
while True: #The loop will run unless "break" was called
    place = input("Enter a place you've been or enter 'quit' to stop \n ") #Putting input statement here will prevent infinite print
                                                                           #Statement from "else"
    if place == 'quit': #Exit loop if user entered "quit"
        break
    else: #If user did not enter "quit", regardless of accuracy of place, this statement will execute
        print(f"Wow! You've been to {place.title()}!") #.title() used to capitalize the input value