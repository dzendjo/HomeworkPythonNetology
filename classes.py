class AliveCreature:

    def born(self):
        print('{} was born'.format(self.__class__.__name__))

    def eat(self):
        print('{} am-am-am'.format(self.__class__.__name__))

    def dead(self):
        print('{} is dead'.format(self.__class__.__name__))

    def voice(self):
        pass


class Animal(AliveCreature):
    def __init__(self, name=''):
        self.name = name

    def walk(self):
        print('{} is walking'.format(self.__class__.__name__))


class Bird(AliveCreature):
    def __init__(self, name=''):
        self.name = name

    def fly(self):
        print('{} is flying'.format(self.__class__.__name__))


class Cow(Animal):

    def voice(self):
        print('Muuuuuuuuu')
        if self.name != '':
            print('Я корова  {}'.format(self.name))


class Pig(Animal):

    def voice(self):
        print('Hru-Hruuuuu')


class Goat(Animal):

    def voice(self):
        print('Beeeeeee lile goat')


class Sheep(Animal):

    def voice(self):
        print('Be-be like sheep!')


class Duck(Bird):

    def voice(self):
        print('Ga-ga-ga like duck')


class Chicken(Bird):

    def voice(self):
        print('Co-co-co')


class Goose(Bird):

    def voice(self):
        print('Ga-ga-ga like goose')
        if self.name != '':
            print('Я гусь  {}'.format(self.name))


cow1 = Cow('Мурка')
cow1.voice()

cow2 = Cow('Зорька')
cow2.voice()

# pig = Pig()
# pig.voice()

# goat = Goat()
# goat.voice()
#
# sheep = Sheep()
# sheep.voice()
#
# duck = Duck()
# duck.voice()
#
# chicken = Chicken()
# chicken.voice()

print('\n')
goose = Goose('Дональд')
goose.born()
goose.eat()
goose.voice()
goose.fly()
goose.dead()
