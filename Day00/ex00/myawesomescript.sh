#!/bin/sh
if [ -z $1 ]; then
	echo "empty arguments"
else
	curl -s $1 | grep -oE \".*\" | grep -oE "[^\"]+"
fi
