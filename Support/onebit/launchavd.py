import onebit
import os
import commands

template = onebit.env.get_template("launchavd.html")

cmd = '"$ANDROID_SDK"/"tools/android" list avds'
text = commands.getoutput(cmd)
devices = text.replace('Available Android Virtual Devices:\n    ', '').replace("\n\nThe following Android Virtual Devices could not be loaded:\n", "n---------\n").split("---------\n")

if devices[0] != "Available Android Virtual Devices:":
    avds = []
    for device in devices:
        attributes = device.split("\n")
        attributesObject = {}
        for attribute in attributes:
            a = attribute.strip()
            if a:
                splits = a.split(": ")
                if len(splits) > 1:
                    attributesObject[splits[0].strip().lower()] = splits[1].strip()
        avds.append(attributesObject)

    print template.render(
        title='Launch Android Virtual Device', 
        avds=avds,
    )
else:
    import newdevice
    newdevice.main(True)