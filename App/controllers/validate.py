from moneyed import Money, BRL

class Val:
  def validate_price(string):
    """
      >>> Val.validate_price('10.42')
      True
      
      >>> Val.validate_price('teste')
      False
    """
    
    try:
      Money(string, BRL)
      return True
    except:
      return False
    
val = Val

import doctest

doctest.testmod()