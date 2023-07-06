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

" zd - Delete the fold under the cursor
" zE - Delete all folds
" zo - Open (expand) a fold under the cursor
" zc - Close (collapse) a fold under the cursor
" za - Toggle the open/close state of a fold under the cursor
" zM - Close all folds
" zR - Open all folds
" zv - View the contents of the current fold
set foldmethod=indent

set nocompatible

call plug#begin("~/.vim/plugged")

" :NERDTree - To open the file tree
Plug 'scrooloose/nerdtree'

" Lean & mean status/tabline for vim that's light as air
Plug 'vim-airline/vim-airline'

" Auto completion
Plug 'vim-scripts/AutoComplPop'

" Expanding abbreviations similar to emmet
Plug 'mattn/emmet-vim'

" Python autocompletion with VIM
Plug 'davidhalter/jedi-vim'

" A collection of language packs for Vim
Plug 'sheerun/vim-polyglot'

" Ctrl + n       - Selects the word at the cursor, or the next occurrence
" Ctrl + Up/Down - Create cursors vertically
" n / N          - Get next/previous occurrence
" [ / ]          - Select next/previous cursor
" q              - Skip current and get next occurrence
" Q              - Remove current cursor/selection
Plug 'mg979/vim-visual-multi'

" Best color scheme
Plug 'dikiaap/minimalist'

" Icons for NERDTree
Plug 'ryanoasis/vim-devicons'

" CSS color name highlighter
Plug 'ap/vim-css-color'

" You need a npm package for this plugin:
"     npm install -g browser-sync
"
" :BrowserSyncStart - To start the server
" :BrowserSyncStop  - To stop the server
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

