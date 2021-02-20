# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



######## Sunflower Images ##################################
image Sun Base:
    "./images/Sunflower/sunflower neutral face gamejam.png"
    zoom .50
image Sun Happy:
    "./images/Sunflower/sunflower happy face gamejam.png"
    zoom .50
image Sun Blush:
    "./images/Sunflower/sunflower blush face gamejam.png"
    zoom .50
image Sun Sad:
    "./images/Sunflower/sunflower sad face gamejam.png"
    zoom .50
image Sun Surprise:
    "./images/Sunflower/sunflower surprised face gamejam.png"
    zoom .50
image Sun Angry:
    "./images/Sunflower/sunflower angry face gamejam.png"
    zoom .50
##################Mushroom Images##############################
image Mush Base:
    "./images/Mushroom/Base.png"
image Mush Happy:
    "./images/Mushroom/Happy.png"
image Mush Blush:
    "./images/Mushroom/Blus.png"
image Mush Sad:
    "./images/Mushroom/Sad.png"
image Mush Surprise:
    "./images/Mushroom/Surprised.png"
image Mush Angry:
    "./images/Mushroom/Angry.png"
image Mush Joke:
    "./images/Mushroom/Joke.png"
######## Cactus Images ##################################
image Cac Base:
    "./images/Sunflower/sunflower neutral face gamejam.png"
    zoom .50
image Cac  Happy:
    "./images/Sunflower/sunflower happy face gamejam.png"
    zoom .50
image Cac  Blush:
    "./images/Sunflower/sunflower blush face gamejam.png"
    zoom .50
image Cac  Sad:
    "./images/Sunflower/sunflower sad face gamejam.png"
    zoom .50
image Cac Surprise:
    "./images/Sunflower/sunflower surprised face gamejam.png"
    zoom .50
image Cac Angry:
    "./images/Sunflower/sunflower angry face gamejam.png"
    zoom .50
#############################Backgrounds####################
#Credit LisadiKaprio
image bg:
    "./images/Backgrounds/pink bubbles.png"
    zoom 4
#############################Character Declarations#############################################
define ce = Character("Chrysanthemum", color="FFFFFF", who_outlines=[ (1, "#000000") ])
define mc = Character("Chrys",color="FFFFFF",who_outlines=[ (1, "#000000") ])
define r = Character("Rose", color = "CC0000",who_outlines=[ (1, "#000000") ])
define f = Character("Fungi",color = "330000",who_outlines=[ (1, "#000000") ])
define s = Character("Sunflower", color = "FFFF33",who_outlines=[ (1, "#000000") ])
define u = Character("???",color="FFFFFF",who_outlines=[ (1, "#000000") ])
define c = Character("Cactus", color = "33FF00",who_outlines=[ (1, "#000000") ])
###################################################################################

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    $ favorSun = 0
    $ favorRose = 0
    $ favorCact = 0
    $ favorFungi = 0

    scene bg

    show Sun Happy
    s "Soooo, who's up first? Who d'ya wanna meet?"
    jump meetPlants

label meetPlants:
    menu:
        "Fungi":
            #jump fungi
            "Hahah, you fool. We haven't written them yet. Bad!"
            jump start
        "Cactus":
            jump cactus
        "Rose":
            #jump rose
            "Hahah, you fool. We haven't written them yet. Bad!"
            jump start
        "I want to hear about you!":
            jump sunflower

################## Cactus Route #################################
label cactus:
    hide Sun
    show Cac Base
    c "Howdy. Name's Cactus."
    c "..."
    c "..."
    menu:
        "...":
            pass
    c "So. Nice weather we're having today. Pretty warm if I do say so myself."
    menu:
        "Isn't it snowing outside?":
            c "Oh. So it is."
            c "Forgot that happens here."
            jump smallTalk
        "Sure is.":
            c "Yep. I sure do miss the feelin' of that warm Texas sun."
            show Cac Happy
            c "'Specially when you're on the windowsill with all your loved ones... it really warms my spines."
            menu:
                "Spines?":
                    pass
            c "Uh... Not like them human spines if that's what you're thinkin' of. More like my spikes 'n all. They're called spines. Yeah."
            jump smallTalk
