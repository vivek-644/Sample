#NAME:ELD-8
#MODULE:SmartStudioFunc

#MODULE:ImsServicesFunc
#----- TEST SCRIPT INPUT FUNCTIONS --- DO NOT MODIFY-----
#--FUNCTION:GetDataFromLog
def GetDataFromLog(columnNum):
	#name of the file to open
	fileName = 'C:\\Program Files (x86)\\Anritsu\\PluginHost\\Plugins\\Android\\Android SDK\\com.tmobile.echolocate.log.manually.txt'
	
	# Read in the file
	# Make sure each line of the file must be of the same format
	f = open(fileName,'r')
	lineCounter = 0
	
	for line in f:
		stringArray = line.split()
		arraySize = len(stringArray)
		#Log.Informational('Number of Columns=' + str(arraySize))
		#Log.Informational('Number of Lines=' + str(lineCounter))
		if lineCounter > 1:
			Log.Warning('Log contains more than 1 line of data. The return data is from line number ' + lineCounter + '.')
		lineCounter = lineCounter + 1
	
	return stringArray[columnNum]

#--END FUNCTION:GetDataFromLog

#----- END OF TEST SCRIPT FUNCTIONS -----
import System
import System.Text
import System.IO
import clr
import time
from System.Text import StringBuilder

#-------------------------------------------------------------------------------------------------
# Prompt user to power OFF UE
# - Stub out function for automation
#-------------------------------------------------------------------------------------------------
#Prompt.NotificationMessage('Please power OFF UE.', '', 30)
Execute.Scriptlet('ToggleAirplaneMode','AirplaneMode=ON',-1)
Execute.PauseSeconds(2)

retVal = SmartStudioFunc.FALSE
pStatusSmartStudio = clr.Reference[System.Int32](SmartStudioFunc.STAT_ERROR)

if SmartStudio.IsConnected == False:
	SmartStudio.SetModeToSmartStudio()
	if SmartStudio.IsConnected == False:
		Outcome.Error('Error:Connecting Smart Studio Plugin to MD8475')

#-------------------------------------------------------------------------------------------------
# Configure Common Network Parameters
# - Set Ethernet0 IP addresses
#-------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
# Configure Test Specific Network Parameters
# - Reset MD8475 to known Simulation and Cell configurations
#-------------------------------------------------------------------------------------------------
retVal = SmartStudio.WNS_GetStatus(pStatusSmartStudio)
if int(pStatusSmartStudio) == SmartStudioFunc.STAT_SIMULATION and (retVal == SmartStudioFunc.TRUE):
	retVal = SmartStudio.StopSimulation()	

if retVal == SmartStudioFunc.TRUE:
	retVal = SmartStudio.WNS_GetStatus(pStatusSmartStudio)
else:
	Outcome.Error('Error:WNS_Stop() or WNS_GetStatus()')

retVal = SmartStudio.WNS_LoadSimParam("C:\\MX847570\\SimParam\\sample\\LTE_IMS.wnssp2")
#retVal = SmartStudio.WNS_LoadSimParam("C:\\MX847570\\SimParam\\sample\\WCDMA.wnssp2")
#retVal = SmartStudio.WNS_LoadSimParam("C:\\MX847570\\SimParam\\sample\\GSMGPRS.wnssp2")
retVal = SmartStudio.WNS_LoadCellParam("C:\\MX847570\\CellParam\\sample\\1cell_Sample.wnscp2")
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_LoadSimParam() or WNS_LoadCellParam()')

# USIM Settings
retVal = SmartStudio.WNS_SelectUSIM('P0135Ax')
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_SelectUSIM().')

# Common Settings
pImsParam = StringBuilder()
pImsParam.Append('SyncEnabled=True\r')
retVal = SmartStudio.WNS_IMS_SetParam(SmartStudioFunc.IMS_SERVER_TYPE_COMMON,1,pImsParam.ToString())
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_IMS_SetParam().')

# CSCF Settings
pCscfParam = StringBuilder()
pCscfParam.Append('IPVersion=Ipv4v6\r')
pCscfParam.Append('IPv4AddrStr=192.168.1.2\r')
pCscfParam.Append('IPv6AddrStr=2001:0:0:1::2\r')
pCscfParam.Append('HostName=msg.lab.t-mobile.com\r')
pCscfParam.Append('Port=5060\r')
pCscfParam.Append('MonitoringUA=sip:001010123456789@ims.mnc01.mcc001.3gppnetwork.org\r')
pCscfParam.Append('SMSCAutoForward=False\r')
pCscfParam.Append('Auth=True\r')
pCscfParam.Append('UserEntry=001010123456789@msg.lab.t-mobile.com,00112233445566778899AABBCCDDEEFF,TS34108,AKAv1_MD5,OPc,00000000000000000000000000000000,8000,False,False,0123456789ABCDEF0123456789ABCDEF,54CDFEAB9889000001326754CDFEAB98,6754CDFEAB9889BAEFDC457623100132,326754CDFEAB9889BAEFDC4576231001,True,True,False,TOPc,0000000000000000000000000000000000000000000000000000000000000000\r')
pCscfParam.Append('UAEnabled=True\r')
pCscfParam.Append('UAIdentity=sip:0123456789@msg.lab.t-mobile.com\r')
pCscfParam.Append('Precondition=True\r')
retVal = SmartStudio.WNS_IMS_SetCSCFParam(ImsServicesFunc.VNID1,pCscfParam.ToString())
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_IMS_SetCSCFParam().')

