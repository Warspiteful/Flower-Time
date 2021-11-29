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
