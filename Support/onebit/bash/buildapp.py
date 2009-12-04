import sys
import os
import commands

def main(*args):    
    os.chdir(os.environ['TM_PROJECT_DIRECTORY'])
    return commands.getoutput("ant %s" % args[1])
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))