"""
this is where the canbus data will be collected formatted and sent
"""

import utils.ConsoleLog as logging
import const
import can
import binascii
from datetime import datetime
class canData(object):

    ID = None
    DATA=None

    #* allows me to configure canbus globally 
    def configureCanBus(self):

        logging.Warning("Configureing canbus UwU~...")
        const.CAN0 = can.interface.Bus(channel='can0', bustype='socketcan_ctypes', notifier = can.Notifier(const.CAN0, const.CAN0, timeout=.5))  # pylint: disable=unused-variable
        logging.PipeLine_Ok("Configured Canbus Succesfully...")

    #* allows me to grab data from the can bus 
    def runDataCollection(self):
        
        logging.info("Starting to Collect data from the can bus...")
        while True:
            msg = const.CAN0.recv(timeout=0.5)

        # watch dog for program
            if(msg == None):
                const.heartbeat += 1
                logging.PipeLine_Ok("Wating for Canbus to send messages..")
                logging.Warning("hartbeet:"+str(const.heartbeat ))
            else:
                # Formats the data into the correct ids ie:(0x123) format 
                self.ID = '0x{0:0{1}X}'.format(msg.arbitration_id, 8 if msg.is_extended_id else 3)
                self.DATA = (binascii.hexlify(msg.data))

            #Saves all files and exiteds program
            if(const.heartbeat == 10):
                logging.PipeLine_Ok('Stopped Recving messages succesfully..')
                logging.Error("WATCHDOG OVER RUN QUITTING PROGRAM...")
                logging.Error("good by Program is Ready to die")
                const.CAN0.shutdown()
                break

            
    

    # this is for relaying data from the canbus to the zmq socket
    def send_packetInfo(self,sender,id,data,time):
        logging.Warning("Sending canbus info to Zmq SSocket...")
        sender.send_string("CANBUS")

        #*  can bytes  "byte 1"+ str(data[0:2])+ " byte 2"+ str(data[2:4])+ "byte 3"+ str(data[4:6])+ "byte 4"+ str(data[6:8])+ "byte 5"+str(data[8:10])+"byte 6" + str(data[10:12])+"byte 7" + str(data[12:14])+"byte 8" + str(data[14:16])
        #! Json Data layout id, canbusdata, time
        sender.send_json(
            {
                "id": str(id),

                "data": {
                    "byte1":data[0:2],
                    "byte2":data[2:4],
                    "byte3":data[4:6],
                    "byte4":data[6:8],
                    "byte5":data[8:10],
                    "byte6":data[10:12],
                    "byte7":data[12:14],
                    "byte8":data[14:16],
                },
                    
                "time": str(datetime.now),
            }
        )
        logging.PipeLine_Ok("Sent data canbus data over the zmq socket ")


