def main(from_launch=False):
    import onebit
    import os
    import commands

    cmd = '"$ANDROID_SDK"/"tools/android" list targets'
    text = commands.getoutput(cmd)
    
    if text == 'Available Android targets:':
        template = onebit.env.get_template("error.html")
        print template.render(
            title='Error',
            error='No build targets found.<br>Try installing some packages using the SDK & AVD Manager.'
        )
    else:
        template = onebit.env.get_template("newdevice.html")
    
        split = text.split("id: ")[1:]
        targets = []

        for s in split:
            parts = s.split("\n")
            if parts[3].strip()[-1:] != ".":
                api = parts[3].strip()[-1:]
            else:
                api = parts[6].strip()[-2:-1]
            targets.append({"id":parts[0][0], "label":"%s (%s)" % (parts[0].replace(" or ", ") "), parts[1].strip()[6:]), "api":api})

        if from_launch:
            pagetitle = 'No devices Found, Create One'
        else:
            pagetitle = 'Create a new Android Virtual Device'

        print template.render(
            title=pagetitle, 
            targets=targets,
            homedir=os.environ['HOME'],
        )
    
if __name__ == "__main__":
    main()