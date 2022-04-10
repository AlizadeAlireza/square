class Square():
    def __init__(self, side):
        self.side = side
        assert side > 0 #for better option choice
    def perimeter(self):
        return self.side * 4
    def area(self):
        return self.side ** 2
    def show(self):
        print("your square side is",self.side)
        print("The perimeter of this square with",self.side,"side size will be", obj.perimeter())
        print("The area of this square with",self.side,"side size will be", obj.area())
    def change_your_side(self):
        self.side = eval(input("Enter your number for changing square side size:\n "))
    def menu(self):
        print("0, Exit")
        print("1, Perimeter")
        print("2, Area")
        print("3, Show")
        print("4, change your side size")
side = eval(input("please enter your side size: "))        
obj = Square(side)

#make a cycle for our loop
choice = 1

while choice != 0:
    assert 5>choice>-1
    obj.menu()
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("it is your square perimeter: \n", obj.perimeter())
    elif choice == 2:
        print("it is your square area: \n",obj.area())
    elif choice == 3:
        obj.show()
    elif choice == 4:
        print("Enter your number for changing your side size: \n", obj.change_your_side())
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("****invalid choice****")
print()

