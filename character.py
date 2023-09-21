from random import randint

class Character:

    def __init__(
        self,
        
    ): pass
    
    def hit(self):
        healthpoint = int(input('вижу врага (введите hp enemy): '))
        print('hp врага  = ', healthpoint)
        
        mainstat : int | float = randint(53, 105)
        agility : float | int = mainstat // 10 * 20.4
        force : float | int = mainstat // 10 * 31.2
        intelligent : float | int = mainstat // 10 * 21.8
    
        hitting : int | float = (agility + force + intelligent)*1000
        print('крит по голове =  ', hitting)
        if hitting >= healthpoint:
            print('отлетел в лобби мусор')
        else:
            print('gg go lobby, go one more time')

class PhantomAssasin(Character):
    def iam(self):
        print('my name is Phantom Assasin')
        

class Slark(Character):
    def iam(self):
        print('im Slark')

class Sniper(PhantomAssasin):
    def comment(self):
        print('I am Sniper, died of Phantom Assasin')

class NagaSiren(Slark):
    def comment(self):
        print('I am Naga Siren, died of Slark')

def start_game():
    print('start?')
    otvet = str(input('da net?'))
    if otvet == 'da':
        print('change ur fighter: Phantom Assasin or Slart')
        otvet = str(input('1 / 2?'))
        if otvet == "1":
            PA = PhantomAssasin()
            PA.iam()
            PA.hit()
            SN = Sniper()
            SN.comment()
        if otvet == "2":
            SL = Slark()
            SL.iam()
            print('я рыба и не больше.... на этом все')
    else: pass
        #  see the enemy

start_game()
# PA = PhantomAssasin()
# SL = Slark()
# PA.iam()
# SL.iam()

# PA.hit()
# side = Dire()
# side.side()