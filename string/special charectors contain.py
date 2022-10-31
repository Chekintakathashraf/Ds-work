# check if a string contains any special character

# Python3 program to check if a string
# contains any special character

# import required package
import re

# Function checks if the string
# contains any special character
def run(string):

	# Make own character set and pass
	# this as argument in compile method
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	
	# Pass the string in search
	# method of regex object.
	if(regex.search(string) == None):
		print("String is accepted")
		
	else:
		print("String is not accepted.")
	

# Driver Code
if __name__ == '__main__' :
	
	# Enter the string
	string = "Geeks$For$Geeks"
	
	# calling run function
	run(string)


print('************')

# Python code
# to check if any special character is present
#in a given string or not

# input string
n="Geeks$For$Geeks"
n.split()
c=0
s='[@_!#$%^&*()<>?/\|}{~:]' # special character set
for i in range(len(n)):
	# checking if any special character is present in given string or not
	if n[i] in s:
	    c+=1 # if special character found then add 1 to the c

# if c value is greater than 0 then print no
# means special character is found in string	
if c:
	print("string is not accepted")
else:
	print("string accepted")

# this code is contributed by gangarajula laxmi
