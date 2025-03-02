def  main(n):
    n = n.lower().replace(' ', '')
    return n == n[::-1]
text = input("Enter text: ")
if main(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")