# Slope-intercept worksheet solutions
# GWC SIP 2016
# AOL DC

class SlopeInterceptLine():
    def __init__(self, m=0, b=0):
        self.m = m
        self.b = b
    
    def getSlope(self):
        return self.m
    
    def getYInt(self):
        return self.b
    
    def setSlope(self, new_slope):
        self.m = new_slope
        
    def setYInt(self, new_y_int):
        self.b = new_y_int
        
    def isOnLine(self, x, y):
        slope_eq = self.m * x + self.b
        if(y == slope_eq):
            return True
        else:
            return False

line1 = SlopeInterceptLine()

line2 = SlopeInterceptLine(3, -2.5)

#A
print(line1.getSlope())

#B
print(line2.getYInt())

#C
line1.setSlope(-3.5)
line2.setSlope(2/3)

#D
print(line1.getSlope())
print(line1.getYInt())

#E
print(line2.isOnLine(6, 17.5))


