class Sphere:
    def __init__(self, sphere_id, radius=1, color="White"):
        self.sphere_id = sphere_id
        self.radius = radius
        self.color = color
        self.volume = self.calculate_volume()

    def calculate_volume(self):
        return 4/3 * 3.1416 * (self.radius ** 3)

    def printDetails(self):
        print(f"Sphere ID: {self.sphere_id}")
        print(f"Color: {self.color}")
        print(f"Volume: {self.volumef}")

    def merge_sphere(self, *spheres):
        print("Spheres are being merged")
        total_volume = self.volume
        mixed_color = False
        
        for sphere in spheres:
            total_volume += sphere.volume
            if sphere.color != self.color:
                mixed_color = True
        
        if mixed_color:
            self.color = "Mixed Color"
        
        self.radius = ((3 * total_volume) / (4 * 3.1416)) ** (1/3)
        self.volume = total_volume

# Driver Code
sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")

sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")

sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")

sphere3.merge_sphere(sphere1, sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")

sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()
