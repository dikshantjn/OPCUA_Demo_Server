'''
These variables are imported into server-raft-xmlexport.py to generate a UANodeset.xml file
'''

from opcua import ua

# one set of tags for Machine Data, emitted by RAFTS on heartbeat interval
out_machine_data = [
        ("OM_MHN_Current_Mode", ua.VariantType.UInt16),
        ("OM_MHN_Current_VPos", ua.VariantType.UInt16),
        ("OM_MHN_Error", ua.VariantType.UInt16),
        ("OM_MHN_VDC_Charge", ua.VariantType.UInt16),
        ("OM_MHN_Current_Pallet_Weigh_LSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Pallet_Weigh_MSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Direction", ua.VariantType.UInt16),
        ("OM_MHN_Current_Aisle_Speed_Min", ua.VariantType.UInt16),
        ("OM_MHN_Current_Aisle_Pos_LSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Aisle_Pos_MSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Lane_Speed_Min", ua.VariantType.UInt16),
        ("OM_MHN_Current_Lane_Pos_LSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Lane_Pos_MSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Level", ua.VariantType.UInt16),
        ("OM_MHN_Current_Lane", ua.VariantType.UInt16),
        ("OM_MHN_Current_Aisle", ua.VariantType.UInt16),
        ("OM_MHN_Current_Position_Type", ua.VariantType.UInt16),
        ("OM_MHN_Current_Pallet_Number_LSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Pallet_Number_MSW", ua.VariantType.UInt16),
        ("OM_MHN_Current_Pallet_Type", ua.VariantType.UInt16),
        ("OM_MHN_Current_Temperature", ua.VariantType.UInt16),
        ("OM_MHN_Serial_Number", ua.VariantType.UInt16),
        ("OM_MHN_Mole_Number", ua.VariantType.UInt16),
        ("OM_MHN_Operational_Hours", ua.VariantType.UInt16),
        ("OM_MHN_Lane_Drive_Error_Code", ua.VariantType.UInt16),
        ("OM_MHN_Aisle_Drive_Error_Code", ua.VariantType.UInt16),
        ("OM_MHN_Lift_Drive_Error_Code", ua.VariantType.UInt16),
        ("OM_MHN_Heart_Beat_Value", ua.VariantType.UInt16),
        ("OM_MHN_Pallet_Drop_Off_Position_LSW", ua.VariantType.UInt16),
        ("OM_MHN_Pallet_Drop_Off_Position_MSW", ua.VariantType.UInt16)
]

in_subtask_assign = [
        ("WMS_STK_Subtask_Ready", ua.VariantType.Boolean),
        ("WMS_STK_Subtask_Update_Ready", ua.VariantType.Boolean), # Optional
        ("WMS_STK_Begin_Subtask", ua.VariantType.Boolean),
        ("WMS_STK_Cancel_Subtask", ua.VariantType.Boolean),
        ("WMS_STK_Subtask_Complete_Ack", ua.VariantType.Boolean),
        ("WMS_STK_Subtask_Incomplete_Ack", ua.VariantType.Boolean),
        ("WMS_STK_Manual_Task_EN", ua.VariantType.Boolean),
        ("WMS_Complete_Instr_in_Lane", ua.VariantType.Boolean), # Optional
        ("WMS_STK_Interlock_Mode", ua.VariantType.Boolean),
]

# 22 Attributes Sent to RAFT before WMS sets 'WMS_STK_BEGIN_SUBTASK' to True, to proceed with a Subtask
in_subtask_data = [
        ("WMS_STK_Task_ID_LSW", ua.VariantType.UInt16),
        ("WMS_STK_Task_ID_MSW", ua.VariantType.UInt16),
        ("WMS_STK_Total_Subtasks", ua.VariantType.UInt16),
        ("WMS_STK_Subtask_ID_LSW", ua.VariantType.UInt16),
        ("WMS_STK_Subtask_ID_MSW", ua.VariantType.UInt16),
        ("WMS_STK_Subtask_Number", ua.VariantType.UInt16),
        ("WMS_STK_Instruction_Type", ua.VariantType.UInt16),
        ("WMS_STK_Speed_Scale", ua.VariantType.UInt16),
        ("WMS_STK_Lane_Stay_Timeout_Sec", ua.VariantType.UInt16),
        ("WMS_STK_From_Level", ua.VariantType.UInt16),
        ("WMS_STK_From_Lane", ua.VariantType.UInt16),
        ("WMS_STK_From_Aisle", ua.VariantType.UInt16),
        ("WMS_STK_To_Level", ua.VariantType.UInt16),
        ("WMS_STK_To_Lane", ua.VariantType.UInt16),
        ("WMS_STK_To_Aisle", ua.VariantType.UInt16),
        ("WMS_STK_Pick_Pallet_Number_LSW", ua.VariantType.UInt16),
        ("WMS_STK_Pick_Pallet_Number_MSW", ua.VariantType.UInt16),
        ("WMS_STK_Aisle_Position_MM_LSW", ua.VariantType.UInt16),
        ("WMS_STK_Aisle_Position_MM_MSW", ua.VariantType.UInt16),
        ("WMS_STK_Lane_Position_MM_LSW", ua.VariantType.UInt16),
        ("WMS_STK_Lane_Position_MM_MSW", ua.VariantType.UInt16),
        ("WMS_STK_Set_Subtask_Timeout_Sec", ua.VariantType.UInt16, 120)
]

