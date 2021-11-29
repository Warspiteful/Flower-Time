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
