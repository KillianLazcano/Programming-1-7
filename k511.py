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

  def i(self):
    """print I with beepers"""
    self.put2()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def a(self):
    """Print A with beepers"""
    self.tl()
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()

  def N(self):
    """Print N with beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.ta()
    self.put5()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    
  def one(self):
    self.tl()
    self.mm(5)
    self.ta()
    self.putm(5)
    self.tl()
    self.mm(2)

  def sob(self) -> bool:
    """standing on beeper"""
    return beepers_present()

  def jump(self):
    """jump for K510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

    def find(self):
      """find for K515"""
      while not facing_north():
        self.tl()
      self.m()
      if not self.sob():
       self.tl()
       self.m()
       self.tl()
       self.m()
      for _ in range(2):
        if not self.sob():
          self.m()
          self.tl()
          self.m()
      pass
      
    
  
  def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.tl()
    kt.mm(3)
    kt.tr()
    kt.mm(3)
    kt.tr()
    kt.mm(3)
    kt.tl()
    kt.mm(2)
    kt.tl()
    kt.mm(8)
    kt.tr()
    kt.mm(2)
    kt.tr()
    kt.mm(8)
    kt.tl()
    kt.m()
    kt.tl()
    kt.mm(5)
    kt.tr()
    kt.mm(7)
    kt.tr()
    kt.mm(5)
    kt.tl()
    kt.m()
    kt.mm(7)
    kt.tr()
    kt.m()
    kt.tr()
    kt.mm(7)
    kt.tl()
    kt.m()
    kt.tl()
    kt.mm(4)
    kt.tr()
    kt.mm(2)
    kt.tr()
    kt.mm(4)
    kt.tl()
    kt.m()
    pick_beeper()
    
    pass


if __name__ == "__main__":
    run_karel_program()