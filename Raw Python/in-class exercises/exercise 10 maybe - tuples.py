#NOT REALLY AN EXERCISE
#create 2 tuples
years = (1987,1985,1981,1996)

#use len(). Returns number of items in the tuple
print(len(years))

#use sum. Returns sum of all numbers in the tuple
print(sum(years))

#use sorted(). returns sorted elements (A-z, 1-10). not permanent
sorted_years = sorted(years)
print(sorted_years)
print(years) # not affected

#use .count(). counts duplicates of an element in the tuple
print(years.count(1987))

#use .index(). returns the index value of an element
print(years.index(1987))

