import sys
import os
import commands

def main(*args):
    args = args[1].split(";-;-;")
    project_name = args[0].strip()
    target_name = args[1].strip()
    workspace_name = args[2].strip()
    package_name = args[3].strip()
    activity_name = args[4].strip()
        
    cmd = '"$ANDROID_SDK"/"tools/android" create project --target "%s" --name "%s" --activity "%s" --path "%s/%s" --package "%s"' % (target_name, project_name, activity_name, workspace_name, project_name, package_name)
    output =  commands.getoutput(cmd)
    
    cmd = 'open -b com.macromates.textmate "%s/%s"' % (workspace_name, project_name)
    commands.getoutput(cmd)
    return output
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))