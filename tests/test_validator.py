from src.core import is_valid_name, is_valid_salary, is_valid_date

# Naming tests
def test_valid_title_case_name():
    assert is_valid_name("John Doe", "title_case") == True

def test_valid_upper_case_name():
    assert is_valid_name("JOHN DOE", "upper_case") == True

def test_valid_lower_case_name():
    assert is_valid_name("john doe", "lower_case") == True

def test_invalid_title_case_name():
    assert is_valid_name("john doe", "title_case") == False

def test_unknown_name_format():
    assert is_valid_name("John Doe", "camel_case") is None

# Salary tests
def test_salary_within_range():
    assert is_valid_salary(75000, 50000, 200000) == True

def test_salary_at_exact_minimum():
    assert is_valid_salary(50000, 50000, 200000) == True

def test_salary_at_exact_maximum():
    assert is_valid_salary(200000, 50000, 200000) == True

def test_salary_below_minimum():
    assert is_valid_salary(10000, 50000, 200000) == False

def test_salary_above_maximum():
    assert is_valid_salary(350000, 50000, 200000) == False

# Date tests
def test_valid_date_format():
    assert is_valid_date("2026-10-04") == True

def test_invalid_date_format():
    assert is_valid_date("04-10-2026") == False

def test_unknown_date_format():
    assert is_valid_date("2026-10-04", "DD-MM-YYYY") is None