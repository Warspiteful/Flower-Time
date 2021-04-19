# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



init python:
    config.debug_sound = True
    artist = ('Artist', 'Lucass0717'), ("Artist", "Elena @lennie_ok"),
    voiceActors = ("Voice Actor", "Ian Arlyn"),('Voice Actor','Megan Karow'), ('Voice Actor','Raydee99 - https://www.raydee99.com/'),('Voice Actor', 'Lindsay Jackman') #each parenthesis is a different line of credit#
    composers = ('Composer','Donovan'), ('Composer','Raydee99 - https://www.raydee99.com/')
    writers = ("Writer", "Jonathon Bickelhaupt @AmIAlwrite"), ("Writer", "Jade Edwards @jadegalexandria"), ('Writer', 'Birbstille'), ("Writer", "Scrapsnomancer"), ('Programmer & Writer', 'Warspiteful')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in artist:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in voiceActors:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in composers:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    for c in writers:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]


define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define mushFloor = Position(ypos=0.4)

####### CACTUS ########
label cactus_AwLove:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound'./voice/Bytes/cactus_AwLove1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/cactus_AwLove2.wav'
    else:
        play sound './voice/Bytes/cactus_AwLove3.wav'
    return
label cactus_AwNah:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/cactus_AwNah1.wav'
    else:
        play sound './voice/Bytes/cactus_AwNah2.wav'
    return
label cactus_AwShucks:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/cactus_AwShucks1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/cactus_AwShucks2.wav'
    else:
        play sound './voice/Bytes/cactus_AwShucks3.wav'
    return
label cactus_er:
    play sound './voice/Bytes/cactus_er_1.wav'
    return
label cactus_FairNough:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/cactus_FairNough1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/cactus_FairNough2.wav'
    else:
        play sound './voice/Bytes/cactus_FairNough3.wav'
    return
label cactus_GettingLate:
    return
    play sound './voice/Bytes/cactus_GettingLate.wav'
label cactus_GladToHaveYa:
    play sound './voice/Bytes/cactus_GladToHaveYa.wav'
    return
label cactus_GoodOne:
    play sound './voice/Bytes/cactus_GoodOne.wav'
    return
label cactus_heheh:
    play sound './voice/Bytes/cactus_heheh.wav'
    return
label cactus_hmm:
    play sound './voice/Bytes/cactus_hmm.wav'
    return
label cactus_Howdy:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/cactus_Howdy1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/cactus_Howdy2.wav'
    else:
        play sound './voice/Bytes/cactus_Howdy3.wav'
    return
label cactus_mhm:
    play sound './voice/Bytes/cactus_mhm.wav'
    return
label cactus_sigh:
    play sound './voice/Bytes/cactus_sigh.wav'
    return
label cactus_ThanksPardner:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/cactus_ThanksPardner1.wav'
    else:
        play sound './voice/Bytes/cactus_ThanksPardner2.wav'
    return
label cactus_YerRight:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/cactus_YerRight1.wav'
    elif sfx == 2:
        play sound 'cactus_YerRight2.wav'
    else:
        play sound './voice/Bytes/cactus_YerRight3.wav'
    return
####### ROSE ########
label Rose_HeyHappy:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_HeyHappy1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_HeyHappy2.wav'
    return
label Rose_HeySad:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_HeySad1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_HeySad2.wav'
    return
label Rose_NervousLaughter:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_NervousLaughter1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_NervousLaughter2.wav'
    return
label Rose_Oh:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_Oh1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_Oh2.wav'
    return
label Rose_OhGod:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_OhGod1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_OhGod2.wav'
    return
label Rose_OhHm:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_OhHm1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_OhHm2.wav'
    return
label Rose_OhNo:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_OhNo1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_OhNo2.wav'
    return
label Rose_OK:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_OK1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_OK2.wav'
    return
label Rose_Sigh:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_Sigh1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_Sigh2.wav'
    return
label Rose_Sorry:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_Sorry1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_Sorry2.wav'
    return
label Rose_UhHuh:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1 :
        play sound './voice/Bytes/Rose/Rose_UhHuh1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_UhHuh2.wav'
    return
label Rose_Yay:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Rose/Rose_Yay1.wav'
    else:
        play sound './voice/Bytes/Rose/Rose_Yay2.wav'
    return

####### MUSHROOM ########

## ANGRY ##
label Mushroom_A_FUNGEDABOUTIT:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound'./voice/Bytes/Angry/Mushroom_FUNGEDABOUTIT1.wav'
    else:
        play sound './voice/Bytes/Angry/Mushroom_FUNGEDABOUTIT2.wav'
    return
define Mushroom_getouttatown = ['./voice/Bytes/Angry/Mushroom_getouttatown!1.wav','./voice/Bytes/Angry/Mushroom_getouttatown!2.wav','./voice/Bytes/Angry/Mushroom_getouttatown!3.wav']
define Mushroom_heynow = ['./voice/Bytes/Angry/Mushroom_heynow!1.wav']
label Mushroom_IMSHROOMINHERE:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/Angry/Mushroom_IMSHROOMINHERE1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/Angry/Mushroom_IMSHROOMINHERE2.wav'
    else:
        play sound './voice/Bytes/Angry/Mushroom_IMSHROOMINHERE3.wav'
    return
define Mushroom_watchit = ['./voice/Bytes/Angry/Mushroom_watchit!1.wav','./voice/Bytes/Angry/Mushroom_watchit!2.wav']

## Blush ##
label Mushroom_badading:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/Blush/Mushroom_badading!1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/Blush/Mushroom_badading!2.wav'
    elif sfx == 3:
        play sound './voice/Bytes/Blush/Mushroom_badading!3.wav'
    else:
        play sound './voice/Bytes/Blush/Mushroom_badading!4.wav'
    return
define Mushroom_heynow = ['./voice/Bytes/Blush/Mushroom_heynow...1.wav','./voice/Bytes/Blush/Mushroom_heynow...2.wav','./voice/Bytes/Blush/Mushroom_heynow...3.wav']
label Mushroom_woah:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound './voice/Bytes/Blush/Mushroom_woah1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/Blush/Mushroom_woah2.wav'
    else:
        play sound './voice/Bytes/Blush/Mushroom_woah3.wav'
    return

## Happy ##
define Mushroom_Ahaa = ['./voice/Bytes/Happy/Mushroom_Ahaa.wav']
define Mushroom_Ayy = ['./voice/Bytes/Happy/Mushroom_Ayy1', './voice/Bytes/Happy/Mushroom_Ayy2', './voice/Bytes/Happy/Mushroom_Ayy3']
label MushroomHappy_BadaBing:
    $ sfx = renpy.random.randint(1,3)
    if sfx == 1:
        play sound'./voice/Bytes/Happy/Mushroom_BadaBing!1.wav'
    elif sfx == 2:
        play sound './voice/Bytes/Happy/Mushroom_BadaBing!2.wav'
    else:
        play sound './voice/Bytes/Happy/Mushroom_BadaBing!3.wav'
    return
define Mushroom_Fungedaboutit = ['./voice/Bytes/Happy/Mushroom_Fungedaboutit!1.wav','./voice/Bytes/Happy/Mushroom_Fungedaboutit!2.wav']
label MushroomHappy_FUNGEDABOUTIT:
    play sound './voice/Bytes/Happy/Mushroom_FUNGEDABOUTIT1.wav'
    return
label Mushroom_Yo:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Happy/Mushroom_Yo!1.wav'
    else:
        play sound './voice/Bytes/Happy/Mushroom_Yo!2.wav'
    return

## Sad ##
label Mushroom_badagloom:
    $ sfx = renpy.random.randint(1,4)
    if sfx == 1:
        play sound './voice/Bytes/Sad/Mushroom_badagloom1.wav'

    elif sfx == 2:
        play sound './voice/Bytes/Sad/Mushroom_badagloom2.wav'

    elif sfx == 3:
        play sound './voice/Bytes/Sad/Mushroom_badagloom3.wav'

    else:
        play sound './voice/Bytes/Sad/Mushroom_badagloom4.wav'
    return
define Mushroom_fungedaboutit = ['./voice/Bytes/Sad/Mushroom_fungedaboutit...1.wav','./voice/Bytes/Sad/Mushroom_fungedaboutit...2.wav','./voice/Bytes/Sad/Mushroom_fungedaboutit...3.wav']
label Mushroom_sigh:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Sad/Mushroom_sigh1.wav'
    else:
        play sound './voice/Bytes/Sad/Mushroom_sigh2.wav'
return

## Surprised ##
define Mushroom_huh = ['./voice/Bytes/Surprised/Mushroom_huh_1.wav','./voice/Bytes/Surprised/Mushroom_huh_2.wav']
define Mushroom_really = ['./voice/Bytes/Surprised/Mushroom_really_1.wav','./voice/Bytes/Surprised/Mushroom_really_2.wav','./voice/Bytes/Surprised/Mushroom_really_3.wav','./voice/Bytes/Surprised/Mushroom_really_4.wav']
label MushroomSurprise_woah:
    play sound './voice/Bytes/Surprised/Mushroom_woah!1.wav'
    return
define Mushroom_woahmama = ['./voice/Bytes/Surprised/Mushroom_woahmama!1.wav', './voice/Bytes/Surprised/Mushroom_woahmama!2.wav', './voice/Bytes/Surprised/Mushroom_woahmama!3.wav']
define Mushroom_woahsapling = ['./voice/Bytes/Surprised/Mushroom_woahsapling1.wav','./voice/Bytes/Surprised/Mushroom_woahsapling2.wav','./voice/Bytes/Surprised/Mushroom_woahsapling3.wav']

####### SUNFLOWER ########

label Sun_Blush:
    play sound './voice/Bytes/Sunflower/Blushy.wav'
    return
label Sun_Mutter:
    play sound './voice/Bytes/Sunflower/AmbientMuttering .wav'
    return
label Sun_Fine:
    $ sfx = renpy.random.randint(1,2)
    if sfx == 1:
        play sound './voice/Bytes/Sunflower/ImFine1.wav'
    else:
        play sound './voice/Bytes/Sunflower/ImFine2.wav'
    return
label Sun_Laugh:
    play sound './voice/Bytes/Sunflower/Teehee.wav'
    return
label Sun_Surprised:
    play sound './voice/Bytes/Sunflower/Surprised.wav'
    return
label Sun_Sing:
    play sound './voice/Bytes/Sunflower/Singing (I am so sorry).wav'
    return
label Sun_GeeHappy:
    play sound './voice/Bytes/Sunflower/GeeHappy.wav'
    return
label Sun_Mhm:
    play sound './voice/Bytes/Sunflower/Mmhm.wav'
    return
label Sun_Shake:
    play sound './voice/Bytes/Sunflower/Shakespeare.wav'
    return
####### IMAGES ######

######## Sunflower Images ##################################
image Char Sun Base:
    "./images/Sunflower/sunflower neutral face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun Happy:
    "./images/Sunflower/sunflower happy face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun Blush:
    "./images/Sunflower/sunflower blush face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun Sad:
    "./images/Sunflower/sunflower sad face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun Surprise:
    "./images/Sunflower/sunflower surprised face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun Angry:
    "./images/Sunflower/sunflower angry face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
image Char Sun VHappy:
    "./images/Sunflower/sunflower veryHappy face gamejam.png"
    zoom .65
    yalign 0.0
    ypos -75
##################Mushroom Images##############################
image Char Mush Base:
    "./images/Mushroom/Base.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Happy:
    "./images/Mushroom/Happy.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Blush:
    "./images/Mushroom/Blush.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Sad:
    "./images/Mushroom/Sad.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Surprise:
    "./images/Mushroom/Surprised.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Angry:
    "./images/Mushroom/Angry.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Joke:
    "./images/Mushroom/Joke.PNG"
    zoom .75
    yalign 0.0
    ypos -175
image Char Mush Reverse:
    "./images/Mushroom/Flip.PNG"
    zoom .75
    yalign 0.0
    ypos -175
######## Cactus Images ##################################
image Char Cac Base:
    "./images/Cactus/cactus neutral game jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Base Flower:
    "./images/Cactus/cactus_neutral_game_jam_hat.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Happy:
    "./images/Cactus/cactus happy game jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Blush:
    "./images/Cactus/cactus blush game jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Sad:
    "./images/Cactus/cactus sad game jam hat.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Surprise:
    "./images/Cactus/cactus surprise game jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Angry:
    "./images/Cactus/cactus_angry_game_jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Sweat:
    "./images/Cactus/cactus nervous game jam.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Sweat Flower:
    "./images/Cactus/cactus nervous game jam hat.png"
    zoom .80
    yalign 0.0
    ypos -200
image Char Cac Happy Flower:
    "./images/Cactus/cactus_happy_game_jam_hat.png"
    zoom .80
    yalign 0.0
    ypos -200

######## Rose Images ##################################
image Char Rose Base:
    "./images/Rose/rose neutral face game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Happy:
    "./images/Rose/rose happy face game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Blush:
    "./images/Rose/rose blush face game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Sad:
    "./images/Rose/rose sad game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Surprise:
    "./images/Rose/rose surprised game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Angry:
    "./images/Rose/rose angry game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Wink:
    "./images/Rose/rose wink face game jame.png"
    zoom .6
    yalign 0.0
    ypos 10
image Char Rose Nervous:
    "./images/Rose/rose_nervous_laughter_game_jame_.png"
    zoom 0.6
    yalign 0.0
    ypos 10
image Char Rose Done:
    "./images/Rose/rose_done_with_shit_game_jame_.png"
    zoom 0.6
    yalign 0.0
    ypos 10
#############################Backgrounds####################
image Open:
    "./images/Backgrounds/Flowershop_Storefront_updated.png"
    zoom .5
image Rose1:
    "./images/Backgrounds/Flowershop_Rose_BG_1_updated.png"
    zoom .5
image cashier:
    "./images/Backgrounds/Flowershop_Storefront_updated_2.png"
    zoom .5
image Cactus1:
    "./images/Backgrounds/Flowershop_Cactus_BG_1_updated.png"
    zoom .5
image Fungi1:
    "./images/Backgrounds/Flowershop_Fungi_BG_1_updated.jpg"
    zoom .5
image Fungi2:
    "./images/Backgrounds/Flowershop_Fungi_BG_2_updated.jpg"
    zoom .5
image Sunflower1:
    "./images/Backgrounds/Flowershop_Sunflower_BG_updated.png"
    zoom .5
image Window:
    "./images/Backgrounds/Flowershop_SideView_updated.png"
    zoom .5
image Rose2:
    "./images/Backgrounds/Flowershop_Rose_BG_2_updated.png"
    zoom .5
image NightRose:
    "./images/Backgrounds/Flowershop_Rose_BG_1_updated_night.png"
    zoom .5
image NightFight:
    "./images/Backgrounds/Flowershop_Storefront_updated_night copy.png"
    zoom .5
#####################################################################
image note:
    "./images/MUSHROOM_EPIC.png"
    zoom .35
    ypos .65
###################

##### AUDIO #######
##### Music #####
define audio.sunflower = "./audio/A Happy Little Sunflower.wav" ### Sunflower
define audio.fungi = "./audio/A Funky Little Funkgus.wav" ### Fungi
define audio.rose = "./audio/A Flirty Little Rose.wav" ## Rose
define audio.chrys = "./audio/A Little Tune for Chrys.wav" ## Chrys
define audio.mainloop =   "<from 13 to 88>./audio/A Little Tune for Chrys.wav"
define audio.cactus = "./audio/A Spiky Little Buckeroo.wav" ## Cactus
define audio.badEnd = "./audio/SadBoyFlowers.wav"
define audio.roseNightime = "./Psychotic-breakdown-RILF.mp3"
define audio.roseConfront = "./audio/RILF-but-spoopier.mp3"
#############################################################################

label before_main_menu:
    play music chrys noloop
    queue music mainloop loop
    return
#############################Character Declarations#############################################
define ce = Character("Chrysanthemum", color="FFFFFF", who_outlines=[ (1, "#000000") ])
define mc = Character("Chrys",color="FFFFFF",who_outlines=[ (1, "#000000") ])
define r = Character("Rose", color = "CC0000",who_outlines=[ (1, "#000000") ])
define m = Character("Mushroom",color = "330000",who_outlines=[ (1, "#000000") ])
define s = Character("Sunflower", color = "FFFF33",who_outlines=[ (1, "#000000") ])
define u = Character("???",color="FFFFFF",who_outlines=[ (1, "#000000") ])
define c = Character("Cactus", color = "33FF00",who_outlines=[ (1, "#000000") ])
define sp = Character("Sprout", color = "33FF00",who_outlines=[ (1, "#000000") ])

###################################################################################


# The game starts here.

label start:

    $ favorSun = 0
    $ favorRose = 0
    $ favorMush = 0
    $ favorCact = 0
    $ ending = 0
    play music mainloop

    "You're a small plant in a big city."
    scene Open with dissolve
    "You arrived in this little downtown plant shop this morning, after a few hours in the dark back of a van. You're excited by the prospect of maybe being bought. You're part of the last shipment of Valentine's Day flowers, after all."
    "But you're also nervous, and curious, as to what floral friends might await you."
    "As you and your fellow flowers are placed in the shop, you catch a glimpse of some of the other residents..."
    show Char Rose Base with dissolve
    "A dashing rose..."
    show Char Cac Base with dissolve
    "A kindly cactus..."
    show Char Mush Base with dissolve
    "A macho mushroom..."
    show Char Sun Base with dissolve
    "And a sweet sunflower."
    hide Char with dissolve
    scene cashier with dissolve
    "You're placed down next to the sunflower."
    show Char Sun Happy with dissolve
    play music sunflower
    s "Oooo! Fresh flora!"
    s "Hehe, hi there! What's your name?"
    menu:
        "I'm Chrysanthemum...":
            pass
    menu:
        "But you can call me Chrys.":
            pass
    s "Hi Chrys! Welcome to the shop!"
    s "Oh, it's always so exciting when the last of the Valentine's Day shipment comes in!"
    call Sun_Laugh from _call_Sun_Laugh
    s "This shop has a deal where you can buy plants in pairs, which means usually you end up leaving with somebody! Teehee!"
    show Char Sun Blush
    s "So it's good to get to know your fellow plants, if you know what I'm saying..."
    show Char Sun Happy
    s "Would you like me to introduce you to everybody?"
    menu:
        "That'd be awesome, thank you!":
            pass
    s "No problem!"





    show Char Sun Happy
    s "Soooo, who's up first? Who d'ya wanna meet?"
    $ paths = [0, 1, 2, 3]
    $ lastPath = -1
    jump meetPlants

