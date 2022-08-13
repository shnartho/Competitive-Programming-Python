class Dog:
    """Represnting a dog"""
    def __init__(self, _name, _age, _color):
        self.name = _name
        self.age = _age
        self.color = _color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def bark(self):
        print('Hulf, huff..')

    def __str__(self):
        return f"My dog name is {self.name}"

tommy = Dog('Tommy', 2, 'Brown')
tommy.bark()
print(tommy.age)
print(tommy)





