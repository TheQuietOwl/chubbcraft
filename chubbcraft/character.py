

class Character():

    # creaters character class constructor
    def __init__(self, race: str):
        self.health=100
        self.attack_dmg=10
        self.magic_dmg=5
        self.defence=2
        self.race=race
        
    @property
    def race(self):
        return self.__race
 
    @race.setter
    def race(self, race: race):
        self.__race=race.lower()
        if self.__race=='orc':
            self.health=self.health*1.2
        elif self.__race=='human':
            self.defence=self.defence+1
        elif self.__race=='elf':
            self.magic_dmg=self.magic_dmg*1.2
        else:
            raise Exception("No such race")

    def get_atributes(self):
        return f"""The character is an {str(self.race)} 
    with \n health:{self.health}\n attack damage:{self.attack_dmg}
    \n magic damage:{self.magic_dmg}\n defence:{self.defence}"""