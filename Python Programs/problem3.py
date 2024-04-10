def sum_and_last_divisible_by_3(string):
    # Split the string
    words = string.split()

    sum_divisible_by_3 = 0
    last_divisible_by_3 = None

    for word in words:
        if word.isdigit():
            num = int(word)
            if num % 3 == 0:
                # sum
                sum_divisible_by_3 += num
                # last divisible number
                last_divisible_by_3 = num

    return sum_divisible_by_3, last_divisible_by_3


string = "The best 6 of 8 will get 9 points"
# Call the function
sum_result, last_result = sum_and_last_divisible_by_3(string)
print("Sum:", sum_result)
print("Last divisible by 3:", last_result)
