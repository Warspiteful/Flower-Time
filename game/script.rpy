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
