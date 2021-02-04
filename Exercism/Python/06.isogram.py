"""
Determine if a word or phrase is an isogram - https://exercism.io/tracks/python/exercises/isogram

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
Examples of isograms:
lumberjacks
background
downstream
six-year-old
"""

def is_isogram(st):
    "Return if the input string is an isogram, otherwise false"
    st = st.strip().replace('-', '').lower()
    return len(st) == len(set(st))


def main():
    str_1, str_2, str_3, str_4 = "lum be-rjjjjacks", "background", "downstream", "six-year-old"
    for i in (str_1, str_2, str_3, str_4):
        if is_isogram(i):
            print(f'{i} is an isogram')
        else:
            print(f'{i} is NOT an isogram')
        print(f'proof: {"".join(sorted(i))}')


if __name__ == "__main__":
    main()