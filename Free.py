import os
if __name__=='__main__':
        os.system('git pull')
        try:os.mkdir('CP')
        except:pass
        try:os.mkdir('OK')
        except:pass
        menu()
