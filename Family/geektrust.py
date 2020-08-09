from FamilyTree import FamilyTree
from GetRelationship import GetRelationship

ADD_CHILD="ADD_CHILD"
GET_RELATIONSHIP="GET_RELATIONSHIP"


def read_initial_tree(dir=None):
	"""
	Loads the inital tree.	
	Functions supported are:
		
		- ADD_HEAD 			-	Adds the Family head		- 
		- ADD_CHILD 		-	Adds a Child to the family via the mother
		- ADD_PARTNER 		-	Adds a Person's Partner


	Args:
		dir: The relative path of the inital text file

	Returns:
		Initial Family Object

	Raises if anything but the default functions are accessed.
	"""
	import os
	family=FamilyTree()
	if not dir:
		dir=os.getcwd()
	path=os.path.join(dir,'family_tree.txt')
	file_obj=open(path,'r')
	for line in file_obj.readlines():
		line=line.rstrip()
		words=line.split()
		try:
			func = getattr(family,words[0].lower())
			func(*words[1:])
		except Exception as e:
			print(e)	
			raise Exception('Module has no attribute named {}'.format(words[0].lower()))
	return family


def read_input(family,file):
	"""
	Read the input from a file to do as specified.
	Functions supported are:
		- ADD_CHILD 		-	Adds a Child to the family via the mother
		- GET_RELATIONSHIP  -	Gets the relations for the person as specified	

	Args:
		family: The initial Family Tree of the Family
		file: The absolute path of the input file

	Raises Invalid Opeartion Error if other than the two functionalites are tried.
	"""
	import os
	try:
		file_obj=open(os.path.abspath(file),'r')
	except Exception:
		raise Exception('File Not Found')
	else:
		for line in file_obj.readlines():
			line=line.rstrip()
			elements=line.split()
			if elements[0] == ADD_CHILD:
				result=family.add_child(*elements[1:])
				print(result)
			elif elements[0] == GET_RELATIONSHIP:
				GetRelationship().form_function(family,elements)
			else:
				raise Excpetion('Invalid Operation Type')


if __name__=="__main__":
	
	import sys
	if len(sys.argv) !=2:
		raise Exception('Invalid Parameters')
	else:

		# Populate the family Trre initially
		family=read_initial_tree()
		# finding the output of the given ouutput file
		read_input(family,sys.argv[1])

