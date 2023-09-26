#
# ~/.bashrc
#

export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# ls aliases
alias ls='eza --color=auto'
alias sl='eza --color=auto'
alias ll='eza -la --color=auto'

# git aliases
alias gss='git status'
alias gcm='git commit -m'
alias cf='git --git-dir=$HOME/config-files/ --work-tree=$HOME'

# aliases
alias ..='cd ..'
alias vi='vim'
alias ip='ip -color=auto'

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
