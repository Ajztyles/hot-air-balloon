namespace SpriteKind {
    export const Background = SpriteKind.create()
    export const Mountain = SpriteKind.create()
}

function spawnSomething(roll: number) {
    if (roll <= 2) {
        createSaucer()
    } else if (roll <= 6) {
        createTree()
    } else if (roll <= 24) {
        createCloud()
    } else if (roll <= 40) {
        createBird()
    }
    
}

function createSaucer() {
    
    if (Math.percentChance(50)) {
        saucerSpeed = 40
    } else {
        saucerSpeed = -40
    }
    
    saucer = sprites.createProjectileFromSide(img`
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
        `, saucerSpeed, 0)
    animation.runImageAnimation(saucer, flyingSaucer, 400, true)
    saucer.y = randint(10, scene.screenHeight() - 10)
}

controller.anyButton.onEvent(ControllerButtonEvent.Pressed, function on_button_pressed() {
    balloon.startEffect(effects.fire)
    balloon.startEffect(effects.fire)
    balloon.ay = -50
    balloon.setImage(balloonInflated)
})
function createAnimationArrays() {
    
    flyingSaucer = [img`
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
        `, img`
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
        `]
    birdGoingLeft = [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `]
    birdGoingRight = [img`
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
        `, img`
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
        `, img`
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
        `, img`
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
        `]
}

controller.anyButton.onEvent(ControllerButtonEvent.Released, function on_button_released() {
    balloon.ay = 50
    effects.clearParticles(balloon)
    balloon.setImage(balloonDeflated)
})
function createBird() {
    
    if (Math.percentChance(50)) {
        saucerSpeed = 20
        chosenAnimation = birdGoingRight
    } else {
        saucerSpeed = -20
        chosenAnimation = birdGoingLeft
    }
    
    bird = sprites.createProjectileFromSide(img`
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
        `, saucerSpeed, 0)
    animation.runImageAnimation(bird, chosenAnimation, 100, true)
    bird.y = randint(12, scene.screenHeight() - 10)
}

function createCloud() {
    
    cloudImages = [img`
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
        `, img`
            . . . 1 1 1 1 . . . 1 1 . . . . . . . . 
                    . . 1 1 1 1 1 1 . 1 1 1 1 . . . . . . . 
                    . 1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . 
                    . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 1 1 . . . 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 . . . . . . .
        `, img`
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
        `]
    cloud = sprites.createProjectileFromSide(cloudImages[randint(0, cloudImages.length - 1)], -5, 0)
    cloud.z = -10
    cloud.setFlag(SpriteFlag.Ghost, true)
    cloud.y = randint(0, scene.screenHeight() * 0.6)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.changeLifeBy(-1)
    otherSprite.setFlag(SpriteFlag.Ghost, true)
    sprite.say("ow!", 500)
})
function placeMountain(leftPosition: number) {
    
    lastCreatedMountain = sprites.create(mountains[randint(0, 1)], SpriteKind.Mountain)
    lastCreatedMountain.setFlag(SpriteFlag.Ghost, true)
    lastCreatedMountain.setFlag(SpriteFlag.AutoDestroy, true)
    lastCreatedMountain.bottom = scene.screenHeight()
    lastCreatedMountain.left = leftPosition
    lastCreatedMountain.z = -15
}

function createTree() {
    
    tree = sprites.createProjectileFromSide(img`
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
        `, -10, 0)
    tree.z = -5
    tree.bottom = scene.screenHeight()
    tree.setFlag(SpriteFlag.Ghost, true)
}

let nearGroundCount = 0
let tree : Sprite = null
let cloud : Sprite = null
let cloudImages : Image[] = []
let bird : Sprite = null
let chosenAnimation : Image[] = []
let birdGoingRight : Image[] = []
let birdGoingLeft : Image[] = []
let flyingSaucer : Image[] = []
let saucer : Sprite = null
let saucerSpeed = 0
let lastCreatedMountain : Sprite = null
let mountains : Image[] = []
let balloon : Sprite = null
let balloonInflated : Image = null
let balloonDeflated : Image = null
balloonDeflated = img`
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
`
balloonInflated = img`
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
`
music.setVolume(0)
balloon = sprites.create(balloonDeflated, SpriteKind.Player)
scene.setBackgroundColor(9)
balloon.ay = 35
balloon.setFlag(SpriteFlag.StayInScreen, true)
balloon.z = 100
info.setScore(0)
info.setLife(3)
createAnimationArrays()
mountains = [img`
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
    `, img`
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
    `]
let sun = sprites.create(img`
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
    `, SpriteKind.Background)
sun.bottom = scene.screenHeight()
sun.setFlag(SpriteFlag.Ghost, true)
sun.z = -20
placeMountain(0)
placeMountain(lastCreatedMountain.right)
game.setDialogFrame(img`
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
`)
game.showLongText("Stay in the air as long as you can! Hold any   button to turn on the burner.", DialogLayout.Center)
for (let index = 0; index < 2; index++) {
    spawnSomething(randint(0, 40))
}
game.onUpdate(function on_on_update() {
    info.changeScoreBy(1)
})
game.onUpdate(function on_on_update2() {
    balloon.vy = Math.constrain(balloon.vy, -25, 25)
})
game.onUpdateInterval(750, function on_update_interval() {
    spawnSomething(randint(0, 100))
})
forever(function on_forever() {
    
    nearGroundCount = -1
    while (balloon.bottom >= scene.screenHeight() - 1) {
        balloon.say("pull up!", 100)
        nearGroundCount += 1
        if (nearGroundCount > 25) {
            info.changeLifeBy(-1)
            nearGroundCount = -20
        }
        
        pause(25)
    }
})
game.onUpdateInterval(200, function on_update_interval2() {
    //  changing position explicitly to avoid fractions of
    //  movement / clipping
    for (let value of sprites.allOfKind(SpriteKind.Mountain)) {
        value.x += -1
    }
    if (lastCreatedMountain.right < scene.screenWidth()) {
        placeMountain(lastCreatedMountain.right)
    }
    
})
