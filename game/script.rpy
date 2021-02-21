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

######## Rose Images ##################################
image Rose Base:
    "./images/Rose/rose neutral face game jame.png"
    zoom .50
image Rose Happy:
    "./images/Rose/rose happy face game jame.png"
    zoom .50
image Rose Blush:
    "./images/Rose/rose blush face game jame.png"
    zoom .50
image Rose Sad:
    "./images/Rose/rose sad game jame.png"
    zoom .50
image Rose Surprise:
    "./images/Rose/rose surprised game jame.png"
    zoom .50
image Rose Angry:
    "./images/Rose/rose angry game jame.png"
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
            jump rose
        "I want to hear about you!":
            jump sunflower

################## Rose Route #################################
label rose:
    hide Sun
    show Rose Base
    r "Oh, my, my. Hello, gorgeous. Who might you be? "
    menu:
        "Uh, hello?":
            show Rose Happy
            r "Oh, a shy one, aren't you? Well, I'm sure you'll warm up soon enough, we've got ourselves a fine gathering of the friendliest people around."
            r "You must be the new flower around here. The name's Rose. It's a pleasure to meet you."
        "Right back at you, cutie!":
            show Rose Blush
            r "Aww, you sure know to make this girl's heart flutter."
    show Rose Base
    r "You must be the new flower around here. The name's Rose. It's a pleasure to meet you."
    r "I have to say, you've arrived at quite the interesting time. Around this time, we see a lot of exports, but not too many going the other way."
    show Rose Sad
    r "It's always a bit tough to say goodbye to everyone but, that's life."
    menu:
        "I'm sorry to hear that.":
            jump sorry
        "What's going on?":
            jump context

label sorry:
    show Rose Base
    r "Oh, honey, don't be."
    show Rose Sad
    r "It's...a natural part the cycle of life. Can't say it hurts any less though."
    show Rose Base
    r "I figure the best way to handle it is to just keep living each day out nice and proud. "
    menu:
        "That's a nice way to think about it.":
            jump think
        "Is that really okay?":
            jump okay
label think:
    show Rose Happy
    r "Haha, thanks, love."
    show Rose Base
    r "I sure hope I'm doing the right thing."
    r "I suppose I shouldn't hold you up with my self pity though."
    r "Now, let's get back to business, then?"
    jump ask
label okay:
    r "Sigh..."
    r "Look here. I know it's far from perfect, but it's what we've got. If you want all the answers, I'm not your girl."
    show Rose Happy
    r "But I'd like to think I'm a pretty fine-looking gal, and I've rolled a pretty good lot in life all things considered."
    r "I've got no intentions of moping around in regrets, thinking of what could have been and all that nonsense."
    r "And I'll be damned if I let any destiny or fate screw with me."
    menu:
        "\*clap\*":
            r "Ahaha, yes! I'm pretty amazing, aren't I?"
        "Uh...wow.":
            show Rose Surprise
            r "Ahahahaha...oh..."
    show Rose Blush
    r "Oh god...uh...I really got into it, didn't I?"
    menu:
        "You sure did":
            show Rose Base
            r "Ah! Um...please try to forget that happened..."
            menu:
                "Well, if you say so...":
                    show Rose Happy
                    r "Ahaha, thanks."
                    jump understand
                "No can do!":
                    show Rose Blush
                    r "Aww, you big tease!"
                    show Rose Base
                    r "Hmph, and I was trying to be cool, too."
                    menu:
                        "Haha, sorry":
                            r "Well...I suppose I can forgive you just this once. Hmph."
                            jump understand
                        "You're more cute than cool":
                            show Rose Blush
                            r "Eh? Oi! You!"
                            show Rose Angry
                            r "You can't just say that, you know!"
                            menu:
                                "Why?":
                                    show Rose Surprise
                                    r "Wha-? Are you serious right now?"
                                    show Rose Blush
                                    r "{i}*Ahem*{/i}"
                                    show Rose Base
                                    r "Look, we've just met, so let's just end it there, okay?"
                                    menu:
                                        "Alright.":
                                            show Rose Blush
                                            r "Oh, thank goodness. You really had me sweating there."
                                            show Rose Happy
                                            r "Now, let's get back to business, then?"
                                            jump ask
                                        "Aww...":
                                            show Rose Blush
                                            r "Oh, come on, lay off me a little, won't you?"
                                            show Rose Angry
                                            r "Hmph, meanie."
                                            show Rose Blush
                                            r "But if you ask really nicely, I suppose I can help answer any questions you might have for me."
                                            menu:
                                                "Please?":
                                                    jump ask
                                "Sorry.":
                                    show Rose Blush
                                    r "Well...I suppose I can forgive you just this once. Hmph."
                                    jump understand
        "It happens.":
            show Rose Base
            r "Well...that's a bit embarrassing. Thanks for your understanding though."
            jump understand
