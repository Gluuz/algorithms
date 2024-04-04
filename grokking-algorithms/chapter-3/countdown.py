def countdown(i):
    # base case
    if i <= 0:
        return []
    # recursive case
    else:
        return [i] + countdown(i - 1)