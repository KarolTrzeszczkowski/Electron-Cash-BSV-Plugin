# Warning! Don't use. It suck.

# Electron Cash BSV Plugin
The plugin overwrites checkpoints and lets you use EC to connect with the Bitcoin SV ElectrumX servers. The main advantage of using the plugin is that it's only about 100 lines of code. If you trust EC, it takes less time to review 100 lines of plugin than the whole other wallet. 

# Warning! 
## Uninstalling BSV Plugin.
The issue with this plugin is that while it is easy to turn it on, it is hard to turn it off, because once EC verified the headers received from the server it won't check them again.  To successfully turn the plugin off you have to:
1. In the Electron Cash window click on the menu Tools>Installed Plugins, 

2. Uninstall BSV Plugin,

3. Close all the instances of EC,

4. From the local configuration directory of your EC (~/.electron-cash on Linux or \Users\YourUserName\AppData\Roaming\Electron
Cash\ on Windows) delete the files "blockchain_headers", "recent_servers" and directories "forks/" and "certs/".

Next time you run EC it won't see any SV server. 
In case of any problems with connections do the 4. step from the list above.
## Use only if you know what you are doing.

# Installing the plugin
To install BSV Plugin and connect to the BSV server you have to:
1. Download bsv-plugin.zip or just pack files "manifest.json" and "bsv-plugin/*" to zip file with your archive manager,

2. In the Electron Cash window click on the menu Tools>Installed Plugins, 

3. Click "Add Plugin" button and choose bsv-plugin.zip file

4. Close Plugins dialog and click Tools>Networks or the round, green button in the right down corner of EC window.

5. Click a blue caption <u>View ban list...</u> and unban one of the sv servers.

6. In the network dialog click "Server" tab, unmark "Select server automatically" and from the list below choose some sv server. They will have "sv" "satoshi.vision" etc. in their name.

7. Rightclick on the server and click "Use as server".

You should be connected to the BSV network. The green button should have the black crossroad pictogram on it. Network overview should show two branches - 4626ff6e3b@556767 (BCH) and 1d95671421@556767 (BSV).


# Donations
Cash Account: Licho#14431
bitcoincash:qq93dq0j3uez8m995lrkx4a6n48j2fckfuwdaqeej2
Legacy format: 121dPy31QTsxAYUyGRbwEmW2c1hyZy1Xnz

![donate](/donate.png)
