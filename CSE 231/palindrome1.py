import string

orig_str = input("Palindrome test -- enter a string: ")

my_str = orig_str.lower()
for bad_char in string.whitespace + string.punctuation:
    my_str = my_str.replace(bad_char,'')
    
# index technique
front = 0
end = len(my_str) - 1
mid = len(my_str)/2

while end >= mid:
    if my_str[front] != my_str[end]:
        print(my_str,'is not a palindrome')
        break
    end -= 1
    front += 1
else:
    print("It's a palindrome")
