function save_pkgs --description "save pacman packages"
    pacman -Qqe > ~/.config/pkg.list
end
