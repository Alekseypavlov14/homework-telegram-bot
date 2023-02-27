from utils.generate_id import generate_id

class Task: 
  id: int
  name: str
  deadline: int
  done: bool
  course_id: int
  user_id: int

  def __init__(self, name: str, course_id: int, deadline: int, user_id: int):
    self.id = generate_id()
    self.done = False
    self.name = name
    self.course_id = course_id
    self.deadline = deadline
    self.user_id = user_id
