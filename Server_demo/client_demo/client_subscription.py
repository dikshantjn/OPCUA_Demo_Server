import time
import asyncio
import logging

from asyncua import Client, Node, ua
from asyncua.ua.uatypes import NodeId

import opc_vars


for i in range(0, len(opc_vars.in_setup_data)):
    for j in range(0, len(opc_vars.out_setup_data)):
        if opc_vars.in_setup_data[i][0][4:] == opc_vars.out_setup_data[j][0][3:]:
            print(f"-- IN : {opc_vars.in_setup_data[i][0]} == {opc_vars.out_setup_data[j][0]} -- OUT === {i} : {j}")