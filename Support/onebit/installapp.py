import onebit
import os
import re

template = onebit.env.get_template("installapp.html")

try:
    f = open(os.environ['TM_PROJECT_DIRECTORY']+"/AndroidManifest.xml")
    text = f.read()
    com = re.compile('package[ ]*=[ ]*"[ 0-9a-zA-Z\.]+[ ]*"')
    package=''
    if com.search(text):
        package = com.search(text).group(0).replace(" ","").replace('package=', '').replace('"','');


    print template.render(
        title='Install Android App', 
        package = package,
    )
except Exception, e:
    template = onebit.env.get_template("error.html")
    print template.render(
        title='Error',
        error=os.environ['TM_PROJECT_DIRECTORY']+"/AndroidManifest.xml not found."
    )







