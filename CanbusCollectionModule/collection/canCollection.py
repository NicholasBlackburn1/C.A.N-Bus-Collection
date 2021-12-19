"""
this is where the canbus data will be collected formatted and sent
"""

import utils.ConsoleLog as logging
import const
import can
import binascii

class canData(object):

    ID = None
    DATA=None

    #* allows me to configure canbus globally 
    def configureCanBus(self):

        logging.Warning("Configureing canbus UwU~...")
        const.CAN0 = can.interface.Bus(channel='can0', bustype='socketcan_ctypes', notifier = can.Notifier(const.CAN0, const.CAN0, timeout=.5))  # pylint: disable=unused-variable
        logging.PipeLine_Ok("Configured Canbus Succesfully...")

    #* allows me to grab data from the can bus 
    def grabData(self):
        
        while True:
            msg = const.CAN0.recv(timeout=0.5)

        # watch dog for program
            if(msg == None):
                const.heartbeat += 1
                logging.Warning("hartbeet:"+str(const.heartbeat ))
            else:
                # Formats the data into the correct ids ie:(0x123) format 
                self.ID = '0x{0:0{1}X}'.format(msg.arbitration_id, 8 if msg.is_extended_id else 3)
                self.DATA = (binascii.hexlify(msg.data))

            #Saves all files and exiteds program
            if(const.heartbeat == 10):
                logging.Error("WATCHDOG OVER RUN QUITTING PROGRAM...")
                
                logging.Error("good by Program is Ready to die")
                const.CAN0.shutdown()
                break