label smallTalk:
        c "..."
        menu:
            "...":
                pass
        c "Sorry. I'm not exactly the best at this... small talk thing. You'd probably do better somewhere else."
        menu:
            "Alright, see you around.":

                "{b}>:( how dare u not romance this boy. 100 years in dungeon for you{/b}"
                "{i}Wait, how'd you get into my console?{/i}"
                "{b}Shhhh...{/b}"
                scene bg
                show Sun Base
                s "Hey, welcome back! Want to talk to someone?"
                jump meetPlants
            "Nah, I don't mind.":
                c "Oh, uh. Thanks."
                c "Me leadin' the conversation gets us nowhere, though."
                c "How 'bout this. You can just ask me questions and I'll answer the best I can. Sounds good?"
                "NOT COMPLETE" ################## INCOMPLETE POINT
                jump meetPlants


################## Sunflower Route #################################
label sunflower:
    show Sun Blush
    s "Meeee!?"
    show Sun Happy
    s "Oki-dokie! Gee, I'm flattered!"
    show Sun Base
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
    ################## INCOMPLETE POINT
    jump meetPlants
label story:
    s "Actually, she's my cousin. As for me, I've been here in the shop for a while. I used to be a big-field kinda gal. It was wonderful! Lots of sun, plenty of neighbors..."
    menu:
        "Why'd you leave?":
            jump leave
        "Sounds like your kind of place!":
            show Sun Happy
            s "Right? There's nothing I love more in this world than sunshine and company. And I had both!"
            s "Staring at the sun togehter, holding leaves... it made me so... happy..."
            s "It was so romantic..."
            menu:
                "Why'd you leave?":
                    jump leave
                "Oh, do you have a partner?":
                    show Sun Surprise
                    s "GAH!? UH..."
                    s "N-No! I mean, who's asking!?"
                    menu:
                        "Uh, I guess I am?":
                            show Sun Blush
                            s "Oh! Gee! Uh, yeah, I'm single. If, uhm, you're asking."
                            s "I mean, if anybody is! Yeah, I'm single."
                        "Sorry, nevermind. You don't have to answer that.":
                            s "N-no worries. Uh, I am single, for the record. Yup."
                    show Sun Sad
                    s "Solo. Ace. ...Lonely."
                    show Sun Happy
                    s "I mean, uh. That was a joke."
                    s "I mean, a quote. A quote joke... from Shakespeare. Teehee."
                    menu:
                        "Guess I really need to read more Shakespeare.":
                            show Sun Base
                            s "He's cool if you're into that. I prefer musicals so I never read him."
                            menu:
                                "Er, right.":
                                    s "Really, I'm not lonely though. I have such good friends right here!"
                                    jump loop
                        "...Are you sure you're okay?":
                            show Sun Happy
                            s "YUP! NEVER BETTER! ALL SUNSHINE AND RAINBOWS OVER HERE! TEEHEE!"
                            "{i}She's smiling so hard it looks like it hurts.{/i}"
                            menu:
                                "Er, right.":
                                    show Sun Base
                                    s "Really, I'm not lonely though. I have such good friends right here!"
                                    jump loop
                "That sounds lovely, Sunny.":
                    show Sun Base
                    s "It was. But hey! I'm here now."
                    s "I like it here. There's way less friends, but they're all good friends. And it's peaceful."
                    jump loop
label leave:
    show Sun Sad
    s "Oh, I just..."
    s "I just had to go. Some things aren't meant to last. It's like Shakespeare says."
    s "\"Candles go out. Then life's dark and you leave.\""
    menu:
        "I'm sorry.":
            show Sun Base
            s "It's okay!"
            s "I like it here. There's way less friends, but they're all good friends. And it's peaceful."
            jump loop
label loop:
    menu:
        "Could you introduce me to some of the other plants around here?":
            s "Okie-dokie! Who do you want to meet?"
            jump meetPlants
        "What do you guys do for fun around here?":
            jump fun
