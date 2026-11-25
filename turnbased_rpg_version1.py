import random as rd 

class Charecters ():

    def __init__(self,attack,defence,health,wt):
        self.attack = attack
        self.defence = defence 
        self.health = health
        self.wt  = wt

    

    def null(self):
        pass



class playable(Charecters):


    def __init__(self, attack, defence, health, wt,mcattack,mcportions):
        super().__init__(attack, defence, health, wt)
        self.mcattack = mcattack
        self.mcportions  = mcportions

    def basic_attack(self, target):

        target.health = target.health - self.attack

    def potionuse (self):
        self.health = self.health + self.mcportions

    def take_turn(self, target):
        choice = input("1. Attack | 2. Heal: ")

        if choice == "1":
            self.basic_attack(target)  
        elif choice == "2":
            self.potionuse()          
        else:
            print("Invalid choice, turn skipped!")

    



class npc(Charecters):
    def __init__(self, attack, defence, health, wt,dialogoptions,npcactions):
        super().__init__(attack, defence, health, wt)
        self.dialogoptions = dialogoptions
        self.npcactions = npcactions


class anti(Charecters):

    antiattlist = [20,13,7,3,0,1,6,3]
    enemyheal = [3,2,6,7]
    rc = [1,2]

    def __init__(self, attack, defence, health, wt,antimcattack,antimcportions):
        super().__init__(attack, defence, health, wt)
        self.antimcattack = antimcattack
        self.antimcportions = antimcportions


    def enemyattack(self, target):
        target.defence = target.defence - rd.choice(self.antiattlist)
        if target.defence == 0:
            target.health = target.health - rd.choice(self.antiattlist)

    def enemyautoheal(self):
        self.health = self.health + rd.choice(self.enemyheal)

    def enemyresponse(self,target):
        choiceatt = rd.choice(self.rc)
        if choiceatt == 1 :
            self.enemyattack(target)
        else:
            self.enemyautoheal()






    


Player = playable(64,30,200,50,130,30)
enemy = anti(44,20,700,70,90,45)


print(Player.take_turn(enemy))
print(enemy.enemyresponse(Player))

print(Player.__dict__)
print(enemy.__dict__)
