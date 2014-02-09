'''
Created on Jan 23, 2014

@author: angelo
'''

class Rational(object):
    
    numer = 0;
    denom = 1;
    
    def __init__(self, numer=0, denom=1):
        self.numer = numer
        self.denom = denom

    def sum (self, other): 
        denom = other.denom * self.denom
        numer = self.numer * other.denom + other.numer * self.denom
        return Rational(numer, denom)
         
    def sub(self, other):
        denom = other.denom * self.denom
        numer = self.numer * other.denom - other.numer * self.denom
        return Rational(numer, denom)
    
    def mult(self, other):
        return Rational(other.numer*self.numer, other.denom * self.denom)
    
    def div(self, other):
        return self.mult(Rational(other.denom, other.numer))
        
    def __eq__(self, other):
        if isinstance(other, Rational) :
            return other.denom * self.numer == self.denom *other.numer
        else:
            return False
        
    def __str__(self):
        pass
        