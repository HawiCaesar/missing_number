
def find_missing(list1, list2):

	if list1 == [] and list2 == []: # Check if both lists are empty
		return 0

	elif list1 == list2: # Check if both lists are equal
		return 0

	else:
		return list(set(list1)^set(list2))[0]


#print (find_missing([4, 6, 8], [4, 6, 8, 10]))

