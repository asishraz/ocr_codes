''' One way
#first converting the normal string to date format : 01/04/2018 to 31/03/2019
import pandas as pd 


def string_taken(str1, str2):
	year_taken_1 = str1[4:]
	year_taken_2 = str2[4:]
	iterate_1 = iter(str1[0:4])
	iterate_2 = iter(str2[0:4])
	slash_join_1 = '/'.join(a+b for a,b in zip(iterate_1,iterate_1))
	slash_join_2 = '/'.join(a+b for a,b in zip(iterate_2,iterate_2))
	full_date_1 = slash_join_1 + '/' + year_taken_1
	full_date_2 = slash_join_2 + '/' + year_taken_2
	print(full_date_1)
	print(full_date_2)


#second we can generate the dates in the above format for the given range
	date1 = full_date_1
	date2 = full_date_2
	mydates = pd.date_range(date1, date2).tolist()
	print(mydates)


my_func = string_taken('01042018', '05042018')
print(my_func)

'''



''' second way , this is more convenient '''
import datetime


def string_taken(str1, str2):
	year_taken_1 = str1[4:]
	year_taken_2 = str2[4:]
	print("year: " +year_taken_1)
	iterate_1 = iter(str1[0:4]) 
	iterate_2 = iter(str2[0:4])
	slash_join_1 = '/'.join(a+b for a,b in zip(iterate_1,iterate_1))
	slash_join_2 = '/'.join(a+b for a,b in zip(iterate_2,iterate_2))
	print("after slash : " +slash_join_1)
	print("after slash : " +slash_join_2)
	full_date_1 = slash_join_1 + '/' + year_taken_1
	full_date_2 = slash_join_2 + '/' + year_taken_2
	print(full_date_1)
	print(full_date_2)


	# date1 = full_date_1
	# date2 = full_date_2

	# start = datetime.datetime.strptime(date1, '%d/%m/%Y')
	# end = datetime.datetime.strptime(date2, '%d/%m/%Y')
	# step = datetime.timedelta(days=1)
	# while start <= end:
	# 	print(start.date())
	# 	start += step 


my_func = string_taken('01042018', '05042018')
print(my_func)



'''for validating the date type
def validate(date_text):
	    try:
		    datetime.datetime.strptime(date_text, '%Y-%m-%d')
	    except ValueError:
		    raise ValueError("Incorrect, it should be 'YYYY-MM-DD'. ")

	validate(date1)
	validate(date2)

'''
