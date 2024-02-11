

class Rectangle:
    def __init__(self, height:int, width:int):
        self.height = height
        self.width = width
    def perimeter(self):
        return 2 * (self.height + self.width)
    def area (self):
        return self.height * self.width

    def draw_box(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

def main():
    print('Rectangle Calculator')
    print()
    
    cont = 'y'
    while cont.lower()== 'y':
        height = int(input(f"{'Height:':15} "))
        width = int(input(f"{'Width:':15} "))
        rect = Rectangle(height,width)
        print(f"{'Perimeter:':15} {rect.perimeter():.0f}")
        print(f"{'Area:':15} {rect.area():.0f} ")
        rect.draw_box()
        
        cont = input('Continue ? (y/n): ').lower()
        
main()


        
    
