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


def main():
    AGE_ON_EARTH_IN_SECS = 365.25 * 24 * 60 * 60
    print(AGE_ON_EARTH_IN_SECS)


if __name__ == "__main__":
    main()
