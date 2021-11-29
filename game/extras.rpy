init -5 python:
    class MusicItem:
        def __init__(self, name, file, length, about):
            self.name = name
            self.file = file
            self.length = length
            self.about = about
            self.refresh_audio()

        def refresh_audio(self):
            if not renpy.seen_audio(self.file):
                self.is_locked = True
            else:
                self.is_locked = False

    audio.sunflower = "./audio/A Happy Little Sunflower.wav" ### Sunflower
    audio.fungi = "./audio/A Funky Little Funkgus.wav" ### Fungi
    audio.rose = "./audio/A Flirty Little Rose.wav" ## Rose
    audio.chrys = "./audio/A Little Tune for Chrys.wav" ## Chrys
    audio.mainloop =   "<from 13 to 88>./audio/A Little Tune for Chrys.wav"
    audio.cactus = "./audio/A Spiky Little Buckeroo.wav" ## Cactus
    audio.badEnd = "./audio/SadBoyFlowers.wav"
    audio.roseNightime = "./Psychotic-breakdown-RILF.mp3"
    audio.roseConfront = "./audio/RILF-but-spoopier.mp3"

    music_list= []
    music_list.append(MusicItem(_("A Happy Little Sunflower{#song title}"),audio.sunflower,1.57,_("Sunflower's theme.{#about the track}")))
    music_list.append(MusicItem(_("A Funky Little Funkgus{#song title}"),audio.fungi,2.40,_("Fungus's theme.{#about the track}")))
    music_list.append(MusicItem(_("A Little Tune for Chrys{#song title}"),audio.chrys,1.36,_("Chrysanthemum's theme.{#about the track}")))
    music_list.append(MusicItem(_("A Flirty Little Rose{#song title}"),audio.rose,3.24,_("Rose's theme.{#about the track}")))
    music_list.append(MusicItem(_("A Spiky Little Buckeroo{#song title}"),audio.cactus,2.10,_("Cactus's theme.{#about the track}")))
    music_list.append(MusicItem(_("Twilight Hour{#song title}"),audio.roseNightime,2.03,_("Rose's Nighttime Theme.{#about the track}")))
    music_list.append(MusicItem(_("A Cry in the Dark{#song title}"),audio.roseConfront,1.39,_("Rose's Confrontation Theme.{#about the track}")))
    music_list.append(MusicItem(_("Sad Boy Flowers{#song title}"),audio.badEnd,1.53,_("Bad End Theme.{#about the track}")))

init python:
    def notify_music():
        for i in music_list:
            if i.file == renpy.music.get_playing('music'):
                renpy.show_screen("notify_music",song=i.name[:-13])
