## ________________________________________________________
##    _______ _  __    ____               _   ___      __
##   <  / __ \ |/ /   / __ \___ _   __   / | / (_)____/ /__
##   / / / / /   /   / / / / _ \ | / /  /  |/ / / ___/ //_/
##  / / /_/ /   |   / /_/ /  __/ |/ /  / /|  / / /__/ ,<
## /_/\____/_/|_|  /_____/\___/|___/  /_/ |_/_/\___/_/|_|
## ________________________________________________________

# 
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls="exa --color=auto -h"
alias ll="exa -Ralh"
alias pacdate="expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort | tail -n 20"
alias grep="grep --color=auto"

# Default: PS1="[\u@\h \W]\$ "
# PS1="[$green\u$blue@$red\h $blue\w$reset]$ " # Old prompt
# PS1="$green\w > $reset"                      # Minimal prompt

PS1="$blue[ $cyan\u$blue \w ]$ $reset"         # Arch Nick prompt
# PS1="$magenta[ $red\u$magenta \w ]$ $reset"  # Root prompt

if [ "$TERM" = "linux" ]; then
	echo -en "\e]P0121212" # Normal
	echo -en "\e]P1C70031"
	echo -en "\e]P229CF13"
	echo -en "\e]P3D8E30E"
	echo -en "\e]P43449D1"
	echo -en "\e]P58400FF"
	echo -en "\e]P600aaff"
	echo -en "\e]P7E2D1E3"
	echo -en "\e]P85A5A5A" # Bright
	echo -en "\e]P9F01578"
	echo -en "\e]PA6CE05C"
	echo -en "\e]PBF3F79E"
	echo -en "\e]PC97A4F7"
	echo -en "\e]PDC495F0"
	echo -en "\e]PE68F2E0"
	echo -en "\e]PFFFFFFF"
fi


#if [ "$TERM" = "linux" ]; then
#	echo -en "\e]P00a0a0a" # Normal
#	echo -en "\e]P1f81118"
#	echo -en "\e]P22dc55e"
#	echo -en "\e]P3aa9943"
#	echo -en "\e]P42a84d2"
#	echo -en "\e]P53e5ab7"
#	echo -en "\e]P61081d6"
#	echo -en "\e]P7ffffff"
#	echo -en "\e]P8222222" # Bright
#	echo -en "\e]P9f81118"
#	echo -en "\e]PA2dc55e"
#	echo -en "\e]PBecba0f"
#	echo -en "\e]PC2a84d2"
#	echo -en "\e]PD4e5ab7"
#	echo -en "\e]PE1081d6"
#	echo -en "\e]PFd6dbe5"
#fi
