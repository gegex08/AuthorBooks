column1 = input("\nEnter the column 1 header:\n")

print('You entered:',column1)

column2 = input("\nEnter the column 2 header:\n")

print('You entered:',column2)

while True:
    datapoint = input("\nEnter a data point (-1 to stop input):\n")
    if datapoint == '-1':
        break


while datapoint != '-1':
    if datapoint == '-1':
        break
    my_dict = {}
    if ',' not in datapoint:

        print('Error: No comma in string.\n')
        datapoint = input("Enter a data point (-1 to stop input):\n")
    else:

        split = datapoint.split(',')
        first = split[0].strip()
        second = split[1].strip()

        my_dict[first] = second

        print("Data string:",first)
        print("Data integer:",second)
        break



# Dictionary we'll be using later on to print our table and histogram
dict = {}

# Title for our table later on, lab requires this be the first input though
string = str(input('Enter a title for the data:\n').rstrip())
print('You entered:', string,)
print('')

# First column header for our table, second input
header1 = str(input('Enter the column 1 header:\n').rstrip())
print('You entered:', header1)
print('')

# Second column header for our table, third input
header2 = str(input('Enter the column 2 header:\n').rstrip())
print('You entered:', header2)
print('')

# Loop used to check for mistakes with how the input is formatted
while True:
# The fourth input, for data_point consisting of a name and an int
    data_point = input('Enter a data point (-1 to stop input):\n')

# Since -1 is our exit code, we need to compare to it first
    if data_point == '-1':
        break

# Outputs an error if user did not include a comma in the data point
    elif ',' not in data_point:
        print('Error: No comma in string.')
        print("\n".rstrip("\n"))
    else:
# Outputs an error if user tries to submit more than 2 data points
        if len(data_point.split(',')) > 2:
            print ('Error: Too many commas in input.')
            print("\n".rstrip("\n"))

# Outputs an error if user doesn't include an int in the data points
        else:
            if not(data_point.split()[-1].isnumeric()):
                print('Error: Comma not followed by an integer.')
                print("\n".rstrip("\n"))

# If no errors are found, the data begins to be processed for output
            else:

#Converts the data point string input into a list of substrings,
#then from a list into a string variable for the author and
# an int variable for the number of books
                blist=data_point.split(',') 
                string_num = int(blist[1])
                string_auth = str(blist[0])
# Appends the authors as keys and number of books as values to our 
# dictionary during each iteration of the loop
                author_dict[string_auth] = string_num

# Outputs the author and number of books for this iteration of the loop
                print('Data string:',blist[0], end='\n')
                print('Data integer:',string_num, end='\n')
                print('')
print('')

# Table formatting
format_title = '{title:>33}'
format_table = '{name:<20}{sep:1}{number:>23}'

# Print the table title and headers based on the formatting above
print(format_title.format(title=string))
print(format_table.format(name=header1, sep='|', number=header2))
print('-' * 44)

# Iterates through the dictionary items to fill in the table data
for k, v in author_dict.items():
    print(format_table.format(name=k, sep='|', number=v))
print('')

# Histogram formatting
format_hist = '{names:>20}{space:1}{hist:<1}'

# Iterates through the dictionary items to fill in the histogram
for k, v in author_dict.items():
    hist_string = ''
    for i in range(v):
        hist_string += '*'
    print(format_hist.format(names=k, space=' ', hist=hist_string))    
author_dict = {}

string = str(input('Enter a title for the data:\n').rstrip())
print('You entered:', string,)
print('')

header1 = str(input('Enter the column 1 header:\n').rstrip())
print('You entered:', header1)
print('')

header2 = str(input('Enter the column 2 header:\n').rstrip())
print('You entered:', header2)
print('')

while True:
    data_point = input('Enter a data point (-1 to stop input):\n')
    if data_point == '-1':
        break
    elif ',' not in data_point:
        print('Error: No comma in string.')
        print("\n".rstrip("\n"))
    else:
        if len(data_point.split(',')) > 2:
            print ('Error: Too many commas in input.')
            print("\n".rstrip("\n"))
        else:
            if not(data_point.split()[-1].isnumeric()):
                print('Error: Comma not followed by an integer.')
                print("\n".rstrip("\n"))
            else:
                blist=data_point.split(',') 
                string_num = int(blist[1])
                string_auth = str(blist[0])
                author_dict[string_auth] = string_num
                print('Data string:',blist[0], end='\n')
                print('Data integer:',string_num, end='\n')
                print('')
print('')

format_title = '{title:>33}'
format_table = '{name:<20}{sep:1}{number:>23}'
print(format_title.format(title=string))
print(format_table.format(name=header1, sep='|', number=header2))
print('-' * 44)
for k, v in author_dict.items():
    print(format_table.format(name=k, sep='|', number=v))
print('')

format_hist = '{names:>20}{space:1}{hist:<1}'
for k, v in author_dict.items():
    hist_string = ''
    for i in range(v):
        hist_string += '*'
    print(format_hist.format(names=k, space=' ', hist=hist_string))
