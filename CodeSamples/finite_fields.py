#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:20:48 2024

@author: uwejaekel
"""

class FiniteFieldElement:
    def __init__(self, z, p):
        self.p = p
        self.z = z % p
    
    def __str__(self):
        return f"{self.z} mod {self.p}"
    
    def __add__(self, num):
        if self.p != num.p:
            raise TypeError("Cannot add numbers of different fields!")
        #return self.__class__( (self.z + num.z) % self.p , self.p)
        return FiniteFieldElement( (self.z + num.z) % self.p , self.p )
    
n1 = FiniteFieldElement(12, 7)
n2 = FiniteFieldElement(3, 7)

print(n1 + n2)
