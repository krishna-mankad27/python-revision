def sprinkle(func):
    def w():
        print("sprinkle")
        func()
    return w
@sprinkle
def ice():
    print("ice cream")

ice()