#!/usr/bin/env python3


class Intern:
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == "__main__":
    you = Intern()
    mark = Intern("Mark")
    print(you)
    print(mark)
    print(mark.make_coffee())
    try:
        you.work()
    except Exception as e:
        print(e)
