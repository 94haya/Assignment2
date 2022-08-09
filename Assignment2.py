# class Location:
#   def __init__(self, location):
#     self.location = location
   

# l1 = Location("Amman")

# print(l1.location)



class Residence:
  def __init__(self,residence,price,country ):
    self._residence = residence
    self._price=price
    self._country=country
    

  def r(self):
    print(self._residence, self._price,self._country)
  
x = Residence("Amman", "500","Jordan")
print(x._residence,x._price,x._country)

class Villa(Residence):
  def __init__(self,residence,price,country,area ):
    super().__init__(self,residence,price,country)
    self._area=area


  def set1(self,area):
        self.__area="144"
    
  def get1(self) :
        return self.__area  


print(Villa.get1())



class Apartment(Villa):
  def __init__(self,residence,price,country,area,apartmentnumber ):
    super().__init__(self,residence,price,country,area)
    self._apartmentnumber=apartmentnumber

    


 