label meetPlants:

    scene cashier
    show Char Sun Happy
    if len(paths) != 4:
        if lastPath != 3:
            s "Hey, hey! Welcome back."
        s "Want to see someone else?"
    menu:
        "Mushroom" if 0 in paths :
            call Sun_Laugh from _call_Sun_Laugh_1
            s "Teehee, you're interested in cool guy Mushroom, huh? Yeah, they're dreamy..."
            show Char Sun Surprise
            s "Maybe it's just the spores."
            show Char Sun Blush
            s "Anyways, I'll take you right to them, they're a bit out of the way."
            show Char Sun Happy
            s "Follow me!"
            jump mushroom
        "Cactus" if 1 in paths:
            s "Oooooo, I love Cactus! They might look abrasive but he's really sweet as a peach! Teehee!"
            jump cactus
        "Rose" if 2 in paths:
            s "Oh, Rose! It's like Shakespeare says..."
            s "A rose named Rose is... sweet?"
            r "Oh, Sunflower! Allow me to take it from here."
            jump rose
        "I want to hear about you!" if 3 in paths:
            jump sunflower
        "I'm done here" if len(paths) != 4:
            scene cashier with fade
            "Looking around, you spot Rose and Cactus near the other succulents. They seem to be practicing something, though by the sounds of it, it's not going great..."
            "Meanwhile, out of the corner of your vision, you see (and hear) a very, very loud commotion. Is- Is that Sunflower and Mushroom?"
            menu:
                "Oh man... I wonder who I should check in with?":
                    pass
            menu:
                "Sunflower and Mushroom":
                    jump SvMConflict
                "Rose and Cactus":
                    jump RvCConflict

label mushroom:
    $favorMush += 1
    $ lastPath = 0
    $ paths.remove(0)
    play music fungi
    scene Fungi1 with dissolve

    "You see a… mushroom? They’re wearing sunglasses? And popping one of the rudest squats you’ve ever seen squatted. The power it radiates? Immense."
    "They rise to greet you."
    show Char Mush Joke with dissolve

    m "New plant in town, huh? Name’s Mushroom! They/them."
    menu:
        "They sell mushrooms in this shop?":
            pass
    m "You see a pot on me? Nah there’s just a whole fungal colony growin’ in the walls of this place."
    menu:
        "Sounds like the kind of thing the shop owner should get looked at.":
            show Char Mush Angry
            m "Hey man, that’s your opinion and I’d ask ya to keep that to yourself."
            m "Just…"
            show Char Mush Joke
            call MushroomHappy_FUNGEDABOUTIT from _call_MushroomHappy_FUNGEDABOUTIT
            m "FUNGEDABOUTIT!"
        "Nice! A shop with unique neighbors.":
            show Char Mush Blush
            m "Heh, yeah I’m like your cool, fun neighbor. Always there with a smile and a devil-may-care. Y’know?"
            show Char Mush Joke
            call MushroomHappy_FUNGEDABOUTIT from _call_MushroomHappy_FUNGEDABOUTIT_1
            m "FUNGEDABOUTIT!"
    m "Anyways, if you’re ever lookin’ to ditch these squares ya know where to find me! Maybe we can engage in a friendly little flexing competition. Gotta warn ya though, I’m undefeated!"
    m "Now, follow me, buddy. Just go right down there and you'll be back with Sunflower."
    m "Catch you on the flipside!"
    play music sunflower
    jump meetPlants
################## Rose Route #################################
label rose:
    $ favorRose +=1
    $ lastPath = 2
    $ paths.remove(2)
    play music rose
    scene Rose1

    show Char Rose Base
    r "Oh, my, my. Hello, gorgeous. Who might you be? "
    menu:
        "Uh, hello?":
            show Char Rose Happy
            r "Oh, a shy one, aren't you? Well, I'm sure you'll warm up soon enough, we've got ourselves a fine gathering of the friendliest people around."
        "Right back at you, cutie!":
            show Char Rose Blush
            r "Aww, you sure know to make this girl's heart flutter."
    show Char Rose Base
    r "You must be the new flower around here. The name's Rose. It's a pleasure to meet you."
    r "I have to say, you've arrived at quite the interesting time. Around this time, we see a lot of exports, but not too many going the other way."
    show Char Rose Sad
    r "It's always a bit tough to say goodbye to everyone but, that's life."
    menu:
        "I'm sorry to hear that.":
            jump sorry
        "What's going on?":
            jump context

label sorry:
    show Char Rose Base
    r "Oh, honey, don't be."
    r "It's...a natural part the cycle of life. Can't say it hurts any less though."
    r "I figure the best way to handle it is to just keep living each day out nice and proud. "
    menu:
        "That's a nice way to think about it.":
            jump think
        "Is that really okay?":
            jump okay
label think:
    show Char Rose Happy
    r "Haha, thanks, love."
    show Char Rose Base
    r "I sure hope I'm doing the right thing."
    r "I suppose I shouldn't hold you up with my self pity though."
    r "Now, let's get back to business, then?"
    jump ask
label okay:
    r "Sigh..."
    r "Look here. I know it's far from perfect, but it's what we've got. If you want all the answers, I'm not your girl."
    show Char Rose Happy
    r "But I'd like to think I'm a pretty fine-looking gal, and I've rolled a pretty good lot in life all things considered."
    r "I've got no intentions of moping around in regrets, thinking of what could have been and all that nonsense."
    r "And I'll be damned if I let any destiny or fate screw with me."
    menu:
        "\*clap\*":
            r "Ahaha, yes! I'm pretty amazing, aren't I?"
        "Uh...wow.":
            show Char Rose Surprise
            r "Ahahahaha...oh..."
    show Char Rose Blush
    r "Oh god...uh...I really got into it, didn't I?"
    menu:
        "You sure did":
            r "Ah! Um...please try to forget that happened..."
            menu:
                "Well, if you say so...":
                    show Char Rose Happy
                    r "Ahaha, thanks."
                    jump understand
                "No can do!":
                    show Char Rose Blush
                    r "Aww, you big tease!"
                    show Char Rose Base
                    r "Hmph, and I was trying to be cool, too."
                    menu:
                        "Haha, sorry.":
                            r "Well...I suppose I can forgive you just this once. Hmph."
                            jump understand
                        "You're more cute than cool.":
                            show Char Rose Blush
                            r "Eh? Oi! You!"
                            show Char Rose Angry
                            r "You can't just say that, you know!"
                            menu:
                                "Why?":
                                    show Char Rose Surprise
                                    r "Wha-? Are you serious right now?"
                                    show Char Rose Blush
                                    r "{i}*Ahem*{/i}"
                                    show Char Rose Base
                                    r "Look, we've just met, so let's just end it there, okay?"
                                    menu:
                                        "Alright.":
                                            show Char Rose Blush
                                            r "Oh, thank goodness. You really had me sweating there."
                                            show Char Rose Happy
                                            r "Now, let's get back to business, then?"
                                            jump ask
                                        "Aww...":
                                            show Char Rose Blush
                                            r "Oh, come on, lay off me a little, won't you?"
                                            show Char Rose Angry
                                            r "Hmph, meanie."
                                            show Char Rose Blush
                                            r "But if you ask really nicely, I suppose I can help answer any questions you might have for me."
                                            menu:
                                                "Please?":
                                                    jump ask
                                "Sorry.":
                                    show Char Rose Blush
                                    r "Well...I suppose I can forgive you just this once. Hmph."
                                    jump understand
        "It happens.":
            show Char Rose Base
            r "Well...that's a bit embarrassing. Thanks for your understanding though."
            jump understand
label understand:
    show Char Rose Base
    r "As you probably saw, I have some pretty strong opinions. Hope I didn't scare you off though."
    menu:
        "It's alright.":
            show Char Rose Happy
            r "Thanks, love."
            show Char Rose Base
            r "Now, let's get back to business, then?"
            jump ask
        "*stay silent*":
            show Char Rose Base
            r "Um...well...ahaha. Maybe I can help with you something?"
            jump ask

label context:
    show Char Rose Surprise
    r "Oh? I don't suppose you know what time of the year it is, do you?"
    menu:
        "No?":
            show Char Rose Angry
            r "You're not pulling my leg, are you? I'm being completely serious, this is pretty commmon knowledge."
            show Char Rose Base
            r "Well, I guess someone has to teach you."
            r "Listen up, we're coming up on a special day called Valentines Day."
        "Valentine's Day.":
            show Char Rose Base
            r "Oh? So you do know the day."
    show Char Rose Sad
    r "When it comes to Valentines, a lot of good flowers get shipped out the door to never return."
    r "It's always been a painful time, every year."
    menu:
        "I'm sorry to hear that.":
            jump sorry
        "Oh, I didn't know.":
            show Char Rose Base
            r "It's alright, although I have to say I'm a bit envious about where you're from."
            show Char Rose Sad
            r "Must be nice..."
            menu:
                "I'm sorry.":
                    jump sorry
                "*stay silent*":
                    show Char Rose Base
                    r "Um...well...ahaha. Maybe I can help with you something?"

label ask:
    show Char Rose Base
    r "Is there anything else you're wondering about?"
    menu:
        "Do you do anything for fun?":
            show Char Rose Happy
            r "Fun? Well, there's never a dull moment with everyone we have here."
            show Char Rose Base
            r "I see you've met Sunflower already."
            menu:
                "She's nice.":
                    show Char Rose Happy
                    r "I'm glad to hear that. She's always been one of the friendliest plants here."
                    show Char Rose Base
                    r "Treat her nicely, ok?"
                "She's cute.":
                    show Char Rose Happy
                    r "I know, right? Aww, I'm sure you two will get along splendidly."
                    r "You better let her know, she'll be over the moon."
                    show Char Rose Base
                    r "It'd be a nice change for her. It's been a while since..no, it's not my place."
                    show Char Rose Happy
                    r "Anyways, tell her that, ok? Even she needs a pick-up every so often."
                    jump talkoptions
        "How are things?":
            jump thingsRose
        "Nope.":
            r "Well, I suppose I'll see you to Sunflower again then?"
            play music sunflower
            jump meetPlants
label talkoptions:
    show Char Rose Base
    r "Want to talk about anything else?"
    menu:
        "How are things?":
            jump thingsRose
        "Nope.":
            r "Well, I suppose I'll see you to Sunflower again then?"
            play music sunflower
            jump meetPlants

label thingsRose:
    r "Well, things have been quiet."
    r "Well...I say that, but it's been a rough past month or so..."
    r "We lost a lot of good flowers recently, so it's been tough on all of us."
    r "But well, we just have to keep going, right?"
    r "For their sake."
    r "Anyways, I rambled long enough. I'll take you back to Sunflower, alright?"
    play music sunflower
    jump meetPlants
################## Cactus Route #################################

label cactus:
    $ favorCact +=1
    $ lastPath = 1
    $ paths.remove(1)
    play music cactus
    scene Cactus1

    show Char Cac Base
    c "Howdy. The name’s Cactus. Carnegiea gigantea cactus."
    c "But you can just call me Cactus."
    c "Been a while since we've gotten a new shipment of plants like you. "
    c "If you've got questions for me 'bout how things work 'round here, by all means feel free to ask."
    menu:
        "What's with the Southern vibes?":
            show Char Cac Happy
            c "Well you're talkin' to a bona-fide Souther Saguaro. Texas born and raised."
            show Char Cac Base
            c "Bit unusual to see among all these flowers and succulents, I know, but I made the choice to move up all the way here."
            call cactus_sigh from _call_cactus_sigh
            c "Sometimes though I sure do miss the feelin' of that warm Texas sun..."
            c "'Specially when you're on the windowsill with all your loved ones... it really warms my spines."
            menu:
                "Spines?":
                    show Char Cac Sweat
                    c "Er, Not like them human spines if that's what you're thinkin' of."
                    show Char Cac Base
                    c "More like my spikes 'n all. They're called spines."
                    jump smallTalk


                "Aw, got a family back home?":
                    show Char Cac Happy
                    c "I sure do!"
                    c "I've got my Ma and Pa in Texas, but the extended family's real spread out."
                    c "We got Grandmama Old Lady Hardee and her side of the family in a fancy plant nursery in Arizona, Great-Aunt Opuntia in New Mexico, Uncle Fishhook up in Colorado..."
                    jump smallTalk

        "How long have you been here?":
            show Char Cac Happy
            c "A good while!"
            show Char Cac Base
            c "I moved here back durin' the summer of last year. Feels like ages ago."
            show Char Cac Happy
            c "But I promise I'm not that old! You can probably tell how old I am just by lookin' at me."
            show Char Cac Sweat
            call cactus_er from _call_cactus_er
            c "Er, well. Maybe it's not as obvious to folks up here."
            c "Compared to like. Y'know. Home."
            jump smallTalk

label smallTalk:
    show Char Cac Base
    menu:
        "...":
            c "..."
    menu:
        "...":
            c "..."
    menu:
        "...":
            pass
    show Char Cac Sweat
    c "Yeah."
    show Char Cac Base
    c "Sorry. I'm not exactly the best at this... small talk thing. You'd probably do better talkin' to the others if you wanna strike up a conversation. Day's still young."
    menu:
        "Alright, see you around.":
            play music sunflower
            jump meetPlants
        "Nah, I don't mind spending time with you.":
            show Char Cac Surprise
            c "... Really?"
            c "Huh. First time for everything I guess."
            show Char Cac Sweat
            c "It's not like you're weird or anything though!"
            show Char Cac Base
            c "Just... never really got the chance to hang out with the other flowers here."
            show Char Cac Happy
            c "Save for Rose and Sunflower, heh! Those two are lovely flora."
            show Char Cac Base
            c "Speakin' of which, have you met them yet? You really should!"
            show Char Cac Happy
            call cactus_AwNah from _call_cactus_AwNah
            c "Aw, nah! Don't worry 'bout me, bud. I'll always be round for a conversation or two. Go meet up with the others."
            play music sunflower
            jump meetPlants
################## Sunflower Route #################################

label sunflower:
    $ favorSun +=1
    $ lastPath = 3
    $ paths.remove(3)
    show Char Sun Blush
    s "Meeee!?"
    show Char Sun Happy
    call Sun_GeeHappy from _call_Sun_GeeHappy
    s "Oki-dokie! Gee, I'm flattered!"
    show Char Sun Base
    s "Soooo, I'm Sunflower! You can call me Sunny too. Or Flower, but around here that might get confusing."
    s "She series pronouns, please. And..."
    s "Well gee, is there anything you wanna know? I'm an open book."
    jump SunChoices
label SunChoices:
    menu:
        "What's your story, Morning-Glory?":
            jump story
        "What do you do for fun around here?":
            jump fun

label fun:
    s "Oh, mostly we just sit around collecting dirt. We each get up to our own shennanigans, though."
    s "I like to chat... a lot."
    s "And when I've talked everybody's petals off I tend to soak up some rays in my corner of the greenhouse..."
    s "And of course, perform."
    menu:
        "Perform?":
            jump musicals
        "You like the sun?":
            show Char Sun Base
            s "..."
            s "..."
            s "Chrys, I am a sunflower."
            menu:
                "Right, yeah. Good point.":
                    pass
            menu:
                "So you perform?":
                    jump musicals
                "Well, moving on...":
                    jump loop2

    jump meetPlants
label musicals:
    show Char Sun Happy
    s "YES! I love the theatre! Especially musicals!"
    menu:
        "Oh, I love musicals!":
            s "You do? It's been so long since I've melt a fellow theatre fan!"
            s "We'll have to talk all about it later! Oh I could go on for days!"
            jump rant

        "That sounds cool!":
            s "Oh, they're beautiful! Nothing like the spotlight, the sweet sound of a song floating on the air like a scented breeze..."
            s "We'll have to talk all about it later! Oh I could go on for days!"
            jump rant
        "Could you perform something for me?":
            show Char Sun Blush
            s "You... want to hear me sing?"
            show Char Sun VHappy
            s "OKAY!"
            show Char Sun Happy
            s "Gee, nobody's asked in so long! I'll do my favorite song..."
            s "The Finale of Ratatouille the Musical!"
            "You understand now why plants don't have vocal chords. The sound emitting from her reminds you of an elephant choking on a rooster. Weirdly, her french accent is perfectly on point."
            menu:
                "That... was...":
                    pass
            menu:
                "Cool.":
                    show Char Sun Blush
                    call Sun_GeeHappy from _call_Sun_GeeHappy_1
                    s "Gee, thanks! Maybe I'll perform for you again sometime!"
                    jump rant
                "Very. Nice!":
                    show Char Sun Blush
                    s "Gee, thanks! Maybe I'll perform for you again sometime!"
                    jump rant
                "I don't think I understand musicals.":
                    s "Oh, they're beautiful! Nothing like the spotlight, the sweet sound of a song floating on the air like a scented breeze..."
                    s "We'll have to talk all about it later! Oh I could go on for days!"
                    jump rant
label rant:

    "You get the impression you won't have a choice in that matter."
    menu:
        "Uh, cool! That will... happen! Eventually!":
            pass
    jump loop2
label story:
    s "Actually, she's my cousin. As for me, I've been here in the shop for a while. I used to be a big-field kinda gal. It was wonderful! Lots of sun, plenty of neighbors..."
    menu:
        "Why'd you leave?":
            jump leave
        "Sounds like your kind of place!":
            show Char Sun Happy
            s "Right? There's nothing I love more in this world than sunshine and company. And I had both!"
            s "Staring at the sun together, holding leaves... it made me so... happy..."
            s "It was so romantic..."
            menu:
                "Why'd you leave?":
                    jump leave
                "Oh, do you have a partner?":
                    show Char Sun Surprise
                    s "GAH!? UH..."
                    s "N-No! I mean, who's asking!?"
                    menu:
                        "Uh, I guess I am?":
                            show Char Sun Blush
                            call Sun_Blush from _call_Sun_Blush
                            s "Oh! Gee! Uh, yeah, I'm single. If, uhm, you're asking."
                            s "I mean, if anybody is! Yeah, I'm single."
                        "Sorry, nevermind. You don't have to answer that.":
                            s "N-no worries. Uh, I am single, for the record. Yup."
                    show Char Sun Sad
                    s "Solo. Ace. ...Lonely."
                    show Char Sun Happy
                    s "I mean, uh. That was a joke."
                    s "I mean, a quote. A quote joke... from Shakespeare. Teehee."
                    menu:
                        "Guess I really need to read more Shakespeare.":
                            show Char Sun Base
                            s "He's cool if you're into that. I prefer musicals so I never read him."
                            menu:
                                "Er, right.":
                                    s "Really, I'm not lonely though. I have such good friends right here!"
                                    jump loop1
                        "...Are you sure you're okay?":
                            show Char Sun VHappy
                            s "YUP! NEVER BETTER! ALL SUNSHINE AND RAINBOWS OVER HERE! TEEHEE!"
                            "{i}She's smiling so hard it looks like it hurts.{/i}"
                            menu:
                                "Er, right.":
                                    show Char Sun Base
                                    s "Really, I'm not lonely though. I have such good friends right here!"
                                    jump loop1
                "That sounds lovely, Sunny.":
                    show Char Sun Base
                    s "It was. But hey! I'm here now."
                    s "I like it here. There's way less friends, but they're all good friends. And it's peaceful."
                    jump loop1
