@namespace
class SpriteKind:
    Background = SpriteKind.create()
    Mountain = SpriteKind.create()
def spawnSomething(roll: number):
    if roll <= 2:
        createSaucer()
    elif roll <= 6:
        createTree()
    elif roll <= 24:
        createCloud()
    elif roll <= 40:
        createBird()
def createSaucer():
    global saucerSpeed, saucer
    if Math.percent_chance(50):
        saucerSpeed = 40
    else:
        saucerSpeed = -40
    saucer = sprites.create_projectile_from_side(img("""
            .........fff.........
                    .......ff888ff.......
                    ......f8888998f......
                    .....f888888998f.....
                    ....f888a8a88998f....
                    ...ff88888888898ff...
                    ..fdddddddddddddddf..
                    .fbbbbbbbbbbbbbbbbbf.
                    fa9b9bb9bb9bb9bb9b9af
                    .facccccccccccccccaf.
                    ..faacccccccccccaaf..
                    ...ffaacccccccaaff...
                    .....fffffffffff.....
                    .....f999999999f.....
                    ......fffffffff......
        """),
        saucerSpeed,
        0)
    animation.run_image_animation(saucer, flyingSaucer, 400, True)
    saucer.y = randint(10, scene.screen_height() - 10)

def on_button_pressed():
    balloon.start_effect(effects.fire)
    balloon.start_effect(effects.fire)
    balloon.ay = -50
    balloon.set_image(balloonInflated)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def createAnimationArrays():
    global flyingSaucer, birdGoingLeft, birdGoingRight
    flyingSaucer = [img("""
            .........fff.........
                    .......ff888ff.......
                    ......f8888998f......
                    .....f888888998f.....
                    ....f888a8a88998f....
                    ...ff88888888898ff...
                    ..fdddddddddddddddf..
                    .fbbbbbbbbbbbbbbbbbf.
                    fa9b9bb9bb9bb9bb9b9af
                    .facccccccccccccccaf.
                    ..faacccccccccccaaf..
                    ...ffaacccccccaaff...
                    .....fffffffffff.....
                    .....f999999999f.....
                    ......fffffffff......
        """),
        img("""
            .........fff.........
                    .......ff888ff.......
                    ......f8888998f......
                    .....f888888998f.....
                    ....f888a8a88998f....
                    ...ff88888888898ff...
                    ..fdddddddddddddddf..
                    .fbbbbbbbbbbbbbbbbbf.
                    fab4b44b44b44b44b4baf
                    .facccccccccccccccaf.
                    ..faacccccccccccaaf..
                    ...ffaacccccccaaff...
                    .....fffffffffff.....
                    .....f999999999f.....
                    ......fffffffff......
        """)]
    birdGoingLeft = [img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 8 8 f f 8 f 
                    f 5 5 5 8 8 f 8 8 8 8 8 8 8 f . 
                    . f f f 8 8 8 f 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . . 
                    . f 8 f 8 8 8 8 8 f 8 f 8 8 8 f . 
                    f 4 5 8 8 8 8 8 8 8 f 8 8 8 8 f . 
                    f 5 5 5 8 8 f 8 8 8 8 f 8 8 f . . 
                    . f f f 8 8 8 f 8 8 8 8 f 8 f . . 
                    . . . . f f a f f 8 8 8 8 f f . . 
                    . . . . . . . . f 8 8 8 f . . . . 
                    . . . . . . . . . f 8 8 f . . . . 
                    . . . . . . . . . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 8 8 f f 8 f 
                    f 5 5 5 8 8 f 8 8 8 8 8 8 8 f . 
                    . f f f 8 8 8 f 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . f f . . . 
                    . . . . . . . . . . f 8 8 f . . 
                    . . . f f f f . f f 8 8 8 f . . 
                    . . f 8 8 8 8 f f 8 8 8 f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 f 8 f f 8 f 
                    f 5 5 5 8 8 8 8 8 f 8 8 8 8 f . 
                    . f f f 8 8 8 8 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """)]
    birdGoingRight = [img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 8 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 f 8 8 8 8 8 f 8 f . 
                    f 8 8 8 8 f 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 f 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 f 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 8 f f f f . . . . 
                    . . . f 8 8 8 f . . . . . . . . 
                    . . . f 8 8 f . . . . . . . . . 
                    . . . . f f . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . f f f f . . . 
                    . f f f . f f f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 8 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 8 8 8 f 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 f 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . f f . . . . . . . . . . . 
                    . . f 8 8 f . . . . . . . . . . 
                    . . f 8 8 8 f f . f f f f . . . 
                    . f f f 8 8 8 f f 8 8 8 8 f . . 
                    f 8 8 8 f 8 8 8 8 8 8 8 f 8 f . 
                    f 8 f f 8 f 8 8 8 8 8 8 8 5 4 f 
                    . f 8 8 8 8 f 8 8 8 8 8 5 5 5 f 
                    . f 8 8 8 8 8 8 8 8 8 8 f f f . 
                    . . f f 8 8 8 f f f f f . . . . 
                    . . . . f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """)]

