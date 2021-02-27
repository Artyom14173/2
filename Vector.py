import math
import random

class Vector(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def lengthVector(self):
		return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

	def scalarVector(self, vector):
		return self.x * vector.x + self.y * vector.y + self.z * vector.z

	def crossVector(self, vector):
		return (
			self.y * vector.z - self.z * vector.y, 
			self.z * vector.x - self.x * vector.z,
			self.x * vector.y -self.y * vector.x
			)

	def cosVector(self, vector):
		return self.scalarVector(vec) / (self.lengthVector() * math.sqrt(vector.x * vector.x + vector.y * vector.y + vector.z * vector.z))

	def addVector(self, vector):
		return (
			self.x + vector.x, 
			self.y + vector.y, 
			self.z + vector.z
			)

	def subtractVector(self, vector):
		return (
			self.x - vector.x, 
			self.y - vector.y, 
			self.z - vector.z
			)

	# def generatorVector(count):
	# 	massive = []
	# 	for i in range(count):
	# 		x = random.uniform(-100,100)
	# 		y = random.uniform(-100,100)
	# 		z = random.uniform(-100,100)
	# 		massive.append([x, y, z])
	# 	return massive
	# print(generatorVector(5))

x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
z1 = int(input('Введите z1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
z2 = int(input('Введите z2: '))

v = Vector(x1, y1, z1)
vec = Vector(x2, y2, z2)

print('===============================')
print('Скалярное произведение: ', v.scalarVector(vec))
print('Векторное произведение с другим вектором: ', v.crossVector(vec))
print('Угол между векторами (или косинус угла): ', v.cosVector(vec))
print('Сумма векторов: ', v.addVector(vec))
print('Разность векторов: ', v.subtractVector(vec))
