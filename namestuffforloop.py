class Person(object):
	def __init__(self):
		print("hi")
	def full_name(self):
		return self.fn + ' ' +self.ln

persons = []

persons.append(Persons('f2','l1'))

persons.append(Person('f2','l2'))

for person in persons:
	print(person.fn)
