'''

python开发基础52-面向对象3大特性之多态

'''


class Sheep:

    def sound(self):
        print('咩咩')

class Dog:

    def sound(self):
        print('汪汪')

class Cat:

    def sound(self):
        print('喵喵')

# common interface
def animal_sounds(Animal):
    animal.sound()

if __name__ == '__main__':
    animal = input('你知道那种动物的叫声？请在小羊、狗狗、猫咪中选一：')

    while animal != '小羊' and animal != '狗狗' and animal != '猫咪':
        animal = input('请在小羊、狗狗、猫咪中选一：')

    if animal == '小羊':
        animal = Sheep()
        animal_sounds(Sheep)

    elif animal == '狗狗':
        animal = Dog()
        animal_sounds(Dog)

    elif animal == '猫咪':
        animal = Cat()
        animal_sounds(Cat)


'''
Example Outputs:

你知道那种动物的叫声？请在小羊、狗狗、猫咪中选一：蛇
请在小羊、狗狗、猫咪中选一：虎
请在小羊、狗狗、猫咪中选一：猫咪
喵喵



'''