label understand:
    show Rose Base
    r "As you probably saw, I have some pretty strong opinions. Hope I didn't scare you off though."
    menu:
        "It's alright.":
            show Rose Happy
            r "Thanks, love."
            show Rose Base
            r "Now, let's get back to business, then?"
            jump ask
        "*stay silent*":
            show Rose Base
            r "Um...well...ahaha. Maybe I can help with you something?"
            jump ask

label context:
    show Rose Surprise
    r "Oh? I don't suppose you know what time of the year it is, do you?"
    menu:
        "No?":
            show Rose Angry
            r "You're not pulling my leg, are you? I'm being completely serious, this is pretty commmon knowledge."
            show Rose Base
            r "Well, I guess someone has to teach you."
            r "Listen up, we're coming up on a special day called Valentines Day."
        "Valentine's Day.":
            show Rose Base
            r "Oh? So you do know the day."
    show Rose Sad
    r "When it comes to Valentines, a lot of good flowers get shipped out the door to never return."
    r "It's always been a painful time, every year."
    menu:
        "I'm sorry to hear that.":
            jump sorry
        "Oh, I didn't know.":
            show Rose Base
            r "It's alright, although I have to say I'm a bit envious about where you're from."
            show Rose Sad
            r "Must be nice..."
            menu:
                "I'm sorry.":
                    jump sorry
                "*stay silent*":
                    show Rose Base
                    r "Um...well...ahaha. Maybe I can help with you something?"

label ask:
    show Rose Base
    r "Is there anything else you're wondering about?"
    menu:
        "Do you do anything for fun?":
            show Rose Happy
            r "Fun? Well, there's never a dull moment with everyone we have here."
            show Rose Base
            r "I see you've met Sunflower already."
            menu:
                "She's nice.":
                    show Rose Happy
                    r "I'm glad to hear that. She's always been one of the friendliest plants here."
                    show Rose Base
                    r "Treat her nicely, ok?"
                "She's cute.":
                    show Rose Happy
                    r "I know, right? Aww, I'm sure you two will get along splendidly."
                    r "You better let her know, she'll be over the moon."
                    show Rose Base
                    r "It'd be a nice change for her. It's been a while since..no, it's not my place."
                    show Rose Happy
                    r "Anyways, tell her that, ok? Even she needs a pick-up ever so often."
                    jump talkoptions
        "How are things?":
            r "Well, things have been quiet."
            r "INCOMPLETE"############INCOMPLETE
        "Nope.":
            r "Well, I suppose I'll see you to Sunflower again then?"
            scene bg
            show Sun Base
            s "Hey, hey! Welcome back."
            s "Want to someone else?"
            jump meetPlants
label talkoptions:
    show Rose Base
    r "Want to talk about anyone else?"
    menu:
        "Cactus":
            r "INCOMPLETE" ##############INCOMPLETE
            jump meetPlants
        "Mushroom":
            r "INCOMPLETE" ##############INCOMPLETE
            jump meetPlants
        "Nope":
            jump ask
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
