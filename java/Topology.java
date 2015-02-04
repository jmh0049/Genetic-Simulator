import java.util.ArrayList;
import java.util.Arrays;



public class Topology {
   
   int[][] dMatrix;
   
   public void setMatrixLength(int length) {
      dMatrix =  new int[length][length];
   }
   
   //for testing purposes
   public static void main(String args[]) {
      Topology k = new Topology();
      int[][] x = {{0,0,0,0,0,0},{4,0,0,0,0,0},{7,9,0,0,0,0},{17,15,14,0,0,0},{18,16,14,3,0,0},{6,8,7,14,12,0}};
      String tmp = k.matrixToGraph(x);
      System.out.println(tmp);
   }
   
   /** 
    * Fills a matrix with distance values from an integer array.
    *
    * @param int denotes what sequence number it is.
    * @param int[] an array of differences in the sequences
    */
    
   public void sequenceToMatrix(int seqNum, int[] distances) {
      
      for (int i = 1; i < length; i++) {
         dMatrix[seqNum][i] = distances[i];
      }
   }
   
   /** 
    * Returns a string that describes the topological tree.
    *
    * @param int[][] A matrix of integer values related to the distances.
    * @return String A string that has a list of pairs along with their distance.
    */
   public String matrixToGraph() {
      int length = dMatrix.length;
      int dCounter = 0;
      int pairCounter = 0;
      int numOfComb = totalCombinations(length);
      DistancePairs[] dPairs = new DistancePairs[numOfComb];
      ArrayList<String> sequences =  new ArrayList<String>();
      
      // fills an arraylist of possible sequences
      for (int i = 0; i < length; i++) {
         sequences.add(i+1 + "");
      }
      
      // fills an array with DistancePairs 
      for (int i = 1; i < length; i++) {
         for (int j = 0; j < i; j++) {
            DistancePairs tmp = new DistancePairs(dMatrix[i][j], i+1, j+1);
            dPairs[dCounter] = tmp;
            dCounter++;
         }
      }
      
      // Sorts the DistancePairs based on distance
      Arrays.sort(dPairs);
      
      // Creates the string that describes the topological graph
      String str = "";
      int counter = 0;
      while (!sequences.isEmpty()) {
         boolean isPartOfTree = false;
         DistancePairs tmp = dPairs[counter];
         String tmpSeq1 = tmp.getSequence1() + "";
         String tmpSeq2 = tmp.getSequence2() + "";
         
         // checks to see if the sequence has not been used
         if (sequences.contains(tmpSeq1)) {
            isPartOfTree = true;
            sequences.remove(tmpSeq1);
         }
         
         if (sequences.contains(tmpSeq2)) {
            isPartOfTree = true;
            sequences.remove(tmpSeq2);
         }
         
         if (isPartOfTree) {
            str += "Distance: " + tmp.getDistance() + " Pair: " + tmp.getSequence1() + ", " + tmp.getSequence2() + "\n";
         }
         counter++;
      }
      
      return str;
   }
   
   /** 
    * Returns an integer that gives the number of combinations possible.
    *
    * @param int The size of the matrix
    * @return int The number of total combinations.
    */
   public int totalCombinations(int x) {
      int tmp = x-1;
      int sum = 0;
      
      for (int i = 0; i < x - 1; i++) {
         sum += tmp;
         tmp--;
      }
      
      return sum;
   }
}
