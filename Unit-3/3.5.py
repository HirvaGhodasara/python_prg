class Temperature:

    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)


temp = Temperature()

temp.convertFahrenheit(25)   
temp.convertCelsius(77)      
