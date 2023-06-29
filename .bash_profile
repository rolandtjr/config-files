#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export XSECURELOCK_SAVER=saver_xscreensaver
export XSECURELOCK_PASSWORD_PROMPT=time_hex
export XSECURELOCK_XSCREENSAVER_PATH="/usr/lib/xscreensaver"
export XSECURELOCK_SHOW_KEYBOARD_LAYOUT=0
export XSECURELOCK_AUTH_BACKGROUND_COLOR="#2E3440"
export XSECURELOCK_AUTH_FOREGROUND_COLOR="#D8DEE9"
export XSECURELOCK_AUTH_SOUNDS=1
export XSECURELOCK_DIM_COLOR="#2E3440"
export XSECURELOCK_NO_COMPOSITE=1

xset s 300 5
xss-lock -n /usr/lib/xsecurelock/dimmer -l -- xsecurelock &
pactl set-default-sink xrdp-sink
picom --animations --no-fading-openclose -b

#if [ -z "${DISPLAY}"] && [ "${XDG_VTNR}" == 1 ]; then
if [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
fi
