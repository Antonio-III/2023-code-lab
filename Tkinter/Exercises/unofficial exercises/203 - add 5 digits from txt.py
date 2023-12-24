sums=0
with open('Text Files/203.txt') as  number_file:
    number_lines=number_file.readlines()
for i in number_lines:
    sums+=int(i)
print(sums)
# total lines: 6
print(f'len of lines: {len(number_lines)}')


# something faster
# number_file = [1\n,2\n,3\n,4\n,5\n]
sums=0

with open('Text Files/203.txt') as number_file:
    for i in number_file:
      sums+=int(i)
print(f'faster: {sums}')
# total lines: 5



