def check_nagative_numbers(lst):
    if not isinstance (lst, list):
        return 'this is not a list'
    for negative in lst:
        

        if negative < 0:
            print(f'negative not found in the list')
            return negative

print(check_nagative_numbers([1, 2, -5, -77]))
