def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) -i -1]:
            return False
    return True

is_palindrome("Apple")
is_palindrome("peep")
is_palindrome("pa nd nd ap")