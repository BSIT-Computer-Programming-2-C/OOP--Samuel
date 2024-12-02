class Hero:
    def hero(self):
     intelligence = 0
     strength = 0
     agility = 0

class MarksMan(Hero):
    def marksman(self):
     print("intelligence = 10\nstrength = 20\nagility = 100")
    def Miya(self):
     print("Marksman: Miya")
    def firstSkillMiya(self):
     print("First Skill: Moon Arrow")
    def secondSkillMiya(self):
     print("Second skill: Arrow of Eclipse")
    def lastSkillMiya(self):
     print("Last Skill: Hidden Moonlight\n")
class Tank(Hero):
    def tank(self):
     print("intelligence = 20\nstrength = 100\nagility = 10")
    def Tigreal(self):
     print("Tank: Tigreal")
    def firstSkillTigreal(self):
     print('First skill: Attack Wave')
    def secondSkillTigreal(self):
     print("Second skill: Sacred Hammer")
    def lastSkillTigreal(self):
     print("Last Skill: Implosion\n")
class Jungle(Hero):
    def jungle(self):
     print("intelligence = 50\nstrength = 50\nagility = 60")
    def Alucard(self):
     print("Jungle: Alucard")
    def firstSkillAlucard(self):
     print('First skill: Ground Splitter')
    def secondSkillAlucard(self):
     print("Second skill: Whirling Smash")
    def lastSkillAlucard(self):
     print("Last Skill: Fission Wave\n")
    

tanks = Tank()  
tanks.Tigreal()
tanks.tank()
tanks.firstSkillTigreal()
tanks.secondSkillTigreal()
tanks.lastSkillTigreal()

marks = MarksMan()
marks.Miya()
marks.marksman()
marks.firstSkillMiya()
marks.secondSkillMiya()
marks.lastSkillMiya()

jung = Jungle()
jung.Alucard()
jung.jungle()
jung.firstSkillAlucard()
jung.secondSkillAlucard()
jung.lastSkillAlucard()












