import sys
import os
import commands

def main(*args):
    files = os.listdir(os.environ['HOME']+"/.android/avd")
    avds = []
    for file in files:
        if file[-4:]==".avd":
            avds.append(file[:-4])

    return ",".join(avds)

if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))