label leave:
    show Char Sun Sad
    s "Oh, I just..."
    call Sun_Shake from _call_Sun_Shake
    s "I just had to go. Some things aren't meant to last. It's like Shakespeare says."
    s "\"Candles go out. Then life's dark and you leave.\""
    menu:
        "I'm sorry.":
            show Char Sun Base
            s "It's okay!"
            s "I like it here. There's way less friends, but they're all good friends. And it's peaceful."
            jump loop1
label loop1:
    menu:
        "Could you introduce me to some of the other plants around here?":
            jump meetPlants
        "What do you guys do for fun around here?":
            jump fun
label loop2:
menu:
    "Could you introduce me to some of the other plants around here?":
        s "Okie-dokie! Who do you want to meet?"
        jump meetPlants
    "What's your story, Morning-Glory?":
        jump story

############### SUNFLOWER AND MUSHROOM CONFLICT ######################
label SvMConflict:
    play music fungi
    scene Window  with dissolve ###BG
    show Char Sun Angry with dissolve
    s "You RUINED my window! It's absolutely FILTHY!"
    s "Deep breaths, Sunny..."
    s "Look, all I want is an APOLOGY and for you to SCRUB that GOO off!"

    show Char Mush Angry
    call Mushroom_IMSHROOMINHERE from _call_Mushroom_IMSHROOMINHERE
    m "Goo? ‘Scuse me? All that sunlight must’ve blinded ya if you can’t recognize art!"

    show Char Sun Angry
    s "ART? THIS IS FILTH!"
    s "AND IT’S BLOCKING--"
    s "MY--"
    s "SUNLIGHT!!!"
    menu:
        "Whoa, calm down! What happened?":
            pass

    show Char Sun Angry
    s "I was practicing my falsetto over by the seed packets..."
    s "You know, because I don’t wanna break the window glass… again…"
    s "And I came back and there was goo! On the window! In front of my home!"

    show Char Mush Joke
    m "And I was just taking a break from flexing my body muscles to flex some creative ones."

    show Char Mush Base
    m "Found this rad spot to put up some fungffiti! How was I supposed to know some plant lived here?"

    show Char Sun Angry
    s "Because I’m there all the time, every day!"
    s "Unlike some of us, I actually LIVE in this flower shop, thank-you-very-much!"

    show Char Mush Angry
    m "Well excuse me, miss high-and-mighty! Not all of us get the privilege of living in the shop."
    m "If anything I did you a favor. Think of it like stained glass art and just…"

    show Char Mush Joke
    with flash
    call MushroomHappy_FUNGEDABOUTIT from _call_MushroomHappy_FUNGEDABOUTIT_2
    m "FUNGEDABOUTIT!"

    show Char Sun Angry

    s "You call that art? It looks a Cats hairball fell in the stage makeup for Wicked!"
    s "And how can I forget about it when it’s--"
    s "BLOCKING!"
    s "MY!"
    s "SUNLIGHT!"

    show Char Mush Surprise
    m "..."
    show Char Mush Base
    m "So we good then?"

    show Char Sun Angry
    s "NO! ABSOLUTELY NOT! YOU VANDALIZED MY WINDOW!"
    "You look over at the window. The “fungfetti” in question seems to depict Mushroom jumping over a venus fly trap while riding a motorcycle, done entirely in some kind of... moss? It’s actually quite impressive and doesn’t seem to be blocking that much light."
    menu:
        "Hey, calm down guys.":
            pass
    menu:
        "I think...":
            pass
    menu:
        "Sunflower, you should respect Mushroom’s art. They could be the next Plantcasso!":

            show Char Mush Blush
            m "Whoa, you really think so? Rad of you to say."
            show Char Mush Joke
            m "I knew there was something I liked about ya. From the first minute I saw you I thought “now this is a plant that knows some good fungffiti when they see it!”"

            show Char Sun Angry
            s "Unbelievable."
            s "Fine, if you guys want to act like total sprouts, be my guest."
            s "As for me, a CULTURED woman, I’m going to…"
            call Sun_Shake from _call_Sun_Shake_1
            s "Like Shakespeare said--"
            s "Exit, pursued by berry."
            hide Char with dissolve
            "She leaves, singing “You’ll be Back” from Hamilton as she does. You swear you see a crack form in the glass, right down the middle of the fungffiti."
            show Char Mush Happy
            m "Wow sapling, really owe you one for getting the warden off my back."
            show Char Mush Base
            m "I'm going to keep a low profile for now, but catch you around later? Just climb that shelf right over there, I'll be hanging around. See you on the flipside!"
            hide Char with dissolve
            "And with that, they're gone."
            jump mushRoute

        "Mushroom, you should clean up Sunflower’s window. That’s… really gross.":
                play music sunflower
                show Char Sun Surprise
                s "Are you… sticking up for me?"
                show Char Sun Blush
                s "Nobody's ever..."
                s "Ahem"
                show Char Sun Base
                s "Sorry, Mushroom. If you could, uh, remove your art… please."

                show Char Mush Surprise
                m "O-oh… Uh…"
                show Char Mush Base
                m "Totally totally totally. Later though my muscles are soooo sore from all the lifts and the fungffiti I did."
                show Char Mush Joke
                m "GOTTA JET BYE!!"

                "One second they’re there, the next they’re gone. Leaving you, Sunflower, and the fungffiti in all it’s gaudy glory smiling down on you."
                show Char Sun Base
                s "..."
                s "..."
                s "I’m going to have to clean it up myself, aren’t I."
                menu:
                    "I think so, yeah.":
                        pass
                s "Oh well. It's not like I'm not tall enough to reach it."
                show Char Sun Happy
                s "But hey, thank you. Really, I didn't expect that."
                call Sun_GeeHappy from _call_Sun_GeeHappy_2
                s "Like gee, I was showing my worst petals and acting like a total sprout..."
                s "It can be hard to express your needs, you know? It's not as easy as acting is..."
                menu:
                    "Yeah, that can be real tough. ":
                        pass
                menu:
                    "Sometimes you really feel like you only have two or three options to express the whole range of your emotions.":
                        pass
                menu:
                    "But anyway.":
                        pass
                s "Teehee, you get it."
                show Char Sun Base
                s "Hey..."
                show Char Sun Blush
                s "Would you want to..."
                s "Er, nevermind, it's silly."
                menu:
                    "Are you asking to... hang out together?":
                        pass
                s "I mean, if you're doing something that's fine. It's just if you want to spend more time together. Or something. No pressure."
                call Sun_Blush from _call_Sun_Blush_1
                s "Gee, I'm such a mess. It's like we just said: expressing your needs is--"
                show Char Sun Surprise
                s "Not like I need you or anything! Er..."
                menu:
                    "Sure, I'd love to hang out with you!":
                        pass
                show Char Sun Happy

                s "Oh! Yay! Gee, that made me nervous..."
                s "And I know the perfect thing to do!"
                s "Er, once I clean up this moss. I don't want it spreading."
                hide Char with dissolve
                "You grab her a napkin and hold her pot as she reaches up to clean off the moss. Goodbye, fungfetti. Sunflower's demeanor immediately brightens as soon as it's gone."
                show Char Sun Base with dissolve
                s "Thanks! So as far as what to do..."
                s "...Well, I didn't actually think I would get this \far."
                s "All I ever do here is what I always do..."
                jump pathSun

######## SUNFLOWER PATH ############
label pathSun:
    show Char Sun Base
    $ paths = [0,1,2,3]
    menu:
        "Would you like to sing together?":
            $ favorSun += 2
            jump singSun
        "Would you like to go talk to other people?" if 1 in paths:
            $ favorSun -= 1
            $ paths.remove(2)
            show Char Sun Surprise
            s "Oh! Um, sure?"
            "You go around to some of the other plants and chat. Sunflower is her typical peppy self, but you notice she keeps passing glances at you and seems distracted."
            menu:
                "Oh, did you want to hang out together alone?":
                    pass
            show Char Sun Base
            s "Er, yeah. But I mean, it's your time, we can do whatever..."
            "She keeps smiling but looks a little deflated."
            jump pathsSun
        "Would you like to turn on the sprinklers and flood the cacti?":
            $ favorSun -= 2
            show Char Sun Surprise
            s "!!"
            s "Is that... something you do for fun?"
            show Char Sun Angry
            s "That's so inappropriate Chrys. Somebody could get hurt. And Cactus is an amazing guy! How could you stand hurting him like that?"
            menu:
                "I didn't mean it! It was a joke!":
                    pass
            s "...Okay."
            "She doesn't look convinced, but she relaxes a little."
            jump pathSun

        "Would you like to soak up some sun and just chat?":
            $favorSun += 1
            show Char Sun Happy
            s "That sounds lovely! Sure!"
            jump pastSun
label singSun:

    show Char Sun Surprise
    s "You want to sing!?"
    s "With me!?"
    show Char Sun VHappy
    s "I would LOVE to!"
    show Char Sun Happy
    call Sun_GeeHappy from _call_Sun_GeeHappy_3
    s "Gee, nobody's ever asked me to sing with them before! "
    show Char Sun Base
    s "Do you know how hard it is to do a whole duet yourself? Like. \"Anything You Can Do\" somehow gets so degrading when you sing it alone."
    menu:
        "I bet...":
            pass
    jump musicalSun

label musicalSun:
    $ paths = [0,1,2,3,4]
    s "So what musical are we doing?"
    menu:
        "Oklahoma!!" if 0 in paths:
            $ favorSun -= 2
            show Char Sun Surprise
            s "!!!"
            s "Oh! Um, sure! We can do that one!"
            "She has the book and lyrics to \"Oklahoma!\" stored in her corner. You notice there are a few pages dog-eared."
            show Char Sun Base
            s "I guess we can start with \"Kansas\"? That's a fun song."
            call Sun_Sing from _call_Sun_Sing
            "Dear God, her voice. It sounds like an alarm clock angrily making love to a frog. Still, her western accent is on point. She guides you through \"Kansas\" and \"Oh, What a Beautiful Mornin'\""
            "As you finish your song, you turn to a random page. It's \"People Will Say We're in Love\". There's a dozen little hearts drawn in the margins."
            show Char Sun Sad
            s "Oh..."
            menu:
                "Are you alright?":
                    $ favorSun += 2
                    s "Yeah, I'm fine..."
                    s "This song just always reminds me of him..."
                    menu:
                        "\"Him?\"":
                            $ favorSun -= 1
                            jump sadSceneSunFlower
                        "Do you want to talk about it?":
                            $ favorSun += 1
                            s "No, not right now."
                            s "Thank you, though. For asking."
                            show Char Sun Base
                            s "What if we talked instead for a bit?"
                            jump selfStorySun
                "Er, let's sing something different.":
                    $favorSun -=1
                    s "N-no thanks. I don't feel like singing anymore."
                    s "Could we just, uhm... chat instead? About other things?"
                    menu:
                        "Okay, sure.":
                            pass
                    show Char Sun Base
                    s "Okay, sure."
                    jump selfStorySun
                "Er, I'm tired of singing. Let's just chat.":
                    s "Yeah..."
                    show Char Sun Base
                    s "Yeah, good idea. Let's do that."
                    jump selfStorySun

        "Hamilton!" if 1 in paths:
            $ favorSun += 1
            show Char Sun Happy
            s "Oh, \"Hamilton\"! Sure, we could do that one!"
            "She has the book and lyrics to \"Hamilton\" stored in her corner."
            show Char Sun Base
            s "I guess we can start with \"Alexander Hamilton\"? That's an iconic song."
            show Char Sun VHappy
            call Sun_Sing from _call_Sun_Sing_1
            "You aren't prepared for how skilled she is at rapping. Like, she is freakily good. After playfully going through \"Say No to This\" and \"What'd I Miss\", you let her show off a little bit with \"My Shot\" and \"Right Hand Man\"."
            show Char Sun Happy
            s "Whew! That might be all for me, I think I'm getting vocal fry!"
            hide Char with dissolve
            "You share a watering can as you catch your breath. After a few minutes, you get to talking."
            "Naturally, you guys quickly transition to talking about yourselves."
            jump pastSun
        "Shakespeare!" if 2 in paths:
            show Char Sun Base
            s "Uh..."
            s "Shakespeare isn't a musical. It's not even a play. Shakespeare is a man."
            menu:
                "Ah, right.":
                    pass
            $ paths.remove(2)
            jump musicalSun
        "Ratatouille!" if 3 in paths:
            $ favorSun += 2
            show Char Sun Surprise
            s "!!!"
            s "That's..."
            show Char Sun VHappy
            s "MY FAVORITE! HOW DID YOU KNOW!?"
            "She has the book and lyrics to \"Ratatouille the Musical\" stored in her corner. It's heavily worn and doggeared."
            show Char Sun Happy
            s "Oh! Let's start with \"Trash is Our Treasure\", it's so fun! Then maybe we can do \"Rat's Way of Life\", and then you can be young Ego in..."
            hide Char with dissolve
            call Sun_Sing from _call_Sun_Sing_2
            "You wind up going through the entire musical. Dear God, her voice. It sounds like an alarm clock angrily making love to a frog. Still, her French accent is on point. Together you sing \"Kitchen Tango\" twice just for fun."
            "By the end, you're both happily panting. That doesn't stop her from giving you an exhaustive explanation of how the musical was made. It's actually pretty interesting."
            show Char  Sun Happy with dissolve
            s "Whew! I haven't had that much fun in... forever!"
            "Naturally, you guys quickly transition to talking about yourselves."
            jump pastSun
        "Your Choice!" if 4 in paths:
            $ paths.remove(4)
            show Char Sun Base
            s "Oh, that's sweet!"
            show Char Sun Blush
            s "I'd love to do my favorite..."
            show Char Sun Happy
            s "But you have to guess what it is!"
            jump musicalSun
label selfStorySun:
    s "I've been hogging the whole day. Tell me about yourself!"
    hide Char with dissolve
    jump pastSun

label pastSun:
    hide Char with dissolve
    "You two sit in the sun together as afternoon turns to evening. You tell her about your home and past. She listens eagerly."
    show Char Sun Base with dissolve
    s "Wow. Well I'm glad that everything in your life led you to this little shop, huh?"
    menu:
        "Yeah, it's crazy how it happened that way.":
            pass
    menu:
        "So...":
            pass
    menu:
        "Did you always plan on coming here?":
            s "Oh, not really..."
            show Char Sun Sad
            s "It sort of just... worked out that way..."
            jump reflectionSun
        "Are you excited for Valentine's Day tomorrow?":
            $ favorSun -= 1
            show Char Sun Sad
            s "Oh..."
            s "Uh..."
            show Char Sun VHappy
            s "Er, I mean! Yeah! Absolutely! Woo, Valentine's Day!"
            menu:
                "Sunny, are you sure you're okay?":
                    $ favorSun +=1
                    s "Yup! Fine!"
                    s "I'm as happy as a cock's comb! Yup yup!"
                    jump SunOkay
                "Er, yeah. Valentine's Day is great...":
                    $ favorSun -= 2
                    s "Yeah, super cool! All the smiles and love..."
                    s "It's... so great..."
                    jump SunOkay
                "Uh, hey! Let's... do something else! Let's sing!":
                    $ favorSun += 2
                    jump singSun
        "Do you ever miss home?":
            $ favorSun += 1
            show Char Sun Base
            call Sun_Blush from _call_Sun_Blush_2
            s "All the time. It was so beautiful. I mean gee, it was a sunflower field, it was where I belonged!"
            jump reflectionSun
label sadSceneSunFlower:
    show Char Sun Surprise
    call Sun_Surprised from _call_Sun_Surprised
    s "!!!"
    s "I..."
    s "He's..."
    show Char Sun VHappy
    s "He's nobody! Just a guy I knew once!"
    s "He's irrelevant! I don't... care..."
    s "Care about him at all!"
    jump SunOkay
label reflectionSun:
    s "..."
    s "It couldn't last forever. I mean, nothing can, right?"
    s "But for a while there, he really made me believe it could last forever."
    menu:
        "\"He\"?":
            $ favorSun -= 1
            jump sadSceneSunFlower
        "I'm sorry.":
            show Char Sun Surprise
            s "Oh! I mean..."
            show Char Sun VHappy
            s "It's fine! I'm fine! Nothing sorry here!"
            s "I'm as happy as a cock's comb! Yup yup!"
            jump SunOkay
        "You're right. Nothing lasts forever.":
            $ favorSun += 2
            s "Yeah... no matter how much you want it to, huh?"
            show Char Sun Surprise
            s "Uh, I mean..."
            show Char Sun VHappy
            call Sun_Fine from _call_Sun_Fine
            s "It's fine! I'm fine! No worries!"
            s "I'm as happy as a cock's comb! Yup yup!"
            jump SunOkay
label SunOkay:

    "She's smiling so hard it doesn't look comfortable."
    menu:
        "Sunny, it's okay to not be okay.":
            $ favorSun += 2
            s "..."
            show Char Sun Happy
            s "..."
            show Char Sun Base
            s "..."
            show Char Sun Sad
            jump sunBreakdown
        "Okay...":
            $ favorSun -= 2
            s "Yeah!"
            s "..."
            s "Did I..."
            show Char Sun Base
            s "Did I break character?"
            show Char Sun Sad
            s "Did I make things weird?"

label sunBreakdown:

    s "..."
    s "Chrys... can I tell you something?"
    s "I... left home after my boyfriend broke up with me."
    s "It shouldn't have hurt me as much as it did..."
    s "But I was devestated. And it made me realize... like..."
    s "...When sunflowers can’t find the sun, they look to each other."
    s "But I don't. I feel like I look to other people first. I want them to like me..."
    s "I want them to like me more than I even want sunshine."
    menu:
        "Oh Sunny...":
            pass
    menu:
        "Nobody can ever create your happiness.":
            $ favorSun += 4
            show Char Sun Surprise
            s "Huh?"
            menu:
                "It can feel like your self-worth comes from being loved and validated by others...":
                    pass
            menu:
                "But it's yours, Sunny. Your love, your value.":
                    pass
            menu:
                "You don't have to please others to be worthy of love.":
                    pass
            menu:
                "You're worthy of love just by being yourself. Nobody can take that away...":
                    pass
            menu:
                "Or give it to you.":
                    pass
            show Char Sun Surprise
            s "..."
            "She starts to cry."
            show Char Sun Sad
            s "I'm sorry... I just..."
            s "I don't like musicals."
            menu:
                "Er, what?":
                    pass
            s "I mean... I don't like acting. I just like singing."
            show Char Sun Angry
            s "I HATE acting!"
            menu:
                "Er, that's okay. You don't have to act.":
                    pass
            s "I don't! I don't have to act for anybody!"
            s "Chrys! I! Am! So! Sad!"
            show Char Sun Sad
            s "And that's..."
            show Char Sun Base
            s "That's okay. And it feels really good to finally say."
            jump dateEndingFinaleSun


        "I like you as you are.":
            $ favorSun -= 1
            menu:
                "The most likable part of you is YOU.":
                    pass
            menu:
                "You don't have to put on an act for everyone else.":
                    pass
            jump dateEndingFinaleSun
