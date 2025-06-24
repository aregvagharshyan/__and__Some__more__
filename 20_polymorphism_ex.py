class Car:
    def start(self):
        return print('It\'s car!')
class Airplane:
    def start(self):
        return print('It\'s plane!')
def engine_start(vehicle):
    return vehicle.start()
engine_start(Car())
engine_start(Airplane())

#

class English:
    def greet(self):
        return print('English')
class Spanish:
    def greet(self):
        return print('Spanish')
for i in [English(), Spanish()]:
    i.greet()

#

class ImagePost:
    def display(self):
        return print('For image!')
class VideoPost:
    def display(self):
        return print('For video!')
class TextPost:
    def display(self):
        return print('For text!')
tuple_of_classes = ImagePost(), VideoPost(), TextPost()
def show(post):
    return post.display()
for each in tuple_of_classes:
    show(each)

#

class Calculator:
    def add(self, *args):
        return sum(args)
def show_info(var):
    return var.add(5, 7, 8)
print(show_info(Calculator()))

#



