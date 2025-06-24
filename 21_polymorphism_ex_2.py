class Device:
    def run(self):
        return print('Generic device...')
class Laptop(Device):
    def run(self):
        return print(' and also laptop!')
class Smartphone(Device):
    def run(self):
        return print(' and also smartphone!')
for each in [Device(), Laptop(), Smartphone()]:
    each.run()

#

class Animal:
    def sound(self):
        return print('Animal\'s sound like this...')
class Dog(Animal):
    def sound(self):
        return print(' Bark!')
class Cat(Animal):
    def sound(self):
        return print(' Meow!')
class Snake(Animal):
    def sound(self):
        return print(' Fssh!')
for each in [Animal(), Dog(), Cat(), Snake()]:
    each.sound()

#

class Transport:
    def move(self):
        return print('Transport moves like...')
class Bike(Transport):
    def move(self):
        return print(' a bike!')
class Car(Transport):
    def move(self):
        return print(' a car!')
class Train(Transport):
    def move(self):
        return print(' a train!')
transport_instances = Bike(), Car(), Train()
def start_tip(transport):
    return transport.move()
for each in transport_instances:
    start_tip(each)

#

class Sender:
    def send(self):
        return print('Messages can be...')
class EmailSender(Sender):
    def send(self):
        return print(' an email!')
class SMSSender(Sender):
    def send(self):
        return print(' an SMS!')
class PushSender(Sender):
    def send(self):
        return print(' an push!')
for each in [Sender(), EmailSender(), SMSSender(), PushSender()]:
    each.send()

#

class SupportBot:
    def respond(self, message):
        return print(message)
class SalesBot:
    def respond(self, message):
        return print(message)
class FeedbackBot:
    def respond(self, message):
        return print(message)
def chat(bot, message):
    return bot.respond(message)
chat(SalesBot(), 'It\'s a Salesbot!')

#1

class PDFReport:
    def generate(self, data):
        return print(data)
class HTMLReport:
    def generate(self, data):
        return print(data)
class CSVReport:
    def generate(self, data):
        return print(data)
def run_report(generator, data):
    return generator.generate(data)

#

class EmailNotifier:
    def notify(self, user, message):
        return print(f'{user} have 1 email: {message}')
class SMSNotifier:
    def notify(self, user, message):
        return print(f'{user} have 1 SMS: {message}')
class SlackNotifier:
    def notify(self, user, message):
        return print(f'{user} have 1 Slack: {message}')
def send_notification(notifier, user, message):
    return notifier.notify(user, message)

#

class ZipCompressor:
    def compress(self, file):
        return print(f'This is a Zip file: {file}')
class TarCompressor:
    def compress(self, file):
        return print(f'This is a Tar file: {file}')
class GzCompressor:
    def compress(self, file):
        return print(f'This is a Gz file: {file}')
def backup(compressor, file):
    return compressor.compress(file)

#

class Warrior:
    def attack(self):
        return print('This is Warrior attack!')
    def defend(self):
        return print('This is Warrior defend!')
class Archer:
    def attack(self):
        return print('This is Archer attack!')
    def defend(self):
        return print('This is Archer defend!')
class Mage:
    def attack(self):
        return print('This is Mage attack!')
    def defend(self):
        return print('This is Mage defend!')
def battle(character):
    return character.attack(), character.defend()

#

class ConsoleLogger:
    def log(self, message):
        return print(message)
class FileLogger:
    def log(self, message):
        return print(message)
class CloudLogger:
    def log(self, message):
        return print(message)

class LoggerClient:
    def call(self, var, message):
        return var.log(message)

l = LoggerClient()
l.call(CloudLogger(), 'hello from cloud')

#

class LightOn:
    def execute(self):
        return print('Light on!')
class LightOff:
    def execute(self):
        return print('Light off!')
class FanOn:
    def execute(self):
        return print('Fan on!')
class FanOff:
    def execute(self):
        return print('Fan off!')
commands = [LightOn(), LightOff(), FanOn(), FanOff()]
class RemoteControl:
    def execute(self, var):
        return var.execute()
r = RemoteControl()
for each in commands:
    r.execute(each)

# Decorator + Polymorphism Combined #

class BaseNotifier:
    def send(self, message):
        print(f"BaseNotifier: {message}")

class SMSDecorator:
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        print("SMS: Sending SMS...")
        self.notifier.send(message)

class SlackDecorator:
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        print("Slack: Posting to Slack...")
        self.notifier.send(message)

class EmailDecorator:
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        print("Email: Sending Email...")
        self.notifier.send(message)

notifier = EmailDecorator(SlackDecorator(SMSDecorator(BaseNotifier())))
notifier.send("System is down!")




