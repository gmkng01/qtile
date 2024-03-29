#!/usr/bin/env bash 

# festival --tts $HOME/.config/qtile/welcome_msg &
# lxsession &
picom --no-fading-openclose &
# /usr/bin/emacs --daemon &
# conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc
volumeicon &
nm-applet &
blueman-applet &
# devilspie &
# indicator-kdeconnect &
volctl &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
# find /usr/share/backgrounds/dtos-backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &
trayer --transparent true --width 5 --edge top --align right --tint 0xEF0EFEA --alpha 0 --tint 0x000000 --margin 10 --distance 10 --distancefrom top &
# /home/abhi/.config/polybar/launch.sh &
# polybar &


