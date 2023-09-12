def check_palindrome(word):
    reversed_word = word[::-1]
    return True if word == reversed_word else False


print(check_palindrome('hannah'))
print(check_palindrome('dog'))
