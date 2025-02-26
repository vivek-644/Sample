#NAME:SmartStudioFunc
#NOTE:Module for SmartStudio helper functions. The functions in this module are derived from the original WNS_*  function calls that are defined in the MD847570A_VX.YZ_Manual_Eng.pdf.  This module may contain definitions taken from the WnsCtrlApi.h which are used for defining values associated with calling WNS_* functions.

#----- TEST SCRIPT INPUT FUNCTIONS --- DO NOT MODIFY-----
#--FUNCTION:GET_UESTAT_UE
def GET_UESTAT_UE():
	UeStatusPtr = clr.Reference[System.Int32](UE_STAT_NONE)
	retVal = FALSE
	
	retVal = SmartStudio.WNS_GetUEStatus(UeStatusPtr)
	ueStatofUe = SmartStudio.GET_UESTAT_UE(int(UeStatusPtr))
	
	if retVal == FALSE:
		Log.Error('Error: WNS_GetUEStatus() - SmartStudioFunc.GET_UESTAT_UE.')
		exit()
	
	return ueStatofUe

#--END FUNCTION:GET_UESTAT_UE


#--FUNCTION:GET_UESTAT_PACKET
def GET_UESTAT_PACKET():
	UeStatusPtr = clr.Reference[System.Int32](UE_STAT_NONE)
	retVal = FALSE
	
	retVal = SmartStudio.WNS_GetUEStatus(UeStatusPtr)
	ueStatofPkt = SmartStudio.GET_UESTAT_PACKET(int(UeStatusPtr))
	
	if retVal == FALSE:
		Log.Error('Error: WNS_GetUEStatus() - SmartStudioFunc.GET_UESTAT_PACKET.')
		exit()
		
	return ueStatofPkt

#--END FUNCTION:GET_UESTAT_PACKET

#----- END OF TEST SCRIPT FUNCTIONS -----
import System.Text
import clr
import System
from System.Text import StringBuilder

# WNS Function Return Value
TRUE  = 1
FALSE = 0

#===== WNS_SaveTraceLog()  FileType =====
FT_BINARY                    = 0    #Binary log (.lgx)
FT_TEXT                      = 1    #Text log (.txt)
FT_H245                      = 2    #H245 log (.pcap)
FT_PACKET                    = 3    #Packet log (.pcap) U-Plane
FT_PACKET_CPLANE             = 4    #Packet log (.pcap) C-Plane
FT_CPLANE                    = 4    #Packet log (.pcap) C-Plane

#===== WNS_SaveTraceLog()  OverWrite =====
OW_OFF  = 0    # Overwrite Off
OW_ON   = 1    # Overwrite On

#===== WNS_SetTargetControlSoftware()  Mode =====
TRACE_MODE_MASTER       = 0x00000001    #Master(Default)
TRACE_MODE_SLAVE1       = 0x00000002    #Slave#1
TRACE_MODE_SLAVE2       = 0x00000004    #Slave#2
TRACE_MODE_SLAVE3       = 0x00000008    #Slave#3


#===== WNS_ShowWindow()  WindowType =====
WINDOW_TYPE_MAIN = 0

#===== WNS_ShowWindow()  Mode =====
SW_HIDE = 0
SW_SHOW = 5

#===== WNS_SetTraceFilter()  Mode =====
FS_FILTER_OFF  = 0
FS_FILTER_FILE = 2


#===== WNS_SetCellParam()  Bts =====
WNS_BTS1 = 1                        
WNS_BTS2 = 2                        
WNS_BTS3 = 3                        
WNS_BTS4 = 4        

#===== WNS_SetOutOfService()Service =====
OS_IN_SERVICE  = 0 #In Service
OS_OUT_SERVICE = 1 #Out of Service

#===== WNS_OperateVirtualPhone()  PhoneOperate =====
VP_OFFHOOK        = 0   #Off Hook
VP_ONHOOK         = 1   #On Hook
VP_VIDEO_OFFHOOK  = 2   #Video Off Hook
VP_VIDEO_ONHOOK   = 3   #Video On Hook
VP_CALL_WAITING   = 4   #Call Waiting

