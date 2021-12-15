#познакомилась с модулем os.path
import os

out = os.path.basename("E:/devops/задания для лекций/python/data.yml")
print(out)

out1 = os.path.isabs("/задания для лекций/python/data.yml")
print(out1)

out = os.path.isfile("E:/devops/tasks/python/data.yml")
print(out)
