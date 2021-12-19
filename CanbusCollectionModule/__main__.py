"""
this class is for  the main code uwU
"""

import utils.ConsoleLog as logger
import zmq
import const 
from collection import canCollection


context = zmq.Context(io_threads=4)

# inits Sender and reciver Sockets for the Module
sender = context.socket(zmq.PUB)

def main():
    #* sets up zmq to be used 
    logger.info("Starting Zmq....")
    sender.bind(const.zmq_send)

    logger.PipeLine_Ok("Started zmq Successfully!")
    logger.Warning("starting Canbus Data Collection Module.....")

    #* confirgures canbus 
    canCollection.canData.configureCanBus(canCollection.canData())

    #* runs the canbus code
    canCollection.canData.runDataCollection(canCollection.canData())

