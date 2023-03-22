syntax enable
filetype plugin indent on

set encoding=UTF-8
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set copyindent

set number

set laststatus=2

nnoremap <C-g> :NERDTreeToggle<CR>
" 
call plug#begin(expand('~/.vim/plugged'))
" Color Scheme
Plug 'arcticicestudio/nord-vim'
Plug 'itchyny/lightline.vim'
Plug 'ap/vim-css-color'
Plug 'ycm-core/YouCompleteMe'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-surround'
Plug 'ryanoasis/vim-devicons'
Plug 'xuhdev/vim-latex-live-preview'
call plug#end()

colorscheme nord
let g:lightline = {
      \ 'colorscheme': 'nord',
      \ }

" vim-laxet-live-preview settings
autocmd Filetype tex setl updatetime=1
let g:livepreview_previewer = 'zathura'
