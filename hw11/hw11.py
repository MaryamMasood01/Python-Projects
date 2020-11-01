# Name: Maryam Masood
# x500: masoo013

# PROBLEM A

# Adventurer class
#==========================================
# Purpose:  represents a jobless character template for all of the job classes to build off of
#
# Input Parameter(s):
# self
# target
# name - a string representing the name of the adventurer
# level - an integer representing the Adventurer’s  level in th egame
# strength - an integer representing the Adventurer’s strength level
# speed - an integer representing the Adventurer’s current speed 
# power - an integer representing the Adventurer’s current power
#
# Return Value(s):
# __repr__(self) - a string stating the Adventurer's name and current HP value
#==========================================


class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = str(name)
        self.level = int(level)
        self.strength = int(strength)
        self.speed = int(speed)
        self.power = int(power)
        self.HP = int(level) * 6
        self.hidden = False

    def __repr__(self):
        return str(self.name) + ' - HP: ' + str(self.HP)

# attack(self,target)
#==========================================
# Purpose: runs an attack on the target based on a variety of current circumstances of the adventurer and the target
#
# Input Parameter(s):
# self
# target
#
# Return Value(s): None
#==========================================

    def attack(self,target):
        if target.hidden == False:
            target.HP = target.HP - (self.strength + 4)
            print(str(self.name) + " attacks " + str(target.name) + " for " + str(self.strength + 4) + ' damage')
            
        else:
            print(str(self.name) + " can't see " + str(target.name))


    def __lt__(self, other):
        if self.HP < other.HP:
            return True
        else:
            return False   

# Fighter class
#==========================================
# Purpose:  represents a fighter character that inherits from the Adventurer class
#
# Input Parameter(s):
# self
# target
# name - a string representing the name of the adventurer
# level - an integer representing the Adventurer’s  level in th egame
# strength - an integer representing the Adventurer’s strength level
# speed - an integer representing the Adventurer’s current speed 
# power - an integer representing the Adventurer’s current power
#
# Return Value(s): None
#==========================================


class Fighter(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = int(level) * 12

# attack(self,target)
#==========================================
# Purpose: runs an attack on the target based on a variety of current circumstances of the adventurer and the target
#
# Input Parameter(s):
# self
# target
#
# Return Value(s): None
#==========================================

    def attack(self,target):
        if target.hidden == False:
            target.HP = target.HP - ((2 * self.strength) + 6)
            print(str(self.name) + " attacks " + str(target.name) + " for " + str((2 * self.strength) + 6) + ' damage')
            
        else:
            print(str(self.name) + " can't see " + str(target.name))

# Thief class
#==========================================
# Purpose:  represents a theif character that inherits from the Adventurer class
#
# Input Parameter(s):
# self
# target
# name - a string representing the name of the adventurer
# level - an integer representing the Adventurer’s  level in th egame
# strength - an integer representing the Adventurer’s strength level
# speed - an integer representing the Adventurer’s current speed 
# power - an integer representing the Adventurer’s current power
#
# Return Value(s): None
#==========================================


class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = int(level) * 8
        self.hidden = True

# attack(self,target)
#==========================================
# Purpose: runs an attack on the target based on a variety of current circumstances of the adventurer and the target
#
# Input Parameter(s):
# self
# target
#
# Return Value(s): None
#==========================================

    def attack(self,target):
        if self.hidden == False:
            super().attack(target)
            
        elif (self.hidden == True and target.hidden == True) and (self.speed < target.speed):
            print(str(self.name) + " can't see " + str(target.name))
        
        else:
            target.hidden = False
            self.hidden = False
            target.HP = target.HP - ((self.speed + self.level) * 5)
            print(str(self.name) + " sneak attacks " + str(target.name) + " for " + str((self.speed + self.level) * 5) + ' damage')


# Wizard class
#==========================================
# Purpose:  represents a wizard character that inherits from the Adventurer class
#
# Input Parameter(s):
# self
# target
# name - a string representing the name of the adventurer
# level - an integer representing the Adventurer’s  level in th egame
# strength - an integer representing the Adventurer’s strength level
# speed - an integer representing the Adventurer’s current speed 
# power - an integer representing the Adventurer’s current power
#
# Return Value(s): None
#==========================================


class Wizard(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = power

# attack(self,target)
#==========================================
# Purpose: runs an attack on the target based on a variety of current circumstances of the adventurer and the target
#
# Input Parameter(s):
# self
# target
#
# Return Value(s): None
#==========================================

    def attack(self,target):
        if self.fireballs_left == 0:
            super().attack(target)

        else:
            target.hidden = False
            self.fireballs_left = self.fireballs_left - 1
            target.HP = target.HP - (self.level * 3)
            print(str(self.name) + " casts fireball on " + str(target.name) + " for " + str(self.level * 3) + ' damage')
            

# duel(adv1, adv2)
#==========================================
# Purpose: takes two Adventurer objects, adv1 and adv2, tests who would win in a one-on-one fight
#
# Input Parameter(s):
# adv1 - an Adventurer object
# adv2 - an Adventurer object
#
# Return Value(s):
# True if adv1 wins
# False if adv2 wins or if everyone loses
#==========================================

def duel(adv1, adv2):
    while adv1.HP > 0 and adv2.HP > 0:
        print(repr(adv1))
        print(repr(adv2))
        adv1.attack(adv2)
        if adv2.HP > 0:
            adv2.attack(adv1)

    print(repr(adv1))
    print(repr(adv2))

    if adv1.HP <= 0 and adv2.HP <= 0:
        print("Everyone loses!")
        return False
    elif adv2.HP <= 0:
        print(str(adv1.name + " wins!"))
        return True
    else:
        print(str(adv2.name) + " wins!")
        return False

    
# PROBLEM B

# tournament(adv_list)
#==========================================
# Purpose: pits a group of Adventurers against each other until there is a single winner 
#
# Input Parameter(s):
# adv_list - a list of Adventurer objects
#
# Return Value(s): The final Adventurer obeject (the winner)
#==========================================

def tournament(adv_list):
    final_list = sorted(list(adv_list))
    if adv_list == []:
        return None
    elif len(adv_list) == 1:
        return adv_list[0]
    else:
        while len(final_list) != 1:
            z = len(final_list)
            list.sort(final_list)
            y = duel(final_list[z-2], final_list[z-1])
            if y == True:
                final_list.pop(z-1)
            else:
                final_list.pop(z-2)
        return final_list[0]

 
