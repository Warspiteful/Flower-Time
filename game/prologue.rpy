###################################################################################

# The game starts here.

label start:

    $ favorSun = 0
    $ favorRose = 0
    $ favorMush = 0
    $ favorCact = 0
    $ ending = 0
    play music mainloop
    $ notify_music()

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
    $ notify_music()
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
