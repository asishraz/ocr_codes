# def string_taken(str1, str2):
#     year_taken_1 = str1[4:]  # 2019
#     year_taken_2 = str2[4:]  # 2019

#     iterate_1 = iter(str1[0:4])  # 0,1,0,4
#     iterate_2 = iter(str2[0:4])  # 0,4,0,4

#     slash_join_1 = '/'.join(a + b for a, b in zip(iterate_1, iterate_1))  #
#     slash_join_2 = '/'.join(a + b for a, b in zip(iterate_2, iterate_2))

#     full_date_1 = slash_join_1 + '/' + year_taken_1
#     full_date_2 = slash_join_2 + '/' + year_taken_2

#     return full_date_1 + ' to ' + full_date_2



# func = string_taken('01042018','01052019')
# print(func)

# import re

# s = "01/04/2018Name:Periodofemployment,dtype:objectto31/03/2019Name:Periodofemployment,dtype:object"
# num1 = "".join(re.split("[^0-9]*", s))
# print(num1)

# first_half = num1[0:len(num1)//2]
# second_half = num1[len(num1)//2 if len(num1)%2 == 0 else ((len(num1)//2)+1):]

# print(first_half)
# print(second_half)

# year_taken_1 = first_half[4:]  # 2019
# year_taken_2 = second_half[4:]

# print(year_taken_1)
# print(year_taken_2)

# iterate_1 = iter(first_half[0:4])  # 0,1,0,4
# iterate_2 = iter(second_half[0:4])

# slash_join_1 = '/'.join(a + b for a, b in zip(iterate_1, iterate_1))  #
# slash_join_2 = '/'.join(a + b for a, b in zip(iterate_2, iterate_2))


# print(slash_join_1)
# print(slash_join_2)

# full_date_1 = slash_join_1 + '/' + year_taken_1
# full_date_2 = slash_join_2 + '/' + year_taken_2

# print(full_date_1)
# print(full_date_2)


import re
st ="  0    bellacao ****"

st = "".join(re.split("[^a-z]*", st))
print(st)
print(len(st))

inputString = " 0    [bellacao, ****] Name: Taxpayer Given name in Full, dtype: object"
inputString.splitlines()