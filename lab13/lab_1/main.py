class Animal:
    def __init__(self, name):
        self.name = name
        print(f'Родилось животное{self.name}!')
    def eat(self):
        print('Намнём')
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def makeNoise(self):
        return f'{self.name} говорит грррр'

class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.__name = name
        self.color = color
        self.weight = weight
        print('Родился кот!')
    def meay(self):
        print('МММММММММЯЯЯЯЯЯЯЯЯЯУ')
    def setName(self, newName):
        self.__name = newName
    def makeNoise(self):
        return f'{self.__name} говорит мяу'

class Dog(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.__name = name
        self.color = color
        self.weight = weight
        print('Родилась собака!')
    def setName(self, newName):
        self.__name = newName
    def makeNoise(self):
        return f'{self.__name} говорит гав!'
    
class StringVar:
    def __init__(self, value):
        self.value = value
    def set(self, newValue):
        self.value = newValue
    def get(self):
        return self.value

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def get(self):
        return (self.x, self.y)
    def setX(self, newX):
        self.x = newX
    def setY(self, newY):
        self.y = newY

# Задание 1
print('----------Задание 1-----------')
little_cat = Cat("Jon", "White", 5)
little_cat.meay()

# Задание 2
print('----------Задание 2-----------')
little_animal = Animal('Biba')
print(little_animal.getName())
little_animal.setName('Boba')
print(little_animal.getName())
little_animal.eat()
little_animal.makeNoise()

# Задание 3
print('----------Задание 3-----------')
little_StringVar = StringVar('Питон')
print(little_StringVar.get())
little_StringVar.set('Питонище')
print(little_StringVar.get())

# Задание 4
print('----------Задание 4-----------')
littlePoint = Point(1,2)
print(littlePoint.get)
littlePoint.setX(5)
littlePoint.setY(7)
print(littlePoint.get)

# Задание 5
print('----------Задание 5-----------')
print(little_cat.makeNoise())

# Задание 6
print('----------Задание 6-----------')
little_dog = Dog('Фитучини','Бежевый',20)
print(little_dog.makeNoise())

# Задание 7
print('----------Задание 7-----------')
someCat = Cat('','Black',7)
someCat.setName('Robert')
someCat.eat()
print(someCat.makeNoise())

someDog = Dog('','Серый', 17)
someDog.setName('Барбариска')
someDog.eat()
print(someDog.makeNoise())

someDog2 = Dog('','Шоколадный', 21)
someDog2.setName('Конфетка')
someDog2.eat()
print(someDog2.makeNoise())

someAnimal = Animal('')
someAnimal.setName('Баран')
someAnimal.eat()
print(someAnimal.makeNoise())




        