class Seq:

    def __init__(self, file):
        self._file = file
        self._seqID = ""
        self._seq = ""
        fasta = open(file, 'r')
        for line in fasta:
            line = line.rstrip()
            if line.startswith(">"):
                self._seqID = line
            else:
                self._seq += line

    def getFile(self):
        return self._file

    def getSeqID(self):
        return self._seqID

    def setSeqID(self, Hdr):
        self._seqID = Hdr

    def getSeq(self):
        return self._seq

    def setSeq(self, seq):
        self._seq = seq
