import random
import pyperclip

levels = {
    "TUT_MOVEMENT": "Movement",
    "TUT_SHOOTINGRANGE": "Pummel",
    "SLUGGER": "Gunner",
    "TUT_FROG": "Cascade",
    "TUT_JUMP": "Elevate",
    "GRID_TUT_BALLOON": "Bounce",
    "TUT_BOMB2": "Purify",
    "TUT_BOMBJUMP": "Climb",
    "TUT_FASTTRACK": "Fasttrack",
    "GRID_PORT": "Glass Port",
    "GRID_PAGODA": "Take Flight",
    "TUT_RIFLE": "Godspeed",
    "TUT_RIFLEJOCK": "Dasher",
    "TUT_DASHENEMY": "Thrasher",
    "GRID_JUMPDASH": "Outstretched",
    "GRID_SMACKDOWN": "Smackdown",
    "GRID_MEATY_BALLOONS": "Catwalk",
    "GRID_FAST_BALLOON": "Fastlane",
    "GRID_DRAGON2": "Distinguish",
    "GRID_DASHDANCE": "Dancer",
    "TUT_GUARDIAN": "Guardian",
    "TUT_UZI": "Stomp",
    "TUT_JUMPER": "Jumper",
    "TUT_BOMB": "Dash Tower",
    "GRID_DESCEND": "Descent",
    "GRID_STAMPEROUT": "Driller",
    "GRID_CRUISE": "Canals",
    "GRID_SPRINT": "Sprint",
    "GRID_MOUNTAIN": "Mountain",
    "GRID_SUPERKINETIC": "Superkinetic",
    "GRID_ARRIVAL": "Arrival",
    "FLOATING": "Forgotten City",
    "GRID_BOSS_YELLOW": "The Clocktower",
    "GRID_HOPHOP": "Fireball",
    "GRID_RINGER_TUTORIAL": "Ringer",
    "GRID_RINGER_EXPLORATION": "Cleaner",
    "GRID_HOPSCOTCH": "Warehouse",
    "GRID_BOOM": "Boom",
    "GRID_SNAKE_IN_MY_BOOT": "Streets",
    "GRID_FLOCK": "Steps",
    "GRID_BOMBS_AHOY": "Demolition",
    "GRID_ARCS": "Arcs",
    "GRID_APARTMENT": "Apartment",
    "TUT_TRIPWIRE": "Hanging Gardens",
    "GRID_TANGLED": "Tangled",
    "GRID_HUNT": "Waterworks",
    "GRID_CANNONS": "Killswitch",
    "GRID_FALLING": "Falling",
    "TUT_SHOCKER2": "Shocker",
    "TUT_SHOCKER": "Bouquet",
    "GRID_PREPARE": "Prepare",
    "GRID_TRIPMAZE": "Triptrack",
    "GRID_RACE": "Race",
    "TUT_FORCEFIELD2": "Bubble",
    "GRID_SHIELD": "Shield",
    "SA L VAGE2": "Overlook",
    "GRID_VERTICAL": "Pop",
    "GRID_MINEFIELD": "Minefield",
    "TUT_MIMIC": "Mimic",
    "GRID_MIMICPOP": "Trigger",
    "GRID_SWARM": "Greenhouse",
    "GRID_SWITCH": "Sweep",
    "GRID_TRAPS2": "Fuse",
    "TUT_ROCKETJUMP": "Heavens Edge",
    "TUT_ZIPLINE": "Zipline",
    "GRID_CLIMBANG": "Swing",
    "GRID_ROCKETUZI": "Chute",
    "GRID_CRASHLAND": "Crash",
    "GRID_ESCALATE": "Ascent",
    "GRID_SPIDERCLAUS": "Straightaway",
    "GRID_FIRECRACKER_2": "Firecracker",
    "GRID_SPIDERMAN": "Streak",
    "GRID_DESTRUCTION": "Mirror",
    "GRID_HEAT": "Escalation",
    "GRID_BOLT": "Bolt",
    "GRID_PON": "Godstreak",
    "GRID_CHARGE": "Plunge",
    "GRID_MIMICFINALE": "Mayhem",
    "GRID_BARRAGE": "Barrage",
    "GRID_1GUN": "Estate",
    "GRID_HECK": "Trapwire",
    "GRID_ANTFARM": "Ricochet",
    "GRID_FORTRESS": "Fortress",
    "GRID_GODTEMPLE_ENTRY": "Holy Ground",
    "GRID_BOSS_GODSDEATHTEMPLE": "The Third Temple",
    "GRID_EXTERMINATOR": "Spree",
    "GRID_FEVER": "Breakthrough",
    "GRID_SKIPSLIDE": "Glide",
    "GRID_CLOSER": "Closer",
    "GRID_HIKE": "Hike",
    "GRID_SKIP": "Switch",
    "GRID_CEILING": "Access",
    "GRID_BOOP": "Congregation",
    "GRID_TRIPRAP": "Sequence",
    "GRID_ZIPRAP": "Marathon",
    "TUT_ORIGIN": "Sacrifice",
    "GRID_BOSS_RAPTURE": "Absolution",
    "SIDEQUEST_OBSTACLE_PISTOL": "Elevate Traversal I",
    "SIDEQUEST_OBSTACLE_PISTOL_SHOOT": "Elevate Traversal II",
    "SIDEQUEST_OBSTACLE_MACHINEGUN": "Purify Traversal",
    "SIDEQUEST_OBSTACLE_RIFLE_2": "Godspeed Traversal",
    "SIDEQUEST_OBSTACLE_UZI2": "Stomp Traversal",
    "SIDEQUEST_OBSTACLE_SHOTGUN": "Fireball Traversal",
    "SIDEQUEST_OBSTACLE_ROCKETLAUNCHER": "Dominion Traversal",
    "SIDEQUEST_RAPTURE_QUEST": "Book of Life Traversal",
    "SIDEQUEST_DODGER": "Doghouse",
    "GRID_GLASSPATH": "Choker",
    "GRID_GLASSPATH2": "Chain",
    "GRID_HELLVATOR": "Hellevator",
    "GRID_GLASSPATH3": "Razor",
    "SIDEQUEST_ALL_SEEING_EYE": "All Seeing Eye",
    "SIDEQUEST_RESIDENTSAWB": "Resident Saw I",
    "SIDEQUEST_RESIDENTSAW": "Resident Saw II",
    "SIDEQUEST_SUNSET_FLIP_POWERBOMB": "Sunset Flip Powerbomb",
    "GRID_BALLOONLAIR": "Balloon Mountain",
    "SIDEQUEST_BARREL_CLIMB": "Climbing Gym",
    "SIDEQUEST_FISHERMAN_SUPLEX": "Fisherman Suplex",
    "SIDEQUEST_STF": "STF",
    "SIDEQUEST_ARENASIXNINE": "Arena",
    "SIDEQUEST_ATTITUDE_ADJUSTMENT": "Attitude Adjustment",
    "SIDEQUEST_ROCKETGODZ": "Rocket",
}


