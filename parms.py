import sys
import os


for arg in sys.argv:
	if arg != 'parms.py':
		#print(sys.argv[1:])
		print(arg)
#
#
#

def DoSomething(usn,pswd):
	print(usn+"/"+pswd)

	return

# filename = '../Forgione/users.txt'
# with open(filename) as file_object:
# 	#open lines to array
# 	lines = file_object.readlines()

# for line in lines:
# 	# iterate array for each line
# 	print(line)

acct_DIR = '../Forgione/accounts'

files = os.listdir(acct_DIR)
#
# For each file in accounts directory
for filename in files:
	#
	#
	this_usn = ''
	this_pswd = ''
	#
	file_path = acct_DIR + '/' + filename
	with open(file_path) as file_object:
 		#open lines to array
 		lines = file_object.readlines()
 		

 		### TBD - remove this loop
 		### there is no reason to loop over each line here
 		### if all we want is the first two lines.
 		#		- probably need another calling program if 
 		# 		  we wanted to check the url portion to de-dep
 		for line_raw in lines:
 			line = line_raw.split(":")
 			#
 			if line[0] == 'urls':
 				#
# The idea here is that once we've reached the urls line
# we will 
				#
 				DoSomething(this_usn,this_pswd)
 				print("Done!")
 				break;
 			elif line[0] == 'usn':
 				this_usn = line[1].strip()
 				#print('this_usn: '+this_usn)
 			elif line[0] == 'pass':
 				this_pswd = line[1].strip()
 				#print('this_pswd: '+this_pswd)
 				
 			#	
 		#
 		file_object.close()
	# 
#