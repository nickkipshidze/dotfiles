## ________________________________________________________
##    _______ _  __    ____               _   ___      __
##   <  / __ \ |/ /   / __ \___ _   __   / | / (_)____/ /__
##   / / / / /   /   / / / / _ \ | / /  /  |/ / / ___/ //_/
##  / / /_/ /   |   / /_/ /  __/ |/ /  / /|  / / /__/ ,<
## /_/\____/_/|_|  /_____/\___/|___/  /_/ |_/_/\___/_/|_|
## ________________________________________________________

#
# ~/.config/fish/config.fish
#

if status is-interactive
    # Commands to run in interactive sessions can go here
	
	# Colors for linux terminal
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
	
	alias ls="exa --color=auto -h"
	alias ll="exa -Ralh"
	alias pacdate="expac --timefmt='%Y-%m-%d %T' '%l\t%n' | sort | tail -n 20"
	alias grep="grep --color=auto"
end
	
function fish_prompt
    printf '%s[ %s%s %s%s ]$ %s' (set_color blue) (set_color cyan) $USER (set_color blue) (prompt_pwd) (set_color normal)
end

# Root
#function fish_prompt
#	printf '%s[ %s%s %s%s ]$ %s' (set_color magenta) (set_color red) $USER (set_color magenta) (prompt_pwd) (set_color normal)
#end

function fish_greeting
	python nsplash.py
end

fish_add_path -m ~/.local/bin
