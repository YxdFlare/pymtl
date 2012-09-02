#=========================================================================
# RegIncrStruct
#=========================================================================
# Instead of using our own register and incrementer implementations, we
# can also simply use the ones provides in pmlib. We would need to
# comment out importing our own implementations, use the imports from
# pmlib instead, and also use the appropriate instantiations in our code
# when we want to instantiate these two models (i.e., arith.Incrementer
# and regs.Register)

from pymtl import *

from Register    import Register
from Incrementer import Incrementer

# from pmlib import arith
# from pmlib import regs

class RegIncrStruct( Model ):

  def __init__( self ):
    self.in_  = InPort( 16 )
    self.out  = OutPort( 16 )

    # Register

    self.reg = Register( 16 )
    connect( self.in_, self.reg.in_ )

    # Incrementer

    self.incr = Incrementer( 16 )
    connect( self.reg.out,  self.incr.in_ )
    connect( self.incr.out, self.out      )

  def line_trace( self ):
    return self.reg.line_trace() + " | " + self.incr.line_trace()
