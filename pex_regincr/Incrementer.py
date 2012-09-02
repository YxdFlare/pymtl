#=========================================================================
# Incrementer
#=========================================================================

from pymtl import *

class Incrementer( Model ):

  def __init__( self, bits ):
    self.in_ = InPort( bits )
    self.out = OutPort( bits)

  @combinational
  def comb_logic( self ):
    self.out.value = self.in_.value + 1

  def line_trace( self ):
    return "{:>2} {:>2}" \
      .format( self.in_.value, self.out.value )
