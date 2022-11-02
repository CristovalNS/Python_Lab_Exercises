
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = celsius
        self.__kelvin = celsius

    def set_to_celsius(self, celsius):
        self.__celsius = celsius

    def set_to_fahrenheit(self, celsius):
        self.__fahrenheit = celsius

    def set_to_kelvin(self, celsius):
        self.__kelvin = celsius

    def to_celsius(self):
        return str(round(self.__celsius, 2))

    def to_fahrenheit(self):
        return str(round((self.__fahrenheit * 9/5 + 32), 2))

    def to_kelvin(self):
        return str(round((self.__kelvin + 273.15), 2))

    def __str__(self):
        return "Celsius:" + self.to_celsius() + "\nFahrenheit:" + self.to_fahrenheit() + "\nKelvin:" + self.to_kelvin()


