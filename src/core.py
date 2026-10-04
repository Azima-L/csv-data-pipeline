import re

def is_valid_name(name, name_format):
    if name_format == "title_case":
        return name == name.title()
    elif name_format == "upper_case":
        return name == name.upper()
    elif name_format == "lower_case":
        return name == name.lower()
    return None

def is_valid_salary(salary, salary_min, salary_max):
    return salary_min <= salary <= salary_max

def is_valid_date(date_string, date_format="YYYY-MM-DD"):
    if date_format == "YYYY-MM-DD":
        return bool(re.match(r"\d{4}-\d{2}-\d{2}", date_string))
    return None