syntax enable
filetype plugin indent on

set encoding=UTF-8
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set copyindent

set number relativenumber

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
Plug 'rust-lang/rust.vim'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'takac/vim-hardtime'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'github/copilot.vim'
call plug#end()

colorscheme nord
let g:lightline = {
      \ 'colorscheme': 'nord',
      \ }

" vim-laxet-live-preview settings
autocmd Filetype tex setl updatetime=1
let g:livepreview_previewer = 'zathura'
let g:hardtime_default_on = 1

let g:copilot_enable = 1
let g:copilot_filetypes = {
            \ 'python': v:true,
            \ 'c': v:true,
            \ 'cpp': v:true,
            \ 'java': v:true,
            \ 'javascript': v:true,
            \ 'typescript': v:true,
            \ 'go': v:true,
            \ 'rust': v:true,
            \ 'html': v:true,
            \ 'css': v:true,
            \ 'perl': v:true
            \}
