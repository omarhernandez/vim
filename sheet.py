;-----------------------------------------

VIM CONFIG.

set autoindent 
set number 
set hlsearch #highlight search
execute pathogen#infect()  #panthogen
syntax on #set syntex on
au VimEnter * NERDTree ~/code/ #open NERDTree in ~/DIR/  

;--------------------------------------

PLUGIN MANAGER

install panthogen

cd  ~/.vim/ && mkdir 
	
	    autoload/
	    bundle/ # here's the vim plugins

;--------------------------------------

My Vim shortcuts
;--------------------------------------

CHANGE BETWEEN TABS IN  NERD TREE

cntrl + w + l  = change window RIGHT
contrl + w + h = change window LEFT
cntrol + w + j = change window DOWN
cntrol + w + k = change window UP  

;--------------------------------------

GO FIRST LETTER IN DOCUMENT

:0

;--------------------------------------

GO LAST LETTER IN DOCUMENT

:$

;--------------------------------------

REPLACE A CHAR ( ESC MODE)

R: (press under the char to change)

;--------------------------------------

CHAGE TO UPPERCASE A STRING (ESC MODE)

gUw:

;--------------------------------------

CHANGE TO LOWERCASE A STRING (ESC MODE)

guw:

;---------------------------------------

OPEN NERDTREE

:NERDTree /path/to/open

;--------------------------------------

DELETE ALL STRINGS AFTER CURSOR (ESC MODE )

c$:

;--------------------------------------

DELETE ALL STRINS BEFORE CURSOR (ESC MODE)

c0:

;---------------------------------------

CLOSE CURRENT TAB NERDTREE

:tabclose

;---------------------------------------

GO FIRST TAB NERDTREE

:tabfirst

;--------------------------------------

MOVE PREVIOUS TAB IN NERDTREE 

gt:

;-------------------------------------

MOVE NEXT TAB IN NERDTREE

gT:

;--------------------------------------

OPEN TAB SPLIT VERTICAL NERDTREE

s:

OPEN TAB SPLIT HORIZONTAL NERDTREE

i:

OPEN IN NEW TAB NERDTREE

T:

