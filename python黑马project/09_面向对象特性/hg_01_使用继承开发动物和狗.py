class Animal:
    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def run(self):
        print("run")

    def drink(self):
        print("drink")


class Dog(Animal):
    def shark(self):
        print("shark")


dog = Dog()
dog.drink()
dog.eat()
dog.run()
dog.sleep()
dog.shark()
