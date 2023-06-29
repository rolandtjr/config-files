#!/usr/bin/env fish
# Exports
set --export EDITOR "vim"
set --export PF_INFO "ascii title os host kernel uptime pkgs memory wm shell editor palette"
set --export MANPAGER "sh -c 'col -bx | bat -l man -p'"
set --export QT_QPA_PLATFORMTHEME "gtk2"
set --export XSECURELOCK_SAVER saver_xscreensaver
set --export XSECURELOCK_PASSWORD_PROMPT time_hex
set --export XSECURELOCK_XSCREENSAVER_PATH /usr/lib/xscreensaver
set --export XSECURELOCK_SHOW_KEYBOARD_LAYOUT 0
set --export XSECURELOCK_AUTH_BACKGROUND_COLOR "#2E3440"
set --export XSECURELOCK_AUTH_FOREGROUND_COLOR "#D8DEE9"
set --export XSECURELOCK_AUTH_SOUNDS 1
set --export XSECURELOCK_DIM_COLOR "#2E3440"
set --export XSECURELOCK_NO_COMPOSITE 1

if status is-interactive
end

# Start X at login
if status --is-login
  if set -q DISPLAY
    xset s 300 5
    xss-lock -n /usr/lib/xsecurelock/dimmer -l -- xsecurelock &
    while pactl load-module module-detect
    end
    if not pactl set-default-sink alsa_output.0.hdmi-stereo
      pactl set-default-sink alsa_output.1.hdmi-stereo
    end
    picom --animations --no-fading-openclose -b
  end
end

switch $DISPLAY
  case ':10.0'
    if test -z "$XSECURELOCK_XRDP"
      set --export XSECURELOCK_XRDP 1
      xset s 300 5
      xss-lock -n /usr/lib/xsecurelock/dimmer -l -- xsecurelock &
      pactl set-default-sink xrdp-sink
      picom --animations --no-fading-openclose -b
    end
end

# Check if DISPLAY is set

fish_add_path "$HOME/.local/bin"
fish_add_path "$HOME/.cargo/bin"
fish_add_path "/usr/lib/xsecurelock"

source "$HOME/.config/fish/abbreviations.fish"

starship init fish | source
