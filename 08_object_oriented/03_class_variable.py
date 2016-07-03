# -*- coding: utf-8 -*-
class Dog:
    counter = 0

    def __init__(self, name='Joe'):
        self.name = name
        Dog.counter += 1

    def bark(self):
        print('{} barks Ruff Ruff!'.format(self.name))


if __name__ == '__main__':
    # 인스턴스 생성할 때마다 카운터 증가
    sam = Dog('Sam')
    print(sam)
    print(Dog.counter)

    ruby = Dog('Ruby')
    print(ruby)
    print(Dog.counter)

    dog = Dog()
    print(dog)
    print(Dog.counter)

    sam.bark()
    ruby.bark()
    dog.bark()
