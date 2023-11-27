def calculate_bmi(height, weight):
    """
    Calculate BMI given height (in meters) and weight (in kilograms).

    Args:
        height (float): Height in meters.
        weight (float): Weight in kilograms.

    Returns:
        float: Calculated BMI.
    """
    try:
        bmi = round(weight / (height**2), 2)
        return bmi
    except ZeroDivisionError:
        return None


def interpret_bmi(bmi):
    """
    Interpret the BMI and provide a classification.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI interpretation.
    """
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    if bmi < 18.5:
        return  "Your BMI is {bmi}, you are underweight."
    elif bmi < 24.9:
        return "Your BMI is {bmi}, you have a normal weight."
    elif bmi < 29.9:
        return "Your BMI is {bmi}, you are overweight."
    elif bmi < 34.9:
        return "Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return "Your BMI is {bmi}, you are obese (Class II)."
    else:
        return "Your BMI is {bmi}, you are obese (Class III)."


def main():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        result = interpret_bmi(bmi)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")


if __name__ == "__main__":
    main()