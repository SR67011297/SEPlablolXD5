from incomplete import Transportation

class Train( Transportation ):

   def __init__( self, start, end, distance, station ):
      Transportation.__init__( self, start, end, distance)
      self.noOfStation = station

   def find_cost( self ):
      return self.noOfStation*5
