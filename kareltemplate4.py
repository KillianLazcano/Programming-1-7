from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    move()
    
  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
   """pick beeper"""
  pick_beeper()

  def put(self):
    """put beeper"""
    put_beeper()
    
  def put2(self):
    """put two beepers in line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """put 5 beepers in line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """print H with beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

    def e(self):
     self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.put2()
    self.m()
    self.m()

  def l(self):
    """print l """
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()
    
  def o(self):
    """print O with beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()

  def fic(self) -> bool:
    """front is clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """front is blocked"""
    return not self.fic()

  def ric(self) -> bool:
    """right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True # Immediately exit the function
    self.tl()
    return False 

  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else: # Otherwise
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

  def mm(self, num):
    """move multiple"""
    for number in range(0, num):
      self.m()

  def putm(self, num):
    """put multiple"""
    for i in range(num-1):
      self.put()
      self.m()
    self.put()

  def pickm(self, num):
    """pick multiple"""
    for _ in range(num-1):
      self.pick()
      self.m()
    self.pick()
   
  
  def k(self):
    """print K with beepers"""
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    
  def one(self):
    self.tl()
    self.mm(5)
    self.ta()
    self.putm(5)
    self.tl()
    self.mm(2)

  

def main():
    """ Karel code goes here! """
    kt = ktools()
    pass


if __name__ == "__main__":
    run_karel_program()