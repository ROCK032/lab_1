import itertools


def main():
    user_input = input()
    permutations = itertools.permutations(user_input)

    for perm in permutations:
        print(''.join(perm))


# Example usage:
main()
