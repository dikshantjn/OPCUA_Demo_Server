import sys
sys.path.insert(0, "..")
import os
# os.environ['PYOPCUA_NO_TYPO_CHECK'] = 'True'

import time
import asyncio
import logging

from asyncua import Client, Node, ua
# from asyncua.ua import ObjectIds
from asyncua.ua.uatypes import NodeId

# Docker logical id
#localhost = "server"
localhost = "127.0.0.1"
port = "4840"

# logging.basicConfig(level=logging.INFO)
# _logger = logging.getLogger('asyncua')
_logger = logging.getLogger(__name__)


class SubscriptionHandler:
    """
    The SubscriptionHandler is used to handle the data that is received for the subscription.
    """
    def datachange_notification(self, node: Node, val, data):
        """
        Callback for asyncua Subscription.
        This method will be called when the Client received a data change message from the Server.
        """
        _logger.info('datachange_notification %r %s', node, val)


async def main():
    """
    Main task of this Client-Subscription example.
    """
    handler = SubscriptionHandler()
    # wait for server to load
    time.sleep(5)

    while True:
        
        client = Client(url=f"opc.tcp://{localhost}:{port}/freeopcua/server/")
        
        #: Server state node address for keep-alive checks
        _SERVER_STATE = NodeId(ua.ObjectIds.Server_ServerStatus_State)
        _logger.warning(f"Server State is {_SERVER_STATE}")

        idx = "2"

        ''' NOTE THESE .get_namespace_index() methods are ARE NOT WORKING 
        # idx = await client.get_namespace_index(uri="http://examples.freeopcua.github.io")

        try:
            uri = "http://gosrsi.com"
            idx = await client.get_namespace_index(uri)
            print(f"idx is {idx}")   
        except(AttributeError, ua.UaError):
            _logger.warning("Attribute Error")
            print(ua.UaError)
            await asyncio.sleep(2)
        '''
            
        try:
            async with client:
                
                _logger.warning("Connected")

                # var1 = await client.nodes.objects.get_child([f"{idx}:OUT_MACHINE_DATA", f"{idx}:RAFT1.OM_MHN_Heart_Beat_Value"])
                # var2 = await client.nodes.objects.get_child([f"{idx}:OUT_MACHINE_DATA", f"{idx}:RAFT1.OM_MHN_Current_Mode"]) 
                var3 = await client.nodes.objects.get_child([f"{idx}:IN_SETUP_DATA", f"{idx}:RAFT1.WMS_SET_Manual_Max_Speed_Percentage"])
                
                # Test format to get Node by ID using convention  NodeId="ns=1;i=1137"
                
                # We create a Client Subscription.
                subscription = await client.create_subscription(500, handler)
                nodes = [
                    # var1, 
                    # var2,
                    var3
                    # client.get_node(ua.ObjectIds.Server_ServerStatus_CurrentTime),
                ]

                print(f"Value for var3 Client RCS : {var3}")
                # We subscribe to data changes for two nodes (variables).
                # print(f"Have nodes, will subscribe to {nodes}")
                await subscription.subscribe_data_change(nodes)
                # keep checking connection, every 1 second, throw error and reconnect if lost
                #while True:
                #    await asyncio.sleep(1)
                #    await client.check_connection()

                        # We let the subscription run for ten seconds
                await asyncio.sleep(120)
                # We delete the subscription (this un-subscribes from the data changes of the two variables).
                # This is optional since closing the connection will also delete all subscriptions.
                await subscription.delete()
                # After one second we exit the Client context manager - this will close the connection.
                await asyncio.sleep(1)

        except(ConnectionError, ua.UaError):
            _logger.warning("Reconnecting in 2 seconds")
            await asyncio.sleep(2)

        

        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
