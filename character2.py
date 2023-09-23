class Character:
    def __init__(
        self,
        name
    ):
        self.name = name



##### ПЕРСОНАЖИ
class Hagrid(Character):
    def say_name(self):
        print(self.name)

class Harry_Potter(Character):
    def say_name(self):
        print(self.name)

class Shrek(Character):
    def say_name(self):
        print(self.name)
        




###### ДЛЯ ФАНКО ПОПА
class MixinFallable:
    def fall(self):
        print('я падаю')

class MixinDust:
    def collect_dust(self):
        print('я собираю пыль')

class MixinFunkoPop(MixinDust, MixinFallable):
    pass





######### ДЛЯ ПЛЭЙИБЛ
class MixinJumpable:
    def jump(self):
        print('я прыгаю')

class MixinTalkable:
    def talk(self):
        print('я говорю')

class MixinPlayable(MixinJumpable, MixinTalkable):
    pass






#### НАСЛЕДОВАНИЕ ПЛЕЙИЛ И ФАНКО

class HagridFunko(Character, MixinFunkoPop):
    def character_type(self):
        print('funko')
        print(self.name)

class HarryFunko(Character, MixinFunkoPop):
    def character_type(self):
        print('funko')
        print(self.name)

class ShrekFunko(Character, MixinFunkoPop):
    def character_type(self):
        print('funko')
        print(self.name)
        







class HagridPlayable(Character, MixinPlayable):
    def character_type(self):
        print(self.name)
        print('playable')

class HarryPlayable(Character, MixinPlayable):
    def character_type(self):
        print(self.name)
        print('playable')

class ShrekPlayable(Character, MixinPlayable):
    def character_type(self):
        print(self.name)
        print('playable')






SH = ShrekPlayable('Shrek')
SH.character_type()
SH.jump()
SH.talk()
print()
SHF = ShrekFunko('Shrek_Funko')
SHF.character_type()
SHF.collect_dust()
SHF.fall()
print()
HAG = HagridPlayable('Hagrid')
HAG.character_type()
HAG.jump()
HAG.talk()
print()
HAGF = HagridFunko('Hagrid_Funko')
HAGF.character_type()
HAGF.collect_dust()
HAGF.fall()
print()
HAR = HarryPlayable('Harry_Potter')
HAR.character_type()
HAR.jump()
HAR.talk()
print()
HARF = HarryFunko('Harry_Potter_Funko')
HARF.character_type()
HARF.collect_dust()
HARF.fall()