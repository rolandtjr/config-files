# Exports
set --export EDITOR "vim"
set --export PF_INFO "ascii title os host kernel uptime pkgs memory wm shell editor palette"
set --export MANPAGER "sh -c 'col -bx | bat -l man -p'"
set --export QT_QPA_PLATFORMTHEME "gtk2"

if status is-interactive
end

# Start X at login
if status --is-login
  while pactl load-module module-detect
  end
  if not pactl set-default-sink alsa_output.0.hdmi-stereo
    pactl set-default-sink alsa_output.1.hdmi-stereo
  end
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
    exec startx -- -keeptty
  end
end

fish_add_path "$HOME/.local/bin"
fish_add_path "$HOME/.cargo/bin"

source "$HOME/.config/fish/abbreviations.fish"

starship init fish | source
