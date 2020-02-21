def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    print(inventory)
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
