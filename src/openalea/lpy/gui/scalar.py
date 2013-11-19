class BaseScalar(object):
    def __init__(self, name):
        super(BaseScalar, self).__init__()
        self.name = name
        
    def isBool(self):
        return False
        
    def isFloat(self):
        return False

    def isCategory(self):
        return False
        
    def tostr(self):
        raise 
        
    def __reduce__(self):
        return (BaseScalar, (self.name,))

class BoolScalar (BaseScalar):
    def __init__(self,name,value = True):
        BaseScalar.__init__(self,name)
        self.value = value
    def importValue(self,other):
        self.name = other.name
        self.value = other.value
    def __eq__(self,other):
        return (self.name == other.name and self.value == other.value)
    def __neq__(self,other):
        return (self.name != other.name or self.value != other.value)
        
    def isBool(self):
        return True
        
    def tostr(self):
        return (self.name,self.value)
        
    def __reduce__(self):
        return (BoolScalar, self.tostr(),)

class IntegerScalar (BaseScalar):
    def __init__(self,name,value = 1,minvalue = 0, maxvalue = 100):
        BaseScalar.__init__(self,name)
        self.value = value
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    def importValue(self,other):
        self.name = other.name
        self.value = other.value
        self.minvalue = other.minvalue
        self.maxvalue = other.maxvalue
        
    def __eq__(self,other):
        return (self.name == other.name and self.value == other.value and 
                self.minvalue == other.minvalue and self.maxvalue == other.maxvalue)
    def __neq__(self,other):
        return (self.name != other.name or self.value != other.value or 
                self.minvalue != other.minvalue or self.maxvalue != other.maxvalue)
                
    def tostr(self):
        return (self.name,self.value,self.minvalue,self.maxvalue)
        
    def __reduce__(self):
        return (IntegerScalar,  self.tostr(),)
       
class FloatScalar (BaseScalar):
    def __init__(self,name,value = 1.,minvalue = 0., maxvalue = 100., decimals = 2):
        BaseScalar.__init__(self,name)
        self.value = value
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.decimals = decimals
        
    def importValue(self,other):
        self.name = other.name
        self.value = other.value
        self.minvalue = other.minvalue
        self.maxvalue = other.maxvalue
        self.decimals = other.decimals
        
    def __eq__(self,other):
        return (self.name == other.name and self.value == other.value and 
                self.minvalue == other.minvalue and self.maxvalue == other.maxvalue)
                
    def __neq__(self,other):
        return (self.name != other.name or self.value != other.value or 
                self.minvalue != other.minvalue or self.maxvalue != other.maxvalue)
        
    def isFloat(self):
        return True
        
    def tostr(self):
        return (self.name,self.value,self.minvalue,self.maxvalue, self.decimals)
        
    def __reduce__(self):
        return (FloatScalar, self.tostr(),)

class EnumScalar (BaseScalar):
    def __init__(self,name,value = 0,values = []):
        BaseScalar.__init__(self,name)
        self.value = value
        self.values = values
        
    def importValue(self,other):
        self.name = other.name
        self.value = other.value
        self.minvalue = other.minvalue
        self.maxvalue = other.maxvalue
        self.decimals = other.decimals
        
    def __eq__(self,other):
        return (self.name == other.name and self.value == other.value and 
                self.values == other.values )
                
    def __neq__(self,other):
        return not self.__eq__(other)
        
        
    def tostr(self):
        return (self.name,self.value,self.values)
        
    def __reduce__(self):
        return (EnumScalar,self.tostr(),)
        
class CategoryScalar (BaseScalar):
    def __init__(self, name):
        BaseScalar.__init__(self,name)
    
    def isCategory(self):
        return True
        
    def tostr(self):
        return (self.name,None)

    def __reduce__(self):
        return (CategoryScalar, self.tostr(),)    
    
def ProduceScalar(v):
    if type(v[1]) == bool : return BoolScalar(v[0],v[1])
    elif type(v[1]) == float : return FloatScalar(*v)
    elif v[1] is None : return CategoryScalar(v[0])
    else : return IntegerScalar(*v)