#! usr/bin/env python
# -*- coding: utf-8 -*-

quitornot = None

while(quitornot != 'q'):
    
    x = int(input('x: '))
    y = int(input('y: '))
    i = int(input('i: '))
    j = int(input('j: '))
                        
    def print_grid(x,y,i,j):
        for a in range(y):
            for b in range(x):
                print('+ ' + '- ' * i, end = '')
            print('+')
            for c in range(j):
                for d in range(x):
                    print('| ' + '  ' * i, end = '')
                print('|')
        for b in range(x):
                print('+ ' + '- ' * i, end = '')
        print('+')
        
    print_grid(x,y,i,j)
        
    quitornot = input('Quit?')

