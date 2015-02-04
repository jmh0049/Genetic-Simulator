public class DistancePairs implements Comparable<DistancePairs>{
   int distance = -1;
   int sequence1 = -1;
   int sequence2 = -1;
   
   public DistancePairs() {}
   
   public DistancePairs(int dist, int seq1, int seq2) {
      distance = dist;
      sequence1 = seq1;
      sequence2 = seq2;
   }
   
   public void setDistance(int dist) {
      distance = dist;
   }
   
   public int getDistance() {
      return distance;
   }
   
   public void setSequence1(int seq1) {
      sequence1 = seq1;
   }
   
   public int getSequence1() {
      return sequence1;
   }
   
   public void setSequence2(int seq2) {
      sequence2 = seq2;
   }
   
   public int getSequence2() {
      return sequence2;
   }
   
   /** 
    * Returns an integer to be used to compare distance
    *
    * @param DistancePairs A DistancePair that contains information about a possible 
    * combination
    * @return int The difference between this DistancePair's distance and the parameters distance.
    */
   public int compareTo(DistancePairs pair) {
      int compareDistance = ((DistancePairs) pair).getDistance();
      
      // ascending order
      return this.distance - compareDistance;
   }
}