label dateEndingFinaleSun:
        s "...Thank you."
        show Char Sun Base
        s "For letting me tell you this. And the whole date. I really did have a good time."
        show Char Sun Blush
        s "Hehe, gee. I'm really not ready for Valentine's Day tomorrow."
        show Char Sun Base
        s "Oh well. It's gonna happen whether I like it or not."
        menu:
            "And you're allowed to hate it!":
                pass
        show Char Sun Happy
        s "Hehe, I am! I can HATE it!!!"
        "She seems very excited by the prospect of hate. She's practically vibrating."
        s "I should probably get to bed. Maybe I'll see you tomorrow?"
        menu:
            "Yeah, see you tomorrow. Goodnight, Sunny.":
                pass
        s "Night, Chrys."
        scene black with fade
        "That night, as you go to flowerbed, you realize there's something you want to ask Sunny in the morning."
        "The next day..."
        scene Sunflower1 with fade
        "You head to Sunflower's spot. She's soaking in the sun, but you notice she looks a little wilted."
        show Char Sun Base with dissolve
        s "Good morning!"
        menu:
            "Hi! Are you alright?":
                pass
        s "Yup! I know I'm a little wilted. I cried a bunch last night. It was..."
        show Char Sun Happy
        s "AMAZING! CRYING WHEN YOU'RE SAD FEELS GREAT!"
        menu:
            "That's... good? I think?":
                pass
        menu:
            "Hey Sunny, there's something I want to ask you.":
                pass
        show Char Sun Base
        s "Sure! What's up?"
        menu:
            "Will you...":
                pass
        menu:
            "Will you be my Valentine?":
                pass
        show Char Sun Surprise
        s "!!!"
        s "You..."
        s "You want me to be your Valentine!?"
        show Char Sun Blush
        s "Chrys, that's so sweet."
        if favorSun >= 5:
            jump SunGoodEnding
        else:
            jump SunBadEnding
label SunGoodEnding:
    show Char Sun Sad
    s "...Can I tell you something, again?"
    s "I'm scared."
    s "I'm scared that if I date somebody right now, I'll try to find my happiness through them."
    s "I'm scared I'm not emotionally ready for a relationship."
    show Char Sun Blush
    s "But you..."
    s "You make me want to try anyway. I genuinely believe that you'll support me."
    s "So if you're okay with that, with me still figuring it out..."
    s "Then I'd love to be your Valentine."
    hide Char with dissolve
    "She leans down and kisses you."
    "You two spend the rest of the day together in the window."
    "In the evening, a patron comes into the shop and buys both of you, together."
    "You expect her to be nervous. But when you glance over at her, she's smiling, that big grin that looks impossibly wide."
    "But this time, it looks genuine."
    ####GOOD ENDING SUNFLOWER
    scene black with fade
    $ ending = 2
    jump credits
    return
label SunBadEnding:
    s "But no. "
    show Char Sun Base
    s "Last night, I realized something."
    s "If I keep trying so hard to make other people like me, I'll only ever like myself as much as everbody else does."
    s "I don't think I'll be ready for a relationship until I learn to love myself no matter what people think of me."
    s "I'm sorry, Chrys. I hope you don't hate me for this."
    menu:
        "I do hate you.":
            $ ending = 4
            show Char Sun Surprise
            s "Oh... okay."
            s "I'm sor--"
            show Char Sun Base
            s "Actually, no. That's okay."
            s "You're allowed to hate me. I hope..."
            s "I hope it makes you happy."
        "I'm proud of you.":
            $ ending = 3
            show Char Sun Blush
            s "Thank you. I knew you'd understand. "
            "She gives you a little kiss on the petal."
            show Char Sun Base
            s "Maybe someday."
            s "But right now... I hope you still have a good Valentine's Day."
    "Later that day, Sunny gets bought, alone."
    "She seems excited. She sings a little riff of \"Wicked\" and it shatters the shop door."
    "You're not sure if you'll see her again."
    ## BAD ENDING SUNFLOWER

    jump credits
    return


##### MUSH ROUTE
label mushRoute:
    show Char Sun Base with dissolve
    "Sunflower eventually returns, a bit more calm and collected, and you pass the time shooting the wind with her. By the time you stop, a good amount of time has passed."
    menu:
        "Time to visit Mushroom":
            pass
    show Char Sun Angry
    s "Oh, you're visiting HIM?"
    show Char Sun Base
    s "Well, just be careful! He should be right up by the big crack in the wall."
    show Char Sun Happy
    s "Have fun!"
    hide Char with dissolve
    menu:
        "Time to take a walk on the wild side.":
            pass
    scene Fungi2 with dissolve
    "Making your way through the crack in the wall that clearly has fungus growing out of it (how does the shop owner not notice that), you find yourself surrounded by fungi of all kinds."
    "Of course, there’s one fun guy in particular you’re looking for. And you spot them…"
    show Char Mush Reverse with dissolve
    "…"
    "Doing a handstand?"
    "Yeah, no bones about it, that’s what they’re doing. Looks like they’re meditating."
    menu:
        "Sneak up behind them and shout “BOO!” real loud":
            $ favorMush += 1
            show Char Mush Surprise
            call MushroomSurprise_woah from _call_MushroomSurprise_woah
            m "WAAAHHHH!"
            hide Char with dissolve
            "Understandably startled, they collapse to the ground. Trying to play it off like they didn’t have the spores scared out of them, they dust themselves off as they regard you with a warm smile."
            show Char Mush Joke with dissolve
            m "Heh, tryna’ gimme a scare, huh? Kudos for trying, but it’s gonna take more than that to scare the cap off of my head!"
            menu:
                "I’ll get you next time, you’ll see!":
                    pass
            m "Well we’ll see about that, sapling!"
            jump mushHelp

        "Wait patiently for them to finish":
            $ favorMush += -1
            call Mushroom_Yo from _call_Mushroom_Yo
            m "Oh, hey. Didn’t hear ya come in."
            show Char Mush Base with fade
            "They carefully lower themselves from their handstand and turn to face you."
            m "I must be losing my touch, if I can’t even sense a lone flower comin’ up behind me."
            menu:
                "Losing your touch?":
                    pass
            show Char Mush Joke
            m "Heh, when ya live dangerously like I do, you always gotta be on alert for danger, sapling. That’s rule numero uno of this crazy flowerbed we call life!"
            jump mushHelp



label mushHelp:
    show Char Mush Base
    m "Anyway, how can I help ya? If ya wanna practice fungffiti, ask some other plant. I got a pretty busy schedule ahead of me..."
    menu:
        "Aw, but I wanted to hang out with you":
            $ favorMush += 1
        "And after I took the time to make it all the way out here…":
            $favorMush -= 1
            show Char Mush Sad
            m "I’m sorry, sapling. I know, my home ain’t exactly easy to get to…"
            show Char Mush Base
            m "Why’d you come out here anyways?"
    menu:
        "I wanted to live dangerously today!":
            pass
        "I wanted to live DANGEROUSLY today! (said while folding a leaf into a horn gesture)":
            pass
    show Char Mush Surprise
    m "W-wait, really?"
    m "Uh, I mean-"
    show Char Mush Joke
    m "FUNG YEAH YOU DO!"
    "\"FUNG YEAH\" indeed."
    m "Heh, well if that’s the case I could make some time for you. Yeah…"
    menu:
        "Fung yeah!":
            pass
        "Didn’t you say you had a pretty busy schedule?":
            show Char Mush Surprise
            m "Oh! Uh, yeah I guess I did say that didn’t I?"
            show Char Mush Blush
            m "Well, y’know… I could be less busy for you, sapling…"
            "Suddenly, as if they’re trying to move past this moment of vulnerability…"
            show Char Mush Joke
            call MushroomHappy_FUNGEDABOUTIT from _call_MushroomHappy_FUNGEDABOUTIT_3
            m "FUNGEDABOUTIT!"
    m "What’re we waiting around here for? Let’s get goin’!"
    hide Char with dissolve
    "And just like that the two of you are off! The two of you spend the day drawing fungffiti, practicing sick flips, and popping ruder squats! It’s the raddest day you’ve ever had. Almost perfect."
    "Almost perfect because the whole time something seems off about Mushroom. Like they aren’t putting their full heart into your radivities. Rad activities."
    show Char Mush Joke with dissolve
    m "Heh, that was a pretty rude squat you pulled, but why don’t ya peep this!"
    "They pop a squat. It’s… lacking."
    menu:
        "I’ve seen you pop ruder, you good?":
            $ favorMush -= 1
            show Char Mush Angry
            m "Ya gotta harsh my mellow like that?"
            show Char Mush Surprise
            m "But since you mentioned it, something is bothering me…"
        "Hey, is something bothering you?":
            $favorMush += 1
            m "Something bothering me? Me?"
            show Char Mush Surprise
            m "Actually… yeah. There is."
    show Char Mush Base
    m "It’s stupid, I should be enjoying myself but I can’t help but think about how this can’t last. Us hanging out like this."
    menu:
        "What do you mean? We can hang out all the time! Two rude dudes against the world!":
            show Char Mush Sad
            "They sigh, releasing a small puff of spores."
            call Mushroom_sigh from _call_Mushroom_sigh
            m "Sapling… you just don’t get it."
        "What's stopping us? Is this about you not living in the shop?":
            show Char Mush Surprise
            m "Looks like you landed the proboscis in the nectar, sapling…"
    show Char Mush Sad
    call Mushroom_sigh from _call_Mushroom_sigh_1
    m "Someday, probably soon, you’ll get bought and then it’ll just be me again."
    show Char Mush Joke
    call Mushroom_badagloom from _call_Mushroom_badagloom
    m "But that’s just the life of a lone fungus like me, amirite?"
    menu:
        "C’mon, you’re deflecting. No plant wants to be alone.":
            $ favorMush += 1
            show Char Mush Surprise
            m "I…"
            show Char Mush Sad
            m "Even if that’s true, who else do I have? No other fungus around here can match me, either in raw radness or even sentience!"

        "If you feel so alone, why don’t you make some friends?":
            $ favorMush += -1
            show Char Mush Angry
            m "With who? The plants in the shop? I ain’t exactly welcome by every plant."
            m "And the fungi around here don’t exactly make for great company. A bit lacking in both raw radness and sentience, you dig?"
    m "Face it, you should just forget about me, sapling..."
    if favorMush >= 3:
        jump mushGoodEnding
    else:
        jump mushBadEnding

label mushGoodEnding:
    menu:
        "A dare...":
            pass
    show Char Mush Surprise
    m "Huh?"
    menu:
        "I dare you… to stick with me to the end! No matter what!":
            pass
    show Char Mush Blush
    m "Sapling…"
    show Char Mush Joke
    call MushroomHappy_BadaBing from _call_MushroomHappy_BadaBing
    m "Fung yeah!"
    menu:
        "And, uh, dare me to do the same…":
            pass
    show Char Mush Blush
    m "Sapling, I dare ya to stick with this bad boy to the end! In sick-nasty-ness and health!"
    menu:
        "You’re on!":
            pass
    scene black with fade
    "And just like that the two of you begin planning. Preparing for the sickest stunt ever."
    "When the day comes that you get bought, Mushroom will be right there with you. The plan is for them to sneak into the bouquet with you. Don’t worry, they’ve been practicing making themselves compact."
    "Until that day comes, the two of you will spend your time drawing fungffiti, doing sicker flips, and aiming for the rudest squats to end all squats."
    $ ending = 0
    jump credits

label mushBadEnding:
    scene black with fade
    "You try to find the words, but you just can’t. They’re right of course, and nothing you can think to say could change that."
    "Before you head back home that day, Mushroom gives you their sunglasses. They don’t say anything, but you know it’s because they want you to remember them."
    "You get purchased in a lovely bouquet the next day, sooner than you would have thought. Though your time was brief, you’ll always have that one day. The raddest day you’ll ever have."
    $ ending = 1
    jump credits

############### ROSE AND CACTUS CONFLICT ########################
label RvCConflict:
    scene Cactus1 with dissolve
    play music cactus
    "You decide to head over to Rose and Cactus. It seems Rose is focusing intently on Cactus’ words."
    "Cactus notices you approaching."
    show Char Cac Happy with dissolve
    c "Well, hey there, new bud! Hope you’re doing well."
    menu:
        "I am, hope you are too! What’s going on here?":
            pass
    show Char Cac Base
    c "I’m tryin’ to teach Rose some Southern slang and sayins’ since she wanted to learn, but…"
    scene Cactus1
    show Char Rose Wink
    r "How Dee y’ee all, I sure do wreck on that this is some fine fancy day for some tooting and shooting..."
    scene Cactus1
    show Char Cac Base
    c "… No one speaks like that, Rose."
    scene Cactus1
    show Char Rose Surprise
    r "Aww, shucks. "
    r "Oh?"
    show Char Rose Happy
    r "How do you do, Chrys. Tis a fine day that the Lord has made, ain’t it?"
    menu:
        "Howdy!":
            pass
        "Are you ok?":
            pass
    show Char Rose Wink
    r "Aww, aren’t you a sweetheart, sweetychums."
    r "I do declare, I’ve never been as righter as rain than where I stand."

    show Char Cac Base
    c "She’s fine, she’s just… Practicing."
    show Char Cac Happy
    c "She’s been getting better though! Better than this morning."
    show Char Cac Base
    c "Anyways, you’re just in time. I was about to teach Rose a new saying!"
    c "Here it is: God willin’ and the creek don’t rise."
    show Char Cac Happy
    c "My ma would say this whenever we were in a tight stitch."
    show Char Cac Base
    c "Kinda like saying \“here’s hoping?\”"

    show Char Rose Happy
    r "Oh, I see! It’s like that other saying you taught me the other day!"
    r "What was it…"
    r "Oh! Drenched like a water rat!"

    show Char Cac Base
    r "Uh… Not quite…."

    show Char Rose Surprise
    r "Oh!"
    r "Um...Risk it for the biscuit?"

    show Char Cac Base
    c "Nah..."

    show Char Rose Surprise
    r "Sweatin’ like a sinner at church on a Sunday?"

    show Char Cac Base
    c "Bless your heart."

    show Char Rose Surprise
    r "Oh, thank you?"

    show Char Cac Base
    c "No it’s-- it’s fine. "
    c "I think you mean “Doing it on a shotgun and a prayer,” right?"

    show Char Rose Base
    r "Hmm…"
    r "No, I’m pretty sure it was the biscuit one."

    show Char Cac Base
    c "Christ almighty, Rose."

    show Char Rose Happy
    r "Wait, I know how we can solve this."
    r "Chrys, you seem like you know Southern sayings. Which is it? Risk it for the Biscuit or Shotgun and a Prayer?"
    menu:
        "Uhhh...":
            pass
    menu:
        "It’s fine Cactus. She’s trying her best to learn!":
            show Char Rose Surprise
            r "See! I’m ri- hold it right there!"
            show Char Rose Blush
            r "Chrys!"

            show Char Cac Base
            c "No, wait. Chrys is right, you are trying your best. Southern slang is a beast of its own."
            show Char Cac Happy
            c "And I really do appreciate you going out of your way to try and learn it! It warms my little Texan heart."

            show Char Rose Blush
            r "Oh? Um…haha, I wasn’t expecting such a warm reception, especially with how rough my learning is."
            r "I hope I didn’t make you feel uncomfortable."

            show Char Cac Base
            c "Nah, Rose. The only thing ‘bout you that could hurt anyone’s your thorns."

            show Char Rose Happy
            r "I’m really happy to hear that!"
            "Suddenly, you hear shouting and aggressive quoting of Shakespeare in the distance. "
            show Char Cac Base
            c "Ah…"
            c "if Y’all don’t mind, It sounds like there’s some trouble brewing over there."
            c "I’ll go ahead and deal with it. Y’all can keep talking."
            show Char Rose Happy
            r "Oh, see you soon!"
            jump roseDate
        "Shotgun and a Prayer":

            show Char Rose Blush
            r "Aw shoot. I’m really trying over here."

            show Char Cac Base
            c "No worries, Rose. I appreciate you trying!"

            show Char Rose Base
            r "This really is tough. I’m impressed you know all this stuff, Cactus."

            show Char Cac Base
            c "Thanks I guess? You know, maybe let’s give this a rest for today."
            show Char Rose Wink

            r "Aww, and here I was about to rope in Sunflower and Mushroom."
            "You hear shouting and aggressive quoting of Shakespeare in the distance. You decide that things would be better off without them getting involved."
            show Char Rose Angry
            r "Hmm...Maybe I should deal with that first. I’ll...be right back."

            r "MUSHROOM! SUNNY!"
            show Char Cac Base
            c "Well I hope that gets all figured out."
            jump cactusDate

######## CACTUS DATE ##########

label cactusDate:
    scene Cactus1 with fade
    show Char Cac Base
    c "Anyways, I did wanna ask you somethin'."
    c "Would'ya be interested in me takin' you round the shop and showin' you the ropes?"
    show Char Cac Sweat
    c "N-Not like a date or anythin' though! Just two sprouts hanging out."
    menu:
        "Sure, I'd love to!":
            #### BIAS POINT
            $ favorCact += 1
            show Char Cac Happy
            call cactus_AwShucks from _call_cactus_AwShucks
            c "Aw, shucks! Thanks for takin' me up on my offer! I promise I won't disappoint."

        "Sure! Not like there's much else to do around here anyway!":
            $favorCact -= 1
            show Char Cac Sweat
            call cactus_heheh from _call_cactus_heheh
            c "Eh-heh... Fair 'nough."

    hide Char with dissolve
    "Cactus shows you around, giving you a pretty detailed tour on daily life here. There's quite a bit of hustle and bustle in the flower shop, though that may be because tomorrow's Valentine's Day."
    "Time passes. Near the end of his tour, Cactus turns to face you."
    show Char Cac Base with dissolve
    call cactus_hmm from _call_cactus_hmm
    c "Hmm. Only a few places left..."
    c "How 'bout you pick where to go next, Chrys?"
    $ paths = [0,1,2]
    jump locationsCactus


label locationsCactus:

    if len(paths) != 3:
        show Char Cac Base
        c "So, where to next?"
    menu:
        "Maybe the Succulents section?" if 0 in paths:
            show Char Cac Happy
            c "Sure, sure! I can show you 'round where I live!"
            c "Follow me!"
            hide Char with dissolve
            "You somehow make it across the store to the succulents. God, scooting your pot is hard work."
            jump succulentsCactus
        "I saw some cool flowers over there, if that works." if 1 in paths:
            jump rosesCactus
        "The moss. It Beckons." if 2 in paths:
            jump mossRoute
            return
