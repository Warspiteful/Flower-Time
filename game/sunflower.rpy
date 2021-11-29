
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
