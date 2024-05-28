password = input("Enter a password: ")

def strong_password(password):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[1:4])
    result = {"LowerCasse": 0, "Digit": 0, "UpperCasse": 0}
    counter_lower = 0
    counter_digit = 0
    counter_upper = 0
    day_temperatures = {}
    day_temperatures["mornig"] = (2.2, 2.3, 2.4)
    day_temperatures["noon"] = (2.2, 2.3, 2.4)
    day_temperatures["evening"] = (2.2, 2.3, 2.4)
    print(day_temperatures)

    for char in password:
        if char.islower():
            counter_lower += 1
            result["LowerCasse"] = counter_lower
        elif char.isdigit():
            counter_digit += 1
            result["Digit"] = counter_digit
        elif char.isupper():
            counter_upper += 1
            result["UpperCasse"] = counter_upper

    print(f"result_digits: {result['Digit']}")
    print(f"result_alpha: {result['LowerCasse']}")
    print(f"result_upper: {result['UpperCasse']}")

    if result['Digit'] >= 3 and result['LowerCasse'] >= 8 and result['UpperCasse'] >= 1:
        return f"Strong password, the result is: True"
    else:
        return f"Weak password, the result is: False"

print(strong_password(password))