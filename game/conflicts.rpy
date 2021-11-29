
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
