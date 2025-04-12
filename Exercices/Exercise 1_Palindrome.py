name = "madam"

def check_palindrome(name):
    rev=""
    for char in name:
        rev = char+rev
    print(rev)

    if(name==rev):
        print (f"{name} and {rev} are palindromes")
    else:
        print(f"{name} and {rev} are not palindromes")


check_palindrome(name)


