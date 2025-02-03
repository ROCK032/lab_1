def main():
    user_input = input()
    words = user_input.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
result = main()
print(result)
