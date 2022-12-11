#
# ~/.bashrc
#

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


PS1='[\u@\h \W]\$ '

# starship prompt
eval "$(starship init bash)"

# colorscript
colorscript random
