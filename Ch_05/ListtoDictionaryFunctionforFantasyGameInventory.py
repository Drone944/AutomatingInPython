def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))
def addToInventory(inventory, addedItems):
    keys = list(inventory.keys())
    for i in addedItems:
        if i in keys:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, addedItems.count(i))
    return(inv)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)