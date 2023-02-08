syntax enable
filetype plugin indent on

set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set copyindent

set number

set laststatus=2
" 
call plug#begin(expand('~/.vim/plugged'))
" Color Scheme
Plug 'arcticicestudio/nord-vim'
Plug 'itchyny/lightline.vim'
Plug 'ap/vim-css-color'
Plug 'ycm-core/YouCompleteMe'
Plug 'preservim/nerdtree'
call plug#end()

colorscheme nord
let g:lightline = {
      \ 'colorscheme': 'nord',
      \ }
