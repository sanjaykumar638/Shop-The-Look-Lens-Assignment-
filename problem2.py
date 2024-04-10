def array_division(arr):
    result = []
    for i in range(len(arr)-1):
        try:
            # Check if the divisor is zero
            if arr[i+1] == 0:
                print("Warning: Division by zero! Skipping division.")
                continue
            result.append(arr[i] / arr[i+1])
        except ZeroDivisionError:
            print("Error: Division by zero!")
            return None
    try:
        # Check if the divisor for the last division is zero
        if arr[0] == 0:
            print("Warning: Division by zero! Skipping division.")
            return None
        result.append(arr[-1] / arr[0])
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    return result

arr = [9, 33, 0, 7, 2, 82, 77]
print(array_division(arr))
