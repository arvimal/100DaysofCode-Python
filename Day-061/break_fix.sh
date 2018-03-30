#!/bin/bash

bold=`tput bold`
normal=`tput sgr0`

MYHOSTNAME=`hostname`
MYNAME=`whoami`

if [[ ! $MYNAME == "root" ]]
then
    echo "$0 needs to be run by the root user."
    exit 3
fi

# startup
logger -p local0.notice "Initiating $0 with option(s) $@"
echo "Initiating $0 with option(s) $@"

####################
####################
# Global vars to be called from the grade functions.
STRING=
TMP_FILE=
####################
####################
# Clean up
cleanup () {
    # echo "Cleaning vestiges of previous break-fixes."
    /usr/bin/rm -rf /mnt/* /mnt/.files/ &> /dev/null
    /usr/bin/rm -rf /tmp/tmp.* &> /dev/null
    /usr/bin/rm -rf /var/tmp/.kc*
    /usr/bin/chattr -Ri /mnt/ &> /dev/null
    # echo -e "Remounting the file system with default mount options.\n"
    /usr/bin/mount -o remount,defaults /mnt
}
####################
####################
# BREAK 1

break1() {
    # insert your break code here
    #1. Make sure /mnt is mounted, else the root FS will be impacted
    /usr/bin/mount | grep /mnt &> /dev/null
    #2. If not, get it mounted (we have an entry in fstab)
    if [ $? -ne 0 ]
        then
            /usr/bin/mount /mnt &> /dev/null
    fi
    #3. Remove previous break-fix vestiges, calling `cleanup()`
    cleanup
    #4. Fill up the available inodes
    # NOTE: We deliberately create the files in a hidden folder, since it won't
    # be obvious and make the user think about the possibilities on how an FS
    # can get full in ways other than space utilization.
    mkdir /mnt/.files/
    #5. Create a large number of files, so as to fill the inode count.
    # `tune2fs -l /dev/<partition>` will list the `Inode count` available
    # We are simply creating files more than the 26K that's possible on a 100MB EXT4
    # In order to get this work for an EXT FS of any size, we can fetch the inode
    # count using `tune2fs -l` or `df -i` and try to create files more than that.
    echo -e "${bold}Please hold on, this may take a few seconds.${normal}\n"
    for i in {1..30000};
        do
            touch /mnt/.files/file-$i 2> /dev/null
        done
    # end your break code here
    touch /var/tmp/.kc1
    echo "Your system has been modified."
    echo ""
    #5. Generating a UUID to put i
    STRING1=$(uuidgen)
    TMP_FILE1=$(mktemp)
    /usr/bin/echo ${STRING1} > ${TMP_FILE1}
    #6. A description of the problem, to the end user.
    echo -e "${bold}Task 1:${normal}"
    echo "* Create a file named ${bold}test1.txt${normal} under ${bold}/mnt/${normal}."
    echo "* Add the string ${bold}${STRING1}${normal} to ${bold}/mnt/test1.txt${normal}."
    echo ""
    echo "* Run ${bold}'./break-fix.sh grade1'${normal} once you successfully complete the task."
    echo -e "* Run ${bold}'./break-fix.sh hint1'${normal} in case you are stuck.\n"
}

hint1() {
    echo ""
    echo "${bold}Hint 1:${normal}"
    echo "- Files in a filesystem are represented by Inodes."
    echo "- Inodes are data-structures that carry metadata of a file,"
    echo "  as well as pointers to data-blocks where the data resides."
    echo "- File systems such as EXT4 comes with a pre-defined number of"
    echo "  inodes that limits the number of files that can be created."
    echo "- File systems can be full either due to space constraints,"
    echo -e "  or due to inode depletion.\n"
    echo "- Use ${bold}'df'${normal} with the ${bold}'-i'${normal} switch, to understand the Inode usage."
    echo -e "  ${bold}# df -ih /mnt/${normal}\n"
}

grade1() {
    STATUS="failed"
    echo "Grading.  Please wait."

    if  ! [ -f /var/tmp/.kc1 ]
    then
        echo "It seems like break1 was not run successfully.  Run $0 break1 first."
        exit 7
    fi
    # insert your grade code here and set STATUS="success" if the lesson criteria is met.
    # This is a very dirty hack. Find a way to call the global variable STRING here
    # Checking for the temporary file created using mktemp (I need to fix this using a global var)
    test -f /tmp/tmp.*
    if [ $? -ne 0 ]
        then
            echo "It seems like break2 was not run successfully.  Run $0 break2 first."
            exit 7
        else
            /usr/bin/grep $(cat /tmp/tmp.*) /mnt/test1.txt &> /dev/null
            if [ $? -eq 0 ]
                then
                    STATUS="success"
            fi
    fi
    # end your grading code here

    if [[ $STATUS == "success" ]]
        then
            echo "Success."
                echo "${bold}COMPLETION CODE: WILD86HORSES${normal}"
        else
                echo "Sorry.  There still seems to be a problem"
    fi
}

####################
####################
# BREAK 2
break2 () {
    # insert your break code here
    #1. Make sure /mnt is mounted
    /usr/bin/mount | grep /mnt &> /dev/null
    #2. If not, get it mounted (we have an entry in fstab)
    if [ $? -ne 0 ]
        then
            mount /mnt &> /dev/null
    fi
    #3. Removing the immutable attribute prior calling `cleanup()`,
    # in case /mnt/test2.txt exists from prior executions.
    # /usr/bin/chattr -i /mnt/test2.txt &> /dev/null
    #4. Remove previous break-fix vestiges, calling `cleanup()`
    cleanup
    #4. Create the file, and set the immutable attribute
    /usr/bin/touch /mnt/test2.txt
    /usr/bin/chattr +i /mnt/test2.txt
    # end your break code here
    touch /var/tmp/.kc2
    echo "Your system has been modified."
    echo ""
    #6. A description of the problem, to the end user.
    STRING2=$(uuidgen)
    TMP_FILE2=$(mktemp)
    /usr/bin/echo ${STRING2} > ${TMP_FILE2}
    echo -e "${bold}Task 2:${normal}"
    echo "* A file named ${bold}test2.txt${normal} exists under /mnt/"
    echo "* Add the string ${bold}${STRING2}${normal} to ${bold}/mnt/test2.txt${normal}."
    echo ""
    echo "* Run ${bold}'./break-fix.sh grade2'${normal} once you successfully complete the task."
    echo "* Run ${bold}'./break-fix.sh hint2'${normal} in case you are stuck."
}

grade2() {
    STATUS="failed"
    echo "Grading.  Please wait."

    if  ! [ -f /var/tmp/.kc2 ]
    then
        echo "It seems like break2 was not run successfully.  Run $0 break2 first."
        exit 7
    fi
    # set -x
    # insert your grade code here and set STATUS="success" if the lesson criteria is met.
    # Checking for the temporary file created using mktemp (I need to fix this using a global var)
    test -f /tmp/tmp.*
    if [ $? -ne 0 ]
        then
            echo "It seems like break2 was not run successfully.  Run $0 break2 first."
            exit 7
        else
            /usr/bin/grep $(cat /tmp/tmp.*) /mnt/test2.txt &> /dev/null
            if [ $? -eq 0 ]
                then
                    STATUS="success"
            fi
    fi
    # end your grading code here
    if [[ $STATUS == "success" ]]
        then
            echo "Success."
                echo "${bold}COMPLETION CODE: WILD86HORSES${normal}"
        else
                echo "Sorry.  There still seems to be a problem"
    fi
}

hint2 () {
    echo ""
    echo "${bold}Hint 2:${normal}"
    echo "- File access is primarily defined by its permissions."
    echo "- An ${bold}'ls -l <file>'${normal} lists the file permissions for the user/group/others."
    echo "- For more details on file permissions, see 'man chmod'."
    echo "- But, there are more ingrained file access controls, such as ACLs and File attributes."
    echo "- See ${bold}'man lsattr'${normal} to know more about file attributes."
    echo ""
}

####################
####################
# BREAK 3
break3() {
    # insert your break code here
    #1. Make sure /mnt is mounted
    /usr/bin/mount | grep /mnt &> /dev/null
    #2. If not, get it mounted (we have an entry in fstab)
    if [ $? -ne 0 ]
        then
            /usr/bin/mount /mnt &> /dev/null
    fi
    #3. Remove previous break-fix vestiges, calling `cleanup()`
    cleanup
    #4. Remount the filesystem with `noexec`
    /usr/bin/mount -o remount,noexec /mnt
    #5. Copy the script from /opt to /mnt
    /usr/bin/cp /opt/myid.sh /mnt/myid.sh
    /usr/bin/chmod 644 /mnt/myid.sh
    #6. Create a test file `test3.txt` file under /mnt
    touch /mnt/test3.txt

    # end your break code here
    touch /var/tmp/.kc3
    echo "Your system has been modified."
    echo ""
    #6. A description of the problem, to the end user.
    echo -e "${bold}Task 3:${normal}"
    echo "* Two files, ${bold}myid.sh${normal} and ${bold}test3.txt${normal} exists under /mnt/"
    echo "* Execute the script ${bold}'myid.sh'${normal}."
    echo "* Add the output string to the empty file ${bold}/mnt/test3.txt${normal}."
    echo ""
    echo "${bold}IMPORTANT:${normal}"
    echo "* The user should execute the script ${bold}'myid.sh'${normal} by calling it as ${bold}'./myid.sh'${normal}"
    echo "* ie. By simply calling the script path, and not calling it as ${bold}bash /mnt/myid.sh${normal}."
    echo "* Of course, it can be executed as ${bold}'bash /mnt/myid.sh'${normal}, but that fails the point"
    echo "* The task is to get the script executed by calling it as ${bold}'./myid.sh'${normal}."
    echo ""
    echo "* Run ${bold}'./break-fix.sh grade3'${normal} once you successfully complete the task."
    echo "* Run ${bold}'./break-fix.sh hint3'${normal} in case you are stuck."

}

grade3() {
    STATUS="failed"
    echo "Grading.  Please wait."

    if  ! [ -f /var/tmp/.kc3 ]
        then
            echo "It seems like break3 was not run successfully.  Run $0 break3 first."
            exit 7
    fi
    #set -x
    # insert your grade code here and set STATUS="success" if the lesson criteria is met.
    # Checking for the temporary file created using mktemp (I need to fix this using a global var)
    test -f /tmp/tmp.*
    if [ $? -ne 0 ]
        then
            echo "It seems like break3 was not run successfully.  Run $0 break3 first."
            exit 7
        else # If the /tmp/tmp.XYZ exits.
            /usr/bin/grep $(cat /tmp/tmp.*) /mnt/test3.txt &> /dev/null
            if [ $? -eq 0 ]
                then
                    STATUS="success"
            fi
    fi
    # end your grading code here

    if [[ $STATUS == "success" ]]
        then
            echo "Success."
                echo "${bold}COMPLETION CODE: WILD86HORSES${normal}"
        else
                echo "Sorry.  There still seems to be a problem"
    fi
}

hint3() {
    echo ""
    echo -e "${bold}Hint 3:${normal}\n"
    echo "- Files require execute permissions to execute it."
    echo "- If a script file is executed with the absolute path, ie '.myid.sh',"
    echo "  it gets executed if it has execute permissions and if the filesystem "
    echo "  mount options allow it. The 'defaults' mount options allow it."
    echo ""
    echo "- But, if the script file is called as an argument to 'bash', the script"
    echo "  does not necessarily require execute permissions (or read for root user)"
    echo "  nor the file system mount options allow it."
    echo "  This is because, while calling it as an argument to 'bash', since the 'bash'"
    echo "  process is of 'root' user, the file can still be read and executed in memory."
    echo ""
    echo "- Execution of scripts can be prevented through the file system mount options."
    echo "  See ${bold}man mount${normal} on the default file system mount options and how to"
    echo "  disallow execution of binaries/executables."
    echo ""
    # Fill in here
}

####################
####################
# BREAK 4

####################
####################
case "$1" in
    break1)
        break1
        ;;
    grade1)
        grade1
        ;;
    hint1)
        hint1
	   ;;
    break2)
        break2
	   ;;
    grade2)
	   grade2
	   ;;
    hint2)
	   hint2
	   ;;
    break3)
	   break3
	   ;;
    grade3)
	   grade3
	   ;;
    hint3)
	   hint3
	   ;;
    cleanup)
        cleanup
        ;;
    *)
        echo $"Usage: $0 {break1|grade1|hint1|break2|grade2|hint2|break3|grade3|hint3|cleanup}"
        exit 2
esac

# ending
logger -p local0.notice "Completed $0 with option(s) $@ successfully"
echo "Completed $0 with option(s) $@ successfully"
exit 0
