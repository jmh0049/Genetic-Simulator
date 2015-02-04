import Topology
import alignment

class JythonTopo(Topology):
	def _init_(self):
		pass
	
	def createTree(list):
		self.setMatrixLength(len(list))
		for i in range(len(list)):
			dominantSeq = list[i]
			subdominateSeqs = []
			aligned = []
			distance = []
			
			for j in range(len(list)):
				if i != j:
					subdominateSeq.append(list[j])
				
			aligned = alignment.alignSequences(dominantSeq, subdominateSeqs)
			distance = alignment.getDistanceMatrix(dominantSeq, aligned)
			self.sequenceToMatrix(i, distance)
		
		graph = self.matrixToGraph()
