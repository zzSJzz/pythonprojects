#!/usr/bin/env python3

class FormaGeometrica:

    def __init__(self):
        pass

    def area(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = self.area * self.altura
        return self.area
    
    def perimetro(self, lado, num_lados):
        self.lado = lado
        self.num_lados = num_lados
        self.perimetro = lado * num_lados
        return self.perimetro
    

class FormaGeometricaTriangulo(FormaGeometrica):

    def area(self, base, altura):
        super().__init__(base, altura)
        self.area = (base * altura) / 2
        return self.area
    
    def perimetro(self, lado, num_lados):
        super().__init__(lado, num_lados)
        self.num_lados = 3
        self.perimetro = lado * num_lados
        return num_lados
    

class FormaGeometricaQuadrado(FormaGeometrica):
    
    def area(self, lado):
        super().__init__(self, lado)
        self.area = lado * lado
        return self.area
    
    def perimetro(self, lado, num_lados):
        super().__init__(lado, num_lados)
        self.num_lados = 4
        self.perimetro = lado * num_lados
        return num_lados
    
