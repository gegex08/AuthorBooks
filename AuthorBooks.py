#Genny Ocampo
#IDLE Project 7

#Dictionary
author_dict = {}

#Prompt the user for the headers of two columns of the table
header1 = str(input('Enter the column 1 header:\n'))
print('You entered:', header1)
print('')

header2 = str(input('Enter the column 2 header:\n'))
print('You entered:', header2)
print('')

#Prompt the user for an author, then prompt for the number of books (
while True:
    data_point = input('Enter a data point Author, Number of Books or press -1 to stop input:\n')
    if data_point == '-1':
        break
    else:
        blist=data_point.split(',') 
        string_num = int(blist[1])
        string_auth = str(blist[0])
        author_dict[string_auth] = string_num
        print(blist[0], end='\n')
        print(string_num, end='\n')
        print('')
print('')

#Output the information in a formatted table. 
format_table = '{name:<20}{sep:1}{number:>23}'
print(format_table.format(name=header1, sep='|', number=header2))
print('-' * 44)
for author, num_book in author_dict.items():
    print(format_table.format(name=author, sep='|', number=num_book))
print('')

#Output the information as a formatted histogram
format_hist = '{names:>20}{space:1}{hist:<1}'
for author, num_book in author_dict.items():
    hist_string = ''
    for i in range(num_book):
        hist_string += '*'
    print(format_hist.format(names=author, space=' ', hist=hist_string))
