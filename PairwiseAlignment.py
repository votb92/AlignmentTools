from abc import ABC, abstractmethod


class PairwiseAlignment(ABC):
    def __init__(self, seq1, seq2):
        self._firstHeader = seq1.getSeqID()
        self._firstSequence = seq1.getSeq()
        self._secondHeader = seq2.getSeqID()
        self._secondSequence = seq2.getSeq()

    def getFirstHeader(self):
        return self._firstHeader

    def getSecondHeader(self):
        return self._secondHeader

    def getFirstSequence(self):
        return self._firstSequence

    def getSecondSequence(self):
        return self._secondSequence

    def setFirstHeader(self, frstHdr):
        self._firstHeader = frstHdr

    def setSecondHeader(self, scndHdr):
        self._secondHeader = scndHdr

    def setFirstSequence(self, frstSq):
        self._firstSequence = frstSq

    def setSecondSequence(self, scndHdr):
        self._secondSequence = scndHdr

    def getMatchCount(self):
        pass

    def setMatchCount(self):
        pass

    def getMismatchCount(self):
        pass

    def setMismatchCount(self):
        pass

    def getGapCount(self):
        pass

    def setGapCount(self):
        pass
