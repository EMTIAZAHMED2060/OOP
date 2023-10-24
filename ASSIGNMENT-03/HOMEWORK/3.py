class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> created.')

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        new_x = self.y * other.z - self.z * other.y
        new_y = self.z * other.x - self.x * other.z
        new_z = self.x * other.y - self.y * other.x
        return Vector3D(new_x, new_y, new_z)

# Create two Vector3D objects
V1 = Vector3D(2, -3, 1)
V2 = Vector3D(-1, 4, 0)

# Calculate and print magnitudes
magnitude1 = V1.magnitude()
magnitude2 = V2.magnitude()
print(f'Magnitude of the first vector = {magnitude1}')
print(f'Magnitude of the second vector = {magnitude2}')

# Calculate and print the dot product
dot_product = V1.dot_product(V2)
print(f'Dot product of the two vectors = {dot_product}')

# Calculate and print the cross product
cross_product = V1.cross_product(V2)
print(f'Cross product of the two vectors = <{cross_product.x}, {cross_product.y}, {cross_product.z}>')
