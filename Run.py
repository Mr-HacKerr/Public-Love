import os,time
def clear():
	os.system('clear')
def banner():
	clear()
	print("""
\033[1;35m
'##::::'##::::::::::'########::::'###::::'####:'##::: ##:
\033[1;92m ###::'###::::::::::..... ##::::'## ##:::. ##:: ###:: ##:
\033[1;93m ####'####:::::::::::::: ##::::'##:. ##::: ##:: ####: ##:
\033[1;94m ## ### ##:'#######:::: ##::::'##:::. ##:: ##:: ## ## ##:
\033[1;95m ##. #: ##:........::: ##::::: #########:: ##:: ##. ####:
\033[1;96m ##:.:: ##::::::::::: ##:::::: ##.... ##:: ##:: ##:. ###:
\033[1;91m ##:::: ##:::::::::: ########: ##:::: ##:'####: ##::. ##:
\033[1;94m..:::::..:::::::::::........::..:::::..::....::..::::..::

\033[1;92m(!)========================================
\033[1;96m(!) Author   : MUHAMMAD ZAIN 
(!) Guthub   : Mr-HacKerr 
(!) Type     : FREE
\033[1;32m(!)========================================""")
def Update():
    banner()
    print('\033[1;95m[1] Cloning Menu')
    print('[2] Phishing ')
    print('[3] Encrypt Your Script')
    print('[4] Contact With Creater')
    zain = input("\033[1;93mChoose What you want: ")
    if zain=='1':
    	za()
    elif zain=='2':
        os.system('git clone https://github.com/Mr-HacKerr/mrphisher.git')
        os.system(' cd mrphisher')
        os.system(' bash mrphisher.sh')
    elif zain=='3':
    	os.system('python2 Hide-me.py')
    elif zain=='4':
    	os.system('xdg-open https://wa.me/+923003566540')
    
def za():
    print("[1] File Cloning")
    print("[2] Number Cloning")
    print("[3] Encrypt your Script")
    print("[4] File Making Menu")
    print("[5] Just Cloning Tool")
    print("[6] Exit Program")
    zain = input("Choose What You Want")
    if zain=='1':
    	os.system('python File.py')
    elif zain=='2':
        os.system('python Num.py')	
    elif zain=='4':
    	print('This option is in under construction')
    	print('Dear Brother/Sister please Wait Untill this option was replace')
    elif zain=='5':
    	os.system('python Free.py')
    elif zain=='6':
    	exit.sys()
    elif zain=='3':
        os.system("python2 H.py")
    else:
    	print("Dear Please Choose Correctly")
    Update()
    
Update()