#===== WNS_OperatePacket()  PhoneOperate =====
VP_PACKET_TERMINATE    = 0  #Packet Terminate
VP_PACKET_PRESERVATION = 1  #Packet Preservation
VP_PACKET_RELEASE      = 2  #Packet Release
VP_DORMANT             = 3  #Dormant

#=== WNS_GetUEStatus()  Status =====
UE_STAT_PAGE_3GPP                 = 0  # GET_UESTAT_PAGE
UE_STAT_PAGE_CDMA1X               = 1  # GET_UESTAT_PAGE
UE_STAT_PAGE_EVDO                 = 2  # GET_UESTAT_PAGE
UE_STAT_PWS_INVALID               = 0  # GET_UESTAT_PWS
UE_STAT_PWS_VALID                 = 1  # GET_UESTAT_PWS
UE_STAT_NONE                      = 0  # GET_UESTAT_UE, GET_UESTAT_PACKET, GET_UESTAT_PPP
UE_STAT_PPP_IDLE                  = 1  # GET_UESTAT_PPP
UE_STAT_PPP_ACTIVE                = 2  # GET_UESTAT_PPP
UE_STAT_PPP_DORMANT               = 3  # GET_UESTAT_PPP
UE_STAT_POWEROFF                  = 1  # GET_UESTAT_UE
UE_STAT_REGISTRATION              = 2  # GET_UESTAT_UE
UE_STAT_DETACH                    = 3  # GET_UESTAT_UE
UE_STAT_IDLE                      = 4  # GET_UESTAT_UE
UE_STAT_ORIGINATION               = 5  # GET_UESTAT_UE
UE_STAT_HANDOVER                  = 7  # GET_UESTAT_UE
UE_STAT_CELLUPDATE                = 8  # GET_UESTAT_UE
UE_STAT_CELLUPDATE_ORIGINATION    = 12 # GET_UESTAT_UE
UE_STAT_TERMINATION               = 6  # GET_UESTAT_PACKET
UE_STAT_COMMUNICATION             = 7  # GET_UESTAT_PACKET
UE_STAT_UE_RELEASE                = 8  # GET_UESTAT_PACKET
UE_STAT_NW_RELEASE                = 9  # GET_UESTAT_PACKET
UE_STAT_IDLE_SMS                  = 10 # GET_UESTAT_PACKET
UE_STAT_COMMUNICATION_TERMINATION = 12 # GET_UESTAT_PACKET
UE_STAT_COMMUNICATION_UE_RELEASE  = 14 # GET_UESTAT_PACKET
UE_STAT_COMMUNICATION_NW_RELEASE  = 15 # GET_UESTAT_PACKET

#TBD - Need to understand how the below function works
#===== WNS_GetBtsStatus()  Status =====
#define BTS_STAT_MAX_COUNT              ( 4)
#define GET_UESTAT_BTS1(p)              (*(p+(WNS_BTS1 -1)))
#define GET_UESTAT_BTS2(p)              (*(p+(WNS_BTS2 -1)))
#define GET_UESTAT_BTS3(p)              (*(p+(WNS_BTS3 -1)))
#define GET_UESTAT_BTS4(p)              (*(p+(WNS_BTS4 -1)))

#===== WNS_GetRrcStatus()  Status =====
RRC_STAT_IDLE     = 0
RRC_STAT_CELLDCH  = 1
RRC_STAT_CELLFACH = 2
RRC_STAT_CELLPCH  = 3
RRC_STAT_URAPCH   = 4

#===== WNS_GetVPStatus()  Status =====
VP_STAT_IDLE                    = 0
VP_STAT_VOICE_CALL_FROM_VP      = 1
VP_STAT_VOICE_CALL_FROM_UE      = 2
VP_STAT_VOICE_COMMUNICATION     = 3
VP_STAT_VOICE_RELEASE_FROM_VP   = 4
VP_STAT_VOICE_RELEASE_FROM_UE   = 5
VP_STAT_VIDEO_CALL_FROM_VP      = 6
VP_STAT_VIDEO_CALL_FROM_UE      = 7
VP_STAT_VIDEO_COMMUNICATION     = 8
VP_STAT_VIDEO_RELEASE_FROM_VP   = 9
VP_STAT_VIDEO_RELEASE_FROM_UE   = 10

