from collections import Counter


def formatted_string(input_string, sorted_count):
    new_string_list = []
    for key, value in sorted_count.items():
        # Refer the input string to get the appropriate letter case
        for og_key in input_string:
            if key.lower() == og_key.lower():
                new_string_list.append(og_key)
    # convert this list to string
    new_string = ''.join(new_string_list)
    return new_string


def first_not_repeated(input_string,sorted_count):
    # The value of the first non repeated letter(if any) would be 1. If no such value exists, an exception is thrown
    # and resolved by sending None
    try:
        a = next((key, value) for key, value in sorted_count.items() if value == 1)
        for char in input_string:
            if a[0] == char.lower():
                return char
    except:
        return None


# This function provides the user with the option to continue testing after every new string or stop the program.
def continue_app():
    cont_app = input("Do you want to continue? y or n: ").strip()
    if cont_app == "y":
        print()
        main()
    else:
        if cont_app == "n":
            return None
        else:
            print("Please select either y or n")
            continue_app()

def main():
    input_string = input("Please input a string: ").strip()
    # Proceed only if an appropriate input is provided i.e. no null input or just spaces
    if input_string:
        # Count the occurrence each letter in the input string irrespective of case
        count = Counter(input_string.casefold())
        # Sort this count in the ascending order of their occurrences
        sorted_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
        print("The first letter that is not repeated: ", first_not_repeated(input_string,sorted_count))
        print("The new formatted string is: ", formatted_string(input_string,sorted_count))
        print()
        continue_app()
    else:
        print("No string was inputted.")
        main()


main()
