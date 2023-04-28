def fizzbuzz(n):

    result = []                         # create an empty list to store the results
    for i in range(1, n+1):             # loop from 1 to n (inclusive)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")   # if i is divisible by 3 and 5, append "FizzBuzz"
        elif i % 3 == 0:
            result.append("Fizz")       # if i is divisible by 3, append "Fizz"
        elif i % 5 == 0:
            result.append("Buzz")       # if i is divisible by 5, append "Buzz"
        else:
            result.append(str(i))       # if none of the above conditions are met, append the number as a string
    return print(result)                       # return the list of results

fizzbuzz(30)