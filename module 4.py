# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1= 'Thirty'
str2= 'Days'
str3= 'Of'
str4= 'Python'
space= " "
result=(str1+ space+ str2+ space+ str3+ space + str4)
print(result)

# Concatenate the string 'Coding', 'For', 'All' to a single string 'Coding For All'.
str1= 'Coding'
str2= 'For'
str3= 'All'
space= ' '
result=(str1 + space + str2 + space + str3)
print(result)

# Declare a variable named Company and assign it to an initial value 'Coding For All'
company= 'Coding For All'
# print the variable copmpany using print().
print(company)

# print the length of the company string using len() method and print()
company= 'Coding For All'
# get the length of the string using len() method
length_of_company= len(company)
print("the length of the string company is:", length_of_company)

#Change all the characters to uppercase letters using upper() method.
company= 'Coding For All'
# Change all characters to uppercase
Company_uppercase= company.upper()
print(Company_uppercase)

# Change all the characters to lowercase letters using lower() method
company= 'Coding For All'
company_lowercase= company.lower()
print(company_lowercase)
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
Company= 'Coding For All'
# using capitalize() method
Company_capitalize= company.capitalize()
# Using title() method
company_title= company.title()
# Using swapcase() method
company_swapcase= company.swapcase()
# Print the formatted strings
print("capitalized:", Company_capitalize)
print("Title case:", company_title)
print("swap case:", company_swapcase)

# Cut(slice) out the first word of Coding For All
Company = 'Coding For All'
# Slice out the first word
first_word_removed = Company[Company.find(' ') + 1:]
# Print the result
print(first_word_removed)

# Check if Coding For All string contains a word coding using the method index, find or other methods.
company= 'Coding For All'
# Check if the string contains the word 'coding' using find() method
contains_coding_find = Company.lower().find('coding') != -1
# Print the result
print("Using find():", contains_coding_find)

# Check if the string contains the word 'coding' using index() method
try:
    Company.lower().index('coding')
    contains_coding_index = True
except ValueError:
    contains_coding_index = False
# Print the result
print("Using index():", contains_coding_index)

# Check if the string contains the word 'coding' using in keyword
contains_coding_in = 'coding' in Company.lower()
# Print the result
print("Using in keyword:", contains_coding_in)

# Replace the word coding in the string 'Coding For All' to Python
company= 'Coding For All'
# Replace the word 'Coding' with 'Python'
Company_replaced = Company.replace('Coding', 'Python')
# Print the result
print(Company_replaced)

# Change Python For Everyone to Python For All using the replace method or other methods
phrase = 'Python For Everyone'

# Replace the word 'Everyone' with 'All'
phrase_replaced = phrase.replace('Everyone', 'All')
# Print the result
print(phrase_replaced)
# Split the string 'Coding For All' using space as a separator (split())
Company = 'Coding For All'
# Split the string using space as the separator
words = Company.split()
# Print the resulting list of words
print(words)
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon", split the string at the comma.
# Declare the variable and assign the initial value
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# Split the string at the commas
companies_list = companies.split(', ')
# Print the resulting list
print(companies_list)
# What is the character at index 0 in the string 'Coding For All'
Company = 'Coding For All'
# Get the character at index 0
first_character = Company[0]
print(first_character)
# What is the last index of the string Coding For All
Company = 'Coding For All'
# Calculate the last index
last_index = len(Company) - 1
# Print the last index
print(last_index)

# What character is at index 10 in Coding For All string
Company = 'Coding For All'
# Get the character at index 10
character_at_index_10 = Company[10]
# Print the character
print(character_at_index_10)

# Create an acronym or abbreviation for the name 'Python For Everyone'.
acronym= 'PFE'
print(acronym)

# Create an acronym or abbreviation for the name 'Coding For All'
acronym= 'CFA'
print(acronym)

# Use index to determine the position of the first occurence of C in Coding For All.
Company = 'Coding For All'
# Determine the position of the first occurrence of 'C'
first_occurrence_C = Company.index('C')
# Print the position
print(first_occurrence_C)

