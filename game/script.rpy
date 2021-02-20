# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



######## Sunflower Images ##################################
image Sun Angry:
    "./images/sunflower angry face gamejam.png"
    zoom .50
image Sun Blush:
    "./images/sunflower blush face gamejam.png"
    zoom .50
image Sun Happy:
    "./images/sunflower happy face gamejam.png"
    zoom .50
image Sun Base:
    "./images/sunflower neutral face gamejam.png"
    zoom .50
image Sun Sad:
    "./images/sunflower sad face gamejam.png"
    zoom .50
image Sun Surpise:
    "./images/sunflower surprised face gamejam.png"
    zoom .50

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

    image bg white = Solid("#FFF")

    show bg white

    ce "Hi! I'm the main character. Call me Chrys."

    mc "Oh boy, I can't wait to meet all of these new plants"

        show Sun Base

    s "Hey, hay, yay! I'm Sunflower, and I'm totally bastardizing my characterization."

    mc "(Oh god, kill it with fire) Oh, awesome. Are there (literally) any other flowers (since I can write them somewhat better)?"

    show Sun Happy

    s "Oh sure, here, meet the three other characters."

    hide Sun

    r "Oh? It's lovely to meet you. My name is Rose, ohoho~."

    c "Howdy, pardner. I'm Cactus, yee haw."

    u "..."

    mc "H-hello?"

    u "My name..."

    f "My name is Fungi, and I'm not like other boys. I'm a bad boy."

    show Sun Happy

    s "So, that's everyone!"

    show Sun Blush

    s "So...this might be extremely forward but are you leaning towards anyone yet?"

    menu:
        "Sunflower":
            $ favorSun += 1
            show Sun Surpise
            s "Huh? M-me? Like, for real?"

            show Sun Blush
            s "{i}Breathe, Sunflower, breath {/i}"

            show Sun Sad
            s "Haha, sorry, I suppose I made it awkward, didn't I?"


        "Rose":
            $ favorRose += 1
            s "Haha, I'm not surprised. Rose is cute after all."
            s "Just...be careful. She needs her space, but you'll be fine if you respect her."
            s "Just don't push her too hard, ok? She's a delicate flower."
        "Cactus":
            $ favorCact += 1
            s "Oh, man! Yes! Cactus is so cool, right? He's my favorite!"
            s "{i}Also, the writers' favorite, but that's neither here nor there{/i}"
            s "Have you heard he wants to go to Texas? Wouldn't that be amazing?"
        "Fungi":
            $ favorFungi += 1
            s "Fungi? Well, I can't say I've talked to him much. He's a man of few words."
            s "I suppose that's his style though. He doesn't really come out of the wall too often"
            s "Maybe he'll open up to you though? We'll have to see if you'll grow on him."

    show Sun Happy
    s "{i}Ahem{/i}. Anyways, moving on."
    show Sun 
    s "Well, Rose and I were going to be watching some Love Island later tonight."
    s "I think Fungi and Cactus were planning on watching The Bachelor at the same time."
    s "What do you want to spend the day doing?"

    menu:
        "Watching Love Island":
            if favorSun > 0:
                s "Awesome! I love you!"
                s "Wait...ah...I mean...ahahah"
            else:
                s "Awesome!"
            s "Well, what're we waiting for? Let's go!"
            jump loveIsland

        "Watching The Bachelor":
            s "Oh...ok."
            jump Bachelor


label loveIsland:

    show bg white
    with fade
    s "Oh man, I love Dandelion!"
    r "Dandelion? But they're so plain! For me...well, no one captures my heart like Poinsettia."
    s "Ugh, they're way too pompous for my taste. Like, have some taste, c'mon!"
    r "Ha, that's rich coming from Miss Basic."
    s "Excuse me? Now, look here, Rose-"
    s "Oh, Chrys. Uh..what's up?"
    r "Exquisite timing, Chrys. Choose, Dandelion or Poinsettia?"
    menu:
        "Dandelion":
            s "See? Like, Rose, I know that's your type but Poinsettia really isn't all they're cracked up to be. I'm only saying this a a friend."
            r "Gah! Sunflower, don't say that to the new flower! How will I ever show my face again!"
            s "Ah...there she goes. Ahaha, whoops?"
            jump SunflowerRoute
        "Poinsettia":
            s "Hah?"
            r "Now do you understand? Clearly, Poinsettia is the superior love."
            s "Ugh, Chrys! She's never going to drop this, y'know."
            r "Bleeeh!"
            s "Oh, grow up! Chrys, I'm going to check on everyone else. Make sure she behaves herself."
            r "Sunflower! I am not some sort of chil- Oh, she's gone. Tch."
            jump RoseRoute





label Bachelor:
    show bg white
    with fade
    f "Ugh, the programmer really wrote themselves into a hole."
    c "Yee haw, this here programmer got tired after writing the Love Island Route and is floundering"
    f "Let's make this easy. You want to talk to me, or Cactus?"
    menu:
        "Fungi":
            f "Good stuff. Let's get to the endings."
            jump FungiRoute
        "Cactus":
            c "Haw yee! Ending time!"
            jump CactusRoute


label RoseRoute:
    show bg white
    with fade
    r "Now, look here, sweetcake. We're not getting many more lines so I'll have to ask: good ending or bad ending?"
    menu:
        "Good Ending":
            s "Oh my! How wonderful!"
            "GOOD ENDING"
        "Bad Ending":
            r "Oh, what a shame. Chrysanthemum tea will be a new one."
            "BAD ENDING"
    return

label SunflowerRoute:
    show bg white
    with fade
    s "Now, the programmer is getting lazy with this so I'll ask this once. Do you want the bad ending or the good ending?"
    menu:
        "Good Ending":
            s "Yay, I love you!"
            "GOOD ENDING"
        "Bad Ending":
            s "Really? Like, seriously?"
            "BAD ENDING"
    return

label CactusRoute:
    show bg white
    with fade
    c "Now then, pardner, let's make this all easy and smooth-like. Are you ready for a hoedown?"
    menu:
        "Yee Haw":
            c "Yee haw, pardner! That's what I want to hear!"
            "GOOD ENDING"
        "Naw Nee":
            c "Aw, shucks! Maybe next time then?"
            "BAD ENDING"
    return


label FungiRoute:
    show bg white
    with fade
    f "Well, what're we waiting for? Choose."
    menu:
        "Good Ending":
            f "Acceptable."
            "GOOD ENDING"
        "Bad Ending":
            f "I see..."
            "BAD ENDING"
    return
