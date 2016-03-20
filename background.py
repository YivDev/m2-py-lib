def IsSoftwareTiling():
	pass

def EnableSoftwareTiling(nIsEnable):
	pass

def EnableSnow(nIsEnable):
	pass

def GlobalPositionToLocalPosition(iX, iY):
	pass

def GlobalPositionToMapInfo(iX, iY):
	pass

def GetRenderShadowTime():
	pass

def LoadMap(szMapPathName, fx, fy, fz):
	pass

def Destroy():
	pass

def RegisterEnvironmentData(iIndex, szEnvironmentFileName):
	pass

def SetEnvironmentData(iIndex):
	pass

def GetCurrentMapName():
	pass

def GetPickingPoint():
	pass

def BeginEnvironment():
	pass

def EndEnvironment():
	pass

def SetCharacterDirLight():
	pass

def SetBackgroundDirLight():
	pass

def Initialize():
	pass

def Update(fCameraX, fCameraY, fCameraZ):
	pass

def Render():
	pass

def RenderPCBlocker():
	pass

def RenderCollision():
	pass

def RenderSky():
	pass

def RenderCloud():
	pass

def RenderWater():
	pass

def RenderEffect():
	pass

def RenderBeforeLensFlare():
	pass

def RenderAfterLensFlare():
	pass

def RenderCharacterShadowToTexture():
	pass

def RenderDungeon():
	pass

def GetHeight(fx, fy):
	pass

def SetShadowLevel(iLevel):
	pass

def SetVisiblePart(ePart, isVisible):
	pass

def GetShadowMapColor(fx, fy):
	pass

def SetSplatLimit(iSplatNum):
	pass

def GetRenderedSplatNum():
	pass

def GetRenderedGraphicThingInstanceNum():
	pass

def SelectViewDistanceNum(iNum):
	pass

def SetViewDistanceSet(iNum, fFarClip):
	pass

def GetFarClip():
	pass

def GetDistanceSetInfo():
	pass

def SetBGLoading(bBGLoading):
	pass

def SetRenderSort(eSort):
	pass

def SetTransparentTree(bTransparent):
	pass

def SetXMasTree(iGrade):
	pass

def RegisterDungeonMapName(szName):
	pass

def VisibleGuildArea():
	pass

def DisableGuildArea():
	pass

def WarpTest(iX, iY):
	pass

PART_SKY = None
PART_TREE = None
PART_CLOUD = None
PART_WATER = None
PART_OBJECT = None
PART_TERRAIN = None
SKY_RENDER_MODE_DEFAULT = None
SKY_RENDER_MODE_DIFFUSE = None
SKY_RENDER_MODE_TEXTURE = None
SKY_RENDER_MODE_MODULATE = None
SKY_RENDER_MODE_MODULATE2X = None
SKY_RENDER_MODE_MODULATE4X = None
SHADOW_NONE = None
SHADOW_GROUND = None
SHADOW_GROUND_AND_SOLO = None
SHADOW_ALL = None
SHADOW_ALL_HIGH = None
SHADOW_ALL_MAX = None
DISTANCE0 = None
DISTANCE1 = None
DISTANCE2 = None
DISTANCE3 = None
DISTANCE4 = None
DISTANCE_SORT = None
TEXTURE_SORT = None
