# Write a function named displayInventory() 
# that would take any possible “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

example_inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

def displayInventory(inventory):
    print("Inventory: \n")
    item_total = 0

    for k, v in inventory.items():
        print(f'{k}: {v}')
        item_total += v

    print(f"\nTotal number of items: {item_total}.\n")


displayInventory(example_inventory)

# Write a function named addToInventory(inventory, addedItems), 
# where the inventory parameter is a dictionary representing the player’s inventory 
# and the addedItems parameter is a list like dragonLoot. 
# The addToInventory() function should return a dictionary that represents the updated inventory. 
# Note that the addedItems list can contain multiples of the same item. 

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def AddToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

AddToInventory(example_inventory, dragonLoot)
displayInventory(example_inventory)
