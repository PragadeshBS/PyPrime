import random
first_run = True

while True:
    try:
        while True:
            def generate_prime_list(maxvalue):
                list_count = 0
                got_list = False
                first_item = True
                output = "Here you go... "
                if maxvalue > 1:
                    if maxvalue > 100000:
                        return "Max value is 1,00,000"
                    elif maxvalue >= 10000:
                        print("This might take a while, calculating...")
                    got_list = True
                    for numbers in range(2, maxvalue+1):
                        for num in range(2, numbers):
                            if numbers % num == 0:
                                break
                        else:
                            if first_item:
                                output += f"{numbers}"
                                list_count += 1
                                first_item = False
                            else:
                                output += f", {numbers}"
                                list_count += 1
                else:
                    output = f"Sorry, 2 is the smallest prime number"

                if got_list:
                    if list_count == 1:
                        output = f"There is only 1 prime number until {maxvalue}"
                        return output
                    else:
                        output += f"\n There are {list_count} primes until {maxvalue}"
                        return output
                else:
                    output = f"Sorry, there are no primes lesser than {maxvalue}"
                    return output


            def check_prime(number, user_called=True):
                is_prime = False
                if number > 10000000:
                    return "Max value is 1,00,00,000"
                if number > 999999 and user_called:
                    print(f"This might take a while if {number} is indeed prime...")
                if number > 1:
                    for i in range(2, number):
                        if number % i == 0:
                            break
                    else:
                        is_prime = True
                if is_prime:
                    return f"\n{number} is a prime number"
                else:
                    return f"\n{number} is NOT a prime number"


            def random_prime(maxvalue2):
                if maxvalue2 > 2:
                    if maxvalue2 > 10000000:
                        return "Max value is 10,00,00,000"
                    if maxvalue2 > 999999:
                        print("This might take a while...")
                    random_number = random.randint(2, maxvalue2-1)
                    while "NOT" in check_prime(random_number, False):
                        random_number = random.randint(2, maxvalue2-1)
                    else:
                        return f"{random_number} is a prime less than {maxvalue2}"
                else:
                    return "A value greater than 2 was expected"


            def user_handler():
                global first_run
                while True:
                    if first_run:
                        print("Hi there, welcome to this 'All in one Python Prime Program'")
                        print("Enter 'help' for a list of commands")
                        user_input = input("\nEnter command >> ")
                        user_input = user_input.lower()
                    else:
                        user_input = input("\nEnter command. Try 'help' for a list of commands >> ")
                        user_input = user_input.lower()

                    first_run = False

                    if user_input == "help":
                        print("\n'list' - generate the list of primes up to a number")
                        print("'check' - check if a number is prime")
                        print("'random' - generate a random prime number less than a given number")
                        print("'lock' - enter this followed by any of the above commands to hold on to that command")
                        print("'unlock' - to quit from a locked command")
                        print("'help' - list all commands")
                        print("'exit' - quit the program")
                    elif user_input == 'exit':
                        exit()

                    elif user_input[:4] == "list":
                        if (user_input[:-5:-1] == "kcol") and (len(user_input) == 9):
                            while True:
                                second_input = input("\nEnter a positive integer or 'unlock' to exit list >> ")
                                if second_input.lower() == "unlock":
                                    break
                                if second_input.isdigit():
                                    print(generate_prime_list(int(second_input)))
                                else:
                                    print("Enter a valid value... Try again")
                        elif len(user_input) == 4:
                            second_input = input("Enter a number to list all primes till that number >> ")
                            print(generate_prime_list(int(second_input)))
                        else:
                            print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")

                    elif user_input[:6] == 'random':
                        if user_input[:-5:-1] == "kcol" and (len(user_input) == 11):
                            while True:
                                second_input = input("\nEnter a positive integer or 'unlock' to exit random >> ")
                                if second_input.lower() == "unlock":
                                    break
                                if second_input.isdigit():
                                    print(random_prime(int(second_input)))
                                else:
                                    print("Enter a valid value... Try again")
                        elif len(user_input) == 6:
                            second_input = input("Enter a number to generate a prime lower than that number >> ")
                            print(random_prime(int(second_input)))
                        else:
                            print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")

                    elif user_input[:5] == "check":
                        if user_input[:-5:-1] == "kcol" and (len(user_input) == 10):
                            while True:
                                second_input = input("\nEnter a positive integer or 'unlock' to exit check >> ")
                                if second_input.lower() == "unlock":
                                    break
                                if second_input.isdigit():
                                    print(check_prime(int(second_input)))
                                else:
                                    print("Enter a valid value... Try again")
                        elif len(user_input) == 5:
                            second_input = input("Enter a number to check if it is prime >> ")
                            print(check_prime(int(second_input)))
                        else:
                            print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")

                    else:
                        print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")

            user_handler()

    except ValueError:
        print("That was not expected... Try again")
