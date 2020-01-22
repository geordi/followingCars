
from engine import Engine, Car, ForwardCar
from vizualization import App


def create_model(engine):
    engine.clear_model()
    engine.add(ForwardCar([0,0], [1,0]))
    engine.add(ForwardCar([0,-50], [0.5,0]))
    engine.add(Car([0,50]))
    engine.summary()

if __name__ == "__main__" :
    engine = Engine()    
    engine.create_model = create_model
    
    app = App(engine)
    app.on_execute()
    
    
