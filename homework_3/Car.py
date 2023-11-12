class Car:
    brand: str
    model: str
    color: str
    body_type: str
    wheel_count: int
    fuel_type: str
    transmission_type: str
    engine_capacity: float

    def __init__(self, brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity):
        self.engine_capacity = engine_capacity
        self.transmission_type = transmission_type
        self.fuel_type = fuel_type
        self.wheel_count = wheel_count
        self.body_type = body_type
        self.color = color
        self.model = model
        self.brand = brand

    def move(self):
        pass

    def service(self):
        pass

    def gear_shifting(self):
        pass

    def turn_lights(self):
        pass

    def turn_wipers(self):
        pass
