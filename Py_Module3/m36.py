student = {
  'name': 'Dev',
  'class': 'VI',
  'roll_id': '1'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Dev'})
print(student.keys() >= {'roll_id', 'name'})