from Project.AlignmentTools.Seq import *
from Project.AlignmentTools.PairwiseAlignment import *
from Project.AlignmentTools.GlobalAlignment import *
pair = Global(Seq(("active_vaccine.fasta")), Seq(("vaccinal.fasta")))
pair.globalAlignment()