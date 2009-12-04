import sys
import os
import commands

def main(*args):  
    target = args[1].strip()
    ids = args[2].strip()
    target_ids = ids.split(",")
    # os.environ['ANDROID_SDK'] = '/Users/peonleon/Documents/Projects/Android/android-sdk-mac/'
    # os.environ['TM_PROJECT_DIRECTORY'] = '/Users/peonleon/Documents/Projects/Android/workspace/MyAndroidApp/'
    cmd = '"%s/tools/android" update project --target "%s" --path "%s"' % (os.environ['ANDROID_SDK'], target_ids[int(target)], os.environ['TM_PROJECT_DIRECTORY'])
    return commands.getoutput(cmd)
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))