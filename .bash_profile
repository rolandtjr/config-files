#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" == 1 ]; then
  exec startx
  exec picom -b
fi

