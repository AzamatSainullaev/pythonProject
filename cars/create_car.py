class Car:

    def __init__(self, title, model, engine, max_speed, speed):
        self.title = title
        self.model = model
        self.engine = engine
        self.max_speed = max_speed
        self.speed = speed

    def start_engine(self):
        return f"{self.model} starting engine"

    def stop_engine(self):
        return f"{self.model} stopping engine"