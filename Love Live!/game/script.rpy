# You can place the script of your game in this file.

# DECLARE BACKGROUNDS
image bg classroom = "classroom.png"

# DECLARE CHARACTERS
image rin uniform bag = im.FactorScale("rin.png", 0.5)
image shigure uniform = im.FactorScale("shigure.png", 0.3)

# Declare characters used by this game.
define Ahri = Character('Ahrigateaux', color='#00ff00')
define Ame = Character('Amelia')
define Cap = Character('Capsairin')
define Chz = Character('Chezz')
define Chun = Character('chun')
define Corn = Character('cornsplosion')
define Dal = Character('Dalliance')
define Esp = Character('Espoir')
define Zer = Character('headphonezero')
define Mig = Character('HeyMiggy', color='#ff2222')
define Rin = Character('HoshiRin-chan', color='#00ff00')
define Ins = Character('Insti', color="#2222ff")
define Katz = Character('-KatZayY-')
define Lake = Character('lakepower')
define Lnk = Character('link2110', color='#ff2222')
define MP = Character('MarcoPolo', color='#00ff33')
define MM = Character('MasterMirage', color='#00ff00')
define Mel = Character('-melodii-')
define Moc = Character('mochaw1ngz')
define Oxd = Character('Oxide')
define Phi = Character('PhiPhi')
define Shg = Character('Shigure')
define Dan = Character('-trueDan-')
define UEF = Character('UltimateEpicFailz', color='#ff2222')
define Xaf = Character('Xaftz', color='#ff8800')

# The game starts here.
label start:

    play music "Snow Halation (Off Vocal).mp3"
    scene classroom
    show rin uniform bag

    Ins "Hi! I am Insti."
    Ins "I live in Malaysia."
    Xaf "Test"
    MM "Test"
    MP "LOL"

    hide rin 
    show shigure uniform

    Ins "o7 Morning shigure"
    Shg ":heyguys: omg insti why are you here :pogchamp:"

    menu:
        "I..I..I was just revising my homework!":
            jump bad_end
        "I was waiting for you to come find me, Shigure-chan!":
            jump good_end

    return
