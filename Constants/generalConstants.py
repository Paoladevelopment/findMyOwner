from Enums.Actions import Actions

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
    0: "Perro cobarde",
    1: "Casilla vacía",
    2: "Abusador amo",
    3: "Gato malvado",
    4: "Muriel",
    5: "Obstaculo",
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