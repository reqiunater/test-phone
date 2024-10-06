define n = Character("Nganu", image="nighten")

# NVL characters are used for the phone texting
define n_nvl = Character("Nganu", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# The game starts here.

label start:

    scene bg nganu with dissolve
    pause 1.0

    show nighten normal e1m1 at center:
        yoffset 1080
        ease 0.7 yoffset 0


    n "Halo og"
    n e1m2 "Ini cara menginstall phone Texting"
    n e1m2 "Langkah pertama adalah mendownload \"Yet Another Phone\" di itch io"
    n phone e1m1 "Terus Salin File namanya PhoneTexting.rpyc ke folder game mu"
    n phone e1m1 "Jangan lupa update di screen.rpy"
    n phone e1m1 "Script update screen.rpy ku kirim WA"


    #Phone conversation start
    show nighten e1m2_b:
        ease 0.5 xalign 0.7 

    nvl_narrator "Ini buat narrator, atau seng biasane buat menunjukkan jam example:"
    nvl_narrator "Wednesday \n12:00"
    n_nvl e2m2_b "Halo, ini Main Char, icon e bisa kamu rubah di images, nama filenya : phone send icon"
    e_nvl "ini char lain, icon e bisa kamu rubah juga"
    e_nvl "Aku ngirim Sticker {image=emoji/fear.png}"
    e_nvl "Kalau mau ngasih link web pakai image tag example {a=link website}image tag{/a} :)"
    e_nvl "Kalau mau kirim gambar bisa juga pakai tag image,contoh (dibawah)"
    e_nvl "{image=EileenSelfieSmall.png}"
    show nighten e2m2_b

    show nighten:
        ease 0.5 xalign 0.5 

    n e1m2 "Sudah itu saja yog"
    n normal e1m2 "Do you have any question?"

    return
