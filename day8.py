print("""You look nice today😘💕

Today you're going to make an
impact and change the World🌎🌏!

keep it up❤️""")

print("Wholesome Positivity Machine")
name = input("Who are you? ")
if name == "david":
    print("Welcome " + name + "!")
else:
    print("Name not found")
achievements = input("What do you want to achieve? ")
if achievements == "Teach people to code!":
    print("That is impressive ")
else:
    print("That is not impressive ")
scale = int(input("On a scale of 1 - 10 how do you feel: "))

emojis = {
    1: "😖", 2: "😤", 3: "🤧", 4: "😩", 5: "😌",
    6: "🥰", 7: "🤩", 8: "😊", 9: "😍", 10: "😘"
}

if scale in emojis:
    print(emojis[scale])
else:
    print("Enter a number between 1 and 10.")

if name == "david" and achievements == "Teach people to code!":
    print("Hey David,keep your chin up! Today you're going to "
          "Teach people to code! in the most amazing way,"
          "simply by being you - YOU ROCK!")
else:
    print("Try again wrong name ")

hair = input("How much hair do you have on your head?")
scale = int(input("On a scale of 1 - 10 bald are you?: "))

emoji = {
    1: "👱‍", 2: "👩", 3: "👱🏼", 4: "‍👱🏾", 5: "👱‍♂️",
    6: "👱", 7: "👶", 8: "👩‍🦲", 9: "🧑‍🦲", 10: "👨‍🦲"
}

if scale in emoji:
    print(emoji[scale])
if name == "Daniel" and hair == "none":
    print("Hey Daniel - you thought i wouln't know who you are because"
          "you didn't capitalise properly! well get that"
          "egg-head and dry your eyes because some amazing insults are coming")