label rosesCactus:
    $ paths.remove(1)
    show Char Cac Surprise
    c "Oh, them blueblood roses with the gold in their petals?"
    show Char Cac Sweat
    call cactus_heheh from _call_cactus_heheh_1
    c "...They don't like me much... so I'd rather not."
    c "Plus, some of 'em are half a brick short of a load, if you get what I'm sayin'."
    jump locationsCactus

    label succulentsCactus:
        $ paths.remove(0)
        scene Cactus1 with fade
        show Char Cac Happy
        call cactus_GladToHaveYa from _call_cactus_GladToHaveYa
        c "Well, welcome to my place, glad to have ya!"
        show Char Cac Base
        c "It's a nice lil shelf tucked away from the hustle n' bustle of city life."
        c "Go ahead n' make yourself at home."
        menu:
            "Wow, are all those succulents your neighbors?":
                show Char Cac Happy
                c "Oh yes indeed!"
                show Char Cac Base
                c "Most of 'em only stay in the store for a week at most, though, unlike me."
                c "People here seem to love 'em."
                show Char Cac Surprise
                call cactus_hmm from _call_cactus_hmm_1
                c "Almost as if there's some hip colleges nearby with a taste for trendy plants..."
                show Char Cac Happy
                c "But who knows? Not me!"
                c "It can get lonely though, being here for so long."
                menu:
                    "Don't feel down! You get to have so many neighbors and meet so many kinds of people!":
                        $ favorCact -= 1
                        show Char Cac Sweat
                        call cactus_heheh from _call_cactus_heheh_2
                        c "He-heh, yeah. Lucky me!"
                        jump aboutYourselfCactus


                    "Hey now, mister! You don't have to be trendy to be cool!":
                        $ favorCact += 1
                        show Char Cac Happy
                        call cactus_FairNough from _call_cactus_FairNough
                        c "Haha! Fair 'nough. Maybe being trendy ain't worth it. And I swear I'm not that old, Chrys!"
                        show Char Cac Base
                        c "Though I did leave home early. I'm probably just as old as Sunflower, even if it doesn't seem it."
                        c "So don't go 'round calling me \"mister,\" or else the newer buds will get the wrong idea."
                        menu:
                            "Got it...Boy?":
                                pass
                        "Cactus snorts. Somehow, against all odds and the laws of nature itself, he can do that."
                        show Char Cac Happy
                        call cactus_GoodOne from _call_cactus_GoodOne
                        c "I do like your sense of humor Chrys! Funnier than a barrel of monkeys!"
                        jump aboutYourselfCactus


            "City life's different, isn't it?":
                show Char Cac Base
                c "It sure is."
                show Char Cac Surprise
                c "Being out here all by myself makes me realize how big this world really is."
                menu:
                    "It must be great to finally leave home and see the world!":
                        $ favorCact -= 1
                        show Char Cac Sweat
                        c "Yeah... It's not exactly what I thought it'd be like, sometimes."
                        show Char Cac Happy
                        c "But it's like what my Ma always said: \"Can't Never Should.\""
                        show Char Cac Base
                        c "So if I want something, I just gotta set my mind on it and I'll get it eventually!"
                        show Char Cac Sweat
                        c "Yeah..."
                        jump aboutYourselfCactus
                    "Doesn't it get a little lonely though?":
                        $ favorCact += 1
                        show Char Cac Sweat
                        c "He-heh... If I'm being honest, sometimes it does."
                        show Char Cac Base
                        c "It's easy to get homesick here, especially when you're new to city life."
                        jump aboutYourselfCactus
label aboutYourselfCactus:
    show Char Cac Happy
    c "But enough 'bout me! Tell me 'bout yourself Chrys!"
    menu:
        "It all started when I was born...":
            "You happily filled Cactus in on your entire life story up until this point, down to the last detail."
        "Well there's this one joke I love about a horse and a bee...":
            "You spent 20 minutes recounting the best joke you've ever heard. Cactus listens intently. He laughs. He cries. He has never been this touched in his entire life. "
    c "Wow, Chrys! Thanks for sharing that!"
    show Char Cac Base
    c "I was wonderin' though, Chrys."
    c "..."
    menu:
        "...":
            pass
    show Char Cac Sweat
    c "This might sound strange, and I apologise..."
    show Char Cac Surprise
    call cactus_sigh from _call_cactus_sigh_1
    c "Do ya ever notice little things in your life that remind you of home?"
    menu:
        "What do you mean?":
            pass
    show Char Cac Sweat
    c "Well it's a bit hard to explain..."
    show Char Cac Base
    c "It's kinda like... how you pick up habits from others you care about."
    show Char Cac Happy
    c "For example, I picked up all my sayin's from my ma and pa, and the fertilizer I use is my Grandmama's recipe!"
    show Char Cac Base
    c "Or sometimes it's the habits from a different place. "
    c "Like wakin' up at 6 in the morning to a rooster's call, even if the bird ain't here anymore."
    c "Does that sorta make sense?"
    menu:
        "Honestly, I don't get what you're on about.":
            $favorCact -= 1
            show Char Cac Sweat
            c "Oh! He-heh... Sorry for talkin' your ear off for something silly like that then."
            call cactus_GettingLate from _call_cactus_GettingLate
            c "It's gettin' late, isn't it..."
            show Char Cac Base
            c "Sorry for keepin' ya for so long. You must be exhausted after today."
            show Char Cac Happy
            c "Here, I'll walk you back home."
            scene black with fade
            menu:
                "Valentine's Day Approaches...":
                    pass
            jump CacBadEnding
        "It does, don't worry.":
            $favorCact += 1
            show Char Cac Happy
            c "Glad you get it. Makes feel a bit less like a stranger here."
            show Char Cac Sweat
            c "But it's not like that stuff hasn't happened here as well either!"
            show Char Cac Base
            c "I sing songs from Ratatouille since Sunflower showed me that musical, and I've been going to more of Rose's lectures."
            show Char Cac Surprise
            c "But I dunno... There's not much I'm a part of here."
            show Char Cac Sweat
            c "Compared to Rose and Sunflower, well... I don't take part in much since I'm not invited to much. None of them fancy hang-outs, plant raves..."
            menu:
                "Plant raves?":
                    pass
            show Char Cac Base
            c "I said what I said."
            c "But I digress."
            show Char Cac Sweat
            c "I moved here thinkin' I could make it big in the arboretum here and make my momma proud..."
            show Char Cac Surprise
            c "But I've been in this shop for so long and I barely know anyone unlike back home..."
            show Char Cac Sweat
            c "It feels like I'm better off going back home to Texas. Maybe I wasn't made for the city. "
            menu:
                "I'd say give the city another chance!":
                    $ favorCact -= 2
                    menu:
                        "With how big it all is, you're bound to find a place to fit in!":
                            pass
                    show Char Cac Happy
                    c "He-heh. Thanks for that, Chrys."
                    show Char Cac Sweat
                    c "Sorry to wear ya' down with that."
                    show Char Cac Base
                    c "I'll keep thinkin' on it. In the meantime, is there anythin' you'd like to do? We could watch a movie or somethin'."
                    menu:
                        "Sure!":
                            pass
                    jump cacMovies
                "Maybe you aren't, but that's okay.":
                    menu:
                        "You don't need to find a place to belong. You can just carve one out for yourself.":
                            pass
                    menu:
                        "So chin up, Cactus. If you can't find a place of your own, make one yourself and go from there.":
                            pass
                    show Char Cac Surprise
                    c "..."
                    show Char Cac Sad
                    c "...Chrys..."
                    call cactus_AwLove from _call_cactus_AwLove
                    c "You have no right bein' this nice to me."
                    show Char Cac Blush
                    call cactus_YerRight from _call_cactus_YerRight
                    c "But yer right. I can't keep feelin' sorry for myself like this."
                    show Char Cac Happy
                    c "In fact, yer right about all that talk on carvin' a place out for myself n all that!"
                    c "I already have one, don't I?!"
                    show Char Cac Base
                    c "With Rose, Sunflower..."
                    show Char Cac Sweat
                    c "..."
                    c "...and you."
                    show Char Cac Base
                    call cactus_ThanksPardner from _call_cactus_ThanksPardner
                    c "Thank you for this, Chrys."
                    show Char Cac Sweat
                    c "Sorry to throw this all out at ya..."
                    show Char Cac Base
                    c "But thank you for listenin'."
                    c "I think I know what I need to do."
                    c "In the meantime, is there anythin' you'd like to do? We could watch a movie or somethin'."
                    menu:
                        "Sure!":
                            pass
                    jump cacMovies

label cacMovies:
    show Char Cac Happy
    c "Boy howdy! Alright then, I'll let you pick the flick."

    menu:
        "Watch a Romance Film":
            scene black with fade
            "You ended up watching The Lego Movie. It wasn't your idea of a romance film, but it was a good film nontheless."
        "Watch a Horror Film":
            scene black with fade
            "You ended up watching The Lego Movie. It wasn't your idea of a horror film, but it was a good film nontheless."
        "Watch a Comedy Film":
            scene black with fade
            "You ended up watching Drive (2011). It wasn't your idea of a comedy film, but it was a good film nontheless. Truly the peak of kino."
    scene Cactus1 with fade
    "It's late by the time the credits roll onto the screen. While you're yawning, Cactus turns to you."
    show Char Cac Base with dissolve
    c "Sorry for keepin' ya for so long. You must be exhausted after today."
    show Char Cac Happy
    c "Here, I'll walk you back home."
    hide Char with dissolve
    "You and Cactus scoot your way back to your place. Before you scoot inside, Cactus speaks."
    show Char Cac Happy with dissolve
    c "Thanks again for everythin', Chrys!"
    show Char Cac Sweat
    c "Apologies again for everythin' I said earlier. Hopefully it wasn't too offputting."
    show Char Cac Base
    c "I'll keep what ya said in mind and sit on it. In the meantime, let's hit the hay!I'll keep what ya said in mind and sit on it. In the meantime, let's hit the hay!"
    "He gives you a tip of his hat, a winning smile, and says goodnight before leaving."
    scene black with fade
    jump cacEndings
label mossRoute:
    show Char Cac Surprise
    c "The moss, eh?"
    show Char Cac Happy
    c "We can definitely do that! Hope ya don't mind the dark!"
    hide Char with dissolve
    "You both make your way down to the depths of the flower shop, to a corner where the walls meet the tile floor."
    show Char Cac Happy with dissolve
    c "And here we are! Moss central!"
    show Char Cac Base
    c "It may not seem like much at first, but it's got charming residents."
    show Char Cac Surprise
    c "I do wonder where that Mushroom fella ran off to..."
    show Char Cac Base
    c "He was with Sunflower earlier, right?"
    show Char Cac Sweat
    c "I reckon he's still gettin' chewed out by Miss Rose, then."
    show Char Cac Surprise
    c "Aw, wait a moment!"
    "Cactus seems to pick something up off the floor."
    show Char Cac Happy
    c "Looks he left a lil' note!"
    scene black with dissolve
    show note with dissolve
    c "He-heh. He might seem rough 'round the edges, but Mushroom really is a fun guy."
    show Cactus1 with dissolve
    show Char Cac Base with dissolve
    c "Get it?"
    menu:
        "...":
            $favorCact -= 1
            c "..."
            show Char Cac Sweat
            c "..."
            call cactus_heheh from _call_cactus_heheh_3
            c "He-heh... Sorry 'bout that. Not my best joke."
        "Heehee, good one!":
            $favorCact += 1
            show Char Cac Sweat
            "Cactus seems flustered."
    c "A-anyway! Accordin' to Sunflower, there's loads to do here if you're interested."
    show Char Cac Base
    c "There's some darn good underground beats here when it comes to music, and the art here is amazing..."
    show Char Cac Happy
    c "Or if yer just too tuckered out, we could always just sit and watch the moss grow!"
    menu:
        "Those music vibes. I want to feel them.":
            c "The music scene, huh? You'll love it!"
            hide Char with dissolve
            scene black with fade
            "You and Cactus decide to go and vibe with the underground scene, watching a band of moss and fungi alike play a jammin' song. You don't say much to each other, but share in the vibes together"
            "The vibes truly are immaculate. After some time passes and you feel all vibed out, Cactus takes you over near the moss to chill."
            jump cacVibes
        "Underground art? I'd love to see it!":
            c "I dunno much 'bout the art scene here, but I've heard it's pretty unique!"
            hide Char with dissolve
            scene black with fade
            "You and Cactus make your way to an art gallery nearby."
            "The pieces you see when you get there are pretty eclectic."
            "A lot of this seems to be a mix of street art and classical art meshed into one. It's honestly quite interesting, and although you and Cactus don't talk much while you walk through the exhibit, you feel like soaking in the fine arts has brought you two closer."
            "A lot of this seems to be a mix of street art and classical art meshed into one. It's honestly quite interesting, and you and Cactus spend a good amount of time in the gallery."
            "Afterwards, you and Cactus decide to go sit next to the moss and relax."
            jump cacVibes

        "The moss... it beckons...":
            show Char Cac Surprise
            c "The moss, huh?"
            show Char Cac Happy
            c "Interestin' choice, Chrys! We can definitely go there."
            scene Fungi1 with fade
            "You and Cactus make your way to the piles of moss and find a nice place to just sit."
            "A gentle breeze from the AC blows your way and the quiet hum of the fridge nearby fills the air. It's nice."
            scene black with fade
            "So nice, in fact, that you begin to doze off..."
            scene Fungi1 with fade
            "... only to wake up a good while later. You look over at Cactus and see him lost in thought, but when you begin to stretch he snaps out of it."
            show Char Cac Surprise with dissolve
            c "Sorry fer wakin' you up, Chrys... you looked pretty darn peaceful. "
            show Char Cac Happy
            c "Glad you're awake though. It's getting pretty darn late and we got a big day tomorrow!"
            show Char Cac Base
            c "We should go ahead n' head on back for the night."
            menu:
                "Sure.":
                    menu:
                        "Tomorrow's Valentine's Day, after all.":
                            pass
                    show Char Cac Sweat
                    c "Yup. Valentine's Day..."
                    show Char Cac Happy
                    c "Here, I'll walk you back home."
                    "You and Cactus scoot your way back to your place. He gives you a tip of his hat, a winning smile, and says goodnight before leaving."
                    menu:
                        "Valentine's Day Approaches...":
                            pass
                    jump CacBadEnding
                "You looked like you were thinking pretty hard about something.":
                    show Char Cac Surprise
                    c "Did I?"
                    jump cacHomesick

label cacVibes:
    scene Cactus1 with fade
    show Char Cac Happy with dissolve
    call cactus_ThanksPardner from _call_cactus_ThanksPardner_1
    c "Thanks for comin' along with me Chrys! I don't usually do these kinds of things, but a slower change of pace is always nice."
    show Char Cac Sweat
    c "Sprouts and buds up here are always hustlin' and bustlin' from place to place, and it's easy to get so swept up in it all."
    show Char Cac Base
    c "Back at home, life was busy in a different way, but there was always time for a smile or a break to talk with others."
    show Char Cac Sweat
    call cactus_sigh from _call_cactus_sigh_2
    c "Guess I'm just missin' that Southern hospitality, is all."
    show Char Cac Happy
    c "But that ain't a big deal! "
    c "..."
    menu:
        "...":
            c "Anyways!"
            menu:
                "...":
                    pass
            show Char Cac Base
            c "It's getting pretty darn late though, and we got a big day tomorrow. We should probably head back."
            jump cacHeadHome

        "You good?":
            $ favorCact -= 1
            show Char Cac Sweat
            c "Yeah, I'm all good. Just thinking 'bout something."
            menu:
                "...":
                    pass
            show Char Cac Base
            c "It's getting pretty darn late though, and we got a big day tomorrow. We should probably head back."
            jump cacHeadHome
        "Are you homesick?":
            $ favorCact += 1
            jump cacHomesick

label cacHomesick:
    show Char Cac Sweat
    c "Was it that obvious?"
    show Char Cac Happy
    c "Well, my ma always said I had an easy face to read!"
    show Char Cac Sweat
    c "...Yeah. I've been feelin' kinda homesick lately."
    c "I haven't really been able to fit in with the other flowers n' sprouts in town..."
    show Char Cac Base
    c "Sure I got Sunflower and Rose to talk to, and they try to make me feel better 'bout it all..."
    show Char Cac Sweat
    c "...but all the other flora seem wary of me and my spikes, sayin' \"it's not appropriate for the flower shop to have me here.\""
    show Char Cac Base
    c "I promise, I'm a big softie..."
    show Char Cac Sweat
    c "..."
    call cactus_heheh from _call_cactus_heheh_4
    c "But to them, I'm just a prickly pear."
    show Char Cac Base
    "Cactus takes a moment to collect himself."
    c "Sorry 'bout that. I uh. I dunno how to feel 'bout all this. Maybe it is better that I head on back home."
    menu:
        "Why head back when you can give the city another chance?":
            menu:
                "With how big it all is, you're bound to find a place to fit in!":
                    pass
            show Char Cac Sweat
            menu:
                " Plus, maybe the other plants just need more time to get used to you.":
                    pass
            call cactus_YerRight from _call_cactus_YerRight_1
            c "He-heh... Maybe you're right."
            show Char Cac Happy
            c "I've been here for a while already, but maybe things will look up soon!"
            show Char Cac Base
            c "I'll sit on it for a 'lil. Give this a bit more thought 'n all."
            c "Thank you for listening, Chrys. I think I'll figure it out."
            c "It's getting pretty darn late though, and we got a big day tomorrow. We should probably head back."
            jump cacHeadHome
        "Not to sound too cheesy, but you have us with you.":
            menu:
                "Sunflower, Rose... They care about you.":
                    pass
            menu:
                " It sounds cliche and all, but it doesn't matter what the others say when they're there for you no matter what.":
                    pass
            show Char Cac Surprise
            c "..."
            show Char Cac Sad
            c "...Chrys..."
            c "You have no right bein' this nice to me."
            show Char Cac Base
            c "Thank you fer that... I'll think about what you've said."
            show Char Cac Sweat
            c "In fact, I feel a bit silly now."
            show Char Cac Base
            c "Goin' back home is still somethin' I'm considering, but thank you for remindin' me that there's also lovely folks here that care 'bout me..."
            show Char Cac Happy
            c "...like you!"
            show Char Cac Base
            c "It'll still be hard to deal with all the others, but I'll try my best."
            call cactus_ThanksPardner from _call_cactus_ThanksPardner_2
            c "Thank you fer that."
            hide Char with dissolve
            scene black with dissolve
            "You and Cactus spend the last moments of the day sitting together and watching the moss grow."
            "Time passes."
            scene Cactus1 with dissolve
            show Char Cac Base with dissolve
            c "It's gettin' pretty darn late, isn't it?"
            show Char Cac Happy
            c "We've got a big day tomorrow. Let's go ahead and head back for the night."
            jump cacHeadHome

