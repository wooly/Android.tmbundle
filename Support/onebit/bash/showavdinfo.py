import sys
import os
import commands

def main(*args):
    if args[1][-4:] == ".avd":
        f = open(args[1]+"/config.ini")
        text = f.read()
        lines = text.split("\n")
        html = ""
        lines.sort()
        for line in lines:
            l = line.split("=")
            if len(l)>1:
                if l[1]!="no":
                    l[0] = l[0].replace("hw.", "").replace(".", " ")
                    if l[1]=="yes":
                        html+=('<li class="attri %s yes"><span class="label">%s support</span></li>' % (l[0].lower().replace(".","-"), l[0]))
                    else:
                        html+=('<li class="attri %s"><span class="label">%s</span> - <span class="value">%s</span></li>' % (l[0].lower().replace(".","-"), l[0], l[1]))
        return html
    else:
        return "An error occured trying to read the config.ini file"

if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))