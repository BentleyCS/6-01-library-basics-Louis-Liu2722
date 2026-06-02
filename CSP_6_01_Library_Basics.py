def process_expenses(rawPrices):
    from analytics import apply_markup

    new_prices = []

    for price in rawPrices:
        new_price = apply_markup(price, 0.15)
        new_prices.append(new_price)

    return new_prices


def analyze_scores(n):
    from analytics import get_average, get_highest

    scores = []

    for i in range(n):
        score = float(input("Enter score: "))
        scores.append(score)

    highest = get_highest(scores)
    average = get_average(scores)

    return highest, average


def sanitize_usernames(usernames):
    from analytics import clean_text

    return clean_text(usernames)


def identify_outliers(numbers):
    from analytics import filter_threshold

    return filter_threshold(numbers, 100)


def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i

    return -1


def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = (left + right) // 2

        if items[middle] == target:
            return middle
        elif items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def search_and_report(items):
    from analytics import clean_text

    cleaned_items = clean_text(items)

    target = input("Enter item to search for: ")
    target = target.strip().lower()

    if cleaned_items == sorted(cleaned_items):
        return binary_search(cleaned_items, target)
    else:
        return linear_search(cleaned_items, target)