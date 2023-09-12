function cfs --description "git push for config-files"
    git --git-dir=$HOME/config-files --work-tree=$HOME status
end
