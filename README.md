# athens-excalidraw
Integrating Excalidraw with Athens Research with the help of an Alfred worklfow + python script or a simple system extension. 
## Requirements 
* The latest version of [Alfred](https://www.alfredapp.com/)
* A fairly recent version of [Athens Research](https://github.com/athensresearch/athens)

## Description 
Creates an iframe with a unique excalidraw link. Uses Python 2.7 which is installed by default and therefore doesn't require any dependencies.
## Demo
[Loom Recording](https://www.loom.com/share/25117c5a40e541a58e57b355b0aeddf6)
## Install 
1. Download the athens workflow file [here](https://github.com/sawhney17/athens-excalidraw/raw/main/athensdraw.alfredworkflow)
2. Double click the file to install the workflow
3. Set a trigger (default is /draw)
4. Excalidraw away!

## Using it on Mac without third party apps via system extension 
1. Unzip the Athens Drawing system [file](https://github.com/sawhney17/athens-excalidraw/raw/main/Athens_Drawing_System_Extension.zip) and double click the file inside. 
2. Accept the installation prompt that follows
3. Go to the security and privacy pane in system preferences and add Athens and Automator to the accessibility tab
4. Go to the keyboard pane in system preferences and go to shortcuts, click the services tab and scroll near the bottom till you find athens draw
5. Click the add shortcut button and key in the shortcut you want
6. Open athens and in the menu bar, go to athens -> services -> athens draw(you only have to do this once to give permission)
7. Now, you can just use the keyboard shortcut to bring up a draw window whenever you want

* This method doesn't use /draw but the keyboard shortcut should work fine and doesn't use any third party apps

## Using it with other Text Expanders or on Windows
* You can remix the python script attached
* You can use witeboard.com [integration](https://github.com/sawhney17/athens-excalidraw) which is simpler, already designed to work with both Expanso and Alfred, and doesn't require a python script.
* You can install the system extension for mac
  * Can only access via command not on expansion of text (cmd-d)

## Credits 
Credits to the excellent [Excalidraw](https://github.com/excalidraw/excalidraw) project! 
