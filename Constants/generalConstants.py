from Enums.Actions import Actions


#Used to save the probability of ocurrence when genereting the random board
PROBABILITIES = {
        1: 0.4,
        2: 0.15,
        3: 0.15,
        5: 0.3
    }


LIST_ACTIONS = {
    0: Actions.GO_UP,
    1: Actions.GO_RIGHT,
    2: Actions.GO_DOWN,
    3: Actions.GO_LEFT
}

COSTS = {
  0: 1,
  1: 1,
  2: -2,
  3: 3,
  4: 1
}

INFO_ENTITIES = {
    0: "Zombie",
    1: "Pasto",
    2: "Girasol",
    3: "Papa explosión",
    4: "Cerebro",
    5: "Agua",
}


INFO_ENTITIES_IMAGES = {
    0: "findMyOwner\Images\zombieMap.jpg",
    1: "findMyOwner\Images\greenMap.jpg",
    2: "findMyOwner\Images/sunflowerMap.jpg",
    3: "findMyOwner\Images\papapumMap.jpg",
    4: "findMyOwner\Images/brainMap.jpg",
    5: "findMyOwner\Images/waterMap.jpg",
    6: "findMyOwner\Images/zombieEatMap.jpg",
    7: "findMyOwner\Images\zombieBurnedMap.jpg",
    8: "findMyOwner\Images\zombieWonMap.jpg"
}


# INFO_ENTITIES_IMAGES = {
#     0: r"D:\Proyecto 1 IA\Images\zombieMap.jpg",
#     1: r"D:\Proyecto 1 IA\Images\greenMap.jpg",
#     2: r"D:\Proyecto 1 IA\Images\sunflowerMap.jpg",
#     3: r"D:\Proyecto 1 IA\Images\papapumMap.jpg",
#     4: r"D:\Proyecto 1 IA\Images\brainMap.jpg",
#     5: r"D:\Proyecto 1 IA\Images\waterMap.jpg",
#     6: r"D:\Proyecto 1 IA\Images\zombieEatMap.jpg",
#     7: r"D:\Proyecto 1 IA\Images\zombieBurnedMap.jpg",
#     8: r"D:\Proyecto 1 IA\Images\zombieWonMap.jpg"
# }