#===== WNS_GetCampingCell()  BTS =====
WNS_BTS_NONE  = 0x00000000
WNS_BTS_1     = 0x00000001
WNS_BTS_2     = 0x00000002
WNS_BTS_3     = 0x00000004
WNS_BTS_4     = 0x00000008
WNS_BTS_INTERMEDIATE = -1

#TBD - Need to understand how the below function works
#define WNS_IS_ACTIVE(x,y)              (y==WNS_BTS_NONE?x==y:(*(x) & y) == y)

#===== WNS_GetCampingCell()  System =====
WNS_SYSTEM_NONE = 0x00000000
WNS_W_CDMA      = 0x00000001
WNS_GSMGPRS     = 0x00000002
WNS_LTE         = 0x00000004
WNS_TD_SCDMA    = 0x00000008
WNS_CDMA_1X     = 0x00000010
WNS_EV_DO       = 0x00000020

#===== WNS_GetBtsConnection()  BTS =====
CONN_COMMON  = 0
CONN_BTS1    = WNS_BTS1
CONN_BTS2    = WNS_BTS2
CONN_BTS3    = WNS_BTS3
CONN_BTS4    = WNS_BTS4

#===== WNS_SetStatusReport() Status =====
SMSC_AUTO_STATUS = -1    # Auto Status by SMSC

#===== WNS_GetStatus()  Status =====
STAT_IDLE       = 0    # Status Idle
STAT_SIMULATION = 1    # Status Simulation
STAT_ERROR      = -1   # Status Error

#===== WNS_ResetSimulation()  Type =====
RESET_TO_IDLE     = 0     # Reset to Idle
RESET_TO_POWEROFF = 1     # Reset to Power Off

#===== WNS_ResetSimulation()  Direction =====
RESET_CAMPING = 0
RESET_BTS1    = WNS_BTS1
RESET_BTS2    = WNS_BTS2
RESET_BTS3    = WNS_BTS3
RESET_BTS4    = WNS_BTS4

#===== WNS_GetTestStatus()  Status =====
TS_IN_PROCESS   = 0
TS_PASS         = 1
TS_FAIL         = 2
TS_ERROR        = 3
TS_INTERRUPTED  = 4

#===== WNS_GetTestStatus()  Error =====
TES_NONE                        = 0
TES_FAIL_UENOTSUPPORT           = 1
TES_FAIL_OUTSYNC                = 2
TES_FAIL_MEASREPORT             = 3
TES_FAIL_REGISTTOUNSUITABLE     = 4
TES_FAIL_CAUSEUNKNOWN           = 5
TES_FAIL_TIMEOUT                = 6
TES_FAIL_RCVFAILUREMSG          = 7
TES_FAIL_UNEXPECTEDFAILURECAUSE = 8
TES_FAIL_CELLUPDATE             = 9
TES_ERR_UNEXPECTEDMSG           = 1
TES_ERR_MSGTIMEOUT              = 2
TES_ERR_TESTUNAVAILABLE         = 3
TES_ERR_UNMATCHPDN              = 4
TES_INTRPT_VOICEORIGINATE       = 1
TES_INTRPT_VOICEUERELEASE       = 2
TES_INTRPT_VIDEOORIGINATE       = 3
TES_INTRPT_VIDEOUERELEASE       = 4
TES_INTRPT_PACKETORIGINATE      = 5
TES_INTRPT_PACKETUERELEASE      = 6
TES_INTRPT_DETACH               = 7
TES_INTRPT_USEROPERATION        = 8
TES_INTRPT_ATTACH               = 9
TES_INTRPT_SMSORIGINATED        = 10

#===== WNS_StartMeasureExport(), WNS_StartThroughputExport()  Separate =====
ME_SEP_30MINS   = 0                                                 
ME_SEP_1HOUR    = 1                                                 
ME_SEP_2HOURS   = 2                                                 
ME_SEP_5HOURS   = 3                                                 
ME_SEP_10HOURS  = 4                                                 
                                                                                             
