# Modifying Global Scope

enemies = "skeliton"



def increase_enemies():
    global enemies
    enemies = "zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


