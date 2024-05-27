#!/usr/bin/env python3

class Animal:
    
    def __init__(self):
        pass

    def emitir_som():
        pass

    def mover():
        pass


class Dog(Animal):

    def emitir_som(self):
        print("Dog: Woof!")

    def mover(self):
        print("Dog: Movendo - se")
    
class Cat(Animal):

    def emitir_som(self):
        print("Cat: Miau!")

    def mover(self):
        print("Cat: movendo- se")





#main

dog1 = Dog()
dog1.emitir_som()
dog1.mover()

cat1 = Cat()
cat1.emitir_som()
cat1.mover()
        