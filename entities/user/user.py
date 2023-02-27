from entities.course import Course

class User:
  id: int
  name: str
  courses: list[Course]

  def __init__(self, name: str, id: int):
    self.id = id
    self.name = name
    self.courses = []

  def add_course(self, course: Course):
    self.courses.append(course)