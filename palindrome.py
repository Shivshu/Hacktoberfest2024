def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
