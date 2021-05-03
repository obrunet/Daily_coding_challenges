"""
https://exercism.io/tracks/python/exercises/space-age
Given an age in seconds, calculate how old someone would be on:

Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they're 31.69 Earth-years old.
"""


class SpaceAge():
    """
    Class initialized with the age of an alien in years on earth 
    that compute the age on other different planets, it also provides all ages with a specific method  
    """
    AGE_ON_EARTH_IN_SECS = 365.25 * 24 * 60 * 60
    orbital_periods = {
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }

    def __init__(self, age_on_earth_in_yrs=0):
        self.age_on_earth_in_yrs = age_on_earth_in_yrs
        self.age_on_venus, self.age_on_mars, self.age_on_mercury = 0, 0, 0

    def on_mercury(self):
        self.age_on_mercury = round(self.age_on_earth_in_yrs * self.AGE_ON_EARTH_IN_SECS / self.orbital_periods["Mercury"], 2)
    
    def on_venus(self):
        self.age_on_venus = round(self.age_on_earth_in_yrs * self.AGE_ON_EARTH_IN_SECS / self.orbital_periods["Venus"], 2)
    
    def on_mars(self):
        self.age_on_mars = round(self.age_on_earth_in_yrs * self.AGE_ON_EARTH_IN_SECS / self.orbital_periods["Mars"], 2)

    def all_ages(self):
        self.on_mercury()
        self.on_mars()
        self.on_venus()
        return f"""age in seconds on :
            - Mercury : {self.age_on_mercury}
            - Venus : {self.age_on_venus}
            - Mars : {self.age_on_mars}
            """


def main():
    while True:
        try:
            nb_user = int(input("How many aliens are you: "))
            print(f'You are {nb_user} different aliens !')
            break
        except:
            print("You didn't enter an integer...try again")
            continue

    for u in range(nb_user):
        alien_age = int(input(f'Alien #{u+1}: how old are you ? '))

        Alien = SpaceAge(alien_age)
        Alien.on_mercury()
        print(f'Alien #{u+1}: you are {Alien.age_on_mercury} seconds old on Mercury, and {Alien.age_on_mars} on Mars !')
        print(Alien.all_ages())


if __name__ == "__main__":
    main()