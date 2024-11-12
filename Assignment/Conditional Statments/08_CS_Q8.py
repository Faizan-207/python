def is_palindrome(string):

    reversed_string = string[::-1]
    return string == reversed_string


string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
