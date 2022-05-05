class fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        print('FRUIT',self.name, self.color)

class apple(fruit):
    def __init__(self,name,color,pesticide=False):
        super().__init__(name,color)
        self.pesticide = pesticide

    def __str__(self):
        print('FRUIT',self.name, self.color,self.pesticide)
        super().__str__()

def test():
    helper('',-1)


def helper(prev,prev_i):
    if len(prev) == 3:
        print(prev)
        return
    for i in range(4):
        if prev_i != i:
            helper(prev+str(i),i)

def map_wrap_around():
    x = -1
    x = 6


if __name__ == "__main__":
    #apple = apple("Red Delicious",'red',True)
    #apple.__str__()
    #test()
    map_wrap_around()
