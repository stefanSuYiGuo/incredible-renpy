define e = Character("Eileen", color = '#ff9900')
define Dave = Character("Dave", color = '#aaefff')
image picture_1 = im.Scale('1.jpg', 1920, 1080)
image picture_2 = im.Scale('2.jpg', 1920, 1080)
image picture_3 = im.Scale('3.jpg', 1920, 1080)


label start:
    
    call variables

    $ GameRunning = True
    while GameRunning:
        $ Output = WeekDays[Day] + " " + Months[Month] + " " + str(Days) + " " + str(Hours).zfill(2) + ":" + str(Minutes).zfill(2)
        '[Output]'
        $ Minutes += 30
        if Minutes == 60:
            $ Minutes = 0
            $ Hours += 1
        if Hours == 24:
            $ Hours = 0
            $ Day += 1
            $ Days += 1
        if Day == 7:
            $ Day = 0
        if Days > MonthDays[Month]:
            $ Month += 1
            $ Days = 1
        if Month == 12:
            $ Month = 0
        
        call EventCheck

    # clock
    """
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
    """

    return


label variables:

    """
    $ Hours = 0
    $ Minutes = 0
    $ Seconds  = 0
    $ GameRunning = True
    """
    
    $ WeekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    $ Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    $ MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    $ Minutes = 0
    $ Hours = 12
    $ Month = 0
    $ Day = 0
    $ Days = 30

    return


label EventCheck:
    if Hours == 12 and Minutes == 0 and Days == 31 and Month == 0:
        "This is an event"
    return