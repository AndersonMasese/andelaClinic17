def fizzbuzz(argument):

    if argument % 3 == 0 and argument % 5 == 0:
        return 'FizzBuzz'
    elif argument % 3 == 0:
        return 'Fizz'
    elif argument % 5 == 0:
        return 'Buzz'
    else:
        return str(argument)

fizzbuzz(5)