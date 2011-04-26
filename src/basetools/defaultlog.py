'''
Created on Apr 11, 2011

@author: jdrumgoole
'''
import logging

class DefaultLog:
    '''
    Setup basic logging template for an ann
    '''

    def __init__( self, name, ext=".log" ):
        '''
        Constructor
        '''
        
        self._name = name
        self.ext = ext
        self._log = logging.getLogger( name )

        
    def setupLogfile(self):
        logging.basicConfig( filename = self._name + self._ext )
        
    def logger(self):
        return self._log
    
    def name(self):
        return self._name
    
    def ext(self):
        return self._ext
    

    def addConsoleHandler(self):
        self._consoleHandler = logging.StreamHandler()
        self._log.addHandler( self._consoleHandler )
        


