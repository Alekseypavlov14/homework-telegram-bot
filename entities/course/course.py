from entities.task import Task
from utils.generate_id import generate_id

class Course:
  id: int
  name: str
  tasks: list[Task]
  user_id: int

  def __init__(self, name: str, user_id: int):
    self.id = generate_id()
    self.user_id = user_id
    self.name = name
    self.tasks = []

  def add_task(self, task: Task): 
    self.tasks.append(task)