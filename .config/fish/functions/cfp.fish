function cfp --description "git push for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME push $argv
end
