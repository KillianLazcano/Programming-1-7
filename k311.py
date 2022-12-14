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
     """print E with beepers"""
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

    

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.put()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.put()
    kt.tr()
    pass


if __name__ == "__main__":
    run_karel_program()