# Use index to determine the position of the first occurence of F in Coding For All.
Company= 'Coding For All'
# Determine the position of the first occurence of 'F'
first_occurrence_F= Company.index('F')
# Print the position
print(first_occurrence_F)

# Use rfind to determine the position of the last occurence of l in Coding For All People.
phrase = 'Coding For All People'
# Determine the position of the last occurrence of 'l'
last_occurrence_l = phrase.rfind('l')
# Print the position
print(last_occurrence_l)

# Use index or find to find the position of the first occurence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'.

sentence = 'You cannot end a sentence with because because because is a conjunction.'
# Find the position of the first occurrence of the word 'because'
first_occurrence_because = sentence.find('because')
# Print the position
print(first_occurrence_because)
# Use rindex to find the position of the last occurence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction.'
# Find the position of the last occurrence of the word 'because'
last_occurrence_because = sentence.rindex('because')
# Print the position
print(last_occurrence_because)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because beccause is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'

# Find the start index of the phrase 'because because because'
start_index = sentence.find('because because because')

# Find the end index of the phrase 'because because because'
end_index = start_index + len('because because because')

# Slice out the phrase and create the new sentence
new_sentence = sentence[:start_index] + sentence[end_index:]
# Print the new sentence
print(new_sentence)

# Does 'Coding For All' starts with a substring Coding?
Company = 'Coding For All'# Check if the string starts with the substring 'Coding'
starts_with_coding = Company.startswith('Coding')
# Print the result
print(starts_with_coding)
# Does 'Coding For All' ends with a substring Coding?
Company = 'Coding For All'

# Check if the string ends with the substring 'Coding'
ends_with_coding = Company.endswith('Coding')
# Print the result
print(ends_with_coding)

# '  Coding For All  ', remove the right and left trailing spaces in the given string
Company = '  Coding For All  '
# Remove the leading and trailing spaces
trimmed_company = Company.strip()
# Print the result
print("'" + trimmed_company + "'")

# which one of the following variables return true when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python
# Define the variables
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
# Check if they are valid identifiers
is_var1_identifier = var1.isidentifier()
is_var2_identifier = var2.isidentifier()
# Print the results
print("30DaysOfPython is a valid identifier:", is_var1_identifier)
print("thirty_days_of_python is a valid identifier:", is_var2_identifier)

# The following list contain the names of some of python libraries:['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. join the list with a hash with space string
# List of Python libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space as the separator
joined_libraries = ' # '.join(libraries)
# Print the result
print(joined_libraries)

# Use the new line escape sequence to separate the following sentences: I am enjoying this challenge. I just wonder what is next.
# Define the sentences
sentence_1 = "I am enjoying this challenge."
sentence_2 = "I just wonder what is next."
# Combine the sentences using the new line escape sequence
combined_sentence = sentence_1 + "\n" + sentence_2
# Print the result
print(combined_sentence)

# Use a tab escape sequence to write the following lines:
name= 'Asabeneh'
Age= 250
Country= 'Finland'
City= 'Helsinki'
header = "Name\t\t\tAge\tCountry\t\tCity"
info = "'Asabeneh'\t250\t'Finland'\t'Helsinki'"
# Print the formatted lines
print(header)
print(info)

# Use the formatting method to display the following:
radius= 10
area= 3.14*radius**2
pi= 3.14
result= 'the area of a circle with radius {} is {}' .format(str(radius), str(area))
print(result)

# make the following using string formatting method
8+6==14, 8-6==2, 8*6==48, 8/6==1.33, 8%6==2, 8//6==1, 8**6==262144
a, b = 8, 6
formatted_string = "{} + {} == {}\n{} - {} == {}\n{} * {} == {}\n{} / {} == {:.2f}\n{} % {} == {}\n{} // {} == {}\n{} ** {} == {}".format(
    a, b, a + b,
    a, b, a - b,
    a, b, a * b,
    a, b, a / b,
    a, b, a % b,
    a, b, a // b,
    a, b, a ** b
)
print(formatted_string)



