# DNS Settings
pDnsParam = StringBuilder()
pDnsParam.Append('Enabled=True\r')
pDnsParam.Append('IPVersion=Ipv4v6\r')
pDnsParam.Append('IPv4AddrStr=192.168.1.2\r')
pDnsParam.Append('IPv6AddrStr=2001:0:0:1::2\r')
retVal = SmartStudio.WNS_IMS_SetDNSParam(ImsServicesFunc.VNID1,pDnsParam.ToString())
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_IMS_SetDNSParam().')

# Cell Settings
pCellParam = StringBuilder()
# pCellParam.Append('Mcc=310\r')
# pCellParam.Append('Mnc=260\r')
pCellParam.Append('EUtraBand=Band2\r')
pCellParam.Append('DlBandwidth=10MHz\r')
pCellParam.Append('DlRefPower=-30.0\r')
retVal = SmartStudio.WNS_SetCellParam(SmartStudioFunc.WNS_BTS1,pCellParam.ToString())
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_SetCellParam()')

# Start Simulation Environment
retVal = SmartStudio.StartSimulation()
if retVal == SmartStudioFunc.FALSE:
	Outcome.Error('Error:WNS_Start()')


#-------------------------------------------------------------------------------------------------
# Prompt user to power ON UE with 60s timeout
# - Stub out function for automation
#-------------------------------------------------------------------------------------------------
timeOut = 60
#Prompt.NotificationMessage('Please power ON UE.', '', timeOut)
Execute.Scriptlet('ToggleAirplaneMode','AirplaneMode=OFF',-1)
loopCounter = 0
while SmartStudioFunc.GET_UESTAT_PACKET() != SmartStudioFunc.UE_STAT_COMMUNICATION:
	if (loopCounter >= timeOut):
		Outcome.Error('Error:UE never camped on the LTE network.')
		break
	loopCounter = loopCounter + 2
	Execute.PauseSeconds(2)

#-------------------------------------------------------------------------------------------------
# Prompt user to toggl Mobile data "ON" on UE
# - Stub out function for automation
#-------------------------------------------------------------------------------------------------
Execute.Scriptlet('ToggleMobiledata','MobileData=ON',-1)
Execute.PauseSeconds(5)

#-------------------------------------------------------------------------------------------------
# Prompt user to trigger network scan from RD-614 APP
# - Stub out function for automation
#-------------------------------------------------------------------------------------------------
if SmartStudioFunc.GET_UESTAT_PACKET() == SmartStudioFunc.UE_STAT_COMMUNICATION:
	# This scriptlet will open the app based on the name (ARG #2) that is passed in.
	Execute.Scriptlet('OpenApp','',-1)
	# This scriptlet will download the file to parse from the UE.
	Execute.Scriptlet('TriggerScan','TestNum=ELD-8',-1)
else:
	Outcome.Error('Error:Scan can not be triggered from app on the UE.')

#-------------------------------------------------------------------------------------------------
# Prompt user to power OFF UE
# - Stub out function for automation
#-------------------------------------------------------------------------------------------------
#Prompt.NotificationMessage('Please power OFF UE.', '', 30)
Execute.Scriptlet('ToggleAirplaneMode','AirplaneMode=ON',-1)
Execute.PauseSeconds(5)

retVal = SmartStudio.WNS_GetStatus(pStatusSmartStudio)
if int(pStatusSmartStudio) == SmartStudioFunc.STAT_SIMULATION and (retVal == SmartStudioFunc.TRUE):
	retVal = SmartStudio.StopSimulation()

#-------------------------------------------------------------------------------------------------
# Parse the log below per requirement of test case
# Verification of Log - com.tmobile.echolocate.log.manually.txt based on expected results:
# - Determine results by calling:
#   1. Outcome.Pass('Test Pass.')
#   2. Outcome.Fail('Test Fail.')
#-------------------------------------------------------------------------------------------------
logDate = GetDataFromLog(0)
logTime = GetDataFromLog(1)
Log.Informational("Log Date:" + logDate)
Log.Informational("Log Time:" + logTime)

mcc = GetDataFromLog(5) # networkIdentity.mcc 
mnc = GetDataFromLog(6) # networkIdentity.mnc

if mcc == '310' and mnc == '260':
	Outcome.Pass('Test Pass.')
else:
	Log.Informational("mcc=" + mcc)
	Log.Informational("mnc=" + mnc)
	Outcome.Fail('Test Fail.')