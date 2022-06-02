DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run ():
  all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
  all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
  adults = list(filter(lambda worker: worker["age"] > 18, DATA))
  adults_list = list(map(lambda worker: worker["name"], adults))
  old_adults = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

  print("This list is about worker who language is python")
  for worker in all_python_devs:
    print(worker)

  print("This list is about platzi workers")
  for platzi_worker in all_platzi_worker:
    print(platzi_worker)

  print("This list about adults")
  for adult in adults_list:
    print(adult)

  print("This list contains the DATA plus aditional item in diccionary")
  for old_adult in old_adults:
    print(old_adult)
    
  # Challange
  print("This list contains python developer using high order functions")
  python_devs_filter = list(filter(lambda worker: worker["language"] == "python", DATA))
  python_devs_map = list(map(lambda worker: worker["name"], python_devs_filter))
  for python_dev in python_devs_map:
    print(python_dev)

  print("This list contains platzi workers using high order functions")
  platzi_workers_filter = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
  platzi_worker_map = list(map(lambda worker: worker["name"], platzi_workers_filter))
  for platzi_worker in platzi_worker_map:
    print(platzi_worker)

  print("This list contains adults people")
  adult_people = [worker["name"] for worker in DATA if worker["age"] > 18]
  for adult in adult_people:
    print(adult)

  print("This code adds a dictonary to another dictionary")
  old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]
  for old in old_people:
    print(old) 

if __name__ == '__main__':
  run()