def display_menu():
    print("\n--- Neon White Random Rush ---")
    print("1. Generate Random Rush")
    print("2. Add Level to Ban List")
    print("3. Remove Level from Ban List")
    print("4. View Ban List")
    print("5. Exit")

def generate_rush(levels, banned, count):
    available = [lvl for lvl in levels if lvl not in banned]
    if count > len(available):
        print("Not enough levels to generate a rush.")
        return
    selected = random.sample(available, count)
    print("\nGenerated Rush:")
    code = "; ".join(selected)
    print(code)
    pyperclip.copy(code)
    print("(rush copied to clipboard)")

def view_levels(levels):
    for k, v in levels.items():
        print(f"{k} - {v}")

def main():
    banned = set()
    name_to_id = {v.lower(): k for k, v in levels.items()}
    
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            try:
                count = int(input("How many levels in the rush? "))
                generate_rush(levels, banned, count)
            except ValueError:
                print("Invalid number.")
        
        elif choice == "2":
            name = input("Enter level name to ban: ").strip().lower()
            level_id = name_to_id.get(name)
            if level_id:
                banned.add(level_id)
                print(f"{level_id} ({levels[level_id]}) added to ban list.")
            else:
                print("Level name not found.")
        
        elif choice == "3":
            name = input("Enter level name to unban: ").strip().lower()
            level_id = name_to_id.get(name)
            if level_id and level_id in banned:
                banned.remove(level_id)
                print(f"{level_id} ({levels[level_id]}) removed from ban list.")
            else:
                print("Level name not found or not in ban list.")
        
        elif choice == "4":
            print("Banned levels:")
            for b in banned:
                print(f"{levels[b]}")
        
        elif choice == "5":
            print("baibai")
            break
        
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

