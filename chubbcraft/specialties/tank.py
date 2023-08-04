from src.character import Character

class Tank(Character):

    def __init__(self, race):
        Character.__init__(self,race)
        self.defence+=2
        self.health*=1.5

    def get_attributes(self):
        return f"""The {str(self.race)} is a tank  
    with /n health:{self.health}/n attack damage:{self.attack_dmg}
    /n magic damage:{self.magic_dmg}/n defence:{self.defence}"""