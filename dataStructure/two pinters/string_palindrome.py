def palindrome_checker(input):
    left = 0
    right = len(input) - 1

    flag = False

    while left < right:
        if input[left] != input[right]:
            print("Not Palindrome")
            break
        else:
            flag = True
        left += 1
        right -= 1
    if flag:
        print("Palindrome")


palindrome_checker(str(121))
