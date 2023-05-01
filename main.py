# -*- coding: utf-8 -*-
"""
Program Prj_generator

Created on 01-05-23 15:32:00

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""

import sys
import os

import str_common as strc

"""
def selfdoc():
    print(
        ''' 
        === Project generator ++++==============================================
            
        Предназначен для генерации каркаса будущей программы

        =======================================================================
        '''
    )
"""

def main():
    #selfdoc()
    strc.titleprogram("Program for generation any projects",
                      "Prj_generator",
                      "LN Starmark",
                      )
    target = ""

    lst_selfdoc = ["Project:    Test", "Target :    tutorial", "Version:    v0.0.1"]
    target = Gen_Selfdoc(target, lst_selfdoc)
    print(target)
    eval(target)


def Gen_Selfdoc(targ: str, lst):
    targ += 'def Selfdoc():\n'
    targ += '\tprint("\\t========================\\n")'+'\n'
    for el in lst:
        targ += '\tprint("\\t=== '+el+'\\n")'+'\n'

    return targ

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

