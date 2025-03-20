print("Generation Identifier")
year = int(input("Enter the year you were born: "))

if 1883 <= year <= 1900:
    generation = "Lost Generation"
elif 1901 <= year <= 1927:
    generation = "Greatest Generation"
elif 1928 <= year <= 1945:
    generation = "Silent Generation"
elif 1946 <= year <= 1964:
    generation = "Baby Boomer"
elif 1965 <= year <= 1980:
    generation = "Generation X"
elif 1981 <= year <= 1996:
    generation = "Millennial"
elif 1997 <= year <= 2012:
    generation = "Generation Z"
elif 2013 <= year <= 2024:
    generation = "Generation Alpha"
elif year >= 2025:
    generation = "Generation Beta"
else:
    generation = "Unknown Generation"

print("Hah! " + generation + ", Avocado toast and Starbucks much! 😆")
