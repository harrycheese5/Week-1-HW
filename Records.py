num_records = int(input('How many records do you want to create? ')) # get number of records
with open('records.txt','w') as record_file: # Open file for writing
  for count in range(1, num_records + 1):
    print(f'Enter data for record #{count}')
    # get fields for a record
    field_1 = input('Field 1: ')
    field_2 = input('Field 2: ')
    field_3 = input('Field 3: ')
    # write record to file
    record_file.write(f'{field_1}\n')
    record_file.write(f'{field_2}\n')
    record_file.write(f'{field_3}\n')
print() # prints a blank line
print('Records have been written to records.txt')

,.,,
