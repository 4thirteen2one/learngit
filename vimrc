set nu
"开启显示行号

set nocompatible
"关闭兼容模式

set encoding=utf-8
""设置utf-8编码

set fileencoding=utf-8
"当前编辑的文件编码

set sw=4
""缩进为4个空格

set ts=4
"tab宽度为4个字符

set et
"编辑时将所有tab替换为空格

set smarttab
"按一次Backspace就删除4个空格

colo desert
"配色方案

set nobackup
"不生成备份文件

set cursorline
"highlight the current line

syntax on
"highlight

set foldenable
set foldmethod=manual

set ruler

:autocmd FileType python: set number 
:autocmd FileType python: set foldmethod=syntax 
:autocmd FileType python :set smartindent
