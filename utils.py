def validate_positive_number(value):
    try:
        number = float(value)
        if number < 0:
            raise ValueError("Amount must be non-negative.")
        return number
    except ValueError:
        raise ValueError("Invalid number format.")
