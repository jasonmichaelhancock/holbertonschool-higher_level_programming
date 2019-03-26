#!/usr/bin/python3
    '''
    class inherits from list
    '''

class MyList(list):
    '''
    class inherits from list
    '''
    def __init__(self):
        '''
        initializes new MyList object
        '''
        pass

    def print_sorted(self):
        '''
        print a sorted list
        '''
        print(sorted(self))
