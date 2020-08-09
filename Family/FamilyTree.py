from Person import Person, gender_map

CHILD_ADDITION_FAILED="CHILD_ADDITION_FAILED"
PERSON_NOT_FOUND="PERSON_NOT_FOUND"
CHILD_ADDITION_SUCCEEDED="CHILD_ADDITION_SUCCEEDED"
VALID_ADD_CHILD_ARGS=4

class FamilyTree:
	"""Represents the whole family.
	   Members dict contain the memebrs information given the names are unique. 
	   Used to get the member from the family using the name.
	   
	   Head represents the family head.
	"""

	def __init__(self):
		self.members={}
		self.head=None


	def add_persons_to_family(self, member):
		"""
		Method to add new members of the family

		args:
			member: Person object to be added to the family
		"""
		self.members.update({member.name:member})


	def get_family_member(self, name):
		"""
		Method to get a member of the family by name

		args:
			name: Person name to be looked up in the family
		"""
		return self.members.get(name, None)


	def add_head(self, name, gender):
		"""
		Method to add head member of the family using name,gender

		Raises exception if the head is being added despite being 
		present assuming only one family head exists

		args:
			name: Person name to be added in the family
			gender: one of male female
		"""
		if self.head is None:
			self.head=Person(name, gender_map[gender.upper()])
			self.add_persons_to_family(self.head)
		else:
			raise Exception("Failed to add Family Head as head already present")	


	def add_partner(self, name, partner_name, gender):
		"""
		Method to add spouse or partner of the family member using name,gender
		if the person is present

		Raises exception if the partner is already there or the person is not found

		args:
			name: Person name whose partner is to be added in the family
			partner_name: Person name to be added in the family
			gender: one of male female
		"""
		member=self.members.get(name,None)
		if member is not None and member.partner is None:
			partner=Person(partner_name, gender_map[gender.upper()], partner=member)
			member.add_partner(partner)
			self.add_persons_to_family(partner)
		else:
			raise Exception("Failed to add Partner as already exists or Person not found")


	def add_child(self, mother_name, child_name, gender):
		"""
		Method to add child to the family using name,gender
		if the mother is present and the correct values are passed

		Assumption:  Child can only be added via mother

		Raises exception if the mother is not found or the Child params are incorrect

		args:
			mother_name: Mother's name whose child is to be added in the family
			child_name: Child name to be added in the family
			gender: one of male female

		returns:
			Success message if child addition succeeds
			Failure message if child addition fails or the person is not found
		"""
		member=self.members.get(mother_name,None)
		if member is None:
			result=PERSON_NOT_FOUND
		elif child_name is None or gender is None:
			result=CHILD_ADDITION_FAILED
		elif member.gender==gender_map["FEMALE"]:
			child=Person(child_name, gender_map[gender.upper()], mother=member, father=member.partner)
			member.add_children(child)
			member.partner.add_children(child)
			self.add_persons_to_family(child)
			result=CHILD_ADDITION_SUCCEEDED
		else:
			result=CHILD_ADDITION_FAILED
		return result