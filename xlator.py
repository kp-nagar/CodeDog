# xlator.py

from progSpec import cdErr

class Xlator(object):
    def getContainerType(self, typeSpec, actionOrField):
        cdErr("In base class Xlator::getContainerType.")

    def adjustBaseTypes(self, fieldType, isContainer):
        cdErr("In base class Xlator::adjustBaseTypes.")

    def applyOwner(self, typeSpec, owner, langType):
        cdErr("In base class Xlator::applyOwner.")

    def getUnwrappedClassOwner(self, classes, typeSpec, fieldType, varMode, ownerIn):
        cdErr("In base class Xlator::getUnwrappedClassOwner.")

    def getReqTagString(self, classes, typeSpec):
        cdErr("In base class Xlator::getReqTagString.")

    def xlateLangType(self, classes, typeSpec, owner, fTypeKW, varMode, actionOrField):
        cdErr("In base class Xlator::xlateLangType.")

    def makePtrOpt(self, typeSpec):
        cdErr("In base class Xlator::makePtrOpt.")

    def codeIteratorOperation(self, itrCommand, fieldType):
        cdErr("In base class Xlator::codeIteratorOperation.")

    def recodeStringFunctions(self, name, typeSpec):
        cdErr("In base class Xlator::recodeStringFunctions.")

    def langStringFormatterCommand(self, fmtStr, argStr):
        cdErr("In base class Xlator::langStringFormatterCommand.")

    def LanguageSpecificDecorations(self, S, typeSpec, owner, LorRorP_Val):
        cdErr("In base class Xlator::LanguageSpecificDecorations.")

    def convertToInt(self, S, typeSpec):
        cdErr("In base class Xlator::convertToInt.")

    def checkForTypeCastNeed(self, lhsTypeSpec, rhsTypeSpec, RHScodeStr):
        cdErr("In base class Xlator::checkForTypeCastNeed.")

    def getTheDerefPtrMods(self, itemTypeSpec):
        cdErr("In base class Xlator::getTheDerefPtrMods.")

    def derefPtr(self, varRef, itemTypeSpec):
        cdErr("In base class Xlator::derefPtr.")

    def ChoosePtrDecorationForSimpleCase(self, owner):
        cdErr("In base class Xlator::ChoosePtrDecorationForSimpleCase.")

    def chooseVirtualRValOwner(self, LVAL, RVAL):
        cdErr("In base class Xlator::chooseVirtualRValOwner.")

    def determinePtrConfigForNewVars(self, LSpec, RSpec, useCtor):
        cdErr("In base class Xlator::determinePtrConfigForNewVars.")

    def determinePtrConfigForAssignments(self, LVAL, RVAL, assignTag, codeStr):
        cdErr("In base class Xlator::determinePtrConfigForAssignments.")

    def getCodeAllocStr(self, varTypeStr, owner):
        cdErr("In base class Xlator::getCodeAllocStr.")

    def getCodeAllocSetStr(self, varTypeStr, owner, value):
        cdErr("In base class Xlator::getCodeAllocSetStr.")

    def getConstIntFieldStr(self, fieldName, fieldValue, intSize):
        cdErr("In base class Xlator::getConstIntFieldStr.")

    def getEnumStr(self, fieldName, enumList):
        cdErr("In base class Xlator::getEnumStr.")

    def codeIdentityCheck(self, S, S2, retType1, retType2, opIn):
        cdErr("In base class Xlator::codeIdentityCheck.")

    def codeComparisonStr(self, S, S2, retType1, retType2, op):
        cdErr("In base class Xlator::codeComparisonStr.")

    def getContaineCategory(self, containerSpec):
        cdErr("In base class Xlator::getContaineCategory.")

    def getContainerTypeInfo(self, containerType, name, idxType, typeSpecIn, paramList, genericArgs):
        cdErr("In base class Xlator::getContainerTypeInfo.")

    def codeArrayIndex(self, idx, containerType, LorR_Val, previousSegName, idxTypeSpec):
        cdErr("In base class Xlator::codeArrayIndex.")

    def codeRangeSpec(self, traversalMode, ctrType, repName, S_low, S_hi, indent):
        cdErr("In base class Xlator::codeRangeSpec.")

    def iterateRangeFromTo(self, classes,localVarsAlloc,StartKey,EndKey,ctnrTSpec,repName,ctnrName,indent):
        cdErr("In base class Xlator::iterateRangeFromTo.")

    def iterateContainerStr(self, classes,localVarsAlloc,ctnrTSpec,repName,ctnrName,isBackward,indent,genericArgs):
        cdErr("In base class Xlator::iterateContainerStr.")

    def codeSwitchExpr(self, switchKeyExpr, switchKeyTypeSpec):
        cdErr("In base class Xlator::codeSwitchExpr.")

    def codeSwitchCase(self, caseKeyValue, caseKeyTypeSpec):
        cdErr("In base class Xlator::codeSwitchCase.")

    def codeNotOperator(self, S, S2,retTypeSpec):
        cdErr("In base class Xlator::codeNotOperator.")

    def codeFactor(self, item, objsRefed, returnType, expectedTypeSpec, LorRorP_Val, genericArgs):
        cdErr("In base class Xlator::codeFactor.")

    def adjustQuotesForChar(self, typeSpec1, typeSpec2, S):
        cdErr("In base class Xlator::adjustQuotesForChar.")

    def adjustConditional(self, S, conditionType):
        cdErr("In base class Xlator::adjustConditional.")

    def codeSpecialReference(sself, egSpec, objsRefed, genericArgs):
        cdErr("In base class Xlator::codeSpecialReference.")

    def checkIfSpecialAssignmentFormIsNeeded(self, AltIDXFormat, RHS, rhsType, LHS, LHSParentType, LHS_FieldType):
        cdErr("In base class Xlator::checkIfSpecialAssignmentFormIsNeeded.")

    def codeMain(self, classes, tags, objsRefed):
        cdErr("In base class Xlator::codeMain.")

    def codeArgText(self, argFieldName, argType, argOwner, typeSpec, makeConst, typeArgList):
        cdErr("In base class Xlator::codeArgText.")

    def codeStructText(self, classes, attrList, parentClass, classInherits, classImplements, structName, structCode, tags):
        cdErr("In base class Xlator::codeStructText.")

    def produceTypeDefs(self, typeDefMap):
        cdErr("In base class Xlator::produceTypeDefs.")

    def addSpecialCode(self, filename):
        cdErr("In base class Xlator::addSpecialCode.")

    def addGLOBALSpecialCode(self, classes, tags):
        cdErr("In base class Xlator::addGLOBALSpecialCode.")

    def variableDefaultValueString(self, fieldType, isTypeArg, owner):
        cdErr("In base class Xlator::variableDefaultValueString.")

    def codeNewVarStr(self, classes, tags, lhsTypeSpec, varName, fieldDef, indent, objsRefed, actionOrField, genericArgs, localVarsAllocated):
        cdErr("In base class Xlator::codeNewVarStr.")

    def codeIncrement(self, varName):
        cdErr("In base class Xlator::codeIncrement.")

    def codeDecrement(self, varName):
        cdErr("In base class Xlator::codeDecrement.")

    def isNumericType(self, convertedType):
        cdErr("In base class Xlator::isNumericType.")

    def codeVarFieldRHS_Str(self, fieldName, cvrtType, innerType, typeSpec, paramList, objsRefed, isAllocated, typeArgList, genericArgs):
        cdErr("In base class Xlator::codeVarFieldRHS_Str.")

    def codeConstField_Str(self, convertedType, fieldName, fieldValueText, className, indent):
        cdErr("In base class Xlator::codeConstField_Str.")

    def codeVarField_Str(self, convertedType, typeSpec, fieldName, fieldValueText, className, tags, typeArgList, indent):
        cdErr("In base class Xlator::codeVarField_Str.")

    def codeConstructor(self, className, ctorArgs, callSuper, ctorInit, funcBody):
        cdErr("In base class Xlator::codeConstructor.")

    def codeConstructors(self, className, ctorArgs, ctorOvrRide, ctorInit, copyCtorArgs, funcBody, callSuper):
        cdErr("In base class Xlator::codeConstructors.")

    def codeConstructorInit(self, fieldName, count, defaultVal):
        cdErr("In base class Xlator::codeConstructorInit.")

    def codeConstructorArgText(self, argFieldName, count, argType, defaultVal):
        cdErr("In base class Xlator::codeConstructorArgText.")

    def codeCopyConstructor(self, fieldName, convertedType, isTemplateVar):
        cdErr("In base class Xlator::codeCopyConstructor.")

    def codeConstructorCall(self, className):
        cdErr("In base class Xlator::codeConstructorCall.")

    def codeSuperConstructorCall(self, parentClassName):
        cdErr("In base class Xlator::codeSuperConstructorCall.")

    def codeFuncHeaderStr(self, className, fieldName, returnType, argListText, localArgsAllocated, inheritMode, overRideOper, isConstructor, typeArgList, typeSpec, indent):
        cdErr("In base class Xlator::codeFuncHeaderStr.")

    def getVirtualFuncText(self, field):
        cdErr("In base class Xlator::getVirtualFuncText.")

    def codeTemplateHeader(self, structName, typeArgList):
        cdErr("In base class Xlator::codeTemplateHeader.")

    def extraCodeForTopOfFuntion(self, argList):
        cdErr("In base class Xlator::extraCodeForTopOfFuntion.")

    def codeSetBits(self, LHS_Left, LHS_FieldType, prefix, bitMask, RHS, rhsType):
        cdErr("In base class Xlator::codeSetBits.")

    def codeSwitchBreak(self, caseAction, indent):
        cdErr("In base class Xlator::codeSwitchBreak.")

    def applyTypecast(self, typeInCodeDog, itemToAlterType):
        cdErr("In base class Xlator::applyTypecast.")

    def includeDirective(self, libHdr):
        cdErr("In base class Xlator::includeDirective.")

    def generateMainFunctionality(self, classes, tags):
        cdErr("In base class Xlator::generateMainFunctionality.")

    def __init__(self):
        cdErr("In base class Xlator::__init__.")
