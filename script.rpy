# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = '#ff9900')
define Dave = Character("Dave", color = '#aaefff')
image picture_1 = im.Scale('1.jpg', 1920, 1080)
image picture_2 = im.Scale('2.jpg', 1920, 1080)
image picture_3 = im.Scale('3.jpg', 1920, 1080)


# The game starts here.

label start:

    call variables

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # $ t = 1
    # while t < 3:
    #     show expression ("[t].jpg")
    #     'click'
    #     $ t += 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e 'Hi [PlayerName], how was your day?'
    # For saving memory
    # hide picture_1
    show picture_2

    menu:
        'My day was great thank you Eileen':
            jump GoodDay
        'My day was not too good':
            jump BadDay
        'My day was great, but go to part 2':
            call GoodDayB
    
    # clear each image before
    scene
    # hide picture_2
    show picture_3
    'This code is the end of the Start block, your name is still [PlayerName]'

    # This ends the game.

    return


label GoodDay:
    $ PlayerScore += 1
    e 'I am glad you had a good day, your score is [PlayerScore]'
    $ PlayerName += '\nDumbo'
    # first bit
    return


label GoodDayB:
    e 'part 2 of the good day block'
    # second bit
    return


label BadDay:
    e 'I am sad that you din not have a good day'
    return


label variables:
    $ PlayerScore = 0
    $ PlayerName = "Dave"

    # if PlayerScore <= 10:
    #     "Score is [PlayerScore]"

    return
