from CSP_6_01_Library_Basics import process_expenses, analyze_scores, sanitize_usernames, identify_outliers, search_and_report, linear_search, binary_search

def test_process_expenses():
    prices = [100, 200, 50]
    result = process_expenses(prices)
    print(result)
    assert result == [114.99999999999999, 229.99999999999997, 57.49999999999999]


def test_sanitize_usernames():
    usernames = ["  Jerry ", "BOB", " Alice  "]
    result = sanitize_usernames(usernames)
    print(result)
    assert result == ["jerry", "bob", "alice"]


def test_identify_outliers():
    numbers = [50, 101, 100, 200, 99]
    result = identify_outliers(numbers)
    print(result)
    assert result == [101, 200]


def test_search_helpers():
    items = ["apple", "banana", "cherry"]

    assert linear_search(items, "banana") == 1
    assert binary_search(items, "cherry") == 2
    assert linear_search(items, "orange") == -1


print("All tests passed!")