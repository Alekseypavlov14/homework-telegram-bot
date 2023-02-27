from store import store

def get_user_courses(user_id: int):
  user = store.find_user_by_id(user_id)
  if not(user): return []
  return user.courses
