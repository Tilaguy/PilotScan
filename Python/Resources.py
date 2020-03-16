import rospy
from diagnostic_msgs.msg import DiagnosticArray
from diagnostic_msgs.msg import DiagnosticStatus
from diagnostic_msgs.msg import KeyValue
from sensor_msgs.msg import Temperature

class listener:
    def __init__(self):
        self.cont = 0
        self.talker()

    def CPUmonitor(self,data):

        pub_T0 = rospy.Publisher('Resources/Core/0/Temperature', Temperature, queue_size=10)
        pub_T1 = rospy.Publisher('Resources/Core/1/Temperature', Temperature, queue_size=10)
        pub_T2 = rospy.Publisher('Resources/Core/2/Temperature', Temperature, queue_size=10)
        pub_T3 = rospy.Publisher('Resources/Core/3/Temperature', Temperature, queue_size=10)
        msg_T0 = Temperature()
        msg_T1 = Temperature()
        msg_T2 = Temperature()
        msg_T3 = Temperature()

        array_info = DiagnosticArray()

        pub_idle = rospy.Publisher('Resources/Core/Idle', DiagnosticArray, queue_size=10)
        msg_Idle0 = DiagnosticStatus()
        msg_Idle1 = DiagnosticStatus()
        msg_Idle2 = DiagnosticStatus()
        msg_Idle3 = DiagnosticStatus()

        pub_HDD = rospy.Publisher('Resources/HDD', DiagnosticArray, queue_size=10)
        msg_Disk = DiagnosticStatus()

        pub_RAM = rospy.Publisher('Resources/RAM', DiagnosticArray, queue_size=10)
        msg_RAM_Phy = DiagnosticStatus()
        msg_RAM_swap = DiagnosticStatus()

        msg_T0.header.stamp = rospy.Time.now()
        msg_T1.header.stamp = rospy.Time.now()
        msg_T2.header.stamp = rospy.Time.now()
        msg_T3.header.stamp = rospy.Time.now()

        array_info.header.stamp = rospy.Time.now()


        #print 'dato1'
        nombre = data.status[0].name
        if nombre == "CPU Temperature (NUC)":
            # print nombre
            # Update_status_CPU = data.status[0].values[0].key
            # valor_Update_status_CPU = data.status[0].values[0].value
            # print Update_status_CPU,"=" , valor_Update_status_CPU
            # Time_Since_Update_CPU = data.status[0].values[1].key
            # valor_Time_Since_Update_CPU = data.status[0].values[1].value
            # print Time_Since_Update_CPU, "=", valor_Time_Since_Update_CPU
            Core_0_Temperature_CPU = data.status[0].values[2].key
            valor_Core_0_Temperature_CPU = data.status[0].values[2].value
            # print Core_0_Temperature_CPU, "=", valor_Core_0_Temperature_CPU
            Core_1_Temperature_CPU = data.status[0].values[3].key
            valor_Core_1_Temperature_CPU = data.status[0].values[3].value
            # print Core_1_Temperature_CPU, "=", valor_Core_1_Temperature_CPU
            Core_2_Temperature_CPU = data.status[0].values[4].key
            valor_Core_2_Temperature_CPU = data.status[0].values[4].value
            # print Core_2_Temperature_CPU, "=", valor_Core_2_Temperature_CPU
            Core_3_Temperature_CPU = data.status[0].values[5].key
            valor_Core_3_Temperature_CPU = data.status[0].values[5].value
            # print Core_3_Temperature_CPU, "=", valor_Core_3_Temperature_CPU
            # Update_status_CPUU = data.status[1].values[0].key
            # valor_Update_status_CPUU = data.status[1].values[0].value
            # print Update_status_CPUU,"=" , valor_Update_status_CPUU
            # Time_Since_Update_CPUU = data.status[1].values[1].key
            # valor_Time_Since_Update_CPUU = data.status[1].values[1].value
            # print Time_Since_Update_CPUU,"=" , valor_Time_Since_Update_CPUU
            # Core_0_Clock_Speed_CPUU = data.status[1].values[2].key
            # valor_Core_0_Clock_Speed_CPUU = data.status[1].values[2].value
            # print Core_0_Clock_Speed_CPUU,"=" , valor_Core_0_Clock_Speed_CPUU
            # Core_1_Clock_Speed_CPUU = data.status[1].std_msgsvalues[3].key
            # valor_Core_1_Clock_Speed_CPUU = data.status[1].values[3].value
            # print Core_1_Clock_Speed_CPUU,"=" , valor_Core_1_Clock_Speed_CPUU
            # Core_2_Clock_Speed_CPUU = data.status[1].values[4].key
            # valor_Core_2_Clock_Speed_CPUU = data.status[1].values[4].value
            # print Core_2_Clock_Speed_CPUU , "=" , valor_Core_2_Clock_Speed_CPUU
            # Core_3_Clock_Speed_CPUU = data.status[1].values[5].key
            # valor_Core_3_Clock_Speed_CPUU = data.status[1].values[5].value
            # print Core_3_Clock_Speed_CPUU,"=" , valor_Core_3_Clock_Speed_CPUU
            # Core_0_Status_CPUU = data.status[1].values[6].key
            # valor_Core_0_Status_CPUU  = data.status[1].values[6].value
            # print Core_0_Status_CPUU ,"=" , valor_Core_0_Status_CPUU
            # Core_0_User_CPUU = data.status[1].values[7].key
            # valor_Core_0_User_CPUU = data.status[1].values[7].value
            # Core_0_Nice_CPUU = data.status[1].values[8].key
            # print Core_0_User_CPUU,"=" , valor_Core_0_User_CPUU
            # valor_Core_0_Nice_CPUU  = data.status[1].values[8].value
            # print Core_0_Nice_CPUU ,"=" , valor_Core_0_Nice_CPUU
            # Core_0_System_CPUU = data.status[1].values[9].key
            # valor_Core_0_System_CPUU = data.status[1].values[9].value
            # print Core_0_System_CPUU,"=" , valor_Core_0_System_CPUU
            Core_0_Idle_CPUU = data.status[1].values[10].key
            valor_Core_0_Idle_CPUU = data.status[1].values[10].value
            # print Core_0_Idle_CPUU,"=" , valor_Core_0_Idle_CPUU
            # Core_1_Status_CPUU = data.status[1].values[11].key
            # valor_Core_1_Status_CPUU = data.status[1].values[11].value
            # print Core_1_Status_CPUU,"=" , valor_Core_1_Status_CPUU
            # Core_1_User_CPUU = data.status[1].values[12].key
            # valor_Core_1_User_CPUU = data.status[1].values[12].value
            # print Core_1_User_CPUU,"=" , valor_Core_1_User_CPUU
            # Core_1_Nice_CPUU = data.status[1].values[13].key
            # valor_Core_1_Nice_CPUU = data.status[1].values[13].value
            # print Core_1_Nice_CPUU,"=" , valor_Core_1_Nice_CPUU
            # Core_1_System_CPUU = data.status[1].values[14].key
            # valor_Core_1_System_CPUU = data.status[1].values[14].value
            Core_1_Idle_CPUU = data.status[1].values[15].key
            valor_Core_1_Idle_CPUU = data.status[1].values[15].value
            # print Core_1_Idle_CPUU,"=" , valor_Core_1_Idle_CPUU
            # Core_2_Status_CPUU = data.status[1].values[16].key
            # valor_Core_2_Status_CPUU = data.status[1].values[16].value
            # print valor_Core_2_Status_CPUU,"=" , valor_Core_2_Status_CPUU
            # Core_2_User_CPUU = data.status[1].values[17].key
            # valor_Core_2_User_CPUU = data.status[1].values[17].value
            # print Core_2_User_CPUU,"=" , valor_Core_2_User_CPUU
            # Core_2_Nice_CPUU = data.status[1].values[18].key
            # valor_Core_2_Nice_CPUU = data.status[1].values[18].value
            # print Core_2_Nice_CPUU,"=" , valor_Core_2_Nice_CPUU
            # Core_2_System_CPUU = data.status[1].values[19].key
            # valor_Core_2_System_CPUU = data.status[1].values[19].value
            # print Core_2_System_CPUU,"=" , valor_Core_2_System_CPUU
            Core_2_Idle_CPUU = data.status[1].values[20].key
            valor_Core_2_Idle_CPUU = data.status[1].values[20].value
            # print Core_2_Idle_CPUU,"=" , valor_Core_2_Idle_CPUU
            # Core_3_Status_CPUU = data.status[1].values[21].key
            # valor_Core_3_Status_CPUU = data.status[1].values[21].value
            # print Core_3_Status_CPUU,"=" , valor_Core_3_Status_CPUU
            # Core_3_User_CPUU = data.status[1].values[22].key
            # valor_Core_3_User_CPUU = data.status[1].values[22].value
            # print Core_3_User_CPUU,"=" , valor_Core_3_User_CPUU
            # Core_3_Nice_CPUU = data.status[1].values[23].key
            # valor_Core_3_Nice_CPUU = data.status[1].values[23].value
            # print Core_3_Nice_CPUU,"=" , valor_Core_3_Nice_CPUU
            # Core_3_System_CPUU = data.status[1].values[24].key
            # valor_Core_3_System_CPUU = data.status[1].values[24].value
            # print Core_3_System_CPUU,"=" , valor_Core_3_System_CPUU
            Core_3_Idle_CPUU = data.status[1].values[25].key
            valor_Core_3_Idle_CPUU = data.status[1].values[25].value
            # print Core_3_Idle_CPUU,"=" , valor_Core_3_Idle_CPUU
            # Load_Average_Status_CPUU = data.status[1].values[26].key
            # valor_Load_Average_Status_CPUU = data.status[1].values[26].value
            # print Load_Average_Status_CPUU,"=" , valor_Load_Average_Status_CPUU
            # Load_Average_1min_CPUU = data.status[1].values[27].key
            # valor_Load_Average_1min_CPUU = data.status[1].values[27].value
            # print Load_Average_1min_CPUU,"=" , valor_Load_Average_1min_CPUU
            # Load_Average_5min_CPUU = data.status[1].values[28].key
            # valor_Load_Average_5min_CPUU = data.status[1].values[28].value
            # print Load_Average_5min_CPUU,"=" , valor_Load_Average_5min_CPUU
            # Load_Average_15min_CPUU = data.status[1].values[29].key
            # valor_Load_Average_15min_CPUU = data.status[1].values[29].value
            # print Load_Average_15min_CPUU,"=" , valor_Load_Average_15min_CPUU

            # -----------'Disk Idle-----------------------------------------------------------------------
            msg_T0.header.frame_id =    Core_0_Temperature_CPU
            aux =        valor_Core_0_Temperature_CPU.split('D')
            msg_T0.temperature =        float(aux[0])
            # ----------------------------------------------------------------------------------
            msg_T1.header.frame_id =    Core_1_Temperature_CPU
            aux =        valor_Core_1_Temperature_CPU.split('D')
            msg_T1.temperature =        float(aux[0])
            # ----------------------------------------------------------------------------------
            msg_T2.header.frame_id =    Core_2_Temperature_CPU
            aux =        valor_Core_2_Temperature_CPU.split('D')
            msg_T2.temperature =        float(aux[0])
            # ----------------------------------------------------------------------------------
            msg_T3.header.frame_id =    Core_3_Temperature_CPU
            aux =        valor_Core_3_Temperature_CPU.split('D')
            msg_T3.temperature =        float(aux[0])
            # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            msg_Idle0.name = Core_0_Idle_CPUU
            msg_Idle0.values.append(KeyValue('Core 0',valor_Core_0_Idle_CPUU))
            # ----------------------------------------------------------------------------------
            msg_Idle1.name = Core_1_Idle_CPUU
            msg_Idle1.values.append(KeyValue('Core 1',valor_Core_1_Idle_CPUU))
            # ----------------------------------------------------------------------------------
            msg_Idle2.name = Core_2_Idle_CPUU
            msg_Idle2.values.append(KeyValue('Core 2',valor_Core_2_Idle_CPUU))
            # ----------------------------------------------------------------------------------
            msg_Idle3.name = Core_3_Idle_CPUU
            msg_Idle3.values.append(KeyValue('Core 3',valor_Core_3_Idle_CPUU))
            # ----------------------------------------------------------------------------------
            array_info.header.frame_id = 'Core Idle use'
            array_info.status = [msg_Idle0, msg_Idle1, msg_Idle2, msg_Idle3]
            # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            pub_T0.publish(msg_T0)
            pub_T1.publish(msg_T1)
            pub_T2.publish(msg_T2)
            pub_T3.publish(msg_T3)
            pub_idle.publish(array_info)
        elif nombre == "HDD Usage (NUC)":
            # print nombre
            # Update_status_HDD = data.status[0].values[0].key
            # valor_Update_status_HDD = data.status[0].values[0].value
            # print Update_status_HDD,"=" , valor_Update_status_HDD
            # Time_Since_Update_HDD = data.status[0].values[1].key
            # valor_Time_Since_Update_HDD = data.status[0].values[1].value
            # print Time_Since_Update_HDD,"=" , valor_Time_Since_Update_HDD
            # Disk_Space_Reading_HDD = data.status[0].values[2].key
            # valor_Disk_Space_Reading_HDD = data.status[0].values[2].value
            # print Disk_Space_Reading_HDD,"=" , valor_Disk_Space_Reading_HDD
            # Disk_1_Name_HDD = data.status[0].values[3].key
            # valor_Disk_1_Name_HDD = data.status[0].values[3].value
            # print Disk_1_Name_HDD,"=" , valor_Disk_1_Name_HDD
            # Disk_1_Size_HDD = data.status[0].values[4].key
            # valor_Disk_1_Size_HDD = data.status[0].values[4].value
            # print Disk_1_Size_HDD,"=" , valor_Disk_1_Size_HDD
            Disk_1_Available_HDD = data.status[0].values[5].key
            valor_Disk_1_Available_HDD = data.status[0].values[5].value
            # print Disk_1_Available_HDD,"=" , valor_Disk_1_Available_HDD
            # Disk_1_Use_HDD = data.status[0].values[6].key
            # valor_Disk_1_Use_HDD = data.status[0].values[6].value
            # print Disk_1_Use_HDD,"=" , valor_Disk_1_Use_HDD
            # Disk_1_Status_HDD = data.status[0].values[7].key
            # valor_Disk_1_Status_HDD = data.status[0].values[7].value
            # print Disk_1_Status_HDD,"=" , valor_Disk_1_Status_HDD
            # Disk_1_Mount_HDD = data.status[0].values[8].key
            # valor_Disk_1_Mount_HDD = data.status[0].values[8].value
            # print Disk_1_Mount_HDD,"=" , valor_Disk_1_Mount_HDD

            # ----------------------------------------------------------------------------------
            msg_Disk.name = Disk_1_Available_HDD
            msg_Disk.values.append(KeyValue('Disk Idle',valor_Disk_1_Available_HDD))
            # ----------------------------------------------------------------------------------
            array_info.header.frame_id = 'HDD Idle'
            array_info.status = [msg_Disk]
            # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            pub_HDD.publish(array_info)

        elif nombre == "Memory Usage (NUC)":
            # print nombre
            # Update_status_Memory = data.status[0].values[0].key
            # valor_Update_status_Memory = data.status[0].values[0].value
            # print Update_status_Memory,"=" , valor_Update_status_Memory
            # Time_Since_Update_Memory = data.status[0].values[1].key
            # valor_Time_Since_Update_Memory = data.status[0].values[1].value
            # print Time_Since_Update_Memory,"=" , valor_Time_Since_Update_Memory
            # Memory_Status_Memory = data.status[0].values[2].key
            # valor_Memory_Status_Memory = data.status[0].values[2].value
            # print Memory_Status_Memory,"=" , valor_Memory_Status_Memory
            # Total_Memory_Physical_Memory = data.status[0].values[3].key
            # valor_Total_Memory_Physical_Memory = data.status[0].values[3].value
            # print Total_Memory_Physical_Memory,"=" , valor_Total_Memory_Physical_Memory
            Used_Memory_Physical_Memory = data.status[0].values[4].key
            valor_Used_Memory_Physical_Memory = data.status[0].values[4].value
            # print Used_Memory_Physical_Memory , "=" , valor_Used_Memory_Physical_Memory
            # Free_Memory_Physical_Memory = data.status[0].values[5].key
            # valor_Free_Memory_Physical_Memory = data.status[0].values[5].value
            # print Free_Memory_Physical_Memory,"=" , valor_Free_Memory_Physical_Memory
            # Used_Memory_Physical_wo_Buffers_Memory = data.status[0].values[6].key
            # valor_Used_Memory_Physical_wo_Buffers_Memory = data.status[0].values[6].value
            # print Used_Memory_Physical_wo_Buffers_Memory,"=" , valor_Used_Memory_Physical_wo_Buffers_Memory
            # Free_Memory_Physical_wo_Buffers_Memory = data.status[0].values[7].key
            # valor_Free_Memory_Physical_wo_Buffers_Memory = data.status[0].values[7].value
            # print Free_Memory_Physical_wo_Buffers_Memory,"=" , valor_Free_Memory_Physical_wo_Buffers_Memory
            # Total_Memory_Swap_Memory = data.status[0].values[8].key
            # valor_Total_Memory_Swap_Memory  = data.status[0].values[8].value
            # print Total_Memory_Swap_Memory ,"=" , valor_Total_Memory_Swap_Memory
            Used_Memory_Swap_Memory = data.status[0].values[9].key
            valor_Used_Memory_Swap_Memory = data.status[0].values[9].value
            # print Used_Memory_Swap_Memory,"=" , valor_Used_Memory_Swap_Memory
            # Free_Memory_Swap_Memory = data.status[0].values[10].key
            # valor_Free_Memory_Swap_Memory = data.status[0].values[10].value
            # print Free_Memory_Swap_Memory,"=" , valor_Free_Memory_Swap_Memory
            # Total_Memory_Memory = data.status[0].values[11].key
            # valor_Total_Memory_Memory = data.status[0].values[11].value
            # print Total_Memory_Memory,"=" , valor_Total_Memory_Memory
            # Used_Memory_Memory = data.status[0].values[12].key
            # valor_Used_Memory_Memory = data.status[0].values[12].value
            # print Used_Memory_Memory,"=" , valor_Used_Memory_Memory
            # Free_Memory_Memory = data.status[0].values[13].key
            # valor_Free_Memory_Memory = data.status[0].values[13].value
            # print Free_Memory_Memory,"=" , valor_Free_Memory_Memory

            # ----------------------------------------------------------------------------------
            msg_RAM_Phy.name = Used_Memory_Physical_Memory
            msg_RAM_Phy.values.append(KeyValue('Physical Memory',valor_Used_Memory_Physical_Memory))
            # ----------------------------------------------------------------------------------
            msg_RAM_swap.name = Used_Memory_Swap_Memory
            msg_RAM_swap.values.append(KeyValue('SWAP Memory',valor_Used_Memory_Swap_Memory))
            # ----------------------------------------------------------------------------------
            array_info.header.frame_id = 'RAM Used'
            array_info.status = [msg_RAM_Phy, msg_RAM_swap]
            # ----------------------------------------------------------------------------------
            # ----------------------------------------------------------------------------------
            pub_RAM.publish(array_info)

        # elif nombre =="Network Usage (NUC)":
        #     # print nombre
        #     # Update_status_NET = data.status[0].values[0].key
        #     valor_Update_status_NET = data.status[0].values[0].value
        #     # print Update_status_NET,"=" , valor_Update_status_NET
        #     # Time_Since_Update_NET = data.status[0].values[1].key
        #     valor_Time_Since_Update_NET = data.status[0].values[1].value
        #     # print Time_Since_Update_NET,"=" , valor_Time_Since_Update_NET
        #     # Interface_Name_NET = data.status[0].values[2].key
        #     valor_Interface_Name_NET = data.status[0].values[2].value
        #     # print Interface_Name_Nself.ser.open()ET,"=" , valor_Interface_Name_NET
        #     # State_NET = data.status[0].values[3].key
        #     valor_State_NET = data.status[0].values[3].value
        #     # print State_NET,"=" , valor_State_NET
        #     # Input_Traffic_NET = data.status[0].values[4].key
        #     valor_Input_Traffic_NET = data.status[0].values[4].value
        #     # print Input_Traffic_NET , "=" , valor_Input_Traffic_NET
        #     # Output_Traffic_NET = data.status[0].values[5].keyvalor_Core_3
        #     valor_Output_Traffic_NET = data.status[0].values[5].value
        #     # print Output_Traffic_NET,"=" , valor_Output_Traffic_NET
        #     # MTU_NET = data.status[0].values[6].key
        #     valor_MTU_NET  = data.status[0].values[6].value
        #     # print MTU_NET ,"=" , valor_MTU_NET
        #     # Total_received_MB_NET = data.status[0].values[7].key
        #     valor_Total_received_MB_NET = data.status[0].values[7].value
        #     # print Total_received_MB_NET,"=" , valor_Total_received_MB_NET
        #     # Total_transmitted_MB_NET = data.status[0].values[8].key
        #     valor_Total_transmitted_MB_NET  = data.status[0].values[8].value
        #     # print Total_transmitted_MB_NET ,"=" , valor_Total_transmitted_MB_NET
        #     # Collisions_NET = data.status[0].values[9].key
        #     valor_Collisions_NET = data.status[0].values[9].value
        #     # print Collisions_NET,"=" , valor_Collisions_NET
        #     # Rx_Errors_NET = data.status[0].values[10].key
        #     valor_Rx_Errors_NET  = data.status[0].values[10].value
        #     # print Rx_Errors_NET ,"=" , valor_Rx_Errors_NET
        #     # Tx_Errors_NET  = data.status[0].values[11].key
        #     valor_Tx_Errors_NET = data.status[0].values[11].value
        #     # print Tx_Errors_NET,"=" , valor_Tx_Errors_NET
        #     # Interface_Name_NET = data.status[0].values[12].key
        #     valor_Interface_Name_NET = data.status[0].values[12].value
        #     # print Interface_Name_NET,"=" , valor_Interface_Name_NET
        #     # State_NET = data.status[0].values[13].key
        #     valor_State_NET = data.status[0].values[13].value
        #     # print State_NET,"=" , valor_State_NET
        #     # Input_Traffic_NET = data.status[0].values[14].key
        #     valor_Input_Traffic_NET = data.status[0].values[14].value
        #     # print Input_Traffic_NET,"=" , valor_Input_Traffic_NET
        #     # Output_Traffic_NET = data.status[0].values[15].key
        #     valor_Output_Traffic_NET = data.status[0].values[15].value
        #     # print Output_Traffic_NET,"=" , valor_Output_Traffic_NET
        #     MTU2_NET = data.status[0].values[16].key
        #     valor_MTU2_NET = data.status[0].values[16].value
        #     # print MTU2_NET,"=" , valor_MTU2_NET
        #     # Total2_received_MB_NET = data.status[0].values[17].key
        #     valor_Total2_received_MB_NET = data.status[0].values[17].value
        #     # print Total2_received_MB_NET,"=" , valor_Total2_received_MB_NET
        #     # Total2_transmitted_MB_NET = data.status[0].values[18].key
        #     valor_Total2_transmitted_MB_NET = data.status[0].values[18].value
        #     # print Total2_transmitted_MB_NET,"=" , valor_Total2_transmitted_MB_NET
        #     # Collisions2_NET = data.status[0].values[19].key
        #     valor_Collisions2_NET = data.status[0].values[19].value
        #     # print Collisions2_NET,"=" , valor_Collisions2_NET
        #     # Rx2_Errors_NET = data.status[0].values[20].key
        #     valor_Rx2_Errors_NET = data.status[0].values[20].value
        #     # print Rx2_Errors_NET,"=" , valor_Rx2_Errors_NET
        #     # Tx2_Errors_NET = data.status[0].values[21].key
        #     valor_Tx2_Errors_NET = data.status[0].values[21].value
        #     # print Tx2_Errors_NET,"=" , valor_Tx2_Errors_NET
        #     # print "-------------------------------------------------------------------------"

    def talker(self):

        rospy.init_node('CPU_Resources', anonymous=False)
        # rate = rospy.Rate(10) # 2hz
        rospy.Subscriber('/diagnostics',DiagnosticArray,self.CPUmonitor )
        rospy.spin()
#         while not rospy.is_shutdown():
#             if self.cont == 10:
# #                print self.serial_message
#                 self.ser.write(self.serial_message)
#                 self.cont = 0
#             str_in = self.ser.readline()
#             if len(str_in)>0:
# #                rospy.loginfo(str_in)
#                 pub.publish(str_in)
#             self.cont = self.cont + 1
#             rate.sleep()

if __name__ == '__main__':
    my_list = listener()
