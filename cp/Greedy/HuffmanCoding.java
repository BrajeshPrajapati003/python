import java.util.PriorityQueue;

public class HuffmanCoding{

    public static int huffmanCost(int[] freq){

        // Min heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // Add all frequencies
        for(int f: freq){
            pq.offer(f);
        }

        int totalCost = 0;

        // Combine until one element left
        while(pq.size() > 1){

            int a = pq.poll(); // smallest
            int b = pq.poll(); // 2nd smallest

            int merged = a + b;
            totalCost += merged;

            pq.offer(merged);
        }
        return totalCost;
    }
    public static void main(String[] args) {
        int[] freq = {5, 9, 12, 13};
        System.out.println(huffmanCost(freq)); // 78
    }
}
