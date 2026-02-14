

def kelvin_to_fahrenheit(temp_kelvin):
    temp_fahrenheit = (temp_kelvin - 273.15) * (9 / 5) + 32
    return round(temp_fahrenheit, 2)


def safe_get_float(value, default_value=0):
    try:
        safe_value = float(value)
    except Exception as e:
        safe_value = default_value
    return safe_value