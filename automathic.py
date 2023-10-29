def get_menu_choice()->list:
    """Prompts the use to enter a valid menu choice to indicate which sequence should be generated.
       Also prompts the user to enter how many terms they would like to see.
    """
    print("Enter your choice:")
    print("-----------------")
    print("  (O)dd Integers")
    print("  (M)ultiples")
    print("  (S)quare numbers")
    print("  (T)riangular numbers")
    print("  (A)rithmetic Sequence")
    print("  (F)ibonacci Sequence")
    choice = input("Which sequence would you like to generate?\n")

    while choice.lower() not in ["o", "m", "s", "t", "a", "f"]:
        choice = input("Which sequence would you like to generate?\n")

    n = int(input("How many terms would you like to see?\n"))

    return [n, choice.lower()]


def positive_odds(n):
    positive_odds = []
    for number in range(1, n*2, 2):
        positive_odds.append(number)
    return positive_odds

def positive_multiples(n, m):
    if m<=0:
        positive_multiples = []
        return positive_multiples
    else:
        positive_multiples = []
        for number in range(m, m*(n+1), m):
            positive_multiples.append(number)
        return positive_multiples


def square_numbers(n):
    square_numbers = []
    for number in range(n):
        square = number*number
        square_numbers.append(square)
    return square_numbers


def triangle_numbers(n):
    triangle_numbers = []
    sum = 0
    for number in range(1, n+1):
        sum += number
        triangle_numbers.append(sum)
    return triangle_numbers

def arithmetic_sequence(n, t1, t2):
    arithmetic_sequence = []
    step = t2 - t1
    for number in range(t1, (n*step+t1), step):
        arithmetic_sequence.append(number)
    return arithmetic_sequence
    

def fibonacci_sequence(n):
    if n <= 0:
        fibonacci_sequence = []
        return fibonacci_sequence
    elif n == 1:
        fibonacci_sequence = [1]
        return fibonacci_sequence
    else:
        fibonacci_sequence = [1, 1]
        for term in range(n-2):
            new_number = fibonacci_sequence[term+1] + fibonacci_sequence[term]
            fibonacci_sequence.append(new_number)
        return fibonacci_sequence


if __name__ == "__main__":
    n, choice = get_menu_choice()

    match choice:
        case "o":
            seq = positive_odds(n)
        case "m":
            multiple = int(input("Which multiple would you like to use?"))
            seq = positive_multiples(n, multiple)
        case "s":
            seq = square_numbers(n)
        case "t":
            seq = triangle_numbers(n)
        case "a":
            term_1 = input("What is the first term of the arithmetic sequence?")
            term_2 = input("What is the second term of the arithmetic sequence?")
            seq = arithmetic_sequence(n, int(term_1), int(term_2))
        case  "f":
            seq = fibonacci_sequence(int(n))
        case _:
            seq = "Invalid input"

    print(seq)