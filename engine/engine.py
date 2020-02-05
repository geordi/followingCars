import logging
from threading import Thread, Event
from time import perf_counter, sleep
import numpy as np


class Engine:

    def __init__(self, step_time):
        """Initialization of the simulation engine
        
        Arguments:
            simulation_step {float} -- a time that elapse between simulation steps in seconds
        """
        self.cars = []
        self.thread = None
        self.thread_event = Event()
        self.on_simulation_step = None
        self._step_time = step_time
        self._step_count = 0
        

    @property
    def car_count(self):
        return len(self.cars)

    @property
    def on_simulation_step(self):
        return self.__on_simulation_step

    @on_simulation_step.setter
    def on_simulation_step(self, fce):
        self.__on_simulation_step = fce

    @property
    def step_count(self):
        return self._step_count

    @step_count.setter
    def step_count(self, count):
        self._step_count = count

    def clear_model(self):
        self.cars = []

    @property
    def create_model(self):
        return self.__create_model

    @create_model.setter
    def create_model(self, fce):
        self.__create_model = fce


    def add(self, car):
        self.cars.append(car)

    def summary(self, brief = False):
        """Summary of the simulation environment with the list of active objects in the simulation
        
        Keyword Arguments:
            brief {bool} -- Is the summary brief or full, brief is used for each step of the simulation (default: {False})
        """
        if not brief:
            logging.debug("Car train simulation engine")
            logging.debug("Number of cars: {}".format(self.car_count))
        for idx, car in enumerate(self.cars):
            logging.debug("\t{:2} - {}".format(idx, car))

    def restart(self):
        """Restart the simulation from start"""
        if self.thread and self.thread.is_alive():
            return
        self.step_count = 0
        self.clear_model()
        if self.__create_model:
            self.__create_model(self)
        self.on_simulation_step(self)

    def simulate(self, max_iter, delay):
        logging.info("Simulation start, max. iterations {}".format(max_iter))
        simulation_start = perf_counter()
        # simulation loop
        for iter in range(max_iter):
            # simulation step procedure
            step_start = perf_counter()
            for car in self.cars:
                car.move(self._step_time, self.cars)
            logging.debug("Iteration {}".format(iter))

            self.summary(True)
            # call connected procedure
            if self.on_simulation_step:
                self.on_simulation_step(self.cars)

            step_stop = perf_counter()
            step_duration = step_stop-step_start
            # wait for the next step for defined amount fo time
            if self.thread_event.wait(0)==True:
                break

            if step_duration<delay:
                sleep(delay-step_duration)
            
            self.step_count += 1

        simulation_stop = perf_counter()
        logging.info("Simulation taken {:0.2f}s".format(simulation_stop-simulation_start))


    def run(self, max_iter = 100, delay = 0.0):
        if not self.thread or not self.thread.is_alive():
            self.thread_event.clear()
            self.thread = Thread(target=self.simulate, args=(max_iter, delay))
            self.thread.daemon = True
            self.thread.start()

    # set the event to tell the running thread that it should be interrupted
    def interrupt(self):
        self.thread_event.set()
