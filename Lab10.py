#The authors' names are Margaret and Lilly

#A
d1 = {"a":1, "b":2, "c":3, "d":4, "e":5}
def my_get_method(k,v):
    if k in d1:
        return d1[k]
    else:
        d1[k] = v
        return d1[k]
print(my_get_method("x", 0))


#B
d2 = {"Schuler":"Serenity", "Smith":"Serenity", "Johnson":"Olivia", "Beck": "Olivia", "Hand": "Colleen", "Raycroft": "Anna", "Garcia Jimenez": "Victoria", "Gangwer": "Gwyneth", "Webster-Hess": "Mairi", "Litvak": "Aliza", "Wyatt": "Elizabeth", "Taylor": "Rylee"}
def histogram(dic):
    uniques = []
    for lasts in dic:
        if dic[lasts] not in uniques:
            uniques.append(dic[lasts])
    return uniques
print(histogram(d2))


#C
my_list_of_names = ["Schuler","Serenity", "Smith","Serenity", "Johnson","Olivia", "Beck", "Olivia", "Hand", "Colleen", "Raycroft", "Anna", "Garcia Jimenez", "Victoria", "Gangwer", "Gwyneth", "Webster-Hess", "Mairi", "Litvak", "Aliza", "Wyatt", "Elizabeth", "Taylor", "Rylee"]
list2 = my_list_of_names[::2]

def cpsc_names(lst1):
    d1 = {}
    for x in lst1:
        val = x[0]
        if val not in d1:
            d1[val] = 1
        else:
            d1[val] += 1
    return d1


print(cpsc_names(list2))


#D
red_cake = {"Conla Oil":1, "egg":3, "Red Velvet Mix":1, "Water":2}
lemon_cake = {"Vegetable Oil":1.5, "egg":3, "Lemon Mix":1, "Water":2}
def similar_ingredients(x):
    mylist = []
    for x in red_cake:
        if x in lemon_cake:
            result = mylist.append(x)
            return result 
        else:
            return None
print(similar_ingredients("egg"))

        

 
