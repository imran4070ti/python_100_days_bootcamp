class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')




# person1 = Person('Imran', 28, 'Male')
# person1.eat()


class Student(Person):
    def __init__(self, name, age, gender, id, dept):
        super().__init__(name, age, gender)
        self.id = id
        self.dept = dept
    
    def eat(self):
        super().eat()
        print('Eating at the canteen.')

    def study(self):
        print(f'{self.name} is studying')


student1 = Student('Imran', 28, 'Male', 112, 'CSE')
student1.sleep()
student1.study()
student1.eat()

