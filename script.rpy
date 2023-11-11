# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = '#ff9900')
define Dave = Character("Dave", color = '#aaefff')


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e 'Hi Dave, how was your day?'

    menu:
        'My day was great thank you Eileen':
            jump GoodDay
        'My day was not too good':
            jump BadDay
        'My day was great, but go to part 2':
            call GoodDayB
    
    'This code is the end of the Start block'

    # This ends the game.

    return


label GoodDay:
    e 'I am glad you had a good day'
    # first bit
    return


label GoodDayB:
    e 'part 2 of the good day block'
    # second bit
    return


label BadDay:
    e 'I am sad that you din not have a good day'
    return