label cacHeadHome:
    show Char Cac Base
    c "Here, I'll walk you back to your place."
    "You and Cactus scoot your way back to your place. Before you scoot inside, Cactus turns to you to speak."
    show Char Cac Happy
    c "Thanks for lettin' me show you 'round the place, Chrys. Hope you enjoyed it as much as I have!"
    show Char Cac Base
    c "Rest up, alright? Hopefully I'll see you tomorrow."
    "He gives you a tip of his hat, a winning smile, and a wave goodbye before leaving."
    hide Char
    scene black with fade
    jump cacEndings
label cacEndings:
    scene cashier with fade
    "With morning comes love in the air!"
    "While the shop prepares for the horde of shoppers buying flowers for their beloved, you decide to go and talk to your potential beloved. That is, that special someone who hopefully feels the same in return."
    "You make your way up to where the succulents stay."
    if favorCact >= 3:
        jump CacGoodEnding
    else:
        jump CacBadEnding

label CacGoodEnding:
    "There you spot Cactus, looking his Sunday best. You make your way over to him."
    show Char Cac Happy with dissolve
    c "Oh, Chrys! Didn't see ya there. Are you ready for today?"
    show Char Cac Surprise
    c "I've realized... That I'll stay here for a bit longer."
    show Char Cac Sweat
    c "Even though I still miss the Texas sun from time to time, I'm willing to give this city another shot."
    show Char Cac Happy
    c "Plus, I've got you, Rose, and Sunflower to count on! Y'all have been lifting me up this whole time, so it's high time I stopped mopin' and do the same for y'all!"
    show Char Cac Blush
    c "Maybe now I can finally teach Rose some actual Southern sayin's instead of the ones she found..."
    show Char Cac Happy
    c "...But that's a thought for later. Fer now, I'll focus on today!"
    c "It's gonna be a busy one alright. Hopefully you and both get picked up soon! "
    menu:
        "Cactus, there's something I want to ask you...":
            pass
    menu:
        "I really liked spending time with you yesterday...":
            pass
    menu:
        "and I was wondering if you wanted to do that more often. As romantic partners.":
            pass
    show Char Cac Base
    c "..."
    show Char Cac Sweat
    c "..."

    show Char Cac Sweat Flower
    with flash
    c "..."
    c "ME?"
    show Char Cac Happy Flower
    c "Haha! Of 'course, Chrys! I'd love to go out with you again!"
    show Char Cac Base Flower
    c "I can show you some other places 'round these here parts that are of interest."
    c "... and thank you again for listenin' to my woes and fer puttin' your faith in a cactus like me."
    show Char Cac Happy Flower
    c "Let's go out again soon!"
    scene black with fade
    "And so, Valentine's Day came to an end."
    "By the end of the day neither you nor Cactus were bought, but that was okay. "
    "Y'all had your good friends... a familiar home..."
    "...and a little space in the big city carved out for each other."
    $ ending = 5
    jump credits

label CacBadEnding:

    "But instead of seeing Cactus at his usual spot, all you see is a note with your name on it, among others."
    c "{i}Dear Chrys,{/i}"
    c "{i}By the time you read this I'll be halfway cross this grand ol' country of ours.{/i}"
    c "{i}After our talk I spent a lot of time thinkin' and realized... I feel like I just don't belong here compared to back home in Texas. Bein' here just made me bitter at others, even if they were tryin' to help.{/i}"
    c "{i}So I've decided to move back for the time being. Maybe one day we'll see each other again.{/i}"
    c "{i}Thank you for everything, and I wish you luck today.{/i}"
    c "{i}Warm Regards,{/i}"
    c "{i}Cactus{/i}"
    scene black with fade
    "Valentine's Day passes by in a blur."
    "You're one of the lucky sprouts to be bought, along with Rose and Sunflower."
    "The days fly by at your new home, until one day..."
    "On a cloudy morning you wake to see the daily mail next to your pot. Something familiar lays on top."
    "In your leaves you hold a postcard from Texas. The photo has a variety of cacti smiling back at you."
    "And although you no longer have feelings for your first love, something tugs at your heart."
    "For a second, the clouds part, letting the sun peek through. You face the bright rays streaking in through the window..."
    "...and just for a moment, you can perfectly picture the warm Texas sun shining down on your face."
    $ ending = 6
    jump credits


############ ROSE DATE #######################
label roseDate:
    "As Cactus begins to walk away you see Rose close her eyes and take a deep breath. When they open up she's startled to see you still standing there."
    show Char Rose Surprise
    call Rose_Oh from _call_Rose_Oh
    r "Oh, Chrys I wasn't expecting to still see you here! Uh, Cactus sure is nice for teaching me slang huh?"
    show Char Rose Nervous
    call Rose_Nervous from _call_Rose_Nervous
    "Rose laughs nervously, her eyes pleading with you to play along."
    menu:
        "Totally!":
            pass
    show Char Rose Done
    call Rose_Sigh from _call_Rose_Sigh
    "What remains of her smile quickly evaporates. She lets out a heavy sigh and her demeanor deflates."
    show Char Rose Base
    r "That's good. Do you think I was being rude at all? I'd hate to impose on you or Cactus."
    menu:
        "Well, it might have been too much. It felt a little abrasive.":
            call Rose_OhNo from _call_Rose_OhNo
            $ favorRose += -1
            show Char Rose Sad
            r "Oh ..."
            "Rose seems taken aback by your answer. She looks at the ground with a sullen expression."
            menu:
                "Everything OK Rose? ":
                    pass
            show Char Rose Nervous
            call Rose_NervousLaughter from _call_Rose_NervousLaughter
            "She looks up to meet your gaze and lets out a nervous laugh."
            r "I guess I'll have to find a way to make it up to him, huh?"
            menu:
                "I guess so.":
                    pass

        "Not at all! It was all in good fun.":
            $ favorRose += 1
            show Char Rose Happy
            call Rose_Yay from _call_Rose_Yay
            r "Oh, thank goodness! Sometimes I, uh, really worry about accidentally being mean."
            menu:
                "Nonsense, I've never seen you be rude before. ":
                    pass
            show Char Rose Blush
            call Rose_OK from _call_Rose_OK
            "Rose looks away bashfully. There's a moment of silence between the two of you."
            show Char Rose Nervous
            call Rose_NervousLaughter from _call_Rose_NervousLaughter_1
            r " Sorry about that. I just... I just get nervous about stuff like that."
            menu:
                "Don't worry about it. ":
                    pass
    show Char Rose Happy
    call Rose_Yay from _call_Rose_Yay_1
    r "Haha, thanks Chrys."
    show Char Rose Sad
    call Rose_Sigh from _call_Rose_Sigh_1
    r "I was just trying to go with the flow. Sometimes that goes well, other times... less so."
    r "In the moment it feels right, but afterwards..."
    show Char Rose Base
    r "Rose frowns and shakes herself. The frown slowly turns into a smile."
    menu:
        "Rose, are you alright?":
            $favorRose += 1
            r "Oh, I'm sorry you had to see that. It's nothing you need to worry about honey."
        "*Ignore it*":
            pass
    show Char Rose Surprise
    call Rose_OhGod from _call_Rose_OhGod
    "Glancing outside, a sudden look of panic overtakes Rose. Turning to you, she gives a sheepish look."
    r "I'm really sorry to have to do this to you, Chrys, but it looks like the time escaped me."
    r "I'll be right back, I just have to talk to someone. I'll be right back, promise!"
    menu:
        "Ok, take your time!":
            pass
    hide Char with fade
    "You watch as Rose makes a mad dash deeper into the store, leaving you all by yourself."
    scene Cactus1 with fade
    "A few minutes pass before you're approached by another plant."
    sp "Hey, you! That was Rose a few minutes ago, wasn't it?"
    menu:
        "Sure was! Isn't she so nice?":
            sp "Sprout: No! She broke her promise to me."
            menu:
                "Really? What did she promise you? ":
                    pass


        "Yeah, it was.":
            sp "Show me where she went! She broke a promise!"
            menu:
                "What are you talking about?":
                    pass
    "Sprout tremors a little bit and tears begin to well in his eyes."
    sp "She said she would keep my parents around. But she lied!"
    sp " I-I woke up on Valentine's last year and I couldn't find them at all!"
    menu:
        "I'm sorry to hear that buddy.":
            sp "I'll never forgive her. Now, I don't have my mommy and daddy with me!"
        "That's a pretty difficult promise to keep.":
            sp "But she made that promise to me! Clearly she didn't care about that."
    "Sprout's sad expression changes to one of anger."
    menu:
        "I'm sure she tried her hardest to prevent it, Sprout.":
            pass
        "Man, that's messed up.":
            pass
    sp "I don't care what you have to say. I'm here to talk to her!"
    sp "Tell me where she is!"
    menu:
        "I don't know where she went, I'm new around here.":
            pass
        "She went to take care of something.":
            pass
        "She just got sold. She was just saying goodbye to me.":
            pass
    sp "You're not trying to lie to me just because I'm young, right?"
    menu:
        "Of course not!":
            pass
        "I'm not lying.":
            pass
        "No, I'm lying.":
            pass
    "Before you can reply to Sprout you see Rose return from within the store."
    show Char Rose Base with dissolve
    call Rose_HeyHappy from _call_Rose_HeyHappy
    r "Hey Chrys, sorry that took so long. I wa-"
    sp " Rose! You have some explaining to do!"
    show Char Rose Surprise
    call Rose_Oh from _call_Rose_Oh_1
    "Rose's eyes widen as she hears Sprout yell. She tenses up at the sound of it."
    show Char Rose Nervous
    call Rose_OhHm from _call_Rose_OhHm
    r "Oh! Sprout I, uh, didn't see you there. What's, um, wrong little buddy?"
    sp "Oh you know what you did! You can't hide from me forever you coward."
    show Char Rose Sad
    call Rose_OhGod from _call_Rose_OhGod_1
    r "What? What did I do wrong? I try really hard to be nice to people! Please, I don't want you to be upset with me."
    menu:
        "Hey Sprout, that's uncalled for.":
            $ favorRose += 1
            sp "No it's not Chrys. She made a promise and then broke it. She needs to explain herself!"
            call Rose_OhNo from _call_Rose_OhNo_1
            "Rose is shaking and tears are welling in her eyes. She looks mortified."
            call Rose_Sorry from _call_Rose_Sorry
            r "Oh no, Sprout. I'm so sorry! I know I gave you my word, and yet..."
            menu:
                "See, I told you Sprout.":
                    pass
            r "You have no idea...no idea how hard I tried. I just wasn't good enough. I...I wasn't enough. I know you might not believe me, but I didn't lie."

        "Rose, this isn't a fixable problem.":
            $ favorRose += -1
            show Char Rose Surprise
            call Rose_OhNo from _call_Rose_OhNo_2
            r "Huh? Chrys what are you talking abou-"
            show Char Rose Base
            "A flash of realization shoots across Rose's face before it's overtaken by a quiet numbness."
            show Char Rose Sad
            call Rose_Sorry from _call_Rose_Sorry_1
            "Rose begins to tremble and cry. The pressure is too much to bear."
            r "I never meant for it to happen. I did my best, but it wasn't enough in the end. Sprout, you have to believe me!"
            r "I never wanted to let you down, but... I guess that's what I always do. I'm sorry."
    sp "No, I don't believe it. There's no way you're telling the truth. I hate you Rose!"
    "Sprout turns and runs away with tears in his eyes."
    show Char Rose Surprise
    call Rose_OhGod from _call_Rose_OhGod_2
    r "No, Sprout, please come back! I... I need to make it up to you."
    show Char Rose Sad
    "Rose is visibly shaking, her tears dripping to the floor."
    call Rose_Sorry from _call_Rose_Sorry_2
    r "I really screwed this one up. God, everyone must really hate me now, huh?"
    show Char Rose Nervous
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_2
    "Rose lets out yet another nervous laugh."
    menu:
        "Rose, are you ok?":
            pass
    show Char Rose Sad
    "Rose doesn't seem to register your question. Her face is blank and her hands are shaking."
    menu:
        "Rose?":
            pass
    show Char Rose Base
    "Rose looks up and quickly shakes her body. The blank expression is replaced by a soft smile."
    show Char Rose Happy
    call Rose_HeyHappy from _call_Rose_HeyHappy_1
    r "Oh, Chrys. It's nothing, don't worry! What's up?"
    menu:
        "Rose, are you alright? It looked like that took a toll on you.":
            pass
    show Char Rose Nervous
    call Rose_Sigh from _call_Rose_Sigh_2
    r "Oh Chrys, I appreciate the concern, but you don't need to worry about me. I don't want to weigh you down. This is my problem, not yours."
    menu:
        "OK, if you say so Rose.":
            pass
    show Char Rose Happy
    call Rose_Yay from _call_Rose_Yay_2
    r "Yes, I'll be alright! Now I'm supposed to show you around, right?"
    menu:
        "Yup, that's what I was told.":
            pass
    r "Well then, they set you up with the right person! I know this place like the back of my hand."
    menu:
        "Great, let's go!":
            pass
    show Char Rose Base
    r "I've got some errands to run, so this is perfect for both of us. Where do you want to go first?"
    menu:
        "The Cashier":
            jump roseCashier
        "The Perennials Section":
            jump rosePerennial
        "The Patio":
            jump rosePatio

label roseCashier:
    show Char Rose Surprise
    call Rose_OhHm from _call_Rose_OhHm_1
    r "Oh, the cashier huh? I guess we can go there."
    menu:
        "Is there something wrong with the cashier? ":
            pass
    show Char Rose Base
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_3
    r "No, no, it's nothing. I did offer to take you there. I'm just surprised, it's not exactly a popular spot."
    menu:
        "Do you not want to go?":
            r "No, nothing like that, Chrys. If you want to go, we can. Come on."
            menu:
                "OK.":
                    pass
        "Lead the way!":
            call Rose_Yay from _call_Rose_Yay_3
            r "OK!"
    r "Maybe we can hit the perennials section on the way back, just so you get the whole experience."
    "You follow Rose as she leads you through the store. You pass by the perennials section, which is full of daisies and other assorted plants."
    "Along the way you pass Mushroom, Cactus, and Sunflower, who all wave."
    menu:
        "Wave back as you walk by":
            "As Rose leads you through the store you wave back to your new friends. Rose gives a small wave to each of them but powers on past them."
            menu:
                "Follow her lead.":
                    pass
        "Stop and say hello.":
            "As you slow down to talk to them Rose turns around to talk to you."
            show Char Base Nervous
            call Rose_Sigh from _call_Rose_Sigh_3
            r "Hey Chrys, I thought we were, uh, going to the cashier."
            menu:
                "Oh yeah, my bad. Let's go!":
                    pass
    hide Char with fade
    "Eventually you reach the massive structure that is the counter. There's a loosely constructed pile of gardening supplies that leads up to the counter. Rose looks intimidated."
    show Char Rose Nervous with fade
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_4
    r "So Chrys, you, uh, ready to climb up there?"
    menu:
        "I'm a little scared, but I'll manage as long as you're with me.":
            show Char Rose Happy
            call Rose_HeyHappy from _call_Rose_HeyHappy_2
            r "Oh Chrys, you're so nice to me for no reason. To be honest I'm scared of it too. It's why so few plants come here."
            r "But with you here I think I'll be just fine."
            menu:
                "Yeah, let's go!":
                    pass
            "Rose gives you a timid nod and begins the trek up to the cashier."
            menu:
                "Follow her.":
                    pass

        "Yeah, this looks fun.":
            r "Oh? I know, righ-"
            call Rose_Sigh from _call_Rose_Sigh_4
            "Rose looks around nervously, before letting out a sigh."
            r "You're a brave one, aren't you?"
            "Rose tries her best to hide it, but she looks really nervous."
            menu:
                "Rose, are you alright?":
                    $favorRose += 1
                    r "Can I be honest with you?"
                    menu:
                        "Of course you can Rose, we're friends.":
                            pass
                    r "And you won't be upset with me?"
                    menu:
                        "No, I could never be upset with you.":
                            pass
                    call Rose_NervousLaughter from _call_Rose_NervousLaughter_5
                    r "OK, um. The truth is that, I, uh, I don't like going up to the cashier. Climbing this stuff scares me."
                    menu:
                        "Honestly Rose, it scares me too.":
                            $favorRose += 1
                            show Char Rose Surprise
                            r "Really? But you don't seem scared at all."
                            menu:
                                "Well on the inside I am, so let's work together and we can get through this.":
                                    pass
                            "Rose gives you a timid nod and begins the trek up to the cashier."
                        "You just have to get over it. Don't be such a scaredy-cat.":
                            $favorRose += -2
                            call Rose_HeySad from _call_Rose_HeySad
                            r "Oh, I'm sorry. I guess you're right. I'll try to be better."
                            menu:
                                "Now let's do this.":
                                    pass
                "Come on, let's go!":
                    $favorRose -= 1
            "Rose gives you a timid nod and begins the trek up to the cashier."
            hide Char with fade
            menu:
                "Follow her.":
                    pass
    "As you and Rose climb upwards you walk over gardening pots, bags of fertilizer, and even some gardening tools. But eventually you reach the cashier counter."
    show Char Rose Happy with fade
    call Rose_Yay from _call_Rose_Yay_4
    r "Wow Chrys, we were able to do it!"
    menu:
        "Of course we were able to. I believed in you the entire time!":
            $favorRose += 1
            show Char Rose Blush
            call Rose_Oh from _call_Rose_Oh_2
            "Rose blushes and hides behind her leaves."
            show Char Rose Wink
            r "Aw, Chrys you're too much. I'm not worth half the compliments you give me."
            menu:
                "Come on Rose, you know you're worth more.":
                    pass
            r "Gosh, you really now how to make me feel better Chrys."

        "I'm a little surprised we made it honestly.":
            show Char Rose Surprise
            r " Oh, really? I'm sorry if I was slowing you down. I tried my hardest but I guess that was still too little."
            menu:
                "Don't feel too bad Rose. You could have done a lot worse.":
                    call Rose_OhNo from _call_Rose_OhNo_3
                    $favorRose += -1
                    r "Yeah, I guess you're right."
                "No Rose, you were great! I was worried about myself.":
                    $favorRose += 1
                    call Rose_HeyHappy from _call_Rose_HeyHappy_3
                    r "Really? I thought you did great, like way better than I did. "
                    menu:
                        "Thanks Rose!":
                            pass
                    "You're welcome Chrys."
    show Char Rose Base
    call Rose_OK from _call_Rose_OK_1
    r "Anyways, I guess I should show you around now. Considering that's my job and all."
    menu:
        "Sounds like a plan.":
            pass
    hide Char with fade
    "Rose walks you further along the counter and you're met with the full beauty of the shop for the first time."
    "The light from outside falls in at the perfect angle, casting each flower in a beautiful bath of sunshine. There are other flowers up here, but you barely notice them while you're caught up in the splendor of the store."
    "You stand together on the counter, taking the sight in. Rose takes a deep breath and relaxes her body. She turns and looks at you."
    show Char Rose Base with fade
    r "This is my favorite place in the whole store Chrys. Did I tell you that?"
    menu:
        "Let her continue.":
            r "I know I shouldn't love this place because of what goes on here... I just can't help it."
            show Char Rose Happy
            r "Normally I don't like to be around other people, even if we aren't talking, but when I'm up here I don't care. The peace I feel here trumps everything else."
            menu:
                "I can see why. It really is beautiful.":
                    pass
            r "I'm really happy to be here right now. Today has been rough, especially with Sprout being upset with me."
            menu:
                "I'm sure. That was really rough to watch.":
                    pass
            show Char Rose Done
            r " It wasn't easy to deal with either. I hate messing things up for people, and I really hate it when they're mad at me. It just makes me feel horrible."
            menu:
                "I've noticed that a lot today. You shouldn't care about what other people think, you're great!":
                    pass


        "No, you didn't mention that.":
            show Char Rose Nervous
            call Rose_OhHm from _call_Rose_OhHm_2
            r "Oh, uh... Well it is. This is my favorite place to be by myself. I'm most calm when I come here. "
            r "Honestly, I was worried having you with me would change that."
            menu:
                "Why would that change things?":
                    show Char Rose Surprise
                    r "Oh no Chyrs, it's not that! I just have trouble being around other people. It makes me really nervous. I was worried that if I came here with someone else it would take away from the experience."
                    show Char Rose Wink
                    r "Being here is kind of theraeputic, and I didn't want that to change. But now that I'm here with you Chrys, I think I was worried about nothing."
                    menu:
                        "Thanks Rose, that means a lot.":
                            pass
                    show Char Rose Base
                    r "No problem. You spending the day with me means a lot too. Thank you for putting up with everything."
                    menu:
                        "No problem.":
                            pass
                    jump roseCashier2
                "Oh, do you not like me?":
                    call Rose_OhNo from _call_Rose_OhNo_4
                    r "No, Chrys. I like you a lot, you're really kind. I just have trouble being around other people. I just get nervous easily and this is the one place I can escape to. I was just worrying about nothing, please don't hate me for it."
                    menu:
                        "OK, I think I understand. And Rose, I could never hate you.":
                            pass
                    r "OK, that's good to hear. I feel like people don't like me a lot of the time, so I worry it's true."
                    menu:
                        "I've noticed that. You have to stop worrying about what other people think Rose.":
                            $favorRose += -1
                            pass
                        "That's alright Rose. Just remember that you're a great person and that most people don't have a reason to hate you.":
                            $ favorRose += 1
                            show Char Rose Blush
                            r "Thanks Chrys. It seems like you always know just what to say."
                            menu:
                                "It's nothing Rose.":
                                    jump roseCashier2
    show Char Rose Angry
    r "I try Chrys but it's not that simple. Listen I appreciate it, but can we move on. I want this to stay my happy place."
    menu:
        "Yeah, if that's what you want.":
            jump roseCashier2

