class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self,value):
        self._health=0
        if value<0:
            self._health+=0
        if value>100:
            self._health+=100
        if 0<=value<=100:
            self._health+=value

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self,value):
        self._mana=0
        if value>50 :
            self._mana+=50
        if value<0:
            self._mana+=0
        if 0<=value<=50:
            self._mana+=value
    @property
    def level(self):
        return self._level
    def level_up(self):
        
        self._level+=1
        self.health =100
        self.mana=50
        print(f"{self._name} leveled up to {self._level}!")

    def __str__(self):
         return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

"""
input:

thanos= GameCharacter('Thanos') 
print(thanos)  

thanos.health -= 30  
thanos.mana -= 10   
print(thanos) 

thanos.level_up()
print(thanos)   

output:

Name: Thanos
Level: 1
Health: 100
Mana: 50
Name: Thanos
Level: 1
Health: 70
Mana: 40
Thanos leveled up to 2!
Name: Thanos
Level: 2
Health: 100
Mana: 50
"""
