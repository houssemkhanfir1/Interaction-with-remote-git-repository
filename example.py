#Importing the packaging.

import sys 

#The first function.

def git_operation():
	print("I'am adding example .py file to the remote repository.")

#Modifying the code by adding a new sum function for an input list 

def new_fun_for_sum_of_list(L=""):
	s=0
	if not L:
		return None
	else:
		try:
			L=L.split(',')
			for i in L:
				s+=i
		except AttributeError as Exception:
			print("there is an error in the data format")
			return None
	return s


#Main program.

git_operation()
result=new_fun_for_sum_of_list(L=sys.argv[1])
print(f"this is the output of the new function: {result}")