out_subtask_assign = [
        ("OM_STK_Request_Subtask", ua.VariantType.Boolean),
        ("OM_STK_Request_Subtask_Update", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Assigned", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Begin_Ack", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Cancel_Ack", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Busy", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Complete", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Incomplete", ua.VariantType.Boolean),
        ("OM_STK_Subtask_Concluded", ua.VariantType.Boolean),
        ("OM_STK_Manual_Task_EN_Ack", ua.VariantType.Boolean),
        ("OM_STK_Subtask_State", ua.VariantType.UInt16),
        ("OM_STK_Current_Subtask_Timeout", ua.VariantType.UInt16),
        ("OM_STK_New_Subtask_Timeout_Sec", ua.VariantType.UInt16),
        ("OM_STK_Timer_Sec", ua.VariantType.UInt16)
]

out_subtask_data = [
        ("OM_STK_Task_ID_LSW", ua.VariantType.UInt16),
        ("OM_STK_Task_ID_MSW", ua.VariantType.UInt16),
        ("OM_STK_Total_Subtasks", ua.VariantType.UInt16),
        ("OM_STK_Subtask_Number", ua.VariantType.UInt16),
        ("OM_STK_Subtask_ID_LSW", ua.VariantType.UInt16),
        ("OM_STK_Subtask_ID_MSW", ua.VariantType.UInt16),
        ("OM_STK_Instruction_Type", ua.VariantType.UInt16),
        ("OM_STK_Speed_Scale", ua.VariantType.UInt16),
        ("OM_STK_Lane_Stay_Timeout_Sec", ua.VariantType.UInt16),
        ("OM_STK_From_Level", ua.VariantType.UInt16),
        ("OM_STK_From_Lane", ua.VariantType.UInt16),
        ("OM_STK_From_Aisle", ua.VariantType.UInt16),
        ("OM_STK_To_Level", ua.VariantType.UInt16),
        ("OM_STK_To_Lane", ua.VariantType.UInt16),
        ("OM_STK_To_Aisle", ua.VariantType.UInt16),
        ("OM_STK_Pick_Pallet_Number_LSW", ua.VariantType.UInt16),
        ("OM_STK_Pick_Pallet_Number_MSW", ua.VariantType.UInt16),
        ("OM_STK_Aisle_Position_MM_LSW", ua.VariantType.UInt16),
        ("OM_STK_Aisle_Position_MM_MSW", ua.VariantType.UInt16),
        ("OM_STK_Lane_Position_MM_LSW", ua.VariantType.UInt16),
        ("OM_STK_Lane_Position_MM_MSW", ua.VariantType.UInt16),
        ("OM_STK_Subtask_Timeout_Sec", ua.VariantType.UInt16),
        ("OM_STK_Subtask_Incomplete_Data", ua.VariantType.UInt16)
]

in_setup_data = [
        ("WMS_SET_Aisle_Alignment_Timeout_sec", ua.VariantType.UInt16),
        ("WMS_SET_Aisle_Flag_Hunting_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Aisle_Travel_Accel_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Aisle_Travel_Decel_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Auto_Subtask_Between_Subtask_Timeout_sec", ua.VariantType.UInt16),
        ("WMS_SET_Auto_Subtask_Self_Conclude_Timeout_sec", ua.VariantType.UInt16),
        ("WMS_SET_Factory_Reset", ua.VariantType.Boolean),
        ("WMS_SET_Lane_Alignment_Timeout_sec", ua.VariantType.UInt16),
        ("WMS_SET_Lane_Flag_Hunting_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Lane_Travel_Accel_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Lane_Travel_Decel_Distance_mm", ua.VariantType.UInt16),
        ("WMS_SET_Manual_Command_Timeout_sec", ua.VariantType.UInt16),
        ("WMS_SET_Manual_Gen_TaskID", ua.VariantType.Boolean),
        ("WMS_SET_Manual_Max_Speed_Percentage", ua.VariantType.UInt16),
        ("WMS_SET_Manual_Response_Poll_Time_sec", ua.VariantType.UInt16),
        ("WMS_SET_Save_Settings", ua.VariantType.Boolean),
        ("WMS_SET_Startup_State", ua.VariantType.UInt16)
]

