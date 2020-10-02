from os import system, name
import random
lines_out = 0
first_run = True
while True:

    def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def is_prime(number, show_inter_print=True):
        number = int(number)
        if number > 1:
            if (number > 100000000000000000) and show_inter_print:
                print(f"This might take a really long time to compute,if {number} is indeed prime. Hold on only if you are patient enough...")
            elif (number > 1000000000000) and show_inter_print:
                print(f"This might take a while to compute if {number} is indeed prime...")
            square_root = round(number ** (1 / 2))
            for num in range(2, square_root + 1):
                if number % num == 0:
                    return 0
            else:
                return 1
        else:
            return 0

    def list_prime(maxvalue):
        if int(maxvalue) > 1:
            if int(maxvalue) > 10000000:
                print("This might take a really long time to compute, hold on only if you are patient enough...")
            elif int(maxvalue) > 200000:
                print("This might take a while to compute...")
            prime_list = []
            for numbers in range(2, int(maxvalue)+1):
                square_root = round(numbers ** (1 / 2))
                for num in range(2, square_root + 1):
                    if numbers % num == 0:
                        break
                else:
                    prime_list.append(numbers)
            return prime_list
        else:
            return 0

    def list_prime_interval(start, stop):
        if int(stop) > 1:
            prime_list = []
            for numbers in range(start, int(stop) + 1):
                square_root = round(numbers ** (1 / 2))
                for num in range(2, square_root + 1):
                    if numbers % num == 0:
                        break
                else:
                    prime_list.append(numbers)
            return prime_list
        else:
            return []

    def random_prime(maxvalue2):
        maxvalue2 = int(maxvalue2)
        if maxvalue2 > 2:
            if maxvalue2 >1000000000000:
                print("This might take a while to compute...")
            random_number = random.randint(2, maxvalue2+1)
            while is_prime(random_number, False) == 0:
                random_number = random.randint(2, maxvalue2+1)
            else:
                return random_number
        else:
            return -1

    def input_handler(task_id, lock=0):
        global lines_out
        if task_id == 1:
            while True:
                if lines_out >= 5:
                    print("\nYou may use 'cls' command to clear the screen")
                if lock == 1:
                    user_input = input("\nEnter a positive integer, use 'unlock' to exit list>>").lower().strip()
                else:
                    user_input = input("\nEnter a positive integer>>").lower().strip()
                if (user_input.isdigit()) and (int(user_input) >= 0):
                    user_input = int(user_input)
                    output_handler(1, user_input)
                    break
                elif ((user_input == "list unlock") or (user_input == "unlock list") or (user_input == "unlock")) and (lock == 1):
                    return 1
                elif user_input == "back":
                    break
                elif user_input == "exit":
                    exit()
                elif user_input == "cls":
                    lines_out = 0
                    clear()
                else:
                    print("A positive integer was expected... Try again")
        elif task_id == 2:
            while True:
                if lines_out >= 5:
                    print("\nYou may use 'cls' command to clear the screen")
                if lock == 1:
                    user_input = input("\nEnter a positive integer, use 'unlock' to exit check>>").lower().strip()
                else:
                    user_input = input("\nEnter a positive integer>>").lower().strip()
                if (user_input.isdigit()) and (int(user_input) >= 0):
                    user_input = int(user_input)
                    output_handler(2, user_input)
                    break
                elif ((user_input == "check unlock") or (user_input == "unlock check") or (user_input == "unlock")) and (lock == 1):
                    return 1
                elif user_input == "back":
                    break
                elif user_input == "exit":
                    exit()
                elif user_input == "cls":
                    lines_out = 0
                    clear()
                else:
                    print("A positive integer was expected... Try again")
        elif task_id == 3:
            while True:
                if lines_out >= 5:
                    print("\nYou may use 'cls' command to clear the screen")
                if lock == 1:
                    user_input = input("\nEnter a positive integer, use 'unlock' to exit random>>").lower().strip()
                else:
                    user_input = input("\nEnter a positive integer>>").lower().strip()
                if user_input.isdigit():
                    user_input = int(user_input)
                    if user_input > 2:
                        output_handler(3, user_input)
                        break
                    else:
                        print("An integer greater than 2 was expected")
                elif ((user_input == "random unlock") or (user_input == "unlock random") or (user_input == "unlock")) and (lock == 1):
                    return 1
                elif user_input == "back":
                    break
                elif user_input == "exit":
                    exit()
                elif user_input == "cls":
                    lines_out = 0
                    clear()
                else:
                    print("A positive integer was expected... Try again")
        elif task_id == 4:
            while True:
                if lines_out >= 5:
                    print("\nYou may use 'cls' command to clear the screen")
                if lock == 1:
                    start = input("\nEnter a value to start from, use 'unlock' to exit this command>>").lower().strip()
                else:
                    start = input("\nStart from>>").lower().strip()
                if start.isdigit():
                    start = int(start)
                    if start >= 0:
                        while True:
                            if lock == 1:
                                stop = input("Enter a value to end with, use 'unlock' to exit this command>>").lower().strip()
                            else:
                                stop = input("End at>>")
                            if stop.isdigit():
                                stop = int(stop)
                                if int(stop) >= 0:
                                    interval_output_handler(start, stop)
                                    break
                            elif ((stop == "interval unlock") or (stop == "unlock interval") or (stop == "unlock")) and (lock == 1):
                                return 1
                            elif stop == "back":
                                break
                            elif stop == "exit":
                                exit()
                            elif stop == "cls":
                                lines_out = 0
                                clear()
                            else:
                                print("A positive integer was expected")
                        break
                elif ((start == "interval unlock") or (start == "unlock interval") or (start == "unlock")) and (lock == 1):
                    return 1
                elif (start == "back") and (lock == 1):
                    print("Use 'unlock' to exit interval command")
                elif start == "back":
                    break
                elif start == "exit":
                    quit()
                elif start == "cls":
                    lines_out = 0
                    clear()
                else:
                    print("A positive integer was expected")

    def interval_output_handler(start, stop):
        global lines_out
        output = ""
        if start == stop:
            answer = is_prime(int(start))
            if answer == 0:
                output += f"\n{start} is NOT a prime number"
            elif answer == 1:
                output += f"\n{start} is a prime number"
            output += f", you can use 'check' command for a single value like {start}"
            print(output)
        else:
            start_value = start
            stop_value = stop
            original_start = start
            if stop - start < 0:
                print("\nEnd value was greater than starting value... Not a problem, we fixed that for you")
                start_value = stop
                stop_value = start
                original_start = stop
            if start_value < 2:
                start_value = 2
            if ((start_value > 200000) or (stop_value > 200000)) and (stop_value - start_value > 10000):
                print("This might take a while to compute...")
            elif ((start_value > 1000000000000) or (stop_value > 1000000000000)) and (stop_value - start_value > 100):
                print("This might take a while to compute...")
            answer = list_prime_interval(start_value, stop_value)
            output = ""
            for item in answer:
                first_item = answer[0]
                last_item = answer[len(answer) - 1]
                if item == first_item:
                    output += str(item)
                elif item == last_item:
                    output += f" and {last_item}"
                else:
                    output += ", " + str(item)
            if len(answer) == 1:
                print(f"\n{answer[0]} is the only prime, try using a larger interval for more primes")
            elif len(answer) == 0:
                print(f"\nThere is no prime number from {original_start} to {stop_value}, try using a larger interval")
            else:
                print(f"\nThere are {len(answer)} primes from {original_start} to {stop_value}... {output}")
        lines_out += 1

    def output_handler(task_id, integer):
        global lines_out
        if task_id == 1:
            answer = list_prime(integer)
            if answer == 0:
                print(f"\nThere are no primes until {integer}")
            else:
                output = ""
                for item in answer:
                    first_item = answer[0]
                    last_item = answer[len(answer)-1]
                    if item == first_item:
                        output += str(item)
                    elif item == last_item:
                        output += f" and {last_item}"
                    else:
                        output += ", " + str(item)
                if len(answer) == 1:
                    print(f"\n{answer[0]} is the smallest prime, try entering a larger number")
                else:
                    print(f"\nThere are {len(answer)} primes until {integer}... {output}")

        elif task_id == 2:
            answer = is_prime(integer)
            if answer == 0:
                print(f"\n{integer} is NOT a prime number")
            elif answer == 1:
                print(f"\n{integer} is a prime number")

        elif task_id == 3:
            answer = random_prime(integer)
            print(f"\nYou have got {answer} as a random prime")
            if integer <= 1000:
                print("Try entering large numbers to get more random primes")
        lines_out += 1

    def lock_unlock_handler(user_input):
        if (user_input == "list lock") or (user_input == "lock list"):
            print("'list' command has been locked, use 'unlock' to quit command")
            while True:
                function_value = input_handler(1, 1)
                if function_value == 1:
                    break
        elif (user_input == "check lock") or (user_input == "lock check"):
            print("'check' command has been locked, use 'unlock' to quit command")
            while True:
                function_value = input_handler(2, 1)
                if function_value == 1:
                    break
        elif (user_input == "random lock") or (user_input == "lock random"):
            print("'random' command has been locked, use 'unlock' to quit command")
            while True:
                function_value = input_handler(3, 1)
                if function_value == 1:
                    break
        elif (user_input == "interval lock") or (user_input == "lock interval"):
            print("'interval' command has been locked, use 'unlock' to quit command")
            while True:
                function_value = input_handler(4, 1)
                if function_value == 1:
                    break
        else:
            print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")

    def main():
        global first_run, lines_out
        if lines_out >= 5:
            lines_out = 0
            print("\nYou may use 'cls' command to clear the screen")
        if first_run:
            print("Hi there, welcome to this All-in-one Python Prime Program")
            print("Enter 'help' for a list of commands")
            user_input = input("\nEnter command>>").lower().strip()
            first_run = False
        else:
            user_input = input("\nEnter command, try 'help' for a list of commands>>").lower().strip()

        if user_input == "help":
            print("\n'list' - generate the list of primes up to a number")
            print("'check' - check if a number is prime")
            print("'random' - generate a random prime number until a given number")
            print("'interval' - to generate list of primes within a interval")
            print("'back' - to return to the main command line from inside any command")
            print("'lock' - enter this followed by any of the above commands to hold on to that command")
            print("'unlock' - to quit from a locked command")
            print("'cls' - clear the terminal screen")
            print("'help' - list all commands")
            print("'exit' - quit the program at any moment")
        elif user_input == "cls":
            lines_out = 0
            clear()
        elif user_input == "exit":
            exit()
        elif user_input == "list":
            input_handler(1)
        elif user_input == "check":
            input_handler(2)
        elif user_input == "random":
            input_handler(3)
        elif user_input == "interval":
            input_handler(4)
        elif "lock" in user_input:
            lock_unlock_handler(user_input)
        else:
            print(f"{user_input} is not a recognised command. Try 'help' for a list of commands")


    if __name__ == "__main__":
        main()
