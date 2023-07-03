syntax enable

set ttymouse=sgr
set mouse=a

set encoding=UTF-8

set number
set ruler
set title
set confirm
set showmode
set wrap

set autoindent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

set colorcolumn=80

set foldmethod=indent

call plug#begin("~/.vim/plugged")

Plug 'scrooloose/nerdtree'
Plug 'ryanoasis/vim-devicons'
Plug 'vim-scripts/AutoComplPop'
Plug 'davidhalter/jedi-vim'
Plug 'mg979/vim-visual-multi'
Plug 'rafi/awesome-vim-colorschemes'

call plug#end()

colorscheme minimalist

autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p

let g:NERDTreeShowHidden=1

autocmd FileType python setlocal omnifunc=jedi#completions
