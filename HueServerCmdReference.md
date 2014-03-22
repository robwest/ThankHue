# ALL COMMANDS

(Borrowed from [Hue Remote](http://hue-remote.com/) because that webpage, while awesome, is hard to read sometimes!)

##Control a single light:

"XXX" should be replaced by your lights or groups name
    XXX on
    XXX off

    XXX: ct:500
153 - 500 white color temperature from cold to warm

    XXX: h:65535
0 - 65535 hue value, the color

    XXX: s:255
0 - 255 saturation

    XXX: b:255
0 - 255 brightness
_NOTICE_: 0 != off.

    XXX: h:0 s:255
    XXX: h:0 s:255 b:255

    XXX:+
All lights will merge to the same brightness and brighten up.

    XXX:-
Same but in the other direction. Dims all.

##Control all lights:
    All on
    All off
    ct:500
    h:65535
    s:255
    b:255
    h:65535 s:255
    h:65535 s:255 b:255
    +
    -
    0%
    5%
    10%
    ...
    100%

## Colors:
Will be applied to all lights that are on.
```
Red
Orange
Yellow
Lemon
Green
Turquoise
Minty
Aqua
Sky blue
Blue
Purple
Violet
Magenta
Pink
White
Warm White
Cold White

Working
Relaxing
Concentrate
Reading
Candle
Sleepy white
Romantic lights
```

Dims the light and triggers a warm white.

## Trigger light-scenes:
Use the name of your light-scene to trigger it

    Good Night
    Shark Attack

## Run AppleScripts:
Use the name of your AppleScripts to trigger it.

If an AppleScript an a light-scene have the same name they "merge to one" and will both be triggered. 
You can manage your AppleScripts in the folder: 

    /Library/Application Support/Hue Server

```
Random Album
iTunes next track
Good Night iTunes -t:600
Kitchen: h:23000 s:200 b:100 -t:0
```

Optionally you can override the default transition-time set on iOS by adding "-t:5" to your command. 
5 stands for 5 ms; you can set a transition-time between 0ms and 2h.

##Special functions:
    say:Hello World!
Change the Mac OS system voice for more fun.

    message:Hello World!
Sends a message to the Mac OS notification center.

    log:Hello World!
You can access the txt files in the folder: 

    /Library/Application Support/Hue Server/.helper/log

    Logging on
Enables the logging in txt files

    Logging off
Disables the logging in txt files

    activity:XXX
Advanced option to feed the system a human context.
You'll find that variable in different AppleScripts to create very unique setups.

    location:XXX
Trigger the motion system.

When you change your location through this command you'll trigger the "Location switch" AppleScript.

You can also trigger actions after minutes to hours while staying at the location. See the "Location update" AppleScript.
    How long am I here?
After setting a location via "Location:XXX" you can ask how long you are at the new location.
    Where am I?
The system will tell you about the current location.
    Status
Nothing is true, everything is permitted. The direct AI feedback from the inner core.
    Speech on
"Status" and other commands will make the system react via speech.
    Speech off

    activate
shows the input window of Hue Server. Put this action into an AppleScript to create a custom shortcut.

    tell application "Hue Server" to run command "activate"