label roseCashier2:
    show Char Rose Happy
    call Rose_Oh from _call_Rose_Oh_3
    "You and Rose sit in silence for some time, ignoring the other plants around you and soaking in the beauty. Rose seems to sink into a deep, trance-like calm and closes her eyes after a while."
    show Char Rose Surprise
    "The solemn moment goes on for a while before Rose opens her eyes. When she sees you sitting next to her she seems startled."
    menu:
        "Everything OK, Rose?":
            pass
    show Char Rose Nervous
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_6
    r "Um, yeah totally. I just got, uh, lost in the moment is all. Sorry I was quiet for so long."
    menu:
        "No worries, it's fine.":
            pass
    show Char Rose Base
    call Rose_OK from _call_Rose_OK_2
    r "OK, good. What do you think of the store so far?"
    menu:
        "It's great! Everybody here seems really nice.":
            jump roseCashierNice
        "It's fine. I guess I'm not super enthused.":
            jump roseCashierAlright
        "I don't really like it so far.":
            jump roseCashierDislike
label roseCashierNice:
    show Char Rose Happy
    "A smile lights up on Rose's face."
    r "That's good to hear. Yeah everybody here is really kind. I just don't talk to them enough to really know them."
    menu:
        "Why is that?":
            pass
    show Char Rose Nervous
    call Rose_Sigh from _call_Rose_Sigh_5
    "Rose's smile turns to a slight frown and she droops a bit."
    r "I don't know. I feel like I'm bad at talking and I get embarrassed when I do. It just makes me uncomfortable, y'know."
    menu:
        "I totally understand, that makes sense. Do you feel that way now?":
            pass
    show Char Rose Done
    "Rose freezes for a moment and all expression bleeds from her face."
    show Char Rose Sad
    call Rose_Sorry from _call_Rose_Sorry_3
    r "I wasn't before, but I guess I am now. Sorry, I tried going with the flow again and it blew up."
    menu:
        "No that's ok Rose. It's my fault, I brought it up. Let's move on, OK?":
            pass
    show Char Rose Base
    "Rose's deadpan expression is replaced with a more neutral look."
    r "OK, yeah. Sorry Chrys."
    menu:
        "It's fine.":
            jump roseCashier3
label roseCashierAlright:
    "Rose grows a small frown and she looks a little worried."
    r "Oh no, I'm sorry to hear that Chrys. Maybe it will grow on you some more."
    menu:
        "Yeah, maybe. What do you like about this place so much?":
            pass
    show Char Rose Surprise
    "Rose's face lights up with a quizzical look."
    show Char Rose Base
    r "That's a good question Chrys. Hmmm.... I guess I would say this place right here. Being able to come here makes it all worth it."
    menu:
        "Oh, so there are parts you don't like?":
            pass
    show Char Rose Nervous
    "Rose seems caught off guard by your question. A nervous smirk replaces her questioning look."
    r "Oh, um, I guess I'd have to say all the people. I don't really do well with others."
    menu:
        "Come on Rose, you handle other people like a pro.":
            pass
    show Char Rose Done
    "Rose's smirk quickly falters into a frown. She looks down at the ground for a moment as her shoulders fall."
    r "Maybe it seems that way Chrys, but that's not how I feel after talking to someone."
    menu:
        "Oh, I'm sorry Rose. I didn't mean to push so hard.":
            pass
    show Char Rose Sad
    r "Don't worry about it, it's nothing new."
    jump roseCashier3
label roseCashierDislike:
    show Char Rose Surprise
    "Rose is taken aback by your comment. Her face goes from shocked to sad in just a few seconds."
    show Char Rose Sad
    call Rose_OhNo from _call_Rose_OhNo_5
    r "Oh Chrys, I'm really sorry to hear that. I know being moved can be a hard adjustment."
    menu:
        "Yeah, it hasn't been the easiest.":
            pass
    "Rose gives you a look of pity. She seems to genuinely feel bad about it."
    show Char Rose Happy
    call Rose_HeyHappy from _call_Rose_HeyHappy_4
    r "But since I've met you just this morning I've grown to like you a lot. You'll get used to it in no time!"
    menu:
        "You really think so?":
            pass
    show Char Rose Nervous
    r "I know so! Hey, you might even become more popular than me."
    menu:
        "Hah, maybe. We'll see though.":
            pass
    show Char Rose Blush
    "Rose turns away as she blushes and shakes her head."
    "Sorry, that was awkward. Let's just... let's just leave it at that."
    menu:
        "Um, OK.":
            jump roseCashier3
label roseCashier3:
    show Char Rose Base
    "An awkward silence settles in the air. Rose looks tenser than when you first arrived at the cashier."
    menu:
        "Do you have any gossip to share?":
            show Char Rose Surprise
            call Rose_Oh from _call_Rose_Oh_4
            "Rose looks up from a trance a little caught off guard."
            show Char Rose Nervous
            r "No, not really. I'm ... I'm sorry, I don't really talk to many people."
            menu:
                "Oh it's alright Rose, I was just trying to make small talk.":
                    pass
            show Char Rose Done
            "Rose takes a deep breath. She looks tired."
        "How long have you been around the store for?":
            show Char Rose Surprise
            call Rose_Oh from _call_Rose_Oh_5
            "Rose is caught off guard by the question at first. She looks at you surprised."
            show Char Rose Nervous
            "How long have I? Oh, um, I've been here for a year and a half. Why?"
            menu:
                "I was just curious and tried to make small talk is all.":
                    pass
            "Oh I see.... sorry I didn't pick up on that."
            menu:
                "It's alright, Rose":
                    pass
    call Rose_Sorry from _call_Rose_Sorry_4
    r "I'm sorry. I guess I'm pretty bad at small talk. Hey... what do you say we, uh, call it a day?"
    menu:
        "Already?":
            r "Yeah. I just had a really long day. C'mone, let's go."
        "OK, yeah. That sounds alright to me.":
            pass
    hide Char with fade
    "Rose begins to lead you back down to the ground. You take one last look at the splendor that is the store before you head down after Rose."
    scene Rose2 with fade
    "You follow Rose down the haphazard path and along the floor to the perennials section. Eventually she leads you to your new home."
    show Char Rose Happy
    call Rose_HeyHappy from _call_Rose_HeyHappy_5
    r "OK Chrys, this is your new home!"
    menu:
        "Thanks for taking me Rose. I had a good time today.":
            pass
    show Char Rose Blush
    "Rose blushes a little, but still looks tired."
    show Char Rose Base
    r "You're welcome Chrys. Now have a good night."
    menu:
        "You too!":
            jump roseWork
label rosePerennial:
    call Rose_OK from _call_Rose_OK_3
    r "OK, that sounds good to me. I can't wait to show you where you'll be living."
    show Char Rose Happy
    "Rose gives you an excited smile before turning around to lead the way."
    hide Char with fade
    "Rose leads you along the floor through the store. You pass by lots of other plants along the way, and you even see Sunflower, Cactus, and Mushroom."
    menu:
        "Wave as you walk by.":
            "You give them a polite wave and Rose follows your lead. They all wave back at you with smiles on their faces."

        "Hey Rose, let's go say hi.":
            show Char Rose Nervous with fade
            r "Oh, uh. I don't know if we'll have time to get to everything then Chrys. I don't want you to miss out on the tour."
            menu:
                "Y'know what, you're right. I can say hi to them another time.":
                    show Char Rose Base
    "Rose looks back at you pleased before continuing to lead you towards the perennials section."
    hide Char with fade

    "Eventually you reach your destination, a table with enough space for every perennial in the store, including you and Rose. Off in the distance you can see the cashier."
    show Char Rose Happy with fade
    "Rose turns around to speak to you with a wide grin on her face."
    r "Oh Chrys, I'm so excited to show you your new home. How do you feel?"
    menu:
        "Honestly, nervous.":
            show Char Rose Base
            "Rose's excitement falters a bit before being replaced by a look of determination."
            "I understand that Chrys. When I first got here I was really nervous too. Hey, I'm still a little nervous now. But you have nothing to worry about."
            menu:
                "But what if they don't like me?":
                    show Char Rose Surprise
                    "Rose looks taken aback for a second."
                    show Char Rose Base
                    r "Oh Chrys, trust me, that won't be a problem. You're wonderful to be around, and all the perennials are very nice."
                    menu:
                        "If you say so.":
                            pass
                    show Char Rose Wink
                    r "I do! And hey, if they don't like you for some bizarre reason, you'll still have me."
                    menu:
                        "Thanks Rose.":
                            pass
                "Thanks Rose. With you here I think I'll be ok.":
                    pass
        "I'm pumped!":
            pass
    "Rose's face lights up again."
    call Rose_Yay from _call_Rose_Yay_5
    r "Great! Come on, let's get up there and show you around."
    hide Char with fade
    "Rose turns back around and shows you the way up to the perennials section."
    scene Rose2 with fade
    "Once you reach the top you're able to see more of the store. It's a beautiful mix of every color imaginable and there are plants everywhere. Rose watches with you, a look of pride on her face."
    show Char Rose Base with fade
    r "Isn't it great Chrys?"
    menu:
        "It's so pretty. Way better than my old store.":
            jump rosePerennialPretty

        "It's alright. My old store was much better.":
            jump rosePerennialNicer

        "It was only a little bit better. This place is still pretty good.":
            jump rosePerennialAlright

label rosePerennialPretty:
    $ roseFavor += 1
    show Char Rose Happy
    "A small smirk takes up Rose's face."
    r "I'm glad you like it so far Chrys. I think you're gonna get along great. But let me show you around here like I'm supposed to."
    menu:
        "Thanks Rose, that sounds good.":
            pass
    jump rosePerennial2

label rosePerennialAlright:
    show Char Rose Base
    r "Oh ok, gotcha. I'm glad it's not too much worse."
    r "But enough of that. How about I show you around now?"
    menu:
        "Sounds good.":
            jump rosePerennial2

label rosePerennialNicer:
        show Char Rose Surprise
        call Rose_Oh from _call_Rose_Oh_6
        "Rose looks at you surprised."
        r "Really? Nicer than all this?"
        menu:
            "Yeah, even nicer than this.":
                "Rose looks at you with total disbelief."
                show Char Rose Base
                r "There is no way, this place is like a paradise. What made it so much better?"
                menu:
                    "Well there were five times as many plants and three times as many colors. It was beautiful.":
                        show Char Rose Surprise
                        "Rose seems awestruck by the idea of even more flowers and colors."
                        r "Wow! That.... that sounds amazing Chrys. No wonder you miss it, I would too. I can't imagine anything more colorful than this store."
                        menu:
                            "Yeah, it was a sight to behold.":
                                pass
                        show Char Rose Base
                        "Rose nods in agreement. She seems lost in her thoughts for a moment before, suddenly, she shakes herself back to reality."
                        "Oh, sorry Chrys. I was just thinking about all those colors. Anyways, I should probably show you around now, huh?"
                        menu:
                            "That seems like a good idea.":
                                jump rosePerennial2
                    "Each plant had their own space separated from everyone else. We also got watered at the perfect time.":
                        "Rose's eyes widen when she first hears this. She seems to be excited by the idea."
                        show Char Rose Happy
                        r "Wow Chrys, I would kill to have a space all to myself!"
                        show Char Rose Nervous
                        r "Er, well not really but I sure would like it."
                        menu:
                            "It was pretty great, but it did get lonely at times.":
                                pass
                        r "I don't think I would mind that too much. Anyways, what do you say I show you around now?"
                        menu:
                            "Seems like a good idea.":
                                jump rosePerennial2
                    "People barely got sold. We would just sit in the ground all day and enjoy life.":
                        show Char Rose Done
                        "Rose seems a little distraught when she first hears this."
                        show Char Rose Base
                        r "Really? That seems crazy. I wish it was like that here. I feel like I've let so many people down. Especially Sprout."
                        menu:
                            "Oh Rose, I'm sure you did everything you could. Don't feel bad about it.":
                                pass
                        "Rose looks at you, a little relieved but still a little upset."
                        r "Yeah I know, I just wish it was that easy."
                        show Char Rose Happy
                        "Rose puts on an over-eager smile again and looks at you."
                        r "Anyways, let's get back to the tour, alright?"
                        menu:
                            "Sounds like a plan.":
                                jump rosePerennial2




label rosePerennial2:
    scene Rose1 with fade
    "Rose turns around and begins leading you through the perennials section. The first group you meet are the daisies."
    show Char Rose Base
    "Rose takes a deep breath and tries to loosen up a bit before speaking."
    r "OK, so these are the, uh, daisies. I think they look really nice and they seem to be polite."
    menu:
        "Is there anything else about them I should know?":
            pass
    show Char Rose Blush
    "Rose looks down at the ground and blushes a bit."
    show Char Rose Base
    r "That's, uh, all I really know Chrys. Sorry, I don't talk to the daisies very often."
    menu:
        "It's fine Rose, don't worry about it.":
            pass
    r "Thanks Chrys. Here, I'll keep showing you around."
    menu:
        "OK.":
            pass
    show Char Rose Happy
    "Rose seems a little dejected at first, but she puts a big smile on again and leads you around."
    r "OK, so these are the...."
    show Char Rose Nervous
    "Rose seems to be thinking really hard. Her hands are shaking a bit."
    show Char Rose Base
    call Rose_Oh from _call_Rose_Oh_7
    r "The.... Oh yeah! These are the foxgloves. They seem kind of mopey at first, but I think they look cool. Whenever I see them they seem very chill."
    menu:
        "Oh so you know them?":
            pass
    show Char Rose Nervous
    "Rose lets out a nervous laugh."
    r "Oh I, uh... No, I actually don't know them that well. If I did I would tell you some more but, y'know."
    menu:
        "Yeah, it's no biggie Rose.":
            pass
    show Char Rose Base
    "Rose nods before turning to lead you to the next spot. She seems to be moving slower than before, and even looks a little down."
    menu:
        "Rose, are you alright?":
            pass
    show Char Rose Surprise
    "She turns around and looks surprised."
    r "Oh yeah, I'm fine. I'm just a little tired because today has been long."
    menu:
        "OK, just making sure.":
            pass
    show Char Rose Wink
    r "Yeah of course! Anyways... This is actually where I live! I would tell you something, but you already know me."
    show Char Rose Nervous
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_7
    "Rose lets out a nervous laugh and looks at you intently."
    menu:
        "Laugh with her":
            $favorRose += 1
            "Rose gives you a nervous smirk when you laugh too."

        "Do nothing.":
            $favorRose += -1
            show Char Rose Sad
            "Rose looks a little sad when you don't laugh too."
            r "Sorry, I, uh, thought that was funny."
    show Char Rose Base
    r "Anyways, let's keep going."
    menu:
        "*Give a thumbs up.*":
            pass
    hide Char with fade
    scene Rose1 with fade
    "Rose leads you deeper into the perennials section and stops at an empty spot."
    show Char Rose Happy with fade
    call Rose_OK from _call_Rose_OK_4
    r "This is actually your new home Chrys! Aren't you happy we found it?"
    menu:
        "Yeah, it looks great.":
            pass
    "Rose gives you a small smile."
    r "I'm glad you like it. I actually have a quick question for you."
    menu:
        "Yeah, what's up?":
            pass
    show Char Rose Nervous
    "Rose swallows hard and looks anxious."
    call Rose_HeySad from _call_Rose_HeySad_1
    r "OK, so, uh, I was wondering, if it's ok with you, if we could... call it a day?"
    menu:
        "Yeah, if that's what you want.":
            pass
    show Char Rose Base
    "Rose looks relieved as she quickly loosens up."
    call Rose_OK from _call_Rose_OK_5
    r "Great. I wanted to show you more, it's just that... Today was really long, especially with the whole Sprout thing. I'm just really tired."
    menu:
        "Don't worry about it Rose. Go get some rest.":
            pass
    r "Thanks for understanding Chrys. See you soon?"
    menu:
        "Totally.":
            pass
    r "Great. Have a good night."
    menu:
        "OK Rose, good luck.":
            pass
    jump roseWork

