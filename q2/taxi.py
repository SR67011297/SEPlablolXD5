from incomplete import Transportation

class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
        self.start = start
        self.end = end
        self.distance = distance

    def find_cost( self ):
        return self.distance * 40