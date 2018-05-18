#!/usr/bin/python3
class MyList(list):
    '''
    class inherits from list
    '''

    def print_sorted(self):
        '''
        print a sorted list
        '''
        print(sorted(self))
