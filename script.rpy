define e = Character("Eileen", color = '#ff9900')
define Dave = Character("Dave", color = '#aaefff')
image picture_1 = im.Scale('1.jpg', 1920, 1080)
image picture_2 = im.Scale('2.jpg', 1920, 1080)
image picture_3 = im.Scale('3.jpg', 1920, 1080)


label start:
    
    call variables

    while GameRunning:
        "[Hours]:[Minutes]:[Seconds]"
        $ Seconds += 1
        if Seconds == 60:
            $ Seconds = 0
            $ Minutes += 1
        if Minutes == 60:
            $ Minutes = 0
            $ Hours += 1
        if Hours == 24:
            $ Hours = 0

    return


label variables:

    $ Hours = 0
    $ Minutes = 0
    $ Seconds  = 0
    $ GameRunning = True

    return