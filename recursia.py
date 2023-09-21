# tree = {
#     1: {
#         1:{
#             1: 'text',
#             2: 'text2',
#             3: 'text3'
#             }
        
#     },

#     2: {
#         1:{
#             1: 'chto',
#             2: 'eto',
#             3: 'target_folder'
#         }
#     }
# }

# def rec_find(tree: dict, name: str):
#     for key, value in tree.items():
#         if key == 2:
#             print(key, value)

# rec_find(tree, 'target_function')


# ПЕРВЫЙ КЛАСС
class Bird:
    def __init__(
        self,
        wings_lenght: float = 12.5,
        legs_lenght: float = 3.5,
        color: str = 'red'
    ):
        self.wings_lenght = wings_lenght
        self.legs_lenght = legs_lenght
        self.color = color
        print('Bird Initialized')
    
    def fly(self):
        print('i fly')
    def swim(self):
        print('i swim')
    def walk(self):
        print('i walk')
    def make_noise(self):
        print('i make noise')

# ВТОРОЙ КЛАСС
class RubberToy:
    toxic: bool = False
    size_cm3: float = 12
    color: str = 'yellow'

    def bounce(self):
        print('plums')
    def deforms(self):
        print('morphing time')
    def make_noise(self):
        print('peep')


# ОБЪЕДИНЕНИЕ КЛАССОВ В ОДИН
class RubberBird(RubberToy, Bird):
    pass


# ТЕПЕРЬ ОБЪЕКТ ВМЕЩАЕТ В СЕБЯ ЗНАЧЕНИЯ НЕСКОЛЬКИХ КЛАССОВ
rub_bird = RubberBird()

rub_bird.walk()