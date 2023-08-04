from src.character import Character

class Warrior(Character):

    def __init__(self, race):
        Character.__init__(self,race)
        self.attack_dmg*=1.2

    def get_attributes(self):
        return f"""The {str(self.race)} is a warrior  
    with /n health:{self.health}/n attack damage:{self.attack_dmg}
    /n magic damage:{self.magic_dmg}/n defence:{self.defence}"""