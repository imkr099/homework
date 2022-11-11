class Hero:
    Head = 1
    ability = True
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self, h=100):
         print(self.hp+h)
    def two_damage(self, td=2):
        print(self.damage*td)
    def greetings(self):
        print('my name is '+ self.name)
    def brand_phrase(self):
        print('good will win')

class Air(Hero):
    Speed = 300
    def __init__(self,name, nickname, hp, damage, fly = False):
        super(Air, self).__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        print('fly in the True_phrase')
        self.fly = True
        __Gen_x = None
class Fire(Hero):
    power = 100
    def __init__(self, name, nickname, hp, damage, fly = False):
        super(Fire, self).__init__(name, nickname, hp, damage)
        self.fly = fly
    def heal(self):
        self.fly = True
        __Gen_x = None
class Magic(Hero):
    mythic = 200
    def __init__(self, name, nickname, hp, damage, fly = False):
        super(Magic, self).__init__(name, nickname, hp, damage)
        self.fly = fly
    def two_damage(self):
        self.fly = True
        __Gen_x = None

p1 = Air(name='Sultan', nickname='SultanChay', hp=77, damage=30)
p2 = Fire(name='Nurlan', nickname='NurlanS', hp=100, damage=40)
p3 = Magic(name='Jack', nickname='Vorobey', hp=111, damage=70)

print(p1.name, p1.nickname, p1.hp, p1.damage)
print(p2.name, p2.nickname, p2.hp, p2.damage)
print(p3.name, p3.nickname, p3.hp, p3.damage)
p1.brand_phrase()
p2.two_damage()
p3.heal()
