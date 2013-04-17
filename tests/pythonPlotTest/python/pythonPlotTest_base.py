#!/usr/bin/env python
#
# AUTO-GENERATED CODE.  DO NOT MODIFY!
#
# Source: pythonPlotTest.spd.xml
# Generated on: Tue Jul 17 16:47:15 EDT 2012
# Redhawk IDE
# Version:@buildLabel@
# Build id: @buildId@
from ossie.cf import CF, CF__POA
from ossie.utils import uuid

from ossie.resource import Resource
from ossie.properties import simple_property

import Queue, copy, time, threading
from ossie.resource import usesport, providesport
from ossie.cf import ExtendedCF
from omniORB import CORBA
import struct #@UnresolvedImport
from bulkio.bulkioInterfaces import BULKIO, BULKIO__POA #@UnusedImport 

NOOP = -1
NORMAL = 0
FINISH = 1
class ProcessThread(threading.Thread):
    def __init__(self, target, pause=0.0125):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.target = target
        self.pause = pause
        self.stop_signal = threading.Event()

    def stop(self):
        self.stop_signal.set()

    def updatePause(self, pause):
        self.pause = pause

    def run(self):
        state = NORMAL
        while (state != FINISH) and (not self.stop_signal.isSet()):
            state = self.target()
            if (state == NOOP):
                # If there was no data to process sleep to avoid spinning
                time.sleep(self.pause)

