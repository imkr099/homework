class Human:
    head=1
    def __init__(self,*name,age=True):
        self.name=name
        self.age=age

    def fly(self):
        print(f'{self} fly')

h1=Human('Bakai','Kudret','Talgar','Barsbek','Sultan','Ivan','Osman',
         'Davlet','SultanN','islambek','Arafat','Medet')

h1.fly()
print()
