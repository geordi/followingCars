
from engine import Engine, Car, ForwardCar
from vizualization import App


def kmh2ms(speed):
    return speed / 3.6

superbdim = [4.861, 1.864]
def create_model(engine):
    engine.clear_model()
    engine.add(ForwardCar([0,-4], superbdim, kmh2ms(20)))
    engine.add(ForwardCar([0,0], superbdim, kmh2ms(30)))
    engine.add(Car([0,4], superbdim))
    engine.summary()

if __name__ == "__main__" :
    engine = Engine()    
    engine.create_model = create_model
    
    app = App(engine)
    app.on_execute()
    
    
