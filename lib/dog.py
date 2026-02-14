# Tasks
# Updating the age property to use decorator
# Adding a new instance property called vets
# Updating checkups to be a list of dictionaries
# Developing new methods to add a new checkup and find a checkup

class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.vets = []
    self.checkups = []

  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      raise ValueError("Not a valid age")
    
  def add_checkup(self, vet, date, notes):
    if vet not in self.vets:
      self.vets.append(vet)
    new_checkup = {
      "vet": vet,
      "date": date,
      "notes": notes
    }
    self.checkups.append(new_checkup)
  
  def find_checkup(self, date):
    for checkup in self.checkups:
      if checkup["date"] == date:
        print(f"Checkup on {date} by {checkup['vet']}: {checkup['notes']}")
        return
    print(f"No check up found on {date}")
    
fido = Dog(
  name = "Fido",
  age = 3,
  breed = "Golden Retriever"
)

fido.add_checkup("DooLittle", "02/20/22", "Good Health")
fido.add_checkup("Dr. Ryan", "03/20/23", "Good Health")
fido.find_checkup("02/20/22")
fido.find_checkup("04/20/22")