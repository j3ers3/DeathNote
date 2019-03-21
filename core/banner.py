# encoding: utf-8
from .color import *

__author__ = "whois"
__update__ = "2019/3/20"
__version__ = "1.0"


def banner_main():
    ston = blue + "[=" + end
    ston2 = blue + "=]" + end
    #print "" #
    print("\t\t->>" + ston + green + "="*20 + ston2 + "->>" + end) 
    print("\tMMMMMM---==" + ston + "Version : " + red + __version__ + end) 
    print("\tMMMMMM---==" + ston + "Powered By : " + cyan + __author__ + end) 
    print("\t\t<<-" + ston + "Update Date : [" + red + __update__ + end + "]") 


class banner:


    windows = red + """
                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888:::::::::::::: """ + cyan + """
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''""" + end


    py = green + """
 ____             ____  _          _ _ 
|  _ \ _   _     / ___|| |__   ___| | |
| |_) | | | |____\___ \| '_ \ / _ \ | |
|  __/| |_| |_____|__) | | | |  __/ | |
|_|    \__, |    |____/|_| |_|\___|_|_|
       |___/                           \n\n""" + end


    wmic = yellow + """
__        __         _           _   _            _
\ \      / / __ ___ (_) ___     | | | | __ _  ___| | __
 \ \ /\ / / '_ ` _ \| |/ __|____| |_| |/ _` |/ __| |/ /
  \ V  V /| | | | | | | (_|_____|  _  | (_| | (__|   <
   \_/\_/ |_| |_| |_|_|\___|    |_| |_|\__,_|\___|_|\_\\\n""" + end


    ban = cyan + """
                           ______    
                        .-        -. 
                       /            \\         
                      |,  .-.  .-.  ,|      
                      | )(_ /  \_ )( |
                      |/     /\     \\|    
             (@_      <__    ^^    __>       
             )""" + red + """ \_______\__|IIIIII|__/____________________ 
      (_)\@8@8{}<________________________________________>""" + cyan + """
             )_/         \ IIIIII /                    
             (@           --------                      \n""" + end
                                         

    linux = red + """
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt\n\n""" + end


    ps = red + """

           |\\ 
           | \\                    
           |  \\      
()#########|""" + cyan + """============================================>""" + red + """ 
           |  /       
           | / 
           |/       
M         """ + yellow + """Death Note""" + red + """               
M                                             
M                                             
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n""" + end



    msfvenom = blue + """

      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.
         ,kOl'M.OOOOOOOOOOOOO.M'dOk,
           :kk;.OOOOOOOOOOOOO.;Ok:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .\n""" + end