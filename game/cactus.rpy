
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
