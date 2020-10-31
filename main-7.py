# Name: Nafisa Chowdhury
# PSID: 1591144

d = {}

for i in range(1, 6):
    jersey = int(input("Enter player {}'s jersey number:\n".format(i)))
    rating = int(input("Enter player {}'s rating:\n\n".format(i)))
    if 0 < jersey < 99 or 1 < rating < 9:
        d[jersey] = rating
    else:
        break

print("ROSTER")
for jersey, rating in sorted(d.items()):
    print("Jersey number: {}, Rating: {}".format(jersey, rating))

option = ""
menu = ("\nMENU\n"
        "a - Add player\n"
        "d - Remove player\n"
        "u - Update player rating\n"
        "r - Output players above a rating\n"
        "o - Output roster\n"
        "q - Quit")

while option != "q":
    print(menu, end="\n")
    print()
    option = input("Choose an option:\n")
    if option == "a":
        new_jersey = int(input("Enter a new player's jersey number:\n"))
        new_rating = int(input("Enter the player's rating:\n"))
        if 0 < new_jersey < 99 and 1 < new_rating < 9:
            d[new_jersey] = new_rating
        else:
            break
    if option == "d":
        del_player = int(input("Enter a jersey number:\n"))
        del d[del_player]
    if option == "u":
        player = int(input("Enter a jersey number:\n"))
        r = int(input("Enter a new rating for player:\n"))
        if 1 < r < 9:
            d[player] = r
    if option == "r":
        above_r = int(input("Enter a rating:\n"))
        print("ABOVE {}".format(above_r))
        for jersey, rating in sorted(d.items()):
            if rating > above_r:
                print("Jersey number: {}, Rating: {}".format(jersey, rating))
    if option == "o":
        print()
        print("ROSTER")
        for jersey, rating in sorted(d.items()):
            print("Jersey number: {}, Rating: {}".format(jersey, rating))
