# Class Structure

# SERVER ---



# RCS Client ---

# TODO 1: Init All Raft IN_SETUP_DATA

# TODO 2: Check all free RAFTS and get the one closest to task start point

# TODO 3: 

# seperate classes for inbound and outbound data? or just using methods?


# RAFT Client ---


# IN-stup-dat and out-setup-data
import asyncio
from asyncua import Client, ua

class Robot:
    def __init__(self, robot_id):
        # Initialize OPC UA client
        self.client = Client(url="opc.tcp://localhost:4840/freeopcua/server/")
        self.robot_id = robot_id

    async def handle_task(self, task_details):
        # Create list of subtasks
        subtasks = self.create_subtasks(task_details)

        # Subscribe to OPC UA server
        await self.client.connect()
        nodes = await self.subscribe_to_nodes(subtasks)

        # Execute subtasks
        for i, subtask in enumerate(subtasks):
            node = nodes[i]
            await self.execute_subtask(subtask, node)

        # Unsubscribe from OPC UA server
        await self.unsubscribe_from_nodes(nodes)
        await self.client.disconnect()

    def create_subtasks(self, task_details):
        # Create list of subtasks based on input data
        subtasks = []
        for i in range(task_details["batch_size"]):
            subtask = {
                "id": task_details["id"] + "_" + str(i),
                "robot_id": self.robot_id,
                "from_position": task_details["from_position"],
                "to_position": task_details["to_position"],
                "type": task_details["type"]
            }
            subtasks.append(subtask)
        return subtasks

    async def subscribe_to_nodes(self, subtasks):
        # Subscribe to OPC UA server for each subtask
        tasks = []
        for subtask in subtasks:
            node = await self.client.get_node("ns=2;s=" + subtask["id"])
            handle = node.subscribe_data_change(self.handle_data_change)
            tasks.append(handle)
        await asyncio.gather(*tasks)
        return [await self.client.get_node("ns=2;s=" + subtask["id"]) for subtask in subtasks]

    def handle_data_change(self, node, val, data):
        # Handle data change notification from OPC UA server
        print("Robot {} - Node {} value changed to {}".format(self.robot_id, node, val))

    async def execute_subtask(self, subtask, node):
        # Execute subtask using OPC UA server
        print("Robot {} - Executing subtask {}".format(self.robot_id, subtask["id"]))
        await node.write_value(subtask)

    async def unsubscribe_from_nodes(self, nodes):
        # Unsubscribe from OPC UA server for each node
        tasks = []
        for node in nodes:
            handle = node.unsubscribe()
            tasks.append(handle)
        await asyncio.gather(*tasks)

# Create Robot objects
robot1 = Robot(1)
robot2 = Robot(2)

# Define task details for each robot
task_details1 = {
    "id": "task1",
    "batch_size": 3,
    "from_position": "A",
    "to_position": "B",
    "type": "move"
}

task_details2 = {
    "id": "task2",
    "batch_size": 2,
    "from_position": "C",
    "to_position": "D",
    "type": "pickup"
}

# Handle tasks for each robot
async def main():
    await asyncio.gather(
        robot1.handle_task(task_details1),
        robot2.handle_task(task_details2),
    )

await main()
