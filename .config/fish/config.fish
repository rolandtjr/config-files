# Exports
set --export EDITOR "vim"
set --export PF_INFO "ascii title os host kernel uptime pkgs memory wm shell editor palette"
set --export MANPAGER "sh -c 'col -bx | bat -l man -p'"
set --export QT_QPA_PLATFORMTHEME "gtk2"

if status is-interactive
    # Commands to run in interactive sessions can go here
end

fish_add_path "$HOME/.local/bin"

source "$HOME/.config/fish/abbreviations.fish"

starship init fish | source
