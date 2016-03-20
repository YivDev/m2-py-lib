def SetPathName(szPathName):
	pass

def RegisterSkill(iSkillIndex, szFileName):
	pass

def LoadSkillData():
	pass

def ClearSkillData():
	pass

def GetSkillName(iSkillIndex):
	pass

def GetSkillDescription(iSkillIndex):
	pass

def GetSkillType(iSkillIndex):
	pass

def GetSkillConditionDescriptionCount(iSkillIndex):
	pass

def GetSkillConditionDescription(iSkillIndex, iConditionIndex):
	pass

def GetSkillAffectDescriptionCount(iSkillIndex):
	pass

def GetSkillAffectDescription(iSkillIndex, iAffectIndex, fSkillPoint):
	pass

def GetSkillCoolTime(iSkillIndex, fSkillPoint):
	pass

def GetSkillNeedSP(iSkillIndex, fSkillPoint):
	pass

def GetSkillContinuationSP(iSkillIndex, fSkillPoint):
	pass

def GetSkillMaxLevel(iSkillIndex):
	pass

def GetSkillLevelUpPoint(iSkillIndex):
	pass

def GetSkillLevelLimit(iSkillIndex):
	pass

def IsSkillRequirement(iSkillIndex):
	pass

def GetSkillRequirementData(iSkillIndex):
	pass

def GetSkillRequireStatCount(iSkillIndex):
	pass

def GetSkillRequireStatData(iSkillIndex, iStatIndex):
	pass

def CanLevelUpSkill(iSkillIndex, iSkillLevel):
	pass

def IsLevelUpSkill(iSkillIndex):
	pass

def CheckRequirementSueccess(iSkillIndex):
	pass

def GetNeedCharacterLevel(iSkillIndex):
	pass

def IsToggleSkill(iSkillIndex):
	pass

def IsUseHPSkill(iSkillIndex):
	pass

def IsStandingSkill(iSkillIndex):
	pass

def CanUseSkill(iSkillIndex):
	pass

def GetIconName(iSkillIndex):
	pass

def GetIconImage(iSkillIndex):
	pass

def GetIconImageNew(iSkillIndex, iGradeIndex):
	pass

def GetIconInstance(iSkillIndex):
	pass

def GetIconInstanceNew(iSkillIndex, iGradeIndex):
	pass

def DeleteIconInstance(iHandle):
	pass

def GetGradeData(iSkillIndex, iGradeIndex):
	pass

def GetNewAffectDataCount(iSkillIndex):
	pass

def GetNewAffectData(iSkillIndex, iAffectIndex, fSkillLevel):
	pass

def GetDuration(iSkillIndex, fSkillLevel):
	pass

def TEST():
	pass

SKILL_TYPE_NONE = None
SKILL_TYPE_ACTIVE = None
SKILL_TYPE_SUPPORT = None
SKILL_TYPE_GUILD = None
SKILL_TYPE_HORSE = None
SKILL_TYPE_MAX_NUM = None
SKILL_GRADE_COUNT = None
SKILL_GRADE_STEP_COUNT = None
SKILL_GRADEGAP = None
SKILL_EFFECT_COUNT = None
