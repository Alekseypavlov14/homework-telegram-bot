from entities.user import User

class Store:
  users: list[User]

  def __init__(self):
    self.users = []
  
  def add_user(self, user: User):
    self.users.append(user)
    return user
  
  def find_user_by_id(self, user_id: int):
    for user in self.users:
      if user.id == user_id:
        return user
  
  def delete_user_by_id(self, user_id: int):
    user = self.find_user(user_id)
    if not(user): return

    self.users.remove(user)

  def clear(self):
    self.users.clear()

store = Store()