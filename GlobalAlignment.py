from Project.AlignmentTools.StringManipulation import *
from Project.AlignmentTools.PairwiseAlignment import *
import numpy


class Global(PairwiseAlignment):

    def __init__(self, seq1, seq2):
        super().__init__(seq1, seq2)

        self._match = 1
        self._mismatch = -1
        self._gap = -2
        self._matchCount = 0
        self._mismatchCount = 0
        self._gapCount = 0

    def getFirstHeader(self):
        return super().getFirstHeader()

    def getSecondHeader(self):
        return super().getSecondHeader()

    def getFirstSequence(self):
        return super().getFirstSequence()

    def getSecondSequence(self):
        return super().getSecondSequence()

    def setFirstHeader(self, frstHdr):
        super().setFirstHeader(frstHdr)

    def setSecondHeader(self, scndHdr):
        super().setSecondHeader(scndHdr)

    def setFirstSequence(self, frstSq):
        super().setFirstSequence(frstSq)

    def setSecondSequence(self, scndHdr):
        super().setSecondSequence(scndHdr)

    def getMatchCount(self):
        return self._matchCount

    def setMatchCount(self, match):
        self._matchCount = match

    def getMismatchCount(self):
        return self._mismatchCount

    def setMismatchCount(self, mismatch):
        self._mismatchCount = mismatch

    def getGapCount(self):
        return self._gapCount

    def setGapCount(self, gap):
        self._gapCount = gap

    def getGapCost(self):
        return self._gap

    def getMismatchCost(self):
        return self._mismatch

    def getMatchCost(self):
        return self._match

    def setgapCost(self, gapCost):
        self._gap = gapCost

    def setMatchCost(self, matchCost):
        self._match = matchCost

    def setMismatchCost(self, MismatchCost):
        self._mismatch = MismatchCost

    def globalAlignment(self):
        frst_len = len(self.getFirstSequence())
        scnd_len = len(self.getSecondSequence())
        matrixShape = (frst_len + 1, scnd_len + 1)
        scr_tbl = numpy.zeros(matrixShape)
        dir_tbl = numpy.zeros(matrixShape)
        for i in range(1, frst_len + 1):
            scr_tbl[i, 0] = i * self.getGapCost()
        for j in range(1, scnd_len + 1):
            scr_tbl[0, j] = j * self.getGapCost()
        scr = 0
        for i in range(1, frst_len + 1):
            for j in range(1, scnd_len + 1):
             if self.getFirstSequence()[i - 1] == self.getSecondSequence()[j - 1]:
                 scr = self._match
             else:
                 scr = self._mismatch
             s1 = scr_tbl[i - 1, j - 1] + scr
             s2 = scr_tbl[i - 1, j] + self.getGapCost()
             s3 = scr_tbl[i, j - 1] + self.getGapCost()
             scr_tbl[i, j] = max(s1, s2, s3)
             if scr_tbl[i, j] == s1:
                 dir_tbl[i, j] = 0
             elif scr_tbl[i, j] == s2:
                 dir_tbl[i, j] = 1
             else:
                 dir_tbl[i, j] = -1
        i = len(self.getFirstSequence())
        j = len(self.getSecondSequence())

        alt_seq1 = ''
        alt_seq2 = ''
        mid_line = ''

        while (i > 0 and j > 0):
            if dir_tbl[i, j] == 0:
             alt_seq1 += self.getFirstSequence()[i - 1]
             alt_seq2 += self.getSecondSequence()[j - 1]
             if self.getFirstSequence()[i - 1] == self.getSecondSequence()[j - 1]:
                 mid_line += "|"
             else:
                 mid_line += " "
                 self._mismatchCount += 1
             i = i - 1
             j = j - 1
            if dir_tbl[i, j] == 1:
             alt_seq1 += self.getFirstSequence()[i - 1]
             alt_seq2 += '-'
             mid_line += " "
             self._gapCount += 1
             i = i - 1
            if dir_tbl[i, j] == -1:
             alt_seq1 += '-'
             alt_seq2 += self.getSecondSequence()[j - 1]
             mid_line += " "
             j = j - 1
             self._gapCount += 1
        while (j > 0):
         alt_seq1 += '-'
         alt_seq2 += self.getSecondSequence()[j - 1]
         mid_line += " "
         j = j - 1
         self._gapCount += 1
        while (i > 0):
         alt_seq1 += self.getFirstSequence()[i - 1]
         alt_seq2 += '-'
         mid_line += " "
         i = i - 1

         self._gapCount += 1
        print("The number of mismatch is: " + str(self.getMismatchCount()) + ". The number of gap is: " + str(self._gapCount))
        print(reverse(alt_seq1))
        print(reverse(mid_line))
        print(reverse(alt_seq2))