#===== WNS_SetSeqLogNote()  EditMode =====
SEQ_NOTE_SET  = 0 #Note Set Mode                             
SEQ_NOTE_ADD  = 1 #Note Add Mode                             
                                                                                             
#===== WNS_SaveMessageLogLatest()  BTS =====
MSG_BTS_OMIT = 0                                                  
MSG_BTS1     = WNS_BTS1                                           
MSG_BTS2     = WNS_BTS2                                           
MSG_BTS3     = WNS_BTS3                                           
MSG_BTS4     = WNS_BTS4                                           
                                                                                             
#===== WNS_SaveMessageLogLatest()  AddIndex =====                                         
ADDINDEX_OFF = 0    #AddIndex Off                              
ADDINDEX_ON  = 1    #AddIndex On                               
                                                                                             
#===== WNS_SetTriggerMessageCondition(), WNS_SetMessageLogMonitorCondition()  Enable =====
MSG_CONDITION_DISABLE           =  0    #Enable Disable                            
MSG_CONDITION_ENALBE            =  1    #Enable Enable                             
MSG_CONDITION_DELETE            = -1    #Enable Delete                             
                                                                                             
#===== WNS_CalibratePathLoss() Type =====
CALIBRATE_DL   = 0                                                
CALIBRATE_UL   = 1                                                
CALIBRATE_BOTH = 2

#===== WNS_IMS_SetParam()  =====
IMS_SERVER_TYPE_CSCF            = "CSCF"
IMS_SERVER_TYPE_MWI             = "MWI"
IMS_SERVER_TYPE_PSAP            = "PSAP"
IMS_SERVER_TYPE_RCS             = "RCS"
IMS_SERVER_TYPE_CONFERENCE      = "VoLTEConference"
IMS_SERVER_TYPE_XCAP            = "XCAP"
IMS_SERVER_TYPE_BSF             = "BSF"
IMS_SERVER_TYPE_MRF             = "MRF"
IMS_SERVER_TYPE_SCRIPT          = "Script"
IMS_SERVER_TYPE_RTP             = "RTP"
IMS_SERVER_TYPE_COMMON          = "Common"


#===== WNS_IMS_GetVirtualNetworkStatus()  Status =====
IMS_VN_STAT_NOT_RUN  = 0
IMS_VN_STAT_RUNNING  = 1

