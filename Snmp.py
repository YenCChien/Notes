from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902

def SnmpGet(target,OID,a=1,community='public'):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((target, 161)),
        OID,
    )
    if errorIndication:
        return(errorIndication)
    else:
        if errorStatus:
            return('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            result = {}
            for name, val in varBinds:
                result.update({name.__str__():val.prettyPrint().__str__()})
            return result

def SnmpSet(target,OID,index,syntax,value):
    cmdGen = cmdgen.CommandGenerator()
    syntaxDict = {'i32':'Integer32','u32':'Unsigned32','c32':'Counter32','g32':'Gauge32','t':'TimeTicks','ip':'IP address','oid':'OID','o':'OctetString','c64':'Counter64',
        'opa':'Opaque','n':'Nsapaddr','b':'Bits','i':'Integer'
    }
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.setCmd(
        cmdgen.CommunityData('private'),
        cmdgen.UdpTransportTarget((target, 161)),
        ((OID+'.'+index), eval('rfc1902'+'.'+syntaxDict[syntax]+'({})'.format(value)))
    )
    if errorIndication:
        return(errorIndication)
    else:
        if errorStatus:
            return('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                return('%s' % (val.prettyPrint()))

def SnmpWalk(target,OID,a=1,community='public'):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((target, 161)),
        OID,
    )
    if errorIndication:
        return(errorIndication)
    else:
        if errorStatus:
            return('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                )
            )
        else:
            result = {}
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    result.update({name.__str__():val.prettyPrint().__str__()})
            return result