out_setup_data = [
        ("OM_SET_Aisle_Alignment_Timeout_sec", ua.VariantType.UInt16),
        ("OM_SET_Aisle_Flag_Hunting_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Aisle_Travel_Accel_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Aisle_Travel_Decel_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Lane_Travel_Accel_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Lane_Travel_Decel_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Lane_Alignment_Timeout_sec", ua.VariantType.UInt16),
        ("OM_SET_Lane_Flag_Hunting_Distance_mm", ua.VariantType.UInt16),
        ("OM_SET_Manual_Command_Timeout_sec", ua.VariantType.UInt16),
        ("OM_SET_Manual_Gen_TaskID", ua.VariantType.Boolean),
        ("OM_SET_Manual_Max_Speed_Percentage", ua.VariantType.UInt16),
        ("OM_SET_Manual_Response_Poll_Time_sec", ua.VariantType.UInt16),
        ("OM_SET_Startup_State", ua.VariantType.UInt16),
        ("OM_SET_Auto_Subtask_Between_Subtask_Timeout_sec", ua.VariantType.UInt16),
        ("OM_SET_Auto_Subtask_Self_Conclude_Timeout_sec", ua.VariantType.UInt16)
]

in_critical_data = [
        ("WMS_CRT_Charge_Complete", ua.VariantType.Boolean),
        ("WMS_CRT_Cstop", ua.VariantType.Boolean),
        ("WMS_CRT_Estop", ua.VariantType.Boolean),
        ("WMS_CRT_GoTo_AutoMode", ua.VariantType.Boolean),
        ("WMS_CRT_GoTo_ManualMode", ua.VariantType.Boolean),
        ("WMS_CRT_GoTo_SetupMode", ua.VariantType.Boolean),
        ("WMS_CRT_Low_Power_State", ua.VariantType.Boolean),
        ("WMS_CRT_M_Reset", ua.VariantType.Boolean),
        ("WMS_CRT_Status_Ack", ua.VariantType.Boolean)
]

out_raw_data = [
        ("OM_ENC_Travel_AIS_Raw_LSW", ua.VariantType.UInt16),
        ("OM_ENC_Travel_AIS_Raw_MSW", ua.VariantType.UInt16),
        ("OM_ENC_Travel_LAN_Raw_LSW", ua.VariantType.UInt16),
        ("OM_ENC_Travel_LAN_Raw_MSW", ua.VariantType.UInt16),
        ("OM_OUT_Drive_ATR_Enable", ua.VariantType.Boolean),
        ("OM_OUT_Drive_KSI", ua.VariantType.Boolean),
        ("OM_OUT_Drive_LIF_Enable", ua.VariantType.Boolean),
        ("OM_OUT_Drive_LTR_Enable", ua.VariantType.Boolean),
        ("OM_OUT_Gener_CHG_Test", ua.VariantType.Boolean),
        ("OM_OUT_Light_GRN", ua.VariantType.Boolean),
        ("OM_OUT_Light_RED", ua.VariantType.Boolean),
        ("OM_OUT_Light_Siren", ua.VariantType.Boolean),
        ("OM_OUT_Light_YEL", ua.VariantType.Boolean),
        ("OM_SEN_Gener_CHG_Contact", ua.VariantType.Boolean),
        ("OM_SEN_Induc_LIF_Bottom", ua.VariantType.Boolean),
        ("OM_SEN_Induc_LIF_Middle", ua.VariantType.Boolean),
        ("OM_SEN_Induc_LIF_Top", ua.VariantType.Boolean),
        ("OM_SEN_Photo_AAL_Front_GRN", ua.VariantType.Boolean),
        ("OM_SEN_Photo_AAL_Front_Red", ua.VariantType.Boolean),
        ("OM_SEN_Photo_AAL_Rear_GRN", ua.VariantType.Boolean),
        ("OM_SEN_Photo_AAL_Rear_Red", ua.VariantType.Boolean),
        ("OM_SEN_Photo_EOR_Front", ua.VariantType.Boolean),
        ("OM_SEN_Photo_EOR_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Photo_LAL_Green_FNT", ua.VariantType.Boolean),
        ("OM_SEN_Photo_LAL_Green_RER", ua.VariantType.Boolean),
        ("OM_SEN_Photo_LAL_Red_FNT", ua.VariantType.Boolean),
        ("OM_SEN_Photo_LAL_Red_RER", ua.VariantType.Boolean),
        ("OM_SEN_Photo_PIP_Front", ua.VariantType.Boolean),
        ("OM_SEN_Photo_PIP_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Photo_REF_Green", ua.VariantType.Boolean),
        ("OM_SEN_Photo_REF_Red", ua.VariantType.Boolean),
        ("OM_SEN_Photo_SDW_Front", ua.VariantType.Boolean),
        ("OM_SEN_Photo_SDW_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Photo_SPC_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Photo_VAR_Green", ua.VariantType.Boolean),
        ("OM_SEN_Photo_VAR_Red", ua.VariantType.Boolean),
        ("OM_SEN_Safe_COL_Front", ua.VariantType.Boolean),
        ("OM_SEN_Safe_COL_Green", ua.VariantType.Boolean),
        ("OM_SEN_Safe_COL_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Safe_COL_Red", ua.VariantType.Boolean),
        ("OM_SEN_Safe_EST_Front", ua.VariantType.Boolean),
        ("OM_SEN_Safe_EST_Rear", ua.VariantType.Boolean),
        ("OM_SEN_Safe_INL_Estop", ua.VariantType.Boolean)
]

