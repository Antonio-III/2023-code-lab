#list your 3 favorite snacks
#print them all then print 1 element in snacks
snacks = ["dorritos","cheetos","pringles"]
print(snacks)
print(f"I like {snacks[0]} the most")


#use len function
print("I have", len(snacks),"favorite snacks!")

#add element in your list using .append()
snacks.append("oreo")
print(snacks) #this will now include the appended element

#use insert .function() twice
snacks.insert(4,"pizza")
snacks.insert(4,"cake")
print(snacks) #will include the 2 added elements

#use the .pop() function
popped_snacks = snacks.pop()
print(snacks)

#how to use .pop() to remove an item BASED on their position?
popped_snacks = snacks.pop(0)
print(snacks)

#use the .remove() to remove an element
snacks.remove("cake")
print(snacks)

#use .sort() on snacks
sort_snacks=snacks.sort()
print(sort_snacks)

#use .sorted() 
sorted_snacks = sorted(snacks)
#print(sorted_snacks)

#use reverse()
snacks.sort(reverse=True)
print(snacks)
