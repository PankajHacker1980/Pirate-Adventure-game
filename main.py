import random
import time

class PirateAdventure:
    def __init__(self):
        self.player_name = ""
        self.ship_health = 100
        self.crew = 20
        self.gold = 0
        self.rum = 100
        self.days_at_sea = 0
        self.island_visited = []
    
    def display_status(self):
        print(f"\n--- {self.player_name}'s Pirate Adventure ---")
        print(f"Ship Health: {self.ship_health}")
        print(f"Crew: {self.crew}")
        print(f"Gold: {self.gold}")
        print(f"Rum: {self.rum}")
        print(f"Days at Sea: {self.days_at_sea}")
        print(f"Islands Visited: {', '.join(self.island_visited)}")
    
    def choose_player_name(self):
        self.player_name = input("Ahoy Captain! What be yer name?: ").strip().capitalize()
        print(f"Welcome aboard, Captain {self.player_name}!")
    
    def sail_the_seas(self):
        print("\nSailing the high seas...")
        time.sleep(2)
        encounter_chance = random.random()
        
        if encounter_chance < 0.3:
            self.encounter_ship()
        else:
            self.explore_island()
    
    def encounter_ship(self):
        print("\nAhoy! You've encountered another ship!")
        time.sleep(1)
        decision = input("Do ye wish to 'attack' or 'flee'?: ").strip().lower()
        
        if decision == "attack":
            enemy_crew = random.randint(10, 30)
            enemy_gold = random.randint(50, 100)
            print(f"\nYou attack the enemy ship!")
            time.sleep(1)
            
            if self.crew > enemy_crew:
                print(f"Victory! Ye plundered {enemy_gold} gold from the enemy ship.")
                self.gold += enemy_gold
            else:
                print("Ye were outnumbered and lost the battle!")
                self.crew -= enemy_crew // 2
                self.ship_health -= random.randint(10, 30)
        elif decision == "flee":
            print("Ye chose to flee the battle.")
            self.rum -= 10
        else:
            print("Invalid choice. The enemy ship attacks while ye hesitate!")
            self.ship_health -= random.randint(10, 30)
    
    def explore_island(self):
        island_name = random.choice(["Treasure Island", "Skull Island", "Secret Cove"])
        print(f"\nLand ho! Ye found {island_name}.")
        time.sleep(1)
        self.island_visited.append(island_name)
        decision = input(f"Do ye wish to 'explore' or 'leave' {island_name}?: ").strip().lower()
        
        if decision == "explore":
            found_gold = random.randint(20, 50)
            found_rum = random.randint(10, 30)
            self.gold += found_gold
            self.rum += found_rum
            print(f"Ye found {found_gold} gold coins and {found_rum} barrels of rum.")
        elif decision == "leave":
            print(f"Ye left {island_name} without further exploration.")
        else:
            print("Invalid choice. Ye wasted time and rum exploring aimlessly.")
            self.rum -= 10
    
    def visit_tavern(self):
        print("\nWelcome to the Tavern!")
        print("What will ye have?")
        print("1. Buy Rum (10 gold) - Restores rum")
        print("2. Recruit Crew (20 gold) - Adds crew members")
        print("3. Leave Tavern")
        
        choice = input("Enter yer choice (1-3): ").strip()
        
        if choice == "1" and self.gold >= 10:
            self.rum = min(100, self.rum + 30)
            self.gold -= 10
            print("Ye bought rum for yer crew.")
        elif choice == "2" and self.gold >= 20:
            self.crew += random.randint(5, 10)
            self.gold -= 20
            print("Ye recruited more crew members.")
        elif choice == "3":
            print("Leaving the tavern.")
        else:
            print("Ye don't have enough gold for that!")
    
    def embark_on_adventure(self):
        self.choose_player_name()
        
        while self.ship_health > 0:
            self.display_status()
            action = input("\nWhat be yer next move, Captain? 'Sail' the seas, visit the 'tavern', or 'quit'?: ").strip().lower()
            
            if action == "quit":
                print(f"Farewell, Captain {self.player_name}! May ye find yer pirate fortune.")
                break
            elif action == "sail":
                self.sail_the_seas()
                self.days_at_sea += 1
            elif action == "tavern":
                self.visit_tavern()
            else:
                print("Invalid command, Captain. Choose wisely!")
            
            if self.ship_health <= 0:
                print("Yer ship has been sunk! Game over, Captain.")
                break
        
        if self.ship_health > 0:
            print(f"Congratulations, Captain {self.player_name}! Ye be a legendary pirate with {self.gold} gold and {self.crew} loyal crew members.")

if __name__ == "__main__":
    game = PirateAdventure()
    game.embark_on_adventure()
