#!/bin/bash

# This line try to import /etc/xprofile if it exists
[ -f /etc/xprofile ] && . /etc/xprofile
# As ditto
[ -f ~/.xprofile ] && . ~/.xprofile