def on_button_released():
    balloon.ay = 50
    effects.clear_particles(balloon)
    balloon.set_image(balloonDeflated)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def createBird():
    global saucerSpeed, chosenAnimation, bird
    if Math.percent_chance(50):
        saucerSpeed = 20
        chosenAnimation = birdGoingRight
    else:
        saucerSpeed = -20
        chosenAnimation = birdGoingLeft
    bird = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . . . . . . 
                    . . f 8 8 8 8 f f f f . f f f . 
                    . f 8 f 8 8 8 8 8 8 8 f 8 8 8 f 
                    f 4 5 8 8 8 8 8 8 8 8 8 f f 8 f 
                    f 5 5 5 8 8 f 8 8 8 8 8 8 8 f . 
                    . f f f 8 8 8 f 8 8 8 8 8 8 f . 
                    . . . . f f f f f 8 8 8 f f . . 
                    . . . . . . . . f f f f . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        saucerSpeed,
        0)
    animation.run_image_animation(bird, chosenAnimation, 100, True)
    bird.y = randint(12, scene.screen_height() - 10)
def createCloud():
    global cloudImages, cloud
    cloudImages = [img("""
            ..................1111...............
                    ................11111111.............
                    ...............1111111111............
                    ..............11111111111....11111...
                    ..............111111111111.11111111..
                    .............11111111111111111111111.
                    ........11111111111111111111111111111
                    .......111111111111111111111111111111
                    1111111111111111111111111111111111111
                    .111111111111111111111111111111111111
                    .......111111111111111111111111111111
                    .......................1111111111111.
        """),
        img("""
            . . . 1 1 1 1 . . . 1 1 . . . . . . . . 
                    . . 1 1 1 1 1 1 . 1 1 1 1 . . . . . . . 
                    . 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . 
                    . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 1 1 . . . 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . .
        """),
        img("""
            ............111111...........
                    ..........111111111..........
                    .........11111111111.........
                    ........1111111111111........
                    ........1111111111111........
                    ........11111111111111.......
                    ....111111111111111111111111.
                    ...11111111111111111111111111
                    ..111111111111111111111111111
                    ..111111111111111111111111111
                    11111111111111111111111111111
                    .11111111111111111111.1.1111.
                    1........11111111111.....11..
                    11111111111111...............
        """)]
    cloud = sprites.create_projectile_from_side(cloudImages[randint(0, len(cloudImages) - 1)], -5, 0)
    cloud.z = -10
    cloud.set_flag(SpriteFlag.GHOST, True)
    cloud.y = randint(0, scene.screen_height() * 0.6)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.set_flag(SpriteFlag.GHOST, True)
    sprite.say("ow!", 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def placeMountain(leftPosition: number):
    global lastCreatedMountain
    lastCreatedMountain = sprites.create(mountains[randint(0, 1)], SpriteKind.Mountain)
    lastCreatedMountain.set_flag(SpriteFlag.GHOST, True)
    lastCreatedMountain.set_flag(SpriteFlag.AUTO_DESTROY, True)
    lastCreatedMountain.bottom = scene.screen_height()
    lastCreatedMountain.left = leftPosition
    lastCreatedMountain.z = -15
def createTree():
    global tree
    tree = sprites.create_projectile_from_side(img("""
            . . . . . . . c c . . . . . . . 
                    . . . . c c c 6 5 c 6 6 . . . . 
                    . . . . c 6 c 5 5 c 7 6 . . . . 
                    . . . 6 c c 7 5 5 7 c 6 6 . . . 
                    . . c c 7 7 7 7 7 5 7 7 c 6 . . 
                    . 6 6 6 c 6 7 7 7 7 6 c c 6 6 . 
                    c 7 7 7 6 c 7 c 6 7 6 7 7 7 7 6 
                    c c c 6 6 6 c 6 6 6 6 7 7 6 6 6 
                    . c c 7 6 6 6 6 6 7 7 7 7 c 6 . 
                    . c 7 7 6 6 7 6 6 7 7 6 7 7 c . 
                    . c c c c 7 7 6 f 7 7 c c c c . 
                    . . . . c 7 c f f c 7 c . . . . 
                    . . . . . 6 f e e e c . . . . . 
                    . . . . . e e e d e e . . . . .
        """),
        -10,
        0)
    tree.z = -5
    tree.bottom = scene.screen_height()
    tree.set_flag(SpriteFlag.GHOST, True)
nearGroundCount = 0
tree: Sprite = None
cloud: Sprite = None
cloudImages: List[Image] = []
bird: Sprite = None
chosenAnimation: List[Image] = []
birdGoingRight: List[Image] = []
birdGoingLeft: List[Image] = []
flyingSaucer: List[Image] = []
saucer: Sprite = None
saucerSpeed = 0
lastCreatedMountain: Sprite = None
mountains: List[Image] = []
balloon: Sprite = None
balloonInflated: Image = None
balloonDeflated: Image = None
balloonDeflated = img("""
    ...................
        ...................
        .......fffff.......
        .....ff22222ff.....
        ....f222222442f....
        ...f22222222442f...
        ..f2222222222442f..
        .f222322223222422f.
        .f222322223222222f.
        .f222322223222222f.
        .f222232222322222f.
        .f222222222222222f.
        ..f2222322232222f..
        ..f2222233322222f..
        ...ff222222222ff...
        ....ffff222ffff....
        .....f.fffff.f.....
        .....f.......f.....
        .....f.......f.....
        ......f.....f......
        ......f.....f......
        .......f...f.......
        .......f.2.f.......
        ......fffffff......
        .....fcccccccf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fcbaaabcf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fccaaaccf.....
        ......fcccccf......
        .......fffff.......
""")
balloonInflated = img("""
    ...................
        ......fffffff......
        ....ff2222222ff....
        ...f22222222442f...
        ..f2222222222442f..
        .f222222222222442f.
        f22232222223222422f
        f22232222223222222f
        f22232222223222222f
        f22223222222322222f
        f22222222222222222f
        f22222222222222222f
        .f222232222232222f.
        .f222223333322222f.
        ..ff22222222222ff..
        ....ffff222ffff....
        .....f.fffff.f.....
        .....f.......f.....
        .....f.......f.....
        ......f.....f......
        ......f.....f......
        .......f...f.......
        .......f.2.f.......
        ......fffffff......
        .....fcccccccf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fcbaaabcf.....
        .....fcbbbbbcf.....
        .....fcabbbacf.....
        .....fccaaaccf.....
        ......fcccccf......
        .......fffff.......
""")
music.set_volume(0)
balloon = sprites.create(balloonDeflated, SpriteKind.player)
scene.set_background_color(9)
balloon.ay = 35
balloon.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
balloon.z = 100
info.set_score(0)
info.set_life(3)
createAnimationArrays()
mountains = [img("""
        ......................333333........................3333........................
            ...................333333333333...................3333333333....................
            ................333333333333333333..............3333333333333333................
            .............33333333333333333333333.........333333333333333333333333...........
            ..........333333333333333333333333333......333333333333333333333333333333.......
            ........3333333333333333333333333333333..33333333333333333333333333bb33333333...
            ......333333333bb3333333333333333b33333b3333333333333333333333333bbbb333333333..
            ....333333333333b33333333333333333b333bb3333333333333333333333bbbbbbbb333333333.
            ..3333333333333bbb33b3333333333b33bbbbbbbb3b33333333333333b3bbbbbbbbbb3333333333
            3333333333333333bb33b3333333333bbbbbbbbbbbbb33333333333333bbbbbbbbbbbbb3333b3333
            3333333333333b33bbbbbb33b3b3bbbbbbbbbbbbbbbbb333333333b33bbbbbbbbbbbbbbbb33b3333
            333333333333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3b333333bbbbbbbbbbbcbbbbbbbbbb3bb3
            333333b33bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb333bbbbbbbbbcbbbcccbbbbbbbbb3b33
            333b33bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbcbbcccccbccbbbbbbbbbb33
            333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccbccbbbbbbbbbb
            33bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccbccbbbbbbcb
            cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbccccccccccccbcccccccccccccbcbbcc
            cccbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbcccbccccccccccccccccccbcccccccccccccbccccc
            cccccbbcbbbbbbbbbbbbbbbbbbbbbbbbbcbcccccccccccccccccccccccccccccccccccccccbbcccc
            ccccccccbcbcbbbbbbbbbbbbbbbbbbcbcccccccccccccccccccccccccccccccccccccccccccccccc
            ccccccccccccbbcbbbbcbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccc
            ccccccccccccccccbcbcbbbbbbcbcccccccccccccccccccccccccccccccccccccccccccccccccccc
            ccccbcccccccccccccccccbcbbcccccccccbcccccccccccccccccccccccccccccccccccccccccccc
            ccccccbcccccccccccccccccccccccccccbccccccccccccccccccccccccccccccccccccccccccccc
            ccccbcccbcccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            ccccccccccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    """),
    img("""
        ....................3...........................................................
            ....................3...........................................................
            ...................333..........................................................
            ...................3333.........................................................
            ..................333333........................................................
            ..................33333333......................................................
            .................33333333333....................................................
            ................33333333333333..................................................
            ...............3333333333333333.......................3.........................
            ..............333333333333333333...................33333........................
            .............33333333333333333333...............333333333333....................
            ...........33333333333333333333333............3333333333333333..................
            ..........3333333333333333333333333..........3333333333333333333................
            ........3333333333333333333333333333.......3333333333333333333b333..............
            .....33333333333333333333333333333333...333333333333333333333bbb3333..........3.
            .33333333333333333333333333333333333333333333333333333333333bbbbb33333......3333
            33333333333333333333333333333333333333333333333333333333333333b33333333333333333
            333333333333333333333333333333333b333333333333333333333333333bb33333333333333333
            333333333333333333333333333333b3bbb3b3333333333333333333333bbbbb333333333b333333
            333333333333b33333333333333333bbbbbbb3333333333333333333bbbbbbbbb33333333bb33333
            333333333b33b33b33b333333b33bbbbbbbbbb333333333333bbbbbbbbbbbbbbb33333333bbb3333
            33333333bbbbbbbbbbbb3b333bbbbbbbbbbbbbb33333333bbbbbbbbbbbbbbbbbbb333333bbbb33b3
            3333b3bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbb3b3bbbbbbbbb
            c333bbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbbbbbbbbb3bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
            cccbbbbbbbbbbbbbbbbbbbbbbbbbcbbccccbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbcbbcc
            ccccbbbbbbbbbbbbbbbbbbbbbbbccccccbccbcbcbbbbbbbbbbbcbbccbbbbbbbbbbbbbbbbbbbcbccc
            ccccccbcbbbbbbbbbbbbbbbbbccccccccccccccccbbbbbbbcbbcccccccbcbbbbbbbbbbbbbcbccccc
            ccccccccbcbbbbbccbbbbbbcccccccccccccccccccccbcbcccccccccccccbbcbbbbbbbbbbccccccc
            cbccccccccbbcbccccbbcbcccccccccccccccccccccccccccccccccccccccccbbbbbcccccccccbcc
            cccccccccccccbbccbbbcccccbcbcccccccccccccccccccccccccccbccccbccccccccccccccccccc
            ccccccccccccccccccccccccccbcbcccccccccccccccccccccccbccccccccccccccccccccccccccc
            ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            ccccccccccccccccccccccccccccccccccccccccccccccbccccccccccccccccccccccccccccccccc
            ccccccbcbcbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbccccccccc
            ccccccccbcbccccccccccccccccccccccccccccccccccccccccccccccbcccccccccccccccccccccc
            ccccccccccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
            cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    """)]
sun = sprites.create(img("""
        ......................................................................444444444444444...........................................................................
            ..............................................................444444444444444444444444444444444.................................................................
            ........................................................44444444444444444444555555444444444444444444444.........................................................
            .....................................................444444444444444444444555555555544444444444444444444444444444...............................................
            ..................................................44444444444444444444445555555555555544444444444444444444444444444.............................................
            ...............................................44444444444444444444444455555555555555554444444444444444444444444444444444444....................................
            .......................................4444444444444444444444444444444455555555555555554444444444444444444444444444444444444444444444444........................
            .................................444444444444444444444444444444444444455555555555555555544444444444444444444444444444444444444444444444444444444................
            .........................44444444444444444444444444444444444444444444455555555555555555544444444444444444444444444444444444444444444444444444444444444444.......
            44444.......444444444444444444444444444444444444444444444444444444444555555555555555555554444444444444444444444444444444444444444444444444444444444444444444....
            444444444444444444444444444444444444444444444444444444444444444444444555555555555555555554444444444444444444444444444444444444444444444444444444444444444444444.
            4444444444444444444444444444444444444444444444444444444444444444444445555555555555555555544444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444445555555555555555555544444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444445555555555555555555544444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444555555555555555555444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444555555555555555555444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444455555555555555554444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444455555555555555554444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444445555555555555544444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444455555555554444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444555555444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
            4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    """),
    SpriteKind.Background)
sun.bottom = scene.screen_height()
sun.set_flag(SpriteFlag.GHOST, True)
sun.z = -20
placeMountain(0)
placeMountain(lastCreatedMountain.right)
game.set_dialog_frame(img("""
    ...cc......................cc....
        ..c55c..bbbb...bbbbb......c55c...
        .cb55bcbdddbbbbbdddbbbbbbcb55bc..
        b555555bbdddb111bdddb11db555555b.
        bb5555bbdbdb11111bdb1111bb5555bb.
        cb5555bcddd11111ddd11111cb5555bc.
        .c5bb5c1111d111d111d111ddc5bb5c..
        .cbbbbc111111111111111111cbbbbc..
        ..b11111111111111111111111d111bb.
        ..b111111111111111111111111d1bdb.
        ..bb11111111111111111111111dbddb.
        .bbdb1d11111111111111111111ddddb.
        .bdddd11111111111111111111d1bdbb.
        .bddbd11111111111111111111111bb..
        .bdb1d111111111111111111111111b..
        .bb111d11111111111111111111111b..
        ..b11111111111111111111111d111bb.
        ..b111111111111111111111111d1bdb.
        ..bb11111111111111111111111dbddb.
        .bbdb1d11111111111111111111ddddb.
        .bdddd11111111111111111111d1bdbb.
        .bddbd11111111111111111111111bb..
        .bdbb1111111111111111111111111b..
        .bbbd1111111111111111111111111b..
        ..bcc111111111111111111111dccdb..
        ..c55c111d111d111d111d1111c55cb..
        .cb55bcdd11111ddd11111dddcb55bc..
        b555555b11111bdb11111bdbb555555b.
        bb5555bbb111bdddb111bdddbb5555bb.
        cb5555bcdbbbbbdddbbbbbddcb5555bc.
        .c5bb5c.bb...bbbbb...bbbbc5bb5c..
        .cbbbbc..................cbbbbc..
        .................................
"""))
game.show_long_text("Stay in the air as long as you can! Hold any   button to turn on the burner.",
    DialogLayout.CENTER)
for index in range(2):
    spawnSomething(randint(0, 40))

def on_on_update():
    info.change_score_by(1)
game.on_update(on_on_update)

def on_on_update2():
    balloon.vy = Math.constrain(balloon.vy, -25, 25)
game.on_update(on_on_update2)

def on_update_interval():
    spawnSomething(randint(0, 100))
game.on_update_interval(750, on_update_interval)

def on_forever():
    global nearGroundCount
    nearGroundCount = -1
    while balloon.bottom >= scene.screen_height() - 1:
        balloon.say("pull up!", 100)
        nearGroundCount += 1
        if nearGroundCount > 25:
            info.change_life_by(-1)
            nearGroundCount = -20
        pause(25)
forever(on_forever)

def on_update_interval2():
    # changing position explicitly to avoid fractions of
    # movement / clipping
    for value in sprites.all_of_kind(SpriteKind.Mountain):
        value.x += -1
    if lastCreatedMountain.right < scene.screen_width():
        placeMountain(lastCreatedMountain.right)
game.on_update_interval(200, on_update_interval2)
