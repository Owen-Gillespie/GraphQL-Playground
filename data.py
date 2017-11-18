class_data = {}

def setup():
	from schema import SchoolClass, CourseCode, DayOfWeek, CourseStatus, School

	global class_data
	stems = SchoolClass(
		id = "1",
		name = "Systems and signals and shit",
		days = [DayOfWeek.MONDAY, DayOfWeek.WEDNESDAY, DayOfWeek.THURSDAY],
		start_date = None,
		end_date = None,
		start_time = None,
		end_time = None,
		credits = 3,
		professors = ["Lape"],
		open_seats = 0,
		total_seats = 100,
		course_status = CourseStatus.CLOSED)
	#	code = CourseCode(department = "ENGR", number = "79", suffix = "",
	#		          school = School.MUDD, section = 1))
	class_data = { "1": stems}

def get_class(id):
	print("recieved at resolver call with id:", id)
	print(class_data.get(id))
	return class_data.get(id)
setup()
