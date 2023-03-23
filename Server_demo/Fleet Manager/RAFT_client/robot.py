import asyncio
from asyncua import Client, Node

class Robot:
    def __init__(self, url, name):
        self.name = f"RAFT{name}"
        self.url = url
        self.client = None
        self.nodes = {}

    async def connect(self):
        self.client = Client(self.url)
        await self.client.connect()
        print(f"Connected to {self.name}")

    async def disconnect(self):
        await self.client.disconnect()

    async def subscribe_nodes(self, node_ids):
        for node_id in node_ids:
            node = await self.client.nodes.find(node_id)
            self.nodes[node_id] = node
            node.add_data_change_callback(self.handle_data_change)

    async def unsubscribe_nodes(self, node_ids):
        for node_id in node_ids:
            node = self.nodes.get(node_id)
            if node is not None:
                node.remove_data_change_callback(self.handle_data_change)
                del self.nodes[node_id]

    async def handle_data_change(self, node, val, data):
        print(f'{node} value changed to {val}')

    async def write_values(self, values):
        for node_id, value in values.items():
            node = self.nodes.get(node_id)
            if node is None:
                node = await self.client.nodes.find(node_id)
                self.nodes[node_id] = node
            await node.write_value(value)