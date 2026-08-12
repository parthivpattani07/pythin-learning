class Planet:
    def __init__ (self,name,planet_type,star):
        
        self.name=name
        self.planet_type=planet_type
        self.star=star
    
        if not isinstance(self.name,str) or not isinstance(self.planet_type,str) or not isinstance(self.star,str):
            raise TypeError('name, planet type, and star must be strings')
        if name=="" or planet_type=="" or star=="":
            raise ValueError('name, planet_type, and star must be non-empty strings')
    
    def orbit(self):
        return (f"{self.name} is orbiting around {self.star}...")
    def __str__(self):
        return (f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}")

planet_1=Planet('Earth','Blue','Sun')
planet_2=Planet("Mars","Red","Sun")
planet_3=Planet("Buster","Cool","Star")
"""
input:
print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

output:
Planet: Earth | Type: Blue | Star: Sun
Planet: Mars | Type: Red | Star: Sun
Planet: Buster | Type: Cool | Star: Star
Earth is orbiting around Sun...
Mars is orbiting around Sun...
Buster is orbiting around Star...
"""
