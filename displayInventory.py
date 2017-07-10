stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)         #
        item_total += v
    print('Total number of items: ' + str(item_total) + '\n')

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():       # if i can be found in inventory
            inventory[i] += 1           # add +1 to count
        else:                           # else if not found in inventory
            inventory.setdefault(i,0)   # set i as key and value as 0
            inventory[i] += 1           # add +1 to count
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
