character = ["Doom guy", "Master Chief", "Mario", "Henry", "Guardian"] # jména postav
weapons = ["Rocket launcher", "Chain saw", "DMR", "Plasma gun", "Stick", "Bow", "Sword"] # zbraně
star = "*" * 40 # výpis hvězdiček pro menu
lines = "-" * 35
champs = """1 - Doom guy 
2 - Master Chief
3 - Mario
4 - Henry
5 - Guardian""" # výpis šampionů
guns = """1 - Rocket launcher
2 - Chain saw
3 - DMR
4 - Plasma gun
5 - Stick
6 - Bow
7 - Sword""" #výpis zbraní
hp_base = 100
energy_base = 100
agility_base = 100
endurance_base = 100
mana_base = 100
warrior = [(hp_base * 1,5), (energy_base * 0,9), (agility_base * 1,2), (endurance_base), (mana_base * 0,3)]
sorcerer = [(hp_base * 0,8), (energy_base * 1,4), (agility_base * 1,3), (endurance_base * 0,8), (mana_base * 1,6)]
assassin = [(hp_base), (energy_base * 1,5), (agility_base * 1,4), (endurance_base * 1,3), (mana_base * 0,5)]
tank = [(hp_base * 2), (energy_base * 0,8), (agility_base * 0,8), (endurance_base * 1,5), (mana_base * 0,6)]
Doom_guy = ["Doom guy is an incredibly agile fighter. He excels in short and medium range combat. His specialty is firearms, but he can handle close combat as well."]
Master_Chief = ["Master Chief is a genetic super soldier. His strengths are great mobility and endurance. He can deal with enemies at any distance."]
Mario = ["Mario is a simple plumber. He is characterized by great tenacity and has many charms in stock."]
Henry = ["Who is Henry? If the creator remembered how he came up with this name, that would be cool. So we don't know who Henry is, but he can definitely do something :-)"]
Guardian = ["The Guardian is a soldier from the future. It is characterized by the ability to use movement spells. He mainly enjoys ambushing enemies."]
option = """1- YES
2 - NO"""

print(star)
print(" WELCOME, WARRIOR, CHOOSE YOUR CHAMPION")
print(star)
print(champs)
print(star)

champ_input = input("CHAMPION SELECT")
chosen_champ = character[int(champ_input) - 1]
print("YOU CHOSE", chosen_champ, ". READ THE DESCRIPTION AND CONFIRM YOUR CHOICE.")
print(lines)
if chosen_champ is character[0]:
    print(Doom_guy)
elif chosen_champ is character[1]:
    print(Master_Chief)
elif chosen_champ is character[2]:
    print(Mario)
elif chosen_champ is character[3]:
    print(Henry)
else:
    print(Guardian)
option_input = input("KEEP YOUR CHOICE? YES/NO")
chosen_option = option[int(option_input) - 1]
for chosen_input in option:
    if option == [(chosen_option) - 1]: # tady mi to nefunguje
        print("CHOICE CONFIRMED")
        break
    else:
        print("MAKE A NEW CHOICE")
print("THANK YOU FOR CONFIRMATION")
print(lines)

print("CHOOSE YOUR WEAPON")
print(star)
print(guns)
print(star)
gun_input = input("WEAPON SELECT")
chosen_gun = weapons[int(gun_input) - 1]
print(chosen_gun)
print(lines)

print("YOU CHOSE", chosen_champ, ".")
print("YOUR TOOL OF DESTRUCTION IS", chosen_gun, ".")
print("GOOD LUCK, WARRIOR. YOUR BATTLE BEGINS NOW!")


