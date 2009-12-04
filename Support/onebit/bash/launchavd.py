import sys
import os

def main(*args):    
    if args[2]=="1":
        return os.system('"%s/tools/emulator" -avd %s -wipe-data > /dev/null 2>&1 &' % (os.environ['ANDROID_SDK'], args[1])) 
    else:
        return os.system('"%s/tools/emulator" -avd %s > /dev/null 2>&1 &' % (os.environ['ANDROID_SDK'], args[1])) 
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))