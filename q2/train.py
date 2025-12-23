from incomplete import Transportation

class Train( Transportation ):

   def __init__( self, start, end, distance, station ):
      Transportation.__init__( self, start, end, distance)
      self.noOfStation = station

   def find_cost( self ):
      return self.noOfStation*5

if __name__ == "__main__":
   trainnyS = Train(0, 19, 599, 6)
   print(trainnyS.find_cost())