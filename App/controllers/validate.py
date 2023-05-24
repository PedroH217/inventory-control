from moneyed import Money, BRL

class Val:
  def validate_price(string):
    try:
      Money(string, BRL)
      return True
    except:
      return False
    
val = Val