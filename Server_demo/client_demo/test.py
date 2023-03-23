import opc_vars
import asyncio
import logging

from asyncua import Client, Node, ua
from asyncua.ua.uatypes import NodeId
# Variant class

task_input = [("WMS_STK_Task_ID_LSW", 1),
              ("WMS_STK_Task_ID_MSW",0),
              ("WMS_STK_Total_Subtasks", 2),
              ("WMS_STK_Subtask_ID_LSW", 123),
              ("WMS_STK_Subtask_ID_MSW", 0),
              ("WMS_STK_Subtask_Number", 1),
              ("WMS_STK_Instruction_Type", 6410),
              ("WMS_STK_Speed_Scale", 0),
              ("WMS_STK_Lane_Stay_Timeout_Sec", 0),
              ("WMS_STK_From_Level", 1),
              ("WMS_STK_From_Lane", 10),
              ("WMS_STK_From_Aisle", 2),
              ("WMS_STK_To_Level", 1),
              ("WMS_STK_To_Lane", 10),
              ("WMS_STK_To_Aisle", 5),
              ("WMS_STK_Pick_Pallet_Number_LSW", 0),
              ("WMS_STK_Pick_Pallet_Number_MSW", 0),
              ("WMS_STK_Aisle_Position_MM_LSW", 0),
              ("WMS_STK_Aisle_Position_MM_MSW", 0),
              ("WMS_STK_Lane_Position_MM_LSW", 4725),
              ("WMS_STK_Lane_Position_MM_MSW", 0),
              ("WMS_STK_Set_Subtask_Timeout_Sec", 120)]

class SubscriptionHandler:
     
     def __init__(self, client) -> None:
         self.client = client
    
     async def datachange_notification(self, node: Node, val, data):
        """
        Callback for asyncua Subscription.
        This method will be called when the Client received a data change message from the Server.
        """
        print(f"Data change notification => Node: {node}, value: {val}")

        node = self.client.get_node("ns=2;i=380")
        print(node)
        value = ua.Variant(True, ua.VariantType.Boolean)
        print(value)
        await node.set_value(value)

    

async def datachange_callback(subscription, data):
    print("Value changed:", data.monitored_items[0].Value.Value)
         

        


async def subscribe_variables(client, nodes):
    """
    Helper function to subscribe to a list of nodes.
    """
    handler = SubscriptionHandler(client)
    subscription = await client.create_subscription(500, handler)
    await subscription.subscribe_data_change(nodes)
    #subscription = await client.create_subscription(100, handler) 
    # sub_handler= await subscription.subscribe_data_change(nodes[0])
    # sub_handler.data_change(datachange_callback)
    # Wait for a data change notification


async def write_variable_values(client, node_ids, values):
    for i in range(len(node_ids)):
        try:
            # Get node object from node_id_string
            node = client.get_node(node_ids[i])
            # Set value to the node object
            await node.set_value(values[i])
        except Exception as e:
            print(f"Error writing value to server: {e}")


async def main():
    localhost = "127.0.0.1"
    port = "4840"
    idx = "2"

    async with Client(url=f"opc.tcp://{localhost}:{port}/freeopcua/server/") as client:
        # subscribe to input nodes WMS = ns=1;i=337
        #client.nodes.objects.get_child([f"{idx}:IN_SETUP_DATA", f"{idx}:RAFT1.{var[0]}"])

        # --- SETUP ---

        setup_in = [await client.nodes.objects.get_child([f"{idx}:IN_SETUP_DATA", f"{idx}:RAFT1.{var[0]}"]) for var in opc_vars.in_setup_data]
        setup_in_string = [node.nodeid.to_string() for node in setup_in]

        #print(in_nodes[0].nodeid.to_string()) # converts node object to string
        #await subscribe_variables(client, in_nodes)

        # subscribe to output nodes
        setup_out = [await client.nodes.objects.get_child([f"{idx}:OUT_SETUP_DATA", f"{idx}:RAFT1.{var[0]}"]) for var in opc_vars.out_setup_data]
        setup_out_string = [node.nodeid.to_string() for node in setup_out]
        # await subscribe_variables(client, out_nodes)
        setup_node_ids = {setup_in_string[i]: setup_out_string[j] for i in range(len(opc_vars.in_setup_data)) for j in range(len(opc_vars.out_setup_data)) if opc_vars.in_setup_data[i][0][4:] == opc_vars.out_setup_data[j][0][3:]}


        # ---- SUBTASK DATA ----

        subtask_in = [await client.nodes.objects.get_child([f"{idx}:IN_SUBTASK_DATA", f"{idx}:RAFT1.{var[0]}"]) for var in opc_vars.in_subtask_data]
        subtask_in_string = [node.nodeid.to_string() for node in subtask_in]

        #print(in_nodes[0].nodeid.to_string()) # converts node object to string
        #await subscribe_variables(client, in_nodes)

        # subscribe to output nodes
        subtask_out = [await client.nodes.objects.get_child([f"{idx}:OUT_SUBTASK_DATA", f"{idx}:RAFT1.{var[0]}"]) for var in opc_vars.out_subtask_data]
        subtask_out_string = [node.nodeid.to_string() for node in subtask_out]
        # await subscribe_variables(client, out_nodes)
        subtask_node_ids = {subtask_in_string[i]: subtask_out_string[j] for i in range(len(opc_vars.in_subtask_data)) for j in range(len(opc_vars.out_subtask_data)) if opc_vars.in_subtask_data[i][0][4:] == opc_vars.out_subtask_data[j][0][3:]}

        values = [value[1] for value in task_input]

        await write_variable_values(client, subtask_in_string, values)



        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())