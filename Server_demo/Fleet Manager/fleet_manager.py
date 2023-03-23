"""
This file contains the RobotManager class, which handles the subscription and write data to the server.
"""

import asyncio
from asyncua import Client
from asyncua.ua.uatypes import VariantType
from RAFT_client.robot import Robot
from config.settings import SERVER_HOST, SERVER_PORT, SERVER_NAMESPACE

TOTAL_RAFTS = 3

# class RobotManager:
#     def __init__(self, robots):
#         self.robots = robots

#     async def connect_to_server(self):
#         # create asyncua client
#         client = Client(f"opc.tcp://{SERVER_HOST}:{SERVER_PORT}/{SERVER_NAMESPACE}")
#         await client.connect()

#         # TODO: add task flow here

#         # subscribe to robot tags
#         for robot in self.robots:
#             await client.create_subscription(100, self.on_data_change).subscribe_data_change(
#                 robot.tags['location'])
#             await client.create_subscription(100, self.on_data_change).subscribe_data_change(
#                 robot.tags['status'])
#             await client.create_subscription(100, self.on_data_change).subscribe_data_change(
#                 robot.tags['task'])

#     async def on_data_change(self, node, val, data):
#         # handle data changes
#         robot = self.get_robot_by_tag(node.nodeid.Identifier)
#         if node.nodeid.Identifier.endswith('location'):
#             robot.location = val.Value
#         elif node.nodeid.Identifier.endswith('status'):
#             robot.status = val.Value
#         elif node.nodeid.Identifier.endswith('task'):
#             robot.task = val.Value

#     def get_robot_by_tag(self, tag):
#         # find robot by tag
#         for robot in self.robots:
#             if tag.startswith(robot.name):
#                 return robot


async def main():
    i=0
    robots = []
    while i in range(0,TOTAL_RAFTS):
        RAFT = Robot('opc.tcp://localhost:4840/freeopcua/server/', i+1)
        await RAFT.connect()
        robots.append(RAFT)
        i += 1
    # await robot.subscribe_nodes(['ns=1;s=Temperature', 'ns=1;s=Pressure'])
    # await robot.write_values({'ns=1;s=Temperature': 25.0, 'ns=1;s=Pressure': 101325.0})
    # # Wait for a few seconds to allow the data changes to be detected
    # await asyncio.sleep(5)
    # await robot.unsubscribe_nodes(['ns=1;s=Temperature'])
    # Wait for a few more seconds to verify that the Temperature node is no longer being monitored
    # await asyncio.sleep(5)
    # await robot.disconnect()

asyncio.run(main())

# if __name__ == '__main__':
#     # create robots
#     i=0
#     robots = []
#     while i in range(0,TOTAL_RAFTS):
#         RAFT = Robot(f"RAFT{i+1}", SERVER_HOST, SERVER_PORT )
#         robots.append(RAFT)
#         i += 1

    # create robot manager
    # manager = RobotManager(robots)

    # TODO: check if this part works --- !
    # connect to server and start event loop
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(manager.connect_to_server())
    # loop.run_forever()