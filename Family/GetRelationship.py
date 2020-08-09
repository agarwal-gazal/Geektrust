from Person import Person,gender_map
from FamilyTree import FamilyTree


VALID=3
PERSON_NOT_FOUND="PERSON_NOT_FOUND"

class GetRelationship:
	"""
	Class which acts as an internediate to get the relevant relations
	as specified in the input file.

	"""


	def form_function(self,family,elements):
		"""
		The method takes a FamilyTree instance and creates functions based on the relationship
		specified in the input file to call the relvant methods of the current class.

		args:
			family : FamilyTree instance containing a family detail
			elements: consists of the relationship to ftech and member name

		exception:
			- invalid relationship has been specified or the one which is not supported currently
			- Invalid arguments are specified for a method

		returns:
			result or failure message

		"""
		if len(elements) is VALID:
			func_name="_".join(elements[2].lower().split('-'))
			func_name="_".join(["get",func_name])
			try:
				func = getattr(GetRelationship,func_name)
				member=family.members.get(elements[1])
				result=func(self,member) if member else PERSON_NOT_FOUND
				print(result)
			except Exception:
				raise Exception('Module has no attribute named {}'.format(func_name))
		else:
			raise Exception('Invalid Number Of Arguments for Operation {}'.format(elements[0]))


	def get_son(self,member):
		"""
		Method to get all sons of the person.
		
		args:
			member: Person object whose son is to be found

		returns:
			space separated sons names or None
		"""

		relations = member.get_child(gender_map["MALE"])
		return " ".join(relations) if relations else None


	def get_daughter(self,member):
		"""
		Method to get all daughters of the person.
		
		args:
			member: Person object whose daughter is to be found

		returns:
			space separated daughters names or None
		"""
		relations = member.get_child(gender_map["FEMALE"])
		return " ".join(relations) if relations else None


	def get_siblings(self,member):
		"""
		Method to get all siblings of the person.
		
		args:
			member: Person object whose siblings is to be found

		returns:
			space separated siblings names or None
		"""
		relations = member.get_siblings()
		relations = [c.name for c in relations]
		return " ".join(relations) if relations else None


	def get_brother_in_law(self,member):
		"""
		Method to get all brother-in-law(Spouse’s brothers,Husbands of siblings ) of the person.
		
		args:
			member: Person object whose brother-in-law is to be found

		returns:
			space separated brother-in-law's names or None
		"""
		relations = member.get_in_laws(gender_map["MALE"])
		return " ".join(relations) if relations else None

	
	def get_sister_in_law(self,member):
		"""
		Method to get all sister-in-law(Spouse’s sisters,Wives of siblings) of the person.
		
		args:
			member: Person object whose sister-in-law is to be found

		returns:
			space separated sister-in-law's names or None
		"""
		relations = member.get_in_laws(gender_map["FEMALE"])
		return " ".join(relations) if relations else None


	def get_paternal_uncle(self,member):
		"""
		Method to get all paternal-uncle(father's brother) of the person.
		
		args:
			member: Person object whose paternal-uncle is to be found

		returns:
			space separated paternal-uncle's names or None
		"""
		relations=[]
		if member.father:
			relations = member.father.get_parents_cousins(gender_map["MALE"])
		return " ".join(relations) if relations else None


	def get_maternal_uncle(self,member):
		"""
		Method to get all maternal-uncle(mother's brother) of the person.
		
		args:
			member: Person object whose maternal-uncle is to be found

		returns:
			space separated maternal-uncle's names or None
		"""
		relations=[]
		if member.mother:
			relations = member.mother.get_parents_cousins(gender_map["MALE"])
		return " ".join(relations) if relations else None


	def get_paternal_aunt(self,member):
		"""
		Method to get all paternal-aunt(father's sister) of the person.
		
		args:
			member: Person object whose paternal-aunt is to be found

		returns:
			space separated paternal-aunt's names or None
		"""
		relations=[]
		if member.father:
			relations = member.father.get_parents_cousins(gender_map["FEMALE"])
		return " ".join(relations) if relations else None


	def get_maternal_aunt(self,member):
		"""
		Method to get all maternal-aunt(mother's sister) of the person.
		
		args:
			member: Person object whose maternal-aunt is to be found

		returns:
			space separated maternal-aunt's names or None
		"""
		relations=[]
		if member.mother:
			relations = member.mother.get_parents_cousins(gender_map["FEMALE"])
		return " ".join(relations) if relations else None
