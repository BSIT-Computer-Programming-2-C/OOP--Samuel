class Hero:
    def hero(self):
     intelligence = 0
     strength = 0
     agility = 0

class MarksMan(Hero):
    def marksman(self):
     print("intelligence = 10\nstrength = 20\nagility = 100\n")
    def Miya(self):
     print("Marksman: Miya")

class Tank(Hero):
    def tank(self):
     print("intelligence = 20\nstrength = 10\nagility = 80")
    def Tigreal(self):
     print("Tank: Tigreal")
    def firstSkill(self):
     print('First skill: Attack Wave')
    def secondSkill(self):
     print("Second skill: Sacred Hammer")
    def lastSkill(self):
     print("Last Skill: Implosion\n")
    

tanks = Tank()  
tanks.Tigreal()
tanks.tank()
tanks.firstSkill()
tanks.secondSkill()
tanks.lastSkill()

marks = MarksMan()
marks.Miya()
marks.marksman()













