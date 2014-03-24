ThankHue
========

##Introduction##

Scripts and Explorations with Philips Hue automation.

This readme was put together quickly, and will be added upon as soon as I have time.

Basically, this repo contains some experiments and other utilities I've been working on to control Philips Hue lights.


##Installation##

Download or clone the repo. Follow the specific instructions in each section below.

###Alfred Workflows

The Alfred Workflows folder contains tools that work with a new app by Futura-Epsis called [Hue Server](http://www.hue-remote.com/). This app is really cool, and I'm hopeful that some of my other experiments with controlling Hue via OSC will make it on here soon. But its only been out for a day, so I'm starting with something simple - Applescript and Alfred.

1. If you haven't already purchased Hue Remote, do that now. I'll wait.
2. Double-click the Hue Server Tools.alfredworkflow - this will install the basic workflow.
3. One of the scripts assigns a keyboard shortcut to bring the Hue Server window to the front (but see below). Alfred, for safety's sake deletes keyboard shortcut assignments. Double-click the hotkey assignment node, and assign a hotkey.

####Usage
    hue <anything>
Run any command from Alfred that you can run in Hue Server. Passes arguments along exactly. Try "hue all on", "hue all off", "hue red". etc.

	hueon
	hueoff
Shortcuts for turning all lights on or off.

    cmd-option-shift-h (at least that's what I assigned)
Tells the Hue Server command window to open. This is redundant, and is included for testing purposes. If you know the command you wish to issue, the `hue` command above should obviate this. If you want hue commands to auto-complete, or to interact with the Hue Server application for some other reason, this is a convenience.

### OSC Directory (Max/MSP Patches)

These are some sample patches I built in an evening to learn about how to communicate with Hue Server from [Cycling 74](http://cycling74.com/)'s wonderful visual programming language, Max 6. 