in_interlock_data = [
        ("WMS_ILK_Current_Interlock_Step", ua.VariantType.UInt16),
        ("WMS_ILK_Interlock_SD_Config", ua.VariantType.UInt16),
        ("WMS_ILK_Interlock_Stop_Config", ua.VariantType.UInt16),
        ("WMS_ILK_Area_Departure_Release", ua.VariantType.Boolean),
        ("WMS_ILK_Area_Entry_Release", ua.VariantType.Boolean),
        ("WMS_ILK_Interlock_Reverse_Events", ua.VariantType.Boolean),
        ("WMS_ILK_Machine_Tool_Complete", ua.VariantType.Boolean),
        ("WMS_ILK_Machine_Tool_Release", ua.VariantType.Boolean),
        ("WMS_ILK_OM_Tool_Request", ua.VariantType.Boolean)
]

out_interlock_data = [
        ("OM_ILK_Area_Departure_Request", ua.VariantType.Boolean),
        ("OM_ILK_Area_Entry_Request", ua.VariantType.Boolean),
        ("OM_ILK_Area_Occupied", ua.VariantType.Boolean),
        ("OM_ILK_Interlock_Complete", ua.VariantType.Boolean),
        ("OM_ILK_Machine_Tool_Request", ua.VariantType.Boolean),
        ("OM_ILK_Tool_Complete", ua.VariantType.Boolean),
        ("OM_ILK_Tool_Release", ua.VariantType.Boolean),
        ("OM_ILK_Current_Interlock_Step", ua.VariantType.UInt16),
        ("OM_ILK_Interlock_SD_Sensor", ua.VariantType.UInt16),
        ("OM_ILK_Interlock_Stop_Sensor", ua.VariantType.UInt16)
]

out_battery_data = [
        ("OM_BAT_Voltage", ua.VariantType.UInt16),
        ("OM_BAT_Cells_Max_Temp", ua.VariantType.UInt16),
        ("OM_BAT_Charge_Current_Limit", ua.VariantType.UInt16),
        ("OM_BAT_Charge_Voltage_Limit", ua.VariantType.UInt16),
        ("OM_BAT_Current", ua.VariantType.UInt16),
        ("OM_BAT_Current_Dir", ua.VariantType.UInt16),
        ("OM_BAT_SOC", ua.VariantType.UInt16)
]

opc_charge_send = [
        ("WMS_Charge_Time", ua.VariantType.Int32),
        ("WMS_Charge_to_Level", ua.VariantType.UInt16),
        ("WMS_OM_Number", ua.VariantType.UInt16),
        ("WMS_StartCharging", ua.VariantType.UInt16),
        ("WMS_StopCharging", ua.VariantType.UInt16)
]

opc_charge_recv = [
        ("OM_ChargeLevel", ua.VariantType.UInt16),
        ("OM_Charge_Complete", ua.VariantType.Boolean),
        ("OM_ChargerState", ua.VariantType.UInt16),
        ("OM_Current_OM_Number", ua.VariantType.UInt16),
        ("OM_Location_Level", ua.VariantType.UInt16),
        ("OM_Safe_to_Move", ua.VariantType.Boolean),
        ("OM_Station_Available", ua.VariantType.Boolean),
        ("OM_Station_Charging", ua.VariantType.Boolean),
        ("OM_Time_Remaining", ua.VariantType.Int32)
]

misc = [
        ("WMS_WRITEBACK", ua.VariantType.UInt16),
        ("OM_READBACK", ua.VariantType.UInt16),
        ("OM_Comm_OK", ua.VariantType.Boolean),
        ("OM_LastHB", ua.VariantType.UInt16)
]