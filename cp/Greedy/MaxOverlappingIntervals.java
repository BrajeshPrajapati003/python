import java.util.*;

public class MaxOverlappingIntervals{
    public static int maxAirplanes(int[][] intervals){
        List<int[]> events = new ArrayList<>();

        for(int[] in: intervals){
            events.add(new int[]{in[0], 1}); // start
            events.add(new int[]{in[1], -1}); // end
        }

        // sort by time, then type (-1 before +1)
        Collections.sort(events, (a,b) -> {
            if(a[0]==b[0]) return a[1]-b[1];
            return a[0]-b[0];
        });

        int curr = 0, max = 0;

        for(int[] e: events){
            curr += e[1];
            max = Math.max(max, curr);
        }

        return max;
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 5}, {2, 6}, {4, 8}, {7, 9}};
        System.out.println(maxAirplanes(intervals)); // 3
    }
}
