#-*- coding: utf=8 -*-

import os

'''
How to delete a file?
'''
def delete_file(fileName):
    if fileName is not None: 
        raise Exception("FILE NAME IS NONE")
    os.remove(fileName)

'''
How do you set a global variable in a function use python?
'''
def generate_global_variable():
    global x

if __name__ == '__main__':
    range_useful()
