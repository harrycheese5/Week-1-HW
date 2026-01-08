num_lines = int(input('How many lines do you want to add? '))
file_variable = open('example_file.txt','w')
for num in range(1, num_lines + 1):
  entry = input('#{num} What would you like to add to the file? ')
  file_variable.write(f'{entry}\n')
file_variable.close
file_object = open('example.txt','r')
for line in file_object:
  print(line)
file_object.close() 
num_list = open('num_list.txt','r')
line = num_list.readline()
sum = 0
while line != '': # While line is not blank
  sum += int(line)
  line = num_list.readline()
num_list.close()
print(f'The sum of the numbers in the list is {sum}')
  with open('list.txt','w') as outfile:
    for number in range(17):
      outfile.write(f'{number}\n')
