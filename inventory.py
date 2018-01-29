#! python3

stuff={'rope':1,'torch':6,'gold coin':42,'dagger':2,'arrow':12}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']

def displayInventory(inventory):
    print('Inventory:')
    itemTotal=0
    for k,v in inventory.items():
          print(str(v)+' '+k)
          itemTotal+=v
    print("Total number of items: "+str(itemTotal))


def addToInventory(inventory,addedItems):
    for k in range(len(addedItems)):
        if addedItems[k] in inventory.keys():
                   inventory[addedItems[k]]+=1
        else:
                   inventory[addedItems[k]]=1
    return inventory

displayInventory(stuff)
stuff=addToInventory(stuff,dragonLoot)
displayInventory(stuff)
          
    
