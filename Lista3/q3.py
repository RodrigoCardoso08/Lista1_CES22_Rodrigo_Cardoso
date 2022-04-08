class A:
    """Tokenize text"""
    def __init__(self, text):
        print('Start A.__init__()')
        print('End A.__init__()')

class C(A):
    """Count words in text"""
    def __init__(self, text):
        print('Start C.__init__()')
        super().__init__(text)
        print('End C.__init__()')


class B(A):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start B.__init__()')
        super().__init__(text)
        print('End B.__init__()')


class D(C, B):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start D.__init__()')
        super().__init__(text)
        print('End D.__init__()')


td = D('maca uva pera banana goiaba')

"""Com esse código podemos perceber o comportamento do método super() com heranças multiplas"""
