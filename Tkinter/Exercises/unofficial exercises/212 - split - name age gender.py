file_dir='Text Files/212.txt'

with open(file_dir) as file_object:
    names=[]
    ages=[]
    gender=[]
    for i in file_object:
        profile=i.strip().split('|')
        names.append(profile[0])
        ages.append(profile[1])
        gender.append(profile[2])

print(f'names: {names}')
print(f'ages: {ages}')
print(f'gender: {gender}')



