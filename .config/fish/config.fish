#!/usr/bin/env fish
# Exports
set --export EDITOR "vim"
set --export PF_INFO "ascii title os host kernel uptime pkgs memory wm shell editor palette"
set --export MANPAGER "sh -c 'col -bx | bat -l man -p'"
set --export MANROFFOPT "-c"
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
# bun
set --export BUN_INSTALL "$HOME/.bun"

if status is-interactive
  source "$HOME/.config/fish/abbreviations.fish"
end

# Start X at login
if status --is-login
  fish_add_path "$HOME/.local/bin"
  fish_add_path "$HOME/.cargo/bin"
  fish_add_path "$HOME/go/bin"
  fish_add_path "/usr/lib/xsecurelock"
  fish_add_path "$HOME/.local/share/gem/ruby/3.0.0/bin"
  fish_add_path "$BUN_INSTALL/bin"
  # Check if DISPLAY is set
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

pyenv init - | source
starship init fish | source

