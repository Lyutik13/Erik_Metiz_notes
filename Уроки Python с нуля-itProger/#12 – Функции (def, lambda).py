# def test_func(word):
#     print(word, end='')
#     print('!')
    # pass                # pass = ничего

# test_func('hi')

# def summa(a, b):
#     res = a + b
#     print('Result', res)
#
# summa(5, 7)
# summa('h', 'i')


# nums1 = [5, 7, 9, 4]
#
# min = nums1[0]
# for i in nums1:
#     if i < min:
#         min = i
# print(min)

def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

    print(min_number)

nums1 = [5, 7, 9, 4]
minimal(nums1)

                               # lamda сокращённая ф-я
x = lambda z, v: z * v
res =x(5, 2)

#                   or
# def summa(z, v):
#     return z * v

print(res)
