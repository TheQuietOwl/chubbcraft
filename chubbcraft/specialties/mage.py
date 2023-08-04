from chubbcraft.character import Character

class Mage(Character):

    def __init__(self, race):
        Character.__init__(self,race)
        self.magic_dmg*=2

    def get_attributes(self):
        return f"""The {str(self.race)} is a mage 
    with \n health:{self.health}\n attack damage:{self.attack_dmg}
    \n magic damage:{self.magic_dmg}\n defence:{self.defence}"""