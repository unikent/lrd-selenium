#!/usr/bin/env bash
# Requires Xvfb

if [ ! -x /usr/bin/Xvfb ]
then
   echo "Please install Xvfb before attempting to use this script.";
   exit 1;
fi;
echo "Starting headless Selenium server..."; 
Xvfb :1 -screen 0 1024x768x24 &
DISPLAY=:1;
java -jar ~/bin/selenium/selenium-server-standalone-2.43.1.jar 1>> ~/log/primo-selenium/giddensTest.log 2>> ~/log/primo-selenium/giddensTest.log &
echo "done.";