label rosePatio:
    show Char Rose Happy
    "Rose looks excited and gives you a big smile."
    call Rose_Yays from _call_Rose_Yays
    r "Great, the patio is awesome. I don't get to go there very often so this will be fun for me too."
    menu:
        "Sweet, let's go.":
            pass
    scene Window with fade
    "Rose begins to lead you through the winding paths of the store. Along the way you pass various sections you've never seen before."
    "You pass by the annuals section, which is filled with all kinds of flowers. You can see a periwinkle, snapdragon, marigold, and a petunia."
    "Rose notices you looking at them, so she turns around to talk to you."
    show Char Rose Base
    r "That's the annuals section. They all seem really nice and I think they're each beautiful, but they don't stay around for very long."
    menu:
        "Why don't they stay around?":
            pass
    "Rose shrugs."
    r "They just don't live as long as us perennials. It's a little weird, but that's just how it is."
    "Rose continues to show you around the store. She hums a small tune as you approach the door to the patio."
    "The door is huge and imposing. Light filters in through the glass set in its middle. You can see the outside world from here."
    "Rose notices your apprehension as you both move closer to the door."
    r "You okay, Chrys? You seem a little nervous."
    menu:
        "Yeah, I'm fine.":
            "Rose gives you a small nod."
            call Rose_OK from _call_Rose_OK_6
            r "OK, if you're sure then let's keep going."


        "I'm honestly a little nervous.":
            "Rose gives you an affirming nod."
            call Rose_OhNo from _call_Rose_OhNo_6
            r "I understand Chrys. I was worried about it at first too, but I did it and I was fine. It wasn't easy, but I think you can do it too."
            menu:
                "Thanks Rose. I think you're right.":
                    pass
            "OK, if you're sure you want to do it we can go."
            menu:
                "I am.":
                    pass
    "As you and Rose near the massive glass door you hear the whir of machinery begin. The door begins to part automatically, and before long there is a way outside."
    menu:
        "Rose, what was that? What just happened?":
            pass
    show Char Rose Surprise
    "Rose looks at you with a puzzled expression for a moment. Then, something clicks in her head and she begins to speak."
    show Char Rose Base
    r "Oh yeah, I forgot to tell you. These doors open automatically! Isn't it cool?"
    menu:
        "Huh, yeah it is.":
            pass
    "Rose leads the way through the doors. Once you pass the threshold you're hit with a blast of fresh air and light."
    "The sound of the city fills your head fully for the first time. The low drone is off-putting at first, but soon fades into the back of your head."
    "Rose turns around to look at you and gestures widely at the store's patio."
    r "So, what do you think Chrys?"
    menu:
        "I like it! It's a nice touch.":
            show Char Rose Happy
            "Rose gives you a big smile."
            call Rose_Yay from _call_Rose_Yay_6
            r "I'm glad you like it Chrys. It's nice to come out here every now and then."
            show Char Rose Base
            r "Let me show you around some more."
            menu:
                "Okay!":
                    jump rosePatio2
        "It's alright. It's really loud out here though.":
            "Rose nods in agreement."
            call Rose_NervousLaughter from _call_Rose_NervousLaughter_8
            "Yeah, it can be annoying. I like to be out here occasionally, but after a while it gets to be too much."
            menu:
                "Is it the noise or something else?":
                    pass
            show Char Rose Nervous
            "Rose looks a little nervous suddenly."
            call Rose_Sigh from _call_Rose_Sigh_6
            r "Well, uh, sometimes when we get put out here we're mixed with other plants. Like perennials will be with annuals. I don't know any of them that well, so I get anxious because they're new people."
            r "So with that and all the noise, it can be rough after a while. That's why I only come here sporadically. It's kind of dumb though."
            menu:
                "Nonsense, it's not dumb":
                    pass
            show Char Rose Base
            call Rose_OK from _call_Rose_OK_7
            r "Thanks Chrys. You're so supportive."
            r "Let me show you around some more Chrys."
            jump rosePatio2


label rosePatio2:
    "Rose leads you towards a table set in front of the store window. Right now it's relatively empty, but it looks like a lot of plants can fit up here."
    show Char Rose Nervous
    "Rose gets a little nervous as she approaches the table."
    call Rose_HeySad from _call_Rose_HeySad_2
    r "So this is the, uh, the table where we, um, we spend time outside. Sometimes we get put out here at random."
    menu:
        "Rose, are you okay?":
            pass
    "Rose shakes herself out a little bit."
    r " Yeah, I'm fine Chrys. I just have some bad memories with this table."
    menu:
        "Do you want to talk about it?":
            pass
    "Rose shakes her head."
    show Char Rose Base
    r "That's alright Chrys, I appreciate the offer though.."
    menu:
        "No problem.":
            pass
    r "Anyways... So yeah, you might get put out here with plants from all the different sections. I guess it's a good way to meet other people."
    menu:
        "You don't seem sure.":
            pass
    show Char Rose Nervous
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_9
    r "Sorry Chrys, I'm just bad at first impressions. Other people seem to do it just fine though. Maybe you should talk to them instead."
    menu:
        "But I want to talk to you Rose.":
            pass
    show Char Rose Blush
    "Rose blushes at the comment."
    r "Thanks Chrys. I don't know why you would want to, but ...."
    show Char Rose Base
    r "Do you have any other questions for me about the patio?"
    menu:
        "I don't think so. Seems like a pleasant straightforward place.":
            pass
    "Rose nods in agreement."
    r "Great, then let's move on."
    menu:
        "Totally.":
            pass
    "Rose leads you back through the glass doors. Once inside she starts leading you towards the perennials section."
    r "I think I'll show you the perennials section and let you get settled in, if that sounds OK."
    menu:
        "Seems like a plan.":
            pass
    "Rose nods in response. She seems a little tense."
    "Eventually Rose leads you to the perennials section. She shows you how to get up and leads through the area."
    "You pass by several other plants and even see Rose's home. Eventually you arrive at your new place of residence."
    r " Well Chrys, this is it for today. Sorry we couldn't do more, I just have something I need to go work on."
    menu:
        "Don't worry about it Rose. I'll see you soon.":
            pass
    r "Definitely. Have a good night."
    jump roseWork

label roseWork:
    show Char Rose Done
    call Rose_Sigh from _call_Rose_Sigh_7
    "As she turns around to leave, Rose's gaze seems to be distant. You hear her mutter something under her breath."
    menu:
        "Rose, are you ok?":
            pass
    show Char Rose Nervous
    call Rose_NervousLaughter from _call_Rose_NervousLaughter_10
    "Rose jumps at the sound of your voice. She turns around and lets out a nervous laugh."
    show Char Rose Base
    call Rose_Hm from _call_Rose_Hm
    r "Oh, uh, yeah! I'm feeling great. I just...have something I need to go work on."
    r "I'll see you tomorrow, ok?"
    hide Char with fade
    "Rose gives you a wave goodbye and leaves. You're now alone in your new home."
    "You decide now is as good a time as any to settle in. You go about preparing your new home and before long it's time for bed."
    menu:
        "Go to Bed":
            pass
    "You settle in for the night and it's not long before sleep washes over you."
    scene black with fade
    "You are able to rest for a few hours, but you awake suddenly in the middle of the night."
    scene NightRose with fade
    play music roseNightime
    "You hear rustling and what sounds like someone talking, but it's distant."
    menu:
        "Check it out.":
            "You force yourself to get up and find out what's happening. It's not easy, and the allure of sleep calls out to you, but you're able to power through."
            "You leave your home and listen closely to where the sounds are coming from."
            menu:
                "Follow them":
                    "You try to locate where the sounds come from your search leads you out of the perennials section."
                    "You get down to the store's floor the way Rose showed you. The sounds seem louder, but are still far away."
                    menu:
                        "Keep following.":
                            "The sounds lead you to the cashier. They sound even closer now, but they're still far above you. The rustling is much clearer and you can even make out what sounds like a woman's voice."
                            menu:
                                "Keep Going":
                                    "You reach the passage way up to the cashier and feel apprehension build. It's even more intimidating when you're in the dark by yourself."
                                    menu:
                                        "Power through it":
                                            "You begin the treacherous climb up to the cashier, taking care not to misstep or fall. You come close a few times, the darkness hindering your skill."
                                            menu:
                                                "Keep Going":
                                                    jump roseNight
                                                "Leave while you can":
                                                    jump roseBadEnding
                                        "Give up":
                                            jump roseBadEnding
                                "Go Back":
                                    jump roseBadEnding
                        "Turn around.":
                            jump roseBadEnding
                "Turn Back":
                    jump roseBadEnding

        "Ignore it and go back to sleep.":
            jump roseBadEnding

label roseNight:
    play music roseConfront
    scene NightFight with fade
    "When you reach the top you're met with a worrying sight. Rose is up here by herself and she seems worn thin."
    menu:
        "Rose? What are you doing up here?":
            pass
    show Char Rose Surprise
    call Rose_Oh from _call_Rose_Oh_8
    "Rose jerks around to look at you. A look of shock flashes across her face as she realizes who you are. she begins to speak while holding back tears."
    show Char Rose Sad
    call Rose_HeySad from _call_Rose_HeySad_3
    r "Oh, it's you Chrys. Listen, this is uh, nothing. Just go back to bed. You don't need to worry about me."
    "You can see her wiping tears from her face."
    menu:
        "Rose, something is clearly wrong here. Please, just talk to me.":
            pass
    r "You're really not gonna leave, huh? Fine then."
    call Rose_Sigh from _call_Rose_Sigh_8
    r "I felt horrible after what Sprout said to me earlier. I feel like I need to make it up to him somehow, so that's what I've been trying to do."
    r "But I feel like there's nothing I can do. I already let him down so hard, and there's no way to come back from that."
    r "I've been trying to come up with something all night, but no matter what I do my brain won't work. I don't know what I'm gonna do Chrys."
    menu:
        "Rose, this isn't something you can solve in a day.":
            jump roseConfront
        "You need to get over this Rose. You can't act like a baby constantly.":
            show Char Rose Angry
            call Rose_OhGod from _call_Rose_OhGod_3
            "Rose's face contorts with disgust."
            r "Seriously Chrys? How could you even say that to me? I'm trying to help Sprout and you tell me I'm a baby?"
            menu:
                "Well it's true. You need to get over it because it already happened. You need to stop worrying so much.":
                    "Rose is glaring at you now. Her hands tremble slightly."
                    r "You jerk. Don't you think I know that? I wake up everyday terrified of what will happen and what people will think."
                    r "If I could just not worry then I would. I don't like how I am. In fact I hate it. I can't believe you would say that."
                    menu:
                        "Well, now you're even more hysterical, Rose. Just calm down.":
                            r "Oh you... How many times do I have to say it? I can't help it."
                            menu:
                                "Well, I don't think you're trying very hard if you're this upset.":
                                    pass
                            "Rose looks like she's ready to scream."
                            "That's it Chrys. You're clearly not helping, so just leave me and go back to sleep."
                            menu:
                                "But Rose, I am trying to help.":
                                    pass
                            "She cuts you off before you can finish."
                            r "Just leave me alone Chrys. I don't want to hear anymore. I thought you cared but it's clear you don't."
                            menu:
                                "Fine!":
                                    pass
                            show Char Rose Sad
                            call Rose_Sigh from _call_Rose_Sigh_9
                            "Rose turns around and ignores you. You hear her begin to weep as you make your way down to the shop's floor."
                            hide Char with fade
                            "By the time you reach the bottom the crying has stopped and the rustling has continued."
                            "You walk home alone in the darkness of the store, Rose's words echoing in your ears."
                            "You eventually reach the perennials section and your home soon after that."
                            "After you settle back in you slowly fall asleep, but you don't sleep well that night."
                            jump roseBadEnding
                "Wait no, I'm sorry Rose. That's not what I meant.":
                    call Rose_OhHm from _call_Rose_OhHm_3
                    show Char Rose Done
                    r "Well then what did you mean?"
                    menu:
                        "I meant that you can't let it eat you up. This isn't a simple problem to solve. It'll take time, but you can't let it destroy you while you try to fix it.":
                            jump roseConfront

label roseConfront:
    show Char Rose Surprise
    "Rose looks at you confusedly."
    r "Chrys, I... What do you mean?"
    menu:
        "I mean that there's nothing you can do to solve this right now. Relationships are complicated and they take time to mend.":
            pass
    show Char Rose Base
    call Rose_OhNo from _call_Rose_OhNo_7
    "Rose looks hopeful for a moment before she begins to cry again."
    show Char Rose Sad
    r "Chrys please, I can't have him hate me. I already feel horrible about it, I just need to make it up to him."
    menu:
        "You can make it up to him eventually, but you can't do it like this.":
            pass
    "Rose lets down her guard a little."
    r "Then what am I supposed to do Chrys? Because I can't figure it out."
    menu:
        "It's gonna have to go step by step. I know it's scary, but over time things will get better.":
            pass
    show Char Rose Base
    "Rose stops crying."
    r "What if they don't get better? What if I screw them up more?"
    menu:
        "I guess that could happen, but you still have to try. It's part of life, and I know it's scary, but you can do it.":
            pass
    "Rose takes a deep breath and sits in silence for a moment."
    r "I just... I don't know if I really can do it Chrys. I don't think I have the strength."
    menu:
        "Well, that's what friends are for. I'll help you along the way Rose.":
            pass
    r "Really Chrys? You would spend your time helping me clean up my mess?"
    menu:
        "Absolutely, Rose. Because I know you would do the same for me.":
            pass
    show Char Rose Happy
    "Rose's eyes begin to tear up again, but this time she's smiling."
    r "If you're with me then I might be able to. I just feel like I need to know how it's going to end right now."
    menu:
        "I get that Rose, but you can't. We can hope things will get better, and chances are they will, but we can't know for sure.":
            pass
    "Rose nods in agreement and wipes her eyes again."
    show Char Rose Base
    r "Well, what do we do then?"
    menu:
        "Right now? We should go back to sleep and talk about it tomorrow.":
            pass
    show Char Rose Sad
    call Rose_Sorry from _call_Rose_Sorry_5
    r "Yeah, I guess you're right. I'm sorry I woke you up with this. I'm just being dumb."
    menu:
        "No Rose, don't apologize. There's nothing dumb about this.":
            pass
    show Char Rose Base
    call Rose_Ok from _call_Rose_Ok
    r "Yeah, you're right Chrys. Let's go."
    "You and Rose begin the walk back to the perennials section, back to your home."
    "Along the way you realize just how beautiful the store is at night. The moonlight casts everything in an ethereal mix of shadow and light."
    "Eventually you make it back to Rose's home. She looks at you with big eyes."
    show Char Rose Happy
    call Rose_HeyHappy from _call_Rose_HeyHappy_6
    r "Thanks Chrys. I really appreciate what you did for me."
    menu:
        "It was nothing Rose. Now try to get some sleep and we can talk tomorrow.":
            pass
    "Rose nods and gives you a little wave before leaving you alone in the perennials section."
    hide Char with fade
    menu:
        "Go home.":
            pass
    "You return to your new home just as you left it. And, slowly but surely, sleep takes you once again."
    scene black with fade
    jump roseGoodEnding

label roseBadEnding:
    play music roseNightime
    "You decide to leave well enough alone and go back to bed. You tune out the sounds and before long you're back to sleep."
    "When you wake up it's raining outside. The sky is dreary and grey, and the store seems lifeless."
    "There's a pit in your stomach and you feel worried about Rose. You decide it might be a good idea to check in."
    "You head to her home, but when you get there you don't see her. You decide to look around the store for her."
    "You head to the cashier first. You're met with the intimidating climb, now cast in the miserable gray of a rainy day."
    "You reach the top and are met with a horrible sight."
    "Rose is sittting on the counter, but she seems like a husk of her former self. She looks withered beyond help."
    "Rose passed in the middle of the night."
    "All around her you see tear stained papers with ideas on how to apologize to Sprout. It seems like her final moments were spent worrying about him."
    $ ending = 8
    jump credits

label roseGoodEnding:
    "When you wake up sunshine is flowing into the store once again. It's early in the morning and everything is cast in a golden glow. You can hear Rose calling out for you."
    menu:
        "Get up.":
            pass
    "By the time you're up, Rose has already found you. She looks like she's doing much better than last night."
    show Char Rose Happy with fade
    call Rose_HeyHappy from _call_Rose_HeyHappy_7
    r "Chrys, there you are! I've been looking for a while now. Listen, I wanted to thank you again."
    menu:
        "Rose, really it was nothing.":
            pass
    show Char Rose Done
    "Rose shakes her head and gives you a stern look."
    show Char Rose Base
    r "No Chrys, it was a big deal. I think you really saved me last night. It means a lot that you came to see me. So... thank you."
    menu:
        "You're welcome Rose.":
            pass
    show Char Rose Happy
    r "But I have some good news. I'm gonna go talk to Sprout and try to mend things. It might not happen right away, but it'll get better eventually."
    r "You helped me realize that. I'll tell you how it goes later. But just enjoy yourself for now. Go explore the store, cause we both know I didn't show you enough of it."
    menu:
        "OK Rose, I will. Good luck with Sprout.":
            pass
    show Char Rose Base
    r "Thanks. I'll see you soon."
    show Char Rose Happy
    call Rose_Yay from _call_Rose_Yay_7
    "Rose gives you a big smile and an even bigger hug."
    hide Char with fade
    "She quickly wanders off in search of Sprout, leaving you to explore the store to your heart's content."
    $ ending = 7
    jump credits

label credits:
    if ending == None:
        $ ending = 0
    if ending == 0 or ending == 2 or ending == 5 or ending == 7:
        play music mainloop
    else:
        play music badEnd
    play music mainloop fadeout 2.0 fadein 2.0
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25
    scene black with fade
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1.5)
    hide theend


    image mushGood = Text("{size=80}Love it When a Plan Fungs Together", text_align=0.5)
    image mushBad = Text("{size=80}Things Left Fungsaid", text_align=0.5)
    image cacBad = Text("{size=80}Texas-Bound", text_align=0.5)
    image cacGood = Text("{size=80}Home Is Where the Heart Is", text_align=0.5)

    image sunGood = Text("{size=80}Sunny Side Up", text_align=0.5)
    image sunBad = Text("{size=80}The Sun Will Come Out", text_align=0.5)
    image sunBad2 = Text("{size=80}Do As Thou Wilt", text_align=0.5)

    image roseGood = Text("{size=80}A Blossoming Relationship", text_align=0.5)
    image roseBad = Text("{size=80}Left Out to Dry", text_align=0.5)
    if ending == 0:

        show mushGood:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide mushGood
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 1:

        show mushBad:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide mushBad
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 2:

        show sunGood:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide sunGood
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 3:

        show sunBad:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide SunBad
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 4:

        show sunBad2:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide sunBad2
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 5:

        show cacGood:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide cacGood
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 6:

        show cacBad:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide cacBad
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 7:

        show roseGood:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide roseGood
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    if ending == 8:

        show roseBad:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        with Pause(1.5)
        hide roseBad
        with dissolve
        with Pause(credits_speed - 5)
        with dissolve
        with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    with dissolve
return
