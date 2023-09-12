function cfc --description "git commit -m for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME commit -m $argv
end
