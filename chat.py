def SetChatColor(iType, r, g, b):
	pass

def Clear():
	pass

def Close():
	pass

def CreateChatSet(iID):
	pass

def Update(iID):
	pass

def Render(iID):
	pass

def SetBoardState(iID, iState):
	pass

def SetPosition(iID, ix, iy):
	pass

def SetHeight(iID, iHeight):
	pass

def SetStep(iID, iStep):
	pass

def ToggleChatMode(iID, iType):
	pass

def EnableChatMode(iID, iType):
	pass

def DisableChatMode(iID, iType):
	pass

def SetEndPos(iID, fPos):
	pass

def GetLineCount(iID):
	pass

def GetVisibleLineCount(iID):
	pass

def GetLineStep(iID):
	pass

def AppendChat(iType, szChat):
	pass

def AppendChatWithDelay(iType, szChat, iDelay):
	pass

def ArrangeShowingChat(iID):
	pass

def IgnoreCharacter(szName):
	pass

def IsIgnoreCharacter(szName):
	pass

def CreateWhisper(szName):
	pass

def AppendWhisper(iType, szName, szChat):
	pass

def RenderWhisper(szName, fx, fy):
	pass

def SetWhisperBoxSize(szName, fWidth, fHeight):
	pass

def SetWhisperPosition(szName, fPosition):
	pass

def ClearWhisper(szName):
	pass

def InitWhisper(poInterface):
	pass

def GetLinkFromHyperlink(szHyperlink):
	pass

CHAT_TYPE_TALKING = None
CHAT_TYPE_INFO = None
CHAT_TYPE_NOTICE = None
CHAT_TYPE_PARTY = None
CHAT_TYPE_GUILD = None
CHAT_TYPE_COMMAND = None
CHAT_TYPE_SHOUT = None
CHAT_TYPE_WHISPER = None
WHISPER_TYPE_CHAT = None
WHISPER_TYPE_SYSTEM = None
WHISPER_TYPE_GM = None
BOARD_STATE_VIEW = None
BOARD_STATE_EDIT = None
BOARD_STATE_LOG = None
CHAT_SET_CHAT_WINDOW = None
CHAT_SET_LOG_WINDOW = None
