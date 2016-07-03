# -*- coding: utf-8 -*-
class Dog:
    def __init__(self, name='Joe'):
        self.name = name

    def bark(self):
        print('{} barks Ruff Ruff!'.format(self.name))


if __name__ == '__main__':
    # 세 개의 인스턴스 생성
    # 가변인자로 디폴트
    sam = Dog('Sam')
    ruby = Dog('Ruby')
    dog = Dog()

    print(sam)
    print(ruby)
    print(dog)

    sam.bark()
    ruby.bark()
    dog.bark()
