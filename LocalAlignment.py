from __future__ import division, print_function
from Project.AlignmentTools.StringManipulation import *
from Project.AlignmentTools.PairwiseAlignment import *
import numpy as np


class Local(PairwiseAlignment):
    def __init__(self, seq1, seq2):
        super().__init__(seq1, seq2)

        self._match = 1
        self._mismatch = -1
        self._gap = -2
        self._matchCount = 0
        self._mismatchCount = 0
        self._gapCount = 0

    def getFirstHeader(self) :
        return super().getFirstHeader()

    def getSecondHeader(self) :
        return super().getSecondHeader()

    def getFirstSequence(self) :
        return super().getFirstSequence()

    def getSecondSequence(self) :
        return super().getSecondSequence()

    def setFirstHeader(self, frstHdr) :
        super().setFirstHeader(frstHdr)

    def setSecondHeader(self, scndHdr) :
        super().setSecondHeader(scndHdr)

    def setFirstSequence(self, frstSq) :
        super().setFirstSequence(frstSq)

    def setSecondSequence(self, scndHdr) :
        super().setSecondSequence(scndHdr)

    def getMatchCount(self) :
        super().getMatchCount()

    def setMatchCount(self) :
        super().setMatchCount()

    def getMismatchCount(self) :
        super().getMismatchCount()

    def setMismatchCount(self) :
        super().setMismatchCount()

    def getGapCount(self) :
        super().getGapCount()

    def setGapCount(self) :
        super().setGapCount()

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

    pt = {'match': getMatchCost(), 'mismatch': getMismatchCost(), 'gap': getGapCost()}
    def mch(alpha, beta, pt=None):
         if pt is None :
             pt = pt
         if alpha == beta:
             return pt['match']
         elif alpha == '-' or beta == '-':
             return pt['gap']
         else:
             return pt['mismatch']

    #def localAlignment(self):
    # def localAlignment(s1, s2):
    #     m, n = len(s1), len(s2)
    #     H = np.zeros((m + 1, n + 1))
    #     T = np.zeros((m + 1, n + 1))
    #     max_score = 0
    #     # Score, Pointer Matrix
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             sc_diag = H[i - 1][j - 1] + mch(s1[i - 1], s2[j - 1])
    #             sc_up = H[i][j - 1] + pt['gap']
    #             sc_left = H[i - 1][j] + pt['gap']
    #             H[i][j] = max(0, sc_left, sc_up, sc_diag)
    #             if H[i][j] == 0: T[i][j] = 0
    #             if H[i][j] == sc_left: T[i][j] = 1
    #             if H[i][j] == sc_up: T[i][j] = 2
    #             if H[i][j] == sc_diag: T[i][j] = 3
    #             if H[i][j] >= max_score:
    #                 max_i = i
    #                 max_j = j
    #                 max_score = H[i][j];
    #
    #     print('H=\n', H, '\n')
    #     print('T=\n', T, '\n')
    #     align1, align2 = '', ''
    #     i, j = max_i, max_j
    #
    #     # Traceback
    #     while T[i][j] != 0:
    #         if T[i][j] == 3:
    #             a1 = s1[i - 1]
    #             a2 = s2[j - 1]
    #             i -= 1
    #             j -= 1
    #         elif T[i][j] == 2:
    #             a1 = '-'
    #             a2 = s2[j - 1]
    #             j -= 1
    #         elif T[i][j] == 1:
    #             a1 = s1[i - 1]
    #             a2 = '-'
    #             i -= 1
    #         print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
    #         align1 += a1
    #         align2 += a2
    #
    #     align1 = align1[::-1]
    #     align2 = align2[::-1]
    #     sym = ''
    #     iden = 0
    #     for i in range(len(align1)):
    #         a1 = align1[i]
    #         a2 = align2[i]
    #         if a1 == a2:
    #             sym += a1
    #             iden += 1
    #         elif a1 != a2 and a1 != '-' and a2 != '-':
    #             sym += ' '
    #         elif a1 == '-' or a2 == '-':
    #             sym += ' '
    #
    #     identity = iden / len(align1) * 100
    #     print('Identity = %f percent' % identity)
    #     print('Score =', max_score)
    #     print(align1)
    #     print(sym)
    #     print(align2)
    #
    #
    # if __name__ == '__main__':
    #     localAlignment('AGATCTGTTCTCTAAACGAACTTTA',
    #                     'CTACCCAGGAAAAGCCAACCAACCTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTAGCTGTCGCTCGGCTGCATGCCTAGTGCA')
