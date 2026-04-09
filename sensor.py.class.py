import random as r

class Sensor:
    """
    Base sensor class,,
    """
    def _init_(self, name: str): -> None:
        self.name = name

    def read(self) -> float:
        return 0.0

class TemperatureSensor(Sensor):
    """
    Simulated temp sensor.
    """
    def _init_(self, name: str) -> None:
        super()._init_(name)

    def read(self) -> float:
        return round (r.uniform(20.0, 30.0), 2)

class LightSensor(Sensor):
    """
    Simulated light sensor.
    """
    def read (self) -> float:
        return round(r.uniform(0, 100), 2)
