function cfd --description "git diff for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME diff $argv
end
