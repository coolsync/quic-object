def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique

print(get_unique_numbers([1,2,3,3,3,3,4,5]))


# reference
# https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/

# https://www.w3resource.com/python-exercises/python-functions-exercise-8.php#:~:text=Python%20Code%3A%20def%20unique_list%20%28l%29%3A%20x%20%3D%20%5B%5D,%28%5B1%2C2%2C3%2C3%2C3%2C3%2C4%2C5%5D%29%29%20Sample%20Output%3A%20%5B1%2C%202%2C%203%2C%204%2C%205%5D
