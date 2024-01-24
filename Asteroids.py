import random
class asteroid :
    def __init__(self ,x , y , m=1 , hp=1  ) :
        self.m = int(random.randint(-10 , 10))
        self.x  = x
        self.y = y
        self.rand_dir =random.choice(["right" , "left"])

        self.rand_x = random.randint(5 , 10)
    def move(self ):
        #applying the changes of y
        self.y += self.m
        if self.x <= 0 :
            self.rand_dir = "right"
            
        elif self.x >= 500 :
            self.rand_dir="left"
           
        if self.y >= 500 :
            self.y = 500
            self.m = self.m - 2*(self.m)
        elif self.y <= 0 :
            self.y = 0 
            self.m = self.m - 2*(self.m)
        
        #m decr
        if self.m > 0 :
            self.m -=0.04
        elif self.m <0 :
            self.m +=0.04
        
        #rand_x decr
        if self.rand_x >0 :
            self.rand_x -=0.04
