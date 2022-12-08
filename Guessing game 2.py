def main():
    minimum = 0
    maximum = 1000
    attempts = 10
    attempt = 1
    print(f'Computer: Think of a number between {minimum} and {maximum}, '
          f'and I will try to guess it in {attempts} tries!')
    input('Click ENTER to continue:')
    print('')

    while attempt <= attempts:
        guess = int((maximum - minimum) / 2) + minimum
        print(f'Computer: My guess number {attempt} is "{guess}"')
        info = ''
        while not info:
            info = take_user_info()

        if info == 'correct':
            print('Computer: Yeah! I am always the best!')
            break
        elif info == 'too small':
            minimum = guess
        else:
            maximum = guess

        attempt += 1

    print('Computer: NOOO! You must have been cheating!')


def take_user_info():
    """Take user's information on correctness of the guess.

    :return: user's input informing whether a guess is correct, too big or too small.
    """

    inputs = {'correct': ['1', 'correct'],
              'too small': ['2', 'too small'],
              'too big': ['3', 'too big']}

    info = input('Is it correct, too small, or too big? Choose 1 for "correct", 2 for "too small", '
                 '3 for "too big" or type in a phrase. ')
    print('')
    for key in inputs.keys():
        if info.strip().lower() in inputs[key]:
            return key
    print('Computer: Sorry, I do not understand.')
    return None


if __name__ == '__main__':
    main()
