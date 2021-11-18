class fraction ():
    def __init__(self,num=0,denum=1):
        self.numerator=num
        self.denumerator=denum

    def __add__(self ,other):
        if self.denumerator == other.denumerator:
           return (self.numerator +other.numerator ,self.denumerator)
        else:
            return("Error!")

    def __sub__(self ,other):
        if self.denumerator == other.denumerator:
           return (self.numerator -other.numerator ,self.denumerator)
        else:
            return ("Error!")
    
    def __mul__(self , other):
        return(self.numerator * other.numerator ,self.denumerator * other.denumerator)
    
    def __truediv__(self , other):
        return(self.numerator * other.denumerator ,self.denumerator * other.numerator)


frct1=fraction(2,5)

frct2=fraction(6,9)

k3=fraction(5,7)

print("+++ Add +++")
print(frct1+frct2)
print(frct1+frct2)
#-------------------
print("--- subtract ---")
print(frct1-frct2)
print(frct1-k3)
#-------------------
print("*** multiply ***")
print(frct1*frct2)
#-------------------
print("/// divide ///")
print(frct1/frct2)
