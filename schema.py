import graphene
from data import get_class
from graphene.types import datetime
class DayOfWeek(graphene.Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

class School(graphene.Enum):
	MUDD = 1
	SCRIPPS = 2
	CMC = 3
	POMONA = 4
	PITZER = 5
	KGI = 6
	CGU = 7
	KECK = 8

class CourseStatus(graphene.Enum):
	OPEN = 1
	CLOSED = 2
	REOPENED = 3

	# Going to need more of these

class Professor(graphene.ObjectType):
	id = graphene.ID()
	name = graphene.String()

class CourseCode(graphene.ObjectType):
	department = graphene.String()
	# Could number be stored as an int?
	number = graphene.String() 
	suffix = graphene.String() 
	school = School()
	section = graphene.Int()
	
	def resolve_course_code(self, info):
		return "{}-{}{}-{} {}".format(self.department, self.number, self.suffix,
					      self.section, self.school)

class SchoolClass(graphene.ObjectType):
	id = graphene.ID()
	name = graphene.String()
	days = graphene.List(DayOfWeek)
	start_time = graphene.types.datetime.Time()
	end_time= graphene.types.datetime.Time()
	start_date = graphene.types.datetime.Date()
	end_date = graphene.types.datetime.Date()
	credits = graphene.Float()
	professors = graphene.List(Professor)
	open_seats = graphene.Int()
	total_seats = graphene.Int()
	course_status = CourseStatus()
	# code = CourseCode()	

class Query(graphene.ObjectType):
	classname = graphene.Field(SchoolClass, id = graphene.String())

	def resolve_classname(self, info, id):
		print("at resolver")
		return get_class(id)

schema = graphene.Schema(query=Query)
# Test query
result = schema.execute('{classname(id: "1") { name }}')
print(result.data['classname'])
