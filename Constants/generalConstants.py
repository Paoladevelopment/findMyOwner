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
    0: r"E:\Universidad\IA\findMyOwner\Images\perroCobarde.png",
    1: r"E:\Universidad\IA\findMyOwner\Images\white.jpg",
    2: r"E:\\Universidad\\IA\findMyOwner\\Images\\abusadorAmo.png",
    3: r"E:\Universidad\IA\findMyOwner\Images\katz.png",
    4: r"E:\Universidad\IA\findMyOwner\Images\muriel.png",
    5: r"E:\Universidad\IA\findMyOwner\Images\black.jpg",
    6: r"E:\Universidad\IA\findMyOwner\Images\abusadorEfecto.jpg",
    7: r"E:\Universidad\IA\findMyOwner\Images\katzEfecto.jpg",
    8: r"E:\Universidad\IA\findMyOwner\Images\murielEfecto.jpg"
}