#===== WNS_GetLastError()  ErrorNo =====
ERROR_WNS_NO_ERROR           	= 0 
ERROR_FILE_NOT_FOUND         	= 2 
ERROR_OUTOFMEMORY            	= 14 
ERROR_WRITE_FAULT            	= 29 
ERROR_FILE_EXISTS       		= 80 
ERROR_INVALID_PARAMETER 		= 87 
ERROR_DISK_FULL         		= 112 
ERROR_ALREADY_EXISTS    		= 183 
ERROR_SERVICE_DOES_NOT_EXIST 	= 1060 
ERROR_PROCESS_ABORTED 			= 1067 
ERROR_CONNECTION_INVALID 		= 1229 
ERROR_REQUEST_ABORTED 			= 1235 
ERROR_TIMEOUT 					= 1460 
ERROR_WNS_INVALID_LICENSE 		= 536870912 
ERROR_WNS_INVALID_FILE 			= 536870913 
ERROR_WNS_NOT_EXISTS_PROCESS 	= 536870914 
ERROR_WNS_NOT_EXISTS_SMS 		= 536870915 
ERROR_WNS_NOT_RUN_SIMULATION 	= 536870916 
ERROR_WNS_ALREADY_RUN_SIMULATION 	= 536870917 
ERROR_WNS_NOT_RUN_TESTCASE 			= 536870918 
ERROR_WNS_NOT_EXISTS_RESOURCE 		= 536870919 
ERROR_WNS_RESOURCE_PROTOCOL 		= 536870920 
ERROR_WNS_INVALID_STATE 			= 536870921 
ERROR_WNS_MISMATCH_SIMULATION_MODEL = 536870922 
ERROR_WNS_NOT_EXISTS_CELL 			= 536870923 
ERROR_WNS_ALREADY_RUN_TESTCASE  	= 536870924 
ERROR_WNS_UE_STATUS_MISMATCH 		= 536870925 
ERROR_WNS_NOT_EXIST_LOG 			= 536870926 
ERROR_WNS_ALREADY_EXPORT			= 536870927
ERROR_WNS_ALREADY_EXPORT_MEASURE 	= 536870927 
ERROR_WNS_SMSC_NOT_CONNECTED        = 536870928 
ERROR_WNS_CANNOT_SEND_SMS           = 536870929 
ERROR_WNS_INVALID_SMS               = 536870930 
ERROR_WNS_SMSC_INVALID_STATE 		= 536870931 
ERROR_WNS_INVALID_OPTION			= 536870932
ERROR_WNS_NOT_EXPORT				= 536870933
ERROR_WNS_NOT_EXPORT_MEASURE        = 536870933 
ERROR_WNS_NOT_LOAD_VERSION 			= 536870934 
ERROR_WNS_NOT_EXIST_PDN 			= 536870935 
ERROR_WNS_NOT_EXIST_DEDICATED       = 536870936 
ERROR_WNS_FULL_PDN 					= 536870937
ERROR_WNS_INVALID_NUMBER_OF_ANTENNA = 536870938 
ERROR_WNS_CALIBRATE_EXTLOSS         = 536870939 
ERROR_WNS_UNRECOGNIZED_CONFIGURATION_PARAMETER 	= 536870940 
ERROR_WNS_INVALID_EVOLUTION_DLREFPOWER 			= 536870941 
ERROR_WNS_INVALID_DCHSDPA_CHANNEL 				= 536870942 
ERROR_WNS_INVALID_DCHSDPA_HSPA_PACKETRATE 		= 536870943 
ERROR_WNS_INVALID_NOTEVOLITION_FDPCH 			= 536870944 
ERROR_WNS_INVALID_TARGET 						= 536870945 
ERROR_WNS_INVALID_PWS 							= 536870946 
ERROR_WNS_INVALID_ECIOR_POWER					= 536870947 
ERROR_WNS_INVALID_ATTACH_TYPE_OR_TA_UPDATE_TYPE = 536870948 
ERROR_WNS_EXPIRED_SERVICE_OPTION				= 536870949 
ERROR_WNS_ALREADY_RUN_PING 						= 536870950 
ERROR_WNS_NOT_RUN_PING 							= 536870951 
ERROR_WNS_INVALID_TESTCASE_PARAM 				= 536870952 
ERROR_WNS_DUPLICATE_IPADDRESS 					= 536870953 
ERROR_WNS_CONVERSION_TFTIE 						= 536870954 
ERROR_WNS_SCENARIO_BUSY 						= 536870955 
ERROR_WNS_PENDING_DATA_EXISTS 					= 536870956 
ERROR_WNS_SAME_CELL_EXISTS 						= 536870957 
ERROR_WNS_OVER_NUMBER_OF_CELL 					= 536870958 
ERROR_WNS_INVALID_LTECA_DLBAND 					= 536870959 
ERROR_WNS_INVALID_TS09_MODE 					= 536870960 
ERROR_WNS_INVALID_AWGN_MODE 					= 536870961 
ERROR_WNS_SLAVE_CANNOT_CONNECT 					= 536870962 
ERROR_WNS_SLAVE_VERSION_MISMATCH 				= 536870963
ERROR_WNS_OBJECT_VERSION_MISMATCH 				= 536870964 
ERROR_WNS_NOT_RUN_MEASURE 						= 536870966 
ERROR_WNS_ALREADY_RUN_MEASURE 					= 536870967 
ERROR_WNS_INVALID_TRANSFER_FOLDER 				= 536870968 
ERROR_WNS_INVALID_TRANSFER_FILE_FORMAT 			= 536870969 
ERROR_WNS_NOT_RUN_IPTRAFFIC 					= 536870970 
ERROR_WNS_ALREADY_RUN_IPTRAFFIC 				= 536870971 
ERROR_WNS_START_IPTRAFFIC 						= 536870972 
ERROR_WNS_STOP_IPTRAFFIC 						= 536870973 
ERROR_WNS_CURRENT_TRACEMODE 					= 536870974 
ERROR_WNS_INVALID_CONFIGURATION_ON_THIS_VERSION = 536875008 
ERROR_WNS_INVALID_OPERATION_ON_THIS_SIGNALLING_TESTER 	= 536875009 
ERROR_WNS_IMS_INVALID_LICENSE 							= 536936448 
ERROR_WNS_IMS_INVALID_FILE 								= 536936449 
ERROR_WNS_IMS_INVALID_STATE 							= 536936450 
ERROR_WNS_IMS_NOT_EXIST_LOG 							= 536936462 
ERROR_WNS_IMS_VUA_INVALID_STATE 						= 536936467
ERROR_WNS_IMS_SETTING 									= 536936480 
ERROR_WNS_IMS_NOT_RUN_VNETWORK 							= 536936707 
ERROR_WNS_IMS_ALREADY_RUN_VNETWORK 						= 536936709 
ERROR_WNS_IMS_NOT_EXIST_VNETWORK 						= 536936727 
ERROR_WNS_IMS_FULL_VNETWORK 							= 536936729 
ERROR_WNS_WLAN_INVALID_LICENSE 							= 537001984 
ERROR_WNS_WLAN_INVALID_FILE 							= 537001985 
ERROR_WNS_WLAN_INVALID_STATE 							= 537002003 
ERROR_WNS_WLAN_NOT_RUN_VNETWORK 						= 537002243 
ERROR_WNS_WLAN_ALREADY_RUN_VNETWORK 					= 537002245 
ERROR_WNS_WLAN_NOT_EXIST_LOG 							= 537001998 
ERROR_WNS_WLAN_NOT_EXIST_VNETWORK 						= 537002263 
ERROR_WNS_WLAN_FULL_VNETWORK 							= 537002265 
ERROR_WNS_WLAN_MULTIPLEX_START 							= 537002498
ERROR_WNS_WLAN_INVALID_VERSION 							= 537001986 
ERROR_WNS_RM_LAUNCHER_INVALID 							= 554762241 
ERROR_WNS_RM_INVALID_LICENSE 							= 554762242 
ERROR_WNS_RM_INVALID_CONFIG_FILE 						= 554762243 
ERROR_WNS_RM_ALREADY_EXISTS 							= 554762244 
ERROR_WNS_RM_PROCESS_ABORTED 							= 554762245 
ERROR_WNS_RM_SERVICE_DOES_NOT_EXIST 					= 554762246 
ERROR_WNS_RM_INVALID_CAL_VERSION 						= 554762247 
ERROR_WNS_RM_INVALID_PARAMETER 							= 554827777 
ERROR_WNS_RM_GPIB_COMMAND_INVALID 						= 554827778 
ERROR_WNS_RM_FILE_LENGTH 								= 554827779 
ERROR_WNS_RM_PARAMETER_NULL 							= 554827780 
ERROR_WNS_RM_MEASURING 									= 555810817 
ERROR_WNS_RM_NOT_MEASURING 								= 555810818
ERROR_WNS_RM_NOT_EXIST_RESULT 							= 555810819 
ERROR_WNS_RM_MEASURE_START 								= 555810820 
ERROR_WNS_RM_MEASURE_SIMULATION_STOPPED 				= 555810821 
ERROR_WNS_RM_MEASURE_FAIL 								= 555810822 
ERROR_WNS_RM_INVALID_SYSTEM 							= 555810823 
ERROR_WNS_RM_SAVING 									= 556859393 
ERROR_WNS_RM_SAVE_DISK_FULL 							= 556859394 
ERROR_WNS_RM_SAVE_FAIL 									= 556859395 
ERROR_WNS_RM_SAVE_READONLY 								= 556859396 
ERROR_WNS_RM_INTERNAL_APP 								= 568328193