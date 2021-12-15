#познакомилась с модулем pyyaml
import yaml

with open('E:/devops/задания для лекций/python/data.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
    print(info)

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('E:/devops/задания для лекций/python/users.yml', 'w') as f:
    data = yaml.dump(users, f)