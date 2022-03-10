import fire

#class MetaTest:
#    def __cls__(cls):
#        cls.tag = "not narf"

class Test:#(MetaTest):
    """
    docstring before Test.__init__
    """
    def __init__(self):
        """
        docstring inside Test.__init__
        """
        self.tag = "not narf"

    def settag(self,inputstring:str):
        """
        Sets self.tag as param, if param is string
        """
        self.tag = inputstring

    def _private_method(self):
        """
        Should be invisible to fire
        """
        if self.tag == "narf":
            print("_private_method goes BRRRRRRRR")

def _private_function():
    """
    Should be invisible to fire
    
    Fire RUNS THIS FUNCTION on init FOR SOME UNGODLY REASON

    """
    print("fuuuuuck ing helllo")

def public_function():
    """
    Public facing method for testing

    Fire RUNS THIS FUNCTION on init FOR SOME UNGODLY REASON
    """
    print("google sucks at documentation, thats why I have to do this")


class MenuGrouping():
    '''    
    MenuGrouping before __init__
    '''
    def __init__(self):
        """
        MenuGrouping.__init__
        """
        # labeled as group
        self.Test    = Test()

        # labeled as value
        self.tag     = Test().tag
        self.settag  = Test().settag("narf")
        self.public  = public_function()
        self.private = _private_function()
        self.settag_noparen = Test.settag(Test, inputstring = "narf")

        # labeled as COMMAND
        self.Test_noparen = Test
        self.public_noparen = public_function
        self.private_noparen =_private_function

        # doesnt work even with cls.tag
        #self.tag_noparen = Test.tag
        

def menu_function():
    """
    docstring for menu function
    """
    fire.Fire(
        {
        "Test_noparen":Test,
        "public_noparen" : public_function,
        "private_noparen": _private_function
       }
    )

if __name__ == "__main__":
    menu_function()
    #fire.Fire(MenuGrouping)

