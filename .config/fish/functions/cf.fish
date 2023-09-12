function cf --description "git command for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME $argv
end