class pythonPlotTest_base(CF__POA.Resource, Resource):
        # These values can be altered in the __init__ of your derived class

        PAUSE = 0.0125 # The amount of time to sleep if process return NOOP
        TIMEOUT = 5.0 # The amount of time to wait for the process thread to die when stop() is called
        DEFAULT_QUEUE_SIZE = 100 # The number of BulkIO packets that can be in the queue before pushPacket will block
        
        def __init__(self, identifier, execparams):
            loggerName = (execparams['NAME_BINDING'].replace('/', '.')).rsplit("_", 1)[0]
            Resource.__init__(self, identifier, execparams, loggerName=loggerName)
            self.process_thread = None
            # self.auto_start is deprecated and is only kept for API compatability
            # with 1.7.X and 1.8.0 components.  This variable may be removed
            # in future releases
            self.auto_start = False
            
        def initialize(self):
            Resource.initialize(self)
            
            # Instantiate the default implementations for all ports on this component

            self.port_dataDouble = PortBULKIODataDoubleOut_i(self, "dataDouble")
            self.port_dataFloat = PortBULKIODataFloatOut_i(self, "dataFloat")
            self.port_dataLong = PortBULKIODataLongOut_i(self, "dataLong")
            self.port_dataLongLong = PortBULKIODataLongLongOut_i(self, "dataLongLong")
            self.port_dataOctet = PortBULKIODataOctetOut_i(self, "dataOctet")
            self.port_dataShort = PortBULKIODataShortOut_i(self, "dataShort")
            self.port_dataUlong = PortBULKIODataUlongOut_i(self, "dataUlong")
            self.port_dataUlongLong = PortBULKIODataUlongLongOut_i(self, "dataUlongLong")
            self.port_dataUshort = PortBULKIODataUshortOut_i(self, "dataUshort")

        def start(self):
            Resource.start(self)
            if self.process_thread == None:
                self.process_thread = ProcessThread(target=self.process, pause=self.PAUSE)
                self.process_thread.start()

        def process(self):
            """The process method should process a single "chunk" of data and then return.  This method will be called
            from the processing thread again, and again, and again until it returns FINISH or stop() is called on the
            component.  If no work is performed, then return NOOP"""
            raise NotImplementedError

        def stop(self):
            # Technically not thread-safe but close enough for now
            process_thread = self.process_thread
            self.process_thread = None

            if process_thread != None:
                process_thread.stop()
                process_thread.join(self.TIMEOUT)
                if process_thread.isAlive():
                    raise CF.Resource.StopError(CF.CF_NOTSET, "Processing thread did not die")
            Resource.stop(self)

        def releaseObject(self):
            try:
                self.stop()
            except Exception:
                self._log.exception("Error stopping")
            Resource.releaseObject(self)

        ######################################################################
        # PORTS
        # 
        # DO NOT ADD NEW PORTS HERE.  You can add ports in your derived class, in the SCD xml file, 
        # or via the IDE.
        
        def compareSRI(self, a, b):
            if a.hversion != b.hversion:
                return False
            if a.xstart != b.xstart:
                return False
            if a.xdelta != b.xdelta:
                return False
            if a.xunits != b.xunits:
                return False
            if a.subsize != b.subsize:
                return False
            if a.ystart != b.ystart:
                return False
            if a.ydelta != b.ydelta:
                return False
            if a.yunits != b.yunits:
                return False
            if a.mode != b.mode:
                return False
            if a.streamID != b.streamID:
                return False
            if a.blocking != b.blocking:
                return False
            if len(a.keywords) != len(b.keywords):
                return False
            for keyA, keyB in zip(a.keywords, b.keywords):
                if keyA.value._t != keyB.value._t:
                    return False
                if keyA.value._v != keyB.value._v:
                    return False
            return True


        # 'BULKIO/dataUshort' port
        class PortBULKIODataUshortOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataUshort port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataLongLong' port
        class PortBULKIODataLongLongOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataLongLong port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataShort' port
        class PortBULKIODataShortOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataShort port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataUlong' port
        class PortBULKIODataUlongOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataUlong port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataFloat' port
        class PortBULKIODataFloatOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataFloat port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataDouble' port
        class PortBULKIODataDoubleOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataDouble port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataUlongLong' port
        class PortBULKIODataUlongLongOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataUlongLong port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataLong' port
        class PortBULKIODataLongOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataLong port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass


        # 'BULKIO/dataOctet' port
        class PortBULKIODataOctetOut(BULKIO__POA.UsesPortStatisticsProvider):
            """This class is a port template for the dataOctet port and
            should not be instantiated nor modified.
            
            The expectation is that the specific port implementation will extend 
            from this class instead of the base CORBA class CF__POA.Port.
            """
            pass

        port_dataDouble = usesport(name="dataDouble",
                                            repid="IDL:BULKIO/dataDouble:1.0",
                                            type_="data",)

        port_dataFloat = usesport(name="dataFloat",
                                            repid="IDL:BULKIO/dataFloat:1.0",
                                            type_="data",)

        port_dataLong = usesport(name="dataLong",
                                            repid="IDL:BULKIO/dataLong:1.0",
                                            type_="data",)

        port_dataLongLong = usesport(name="dataLongLong",
                                            repid="IDL:BULKIO/dataLongLong:1.0",
                                            type_="control",)

        port_dataOctet = usesport(name="dataOctet",
                                            repid="IDL:BULKIO/dataOctet:1.0",
                                            type_="data",)

        port_dataShort = usesport(name="dataShort",
                                            repid="IDL:BULKIO/dataShort:1.0",
                                            type_="data",)

        port_dataUlong = usesport(name="dataUlong",
                                            repid="IDL:BULKIO/dataUlong:1.0",
                                            type_="control",)

        port_dataUlongLong = usesport(name="dataUlongLong",
                                            repid="IDL:BULKIO/dataUlongLong:1.0",
                                            type_="data",)

        port_dataUshort = usesport(name="dataUshort",
                                            repid="IDL:BULKIO/dataUshort:1.0",
                                            type_="data",)        

        ######################################################################
        # PROPERTIES
        # 
        # DO NOT ADD NEW PROPERTIES HERE.  You can add properties in your derived class, in the PRF xml file
        # or by using the IDE.       
        frequency = simple_property(id_="DCE:0fdbf3a0-b0cc-486d-a9d6-8f6f9c59a1c8",
                                          name="frequency", 
                                          type_="double",
                                          defvalue=1000,
                                          units="Hz", 
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )       
        sample_rate = simple_property(id_="DCE:f1c18ed4-8e87-4c1a-b7b0-f88f4c4d0bfb",
                                          name="sample_rate", 
                                          type_="double",
                                          defvalue=5000,
                                          units="Hz", 
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )       
        magnitude = simple_property(id_="DCE:8c6aa87d-7242-4819-aec5-83902182fb8f",
                                          name="magnitude", 
                                          type_="double",
                                          defvalue=1,
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )       
        shape = simple_property(id_="DCE:424e864a-7561-435e-ad53-1857d0bed75b",
                                          name="shape", 
                                          type_="string",
                                          defvalue="sine",
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )       
        xfer_len = simple_property(id_="DCE:c6344083-2a6d-4491-aed4-63510295ea92",
                                          name="xfer_len", 
                                          type_="long",
                                          defvalue=1000,
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )       
        throttle = simple_property(id_="DCE:cd4b1959-c600-4ae1-9bf9-038c4a0c8f1b",
                                          name="throttle", 
                                          type_="boolean",
                                          defvalue=True,
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",),
                                          description="""If true, the data will approximately be throttled based on the sample_rate.""" 
                                          )       
        stream_id = simple_property(id_="DCE:0e8b57b0-6143-4555-9d72-b707676ea0b0",
                                          name="stream_id", 
                                          type_="string",
                                          mode="readwrite",
                                          action="external",
                                          kinds=("configure",)
                                          )

