printError() {
	echo "<span class='error'>Error: $1</span>"
}

checkBuildPath() {
    path=$TM_PROJECT_DIRECTORY
    if test -e "$path/build.xml"; then
    	path=$path
    else 
        printError "Could not find build.xml"
    fi
}

