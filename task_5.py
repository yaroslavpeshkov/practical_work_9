for i in range(100000, 999999+1):
    palindrome_1_1 = i % 100000
    palindrome_1_2 = ((i % 10) * 10000 + ((i % 100) // 10) * 1000 + ((i % 1000) // 100) * 100 +
                      ((i % 10000) // 1000) * 10 + (i % 100000) // 10000)
    if palindrome_1_1 == palindrome_1_2:
        i += 1
        palindrome_2_1 = i % 100000
        palindrome_2_2 = ((i % 10) * 10000 + ((i % 100) // 10) * 1000 + ((i % 1000) // 100) * 100 +
                          ((i % 10000) // 1000) * 10 + (i % 100000) // 10000)
        if palindrome_2_1 == palindrome_2_2:
            i += 1
            palindrome_3_1 = (i % 100000) // 10
            palindrome_3_2 = ((palindrome_3_1 % 10) * 1000 + ((palindrome_3_1 % 100) // 10) * 100 +
                              ((palindrome_3_1 % 1000) // 100) * 10 + palindrome_3_1 // 1000)
            if palindrome_3_1 == palindrome_3_2:
                i += 1
                palindrome_i = ((i % 10) * 100000 + ((i % 100) // 10) * 10000 + ((i % 1000) // 100) * 1000 +
                                ((i % 10000) // 1000) * 100 + ((i % 100000) // 10000) * 10 + ((i % 1000000) // 100000))
                if i == palindrome_i:
                    print(i-3)
