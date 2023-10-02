class Triangle:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
    
    def check_triangle(self):
        if self.first + self.second < self.third or self.first + self.third < self.second or self.third +self.second < self.first:
            return f'Треугольника не существует'
        elif self.first == self.second == self.third:
            print('Треугольник равносторонний')
        elif self.first != self.second  and self.first != self.third and self.second != self.third :
            return f'Треугольник разносторонний'
        else:
            return f'Треугольник равнобедренный'

one = Triangle(10, 5 , 7)
print(one.check_triangle())