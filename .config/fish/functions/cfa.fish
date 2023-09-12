function cfa --description "git add for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME add $argv
end
