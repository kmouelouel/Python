def kelvintoFahreheit(temperature):
    assert(temperature>=0);
    return ((temperature-273)*1.8)+32
 
    print(kelvintoFahreheit(273));
    print(kelvintoFahreheit(505.78));
  #  print(kelvintoFahreheit(-5));
except IOError:
    print("Error: the value entrend was negative");
else:
    print("the conversion is successfully done");
    
