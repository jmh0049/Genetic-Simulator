#from Bio.Seq import Seq

def _getLongestLength(listOfLists):
	""" gets length of longest list from a list of lists """
	max = -1
	for list in listOfLists:
		if len(list) > max:
			max = len(list)
	return max
	
def _advanceList(list):
	""" shifts all non-dash characters to the right by one, overwriting dash characters if necessary """
	newList = ["-"] * len(list)
	for i in range(len(list) - 1):
		newList[i + 1] = list[i]
	return newList
	
def _getNumberOfAlignedNucleotides(dominant, subdominant):
	""" gets the number of aligned nucleotides geven to already-aligned sequences """
	numAligned = 0
	for i in range(len(dominant)):
		if dominant[i] is not "-" and subdominant[i] is not "-":
			if dominant[i] == subdominant[i]:
				numAligned += 1
	return numAligned
	
def alignSequences(dominantSequence, sequenceMatrix):
	"""
		takes a dominant sequence and sequences to be aligned with it
		returns a tuple with the dominant sequence (with gaps) in position 0 and 
		the aligned other sequences (with gaps) in position 1
	"""
	maxNumAligned = -1
	# prepare the empty lists
	longestSubdominantSequenceLength = _getLongestLength(sequenceMatrix)
	dominantSequenceLength = len(dominantSequence)
	dominantSeq = ["-"] * (2*longestSubdominantSequenceLength + dominantSequenceLength - 2)
	subdominantSequences = []
	for i in range(len(sequenceMatrix)):
		subdominantSequences.append(["-"] * (2*longestSubdominantSequenceLength + dominantSequenceLength - 2))	
	# copy the sequences into the lists appropriately
	for i in range(longestSubdominantSequenceLength - 1, longestSubdominantSequenceLength - 1 + dominantSequenceLength - 1):
		dominantSeq[i] = dominantSequence[i - (longestSubdominantSequenceLength - 1)]
	for i in range(len(subdominantSequences)):
		for j in range(len(sequenceMatrix[i])):
			subdominantSequences[i][j] = sequenceMatrix[i][j]

	for i in range(len(subdominantSequences)):
		maxNumAligned = -1
		numAligned = -1
		alignedSequence = []
		for j in range(dominantSequenceLength + longestSubdominantSequenceLength - 1):
			numAligned = _getNumberOfAlignedNucleotides(dominantSeq, subdominantSequences[i])
			if numAligned > maxNumAligned:	
				maxNumAligned = numAligned
				alignedSequence = list(subdominantSequences[i])
			subdominantSequences[i] = _advanceList(subdominantSequences[i])
		subdominantSequences[i] = list(alignedSequence)
	return (dominantSeq, subdominantSequences)
	
def getDistanceMatrix(dominantAlignedSequence, alignedSequences):
  """
    returns a list of numbers of differences between the aligned 
    dominant sequence and aligned subdominant sequences
  """
	distanceMatrix = []
	for seq in alignedSequences:
		distanceMatrix.append(_getNumberOfAlignedNucleotides(dominantAlignedSequence, seq))
	return distanceMatrix
	
def generateDotMatrix(dominantAlignedSequence, alignedSequences):
  """
    returns the aligned subdominant sequences with all aligned matching 
    nucleotides replaced with dots (".")
  """
	for sequence in alignedSequences:
		for i in range(len(sequence)):
			if sequence[i] is not "-" and dominantAlignedSequence[i] is not "-":
				if sequence[i] == dominantAlignedSequence[i] :
					sequence[i] = "."
	alignedSequences.insert(0, dominantAlignedSequence)
	dotMatrix = []
	for sequence in alignedSequences:
		dotMatrix.append(sequence)
	return dotMatrix
	
	
	
majorSample = list("TAGCTGATGCTGACTAGAAAGCTTGC")
sample = []
sample.append(list("TGGCTGTAGCTGTAATAAAATGTTTG"))
sample.append(list("AGGGCTGTATTATATATGATTAAGTA"))
sample.append(list("TTATCCGCGTCGTATCTTTTTAGTAG"))
sample.append(list("GATCTGTGTGTGSAATATATATAAAA"))
sample.append(list("GGATTACCTCGCGGAGACTAGCTCGT"))
sample.append(list("GGATCATCGTATCGTGATCGTCTAGC"))
tuple = alignSequences(majorSample, sample)

print ''.join(tuple[0])
for seq in tuple[1]:
	print ''.join(seq), _getNumberOfAlignedNucleotides(tuple[0], seq)

print ""

print getDistanceMatrix(tuple[0], tuple[1])

print ""

for seq in generateDotMatrix(tuple[0], tuple[1]):
	print ''.join(seq)