'''uses port(s)'''


class PortBULKIODataUshortOut_i(pythonPlotTest_base.PortBULKIODataUshortOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('c') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataUshort)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataLongLongOut_i(pythonPlotTest_base.PortBULKIODataLongLongOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('c') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataLongLong)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataShortOut_i(pythonPlotTest_base.PortBULKIODataShortOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('h') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataShort)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataUlongOut_i(pythonPlotTest_base.PortBULKIODataUlongOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('L') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataUlong)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataFloatOut_i(pythonPlotTest_base.PortBULKIODataFloatOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('f') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataFloat)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataDoubleOut_i(pythonPlotTest_base.PortBULKIODataDoubleOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('d') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataDouble)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataUlongLongOut_i(pythonPlotTest_base.PortBULKIODataUlongLongOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('c') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataUlongLong)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataLongOut_i(pythonPlotTest_base.PortBULKIODataLongOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('c') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataLong)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 


class PortBULKIODataOctetOut_i(pythonPlotTest_base.PortBULKIODataOctetOut):
    class linkStatistics:
        class statPoint:
            def __init__(self):
                self.elements = 0
                self.queueSize = 0.0
                self.secs = 0.0
                self.streamID = ""

        def __init__(self, port_ref):
            self.enabled = True
            self.bitSize = struct.calcsize('B') * 8
            self.historyWindow = 10
            self.receivedStatistics = {}
            self.port_ref = port_ref
            self.receivedStatistics_idx = {}

        def setEnabled(self, enableStats):
            self.enabled = enableStats

        def update(self, elementsReceived, queueSize, streamID, connectionId):
            if not self.enabled:
                return

            if self.receivedStatistics.has_key(connectionId):
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId]%self.historyWindow
            else:
                self.receivedStatistics[connectionId] = []
                self.receivedStatistics_idx[connectionId] = 0
                for i in range(self.historyWindow):
                    self.receivedStatistics[connectionId].append(self.statPoint())
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].elements = elementsReceived
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].queueSize = queueSize
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].secs = time.time()
                self.receivedStatistics[connectionId][self.receivedStatistics_idx[connectionId]].streamID = streamID
                self.receivedStatistics_idx[connectionId] += 1
                self.receivedStatistics_idx[connectionId] = self.receivedStatistics_idx[connectionId] % self.historyWindow

        def retrieve(self):
            if not self.enabled:
                return

            retVal = []
            for entry in self.receivedStatistics:
                runningStats = BULKIO.PortStatistics(portName=self.port_ref.name,averageQueueDepth=-1,elementsPerSecond=-1,bitsPerSecond=-1,callsPerSecond=-1,streamIDs=[],timeSinceLastCall=-1,keywords=[])

                listPtr = (self.receivedStatistics_idx[entry] + 1) % self.historyWindow    # don't count the first set of data, since we're looking at change in time rather than absolute time
                frontTime = self.receivedStatistics[entry][(self.receivedStatistics_idx[entry] - 1) % self.historyWindow].secs
                backTime = self.receivedStatistics[entry][self.receivedStatistics_idx[entry]].secs
                totalData = 0.0
                queueSize = 0.0
                streamIDs = []
                while (listPtr != self.receivedStatistics_idx[entry]):
                    totalData += self.receivedStatistics[entry][listPtr].elements
                    queueSize += self.receivedStatistics[entry][listPtr].queueSize
                    streamIDptr = 0
                    foundstreamID = False
                    while (streamIDptr != len(streamIDs)):
                        if (streamIDs[streamIDptr] == self.receivedStatistics[entry][listPtr].streamID):
                            foundstreamID = True
                            break
                        streamIDptr += 1
                    if (not foundstreamID):
                        streamIDs.append(self.receivedStatistics[entry][listPtr].streamID)
                    listPtr += 1
                    listPtr = listPtr % self.historyWindow

                currentTime = time.time()
                totalTime = currentTime - backTime
                if totalTime == 0:
                    totalTime = 1e6
                receivedSize = len(self.receivedStatistics[entry])
                runningStats.bitsPerSecond = (totalData * self.bitSize) / totalTime
                runningStats.elementsPerSecond = totalData/totalTime
                runningStats.averageQueueDepth = queueSize / receivedSize
                runningStats.callsPerSecond = float((receivedSize - 1)) / totalTime
                runningStats.streamIDs = streamIDs
                runningStats.timeSinceLastCall = currentTime - frontTime
                usesPortStat = BULKIO.UsesPortStatistics(connectionId=entry, statistics=runningStats)
                retVal.append(usesPortStat)
            return retVal

    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.outConnections = {} # key=connectionId,  value=port
        self.refreshSRI = False
        self.stats = self.linkStatistics(self)
        self.port_lock = threading.Lock()
        self.sriDict = {} # key=streamID  value=StreamSRI

    def connectPort(self, connection, connectionId):
        self.port_lock.acquire()
        try:
            port = connection._narrow(BULKIO.dataOctet)
            self.outConnections[str(connectionId)] = port
            self.refreshSRI = True
        finally:
            self.port_lock.release()

    def disconnectPort(self, connectionId):
        self.port_lock.acquire()
        try:
            self.outConnections.pop(str(connectionId), None)
        finally:
            self.port_lock.release()

    def enableStats(self, enabled):
        self.stats.setEnabled(enabled)
        
    def _get_connections(self):
        currentConnections = []
        self.port_lock.acquire()
        for id_, port in self.outConnections.items():
            currentConnections.append(ExtendedCF.UsesConnection(id_, port))
        self.port_lock.release()
        return currentConnections

    def _get_statistics(self):
        self.port_lock.acquire()
        recStat = self.stats.retrieve()
        self.port_lock.release()
        return recStat

    def _get_state(self):
        self.port_lock.acquire()
        numberOutgoingConnections = len(self.outConnections)
        self.port_lock.release()
        if numberOutgoingConnections == 0:
            return BULKIO.IDLE
        else:
            return BULKIO.ACTIVE
        return BULKIO.BUSY

    def _get_activeSRIs(self):
        self.port_lock.acquire()
        sris = []
        for entry in self.sriDict:
            sris.append(copy.deepcopy(self.sriDict[entry]))
        self.port_lock.release()
        return sris

    def pushSRI(self, H):
        self.port_lock.acquire()
        self.sriDict[H.streamID] = copy.deepcopy(H)
        try:
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushSRI(H)
            except Exception:
                self.parent._log.exception("The call to pushSRI failed on port %s connection %s instance %s", self.name, connId, port)
                raise
        finally:
            self.refreshSRI = False
            self.port_lock.release()

    def pushPacket(self, data, T, EOS, streamID):
        if self.refreshSRI:
            if self.sriDict.has_key(streamID): 
                self.pushSRI(self.sriDict[streamID])

        self.port_lock.acquire()

        try:    
            try:
                for connId, port in self.outConnections.items():
                    if port != None:
                        port.pushPacket(data, T, EOS, streamID)
                        self.stats.update(len(data), 0, streamID, connId)
            except Exception:
                self.parent._log.exception("The call to pushPacket failed on port %s connection %s instance %s", self.name, connId, port)
                raise
            if EOS==True:
                if self.sriDict.has_key(streamID):
                    tmp = self.sriDict.pop(streamID)
        finally:
            self.port_lock.release()
 
