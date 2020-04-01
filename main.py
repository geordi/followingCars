
from engine import Engine, Car, LidarSensor
from visualization import Visualization

def kmh2ms(speed):
    """Transform the speed in km per hour into meter per second
    
    Arguments:
        speed {float} -- input speed
    
    Returns:
        float -- converted speed
    """
    return speed / 3.6

"""Dimension of Skoda SuperB"""
superbdim = [4.861, 1.864]
def create_model(engine):
    engine.clear_model()
    
    engine.add(Car([0,0], superbdim, kmh2ms(0)))
    engine.add(Car([5,0], superbdim, kmh2ms(20), steering=-30))
    # engine.add(Car([0,-2], superbdim, kmh2ms(20)))
    # engine.add(Car([0,2], superbdim))
    engine.summary()


if __name__ == "__main__" :
    engine = Engine(step_time = 1/60.0, delay = 1/60.0)    
    engine.create_model = create_model
    
    app = Visualization(engine)
    app.on_execute()
    
    
