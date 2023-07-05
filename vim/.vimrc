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
set smartindent
set tabstop=4
set softtabstop=4

set colorcolumn=80

set foldmethod=indent

set nocompatible

call plug#begin("~/.vim/plugged")

Plug 'scrooloose/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'ryanoasis/vim-devicons'

Plug 'vim-scripts/AutoComplPop'
Plug 'mattn/emmet-vim'
Plug 'davidhalter/jedi-vim'
Plug 'mg979/vim-visual-multi'
Plug 'sheerun/vim-polyglot'

Plug 'rafi/awesome-vim-colorschemes'
Plug 'ap/vim-css-color'

Plug 'tamago324/vim-browsersync'

call plug#end()

colorscheme minimalist

autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p

let g:NERDTreeShowHidden=1

autocmd FileType python setlocal omnifunc=jedi#completions

let g:airline#extensions#tabline#enabled = 1
let g:airline_left_sep = ''
let g:airline_right_sep = ''
let g:airline_section_z = '%p%% -%3l %c'

