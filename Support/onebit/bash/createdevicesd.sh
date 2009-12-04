#!/bin/bash
"$ANDROID_SDK/tools/android" create avd -n "$1" -t "$2" -c "$3"<< END_SCRIPT
no
END_SCRIPT