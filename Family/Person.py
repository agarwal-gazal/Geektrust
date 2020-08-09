
gender_map={
	"FEMALE":"F",
	"MALE":"M"
	}

class Person:
	"""This class represents a person in a family tree.
	Characteristics:
	- name			real name of the person also used to lookup a person in a family
					assuming name is unique
	- gender		gender of the person ('M' for male , 'F' for female)
	- mother    	mother of the person(Person object)
	- father    	father of the person(Person object)
	- partner    	partner of the person(Person object)
	- children    	list of children of the person(Person object)
	"""

	def __init__(self, name, gender, mother=None, father=None, partner=None):

		self.name = name
		self.gender = gender
		self.mother = mother
		self.father = father
		self.partner = partner
		self.children = []


	def add_partner(self, member):
		"""
		Method to add spouse or partner of the person called from the FamilyTree
		on Person object
		
		args:
			member: Person object to be added to the family
		"""
		self.partner=member


	def add_children(self, child):
		"""
		Method to add children of the person called from the FamilyTree
		on Person object
		
		args:
			child: Person object to be added to the family
		"""

		self.children.append(child)


	def get_children(self):
		"""
		Method to get all children of the person called from the FamilyTree
		on Person object
		
		returns:
			child: List of Children names
		"""
		child=[c.name for c in self.children]
		return child

	
	def get_partner(self):
		"""
		Method to get partner of the person called from the FamilyTree
		on Person object
		
		returns:
			Partners name of a person

		"""

		return self.partner.name if self.partner else None

	
	def get_child(self, gender):
		"""
		Method to get all children of the person of a particular gender
		called from the FamilyTree on Person object.
		Used to get sons and daughters
		
		returns:
			child: List of Children names
		"""
		child=[c.name for c in self.children if c.gender==gender]
		return child


	def get_siblings(self):
		"""
		Method to get all siblings of the person called from the 
		FamilyTree on Person object if the mother exists of the person
		
		returns:
			siblings: List of Sibling objects
		"""

		siblings=[]
		if self.mother:
			siblings=[c for c in self.mother.children if c.name!=self.name]
			return siblings


	def get_partner_siblings(self, gender, name):
		"""
		Method to get all siblings of the person's partner of a particular gender called from the 
		FamilyTree on Person object if the mother of the partner exists for the person
		
		returns:
			partner_siblings: List of Sibling names of the person's partner
		"""
		
		partner_siblings=[c.name for c in self.children if c.gender==gender and c.name!=name]
		return partner_siblings


	def get_parents_cousins(self, gender):
		"""
		Method to get all siblings of the person's parent of a particular gender called from the 
		FamilyTree on Person object if the mother of the parent exists for the person
		
		returns:
			child: List of Sibling names of the person's parents
		"""
		child=[]
		if self.mother:
			child=[c.name for c in self.mother.children if c.gender==gender and c.name!=self.name]
		return child


	def get_in_laws(self, gender):
		"""
		Method to get all in-laws of the person of a particular gender called from the 
		FamilyTree on Person object. It is the basically partner's siblings and self's siblings partners
		
		returns:
			result: List of in laws names of the person
		"""
		result=[]
		if self.partner and self.partner.mother:
			result = self.partner.mother.get_partner_siblings(gender, self.partner.name)
		
		self_siblings=self.get_siblings()
		
		if self_siblings:
			siblings_partners=[sibling.get_partner() for sibling in self_siblings if sibling.get_partner()]		
			result.extend(siblings_partners)

		return result