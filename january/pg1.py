#1. Write a Python program to:
   # a) Count the vowels in a given string.
 #   b) Replace all vowels in the string with ‘#’

a = input("Enter the string: ")
vowels = "aeiouAEIOU"


processed_string = list(a)


for i in range(len(processed_string)):
    if processed_string[i] in vowels:
        processed_string[i] = '#'  


processed_string = ''.join(processed_string)

print("Processed string:", processed_string)
