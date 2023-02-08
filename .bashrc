#
# ~/.bashrc
#

export PYTHONPATH=~/Documents/Course-Material/module-o/book/src
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# ls aliases
alias ls='exa --color=auto'
alias sl='exa --color=auto'
alias ll='exa -la --color=auto'

# git aliases
alias gs='git status'
alias gcm='git commit -m'
alias config='git --git-dir=$HOME/config-files/ --work-tree=$HOME'

# aliases
alias ..='cd ..'
alias vi='vim'
alias ip='ip -color=auto'

# vi key bindings
set -o vi

PS1='[\u@\h \W]\$ '

# starship prompt
eval "$(starship init bash)"

colorscript -e roshar

case ${TERM} in

  xterm*|rxvt*|alacritty*|Eterm|aterm|kterm|gnome*)
     PROMPT_COMMAND=${PROMPT_COMMAND:+$PROMPT_COMMAND; }'printf "\033]0;%s@%s:%s\007" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'

    ;;
  screen*)
    PROMPT_COMMAND=${PROMPT_COMMAND:+$PROMPT_COMMAND; }'printf "\033_%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/\~}"'
    ;;
esac
