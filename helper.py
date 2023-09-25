def days_to_units(number_of_days, unit):
    if unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        print("Not support unit!")


def validate_and_execute(data):
    days = data["days"]
    unit = data["unit"]

    try:
        user_input_number = int(days)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, unit)
            print(calculated_value)
        elif user_input_number == 0:
            print('You entered a 0, please enter a valid positive number')
        else:
            print('You entered a negative number, no conversion for you')
    except ValueError:
        print("Your input is not a valid number, don't ruin my program")


user_message = "Hey user, enter a list number of days and I will convert it to hours!\n"
