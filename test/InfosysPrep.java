import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class InfosysPrep{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String[] words = str.trim().split(",");

        int[] nums = new int[words.length];
        for(int i=0; i<words.length; i++){
            nums[i] = Integer.parseInt(words[i], 10);
        }

        // System.out.println(Arrays.toString(twoSum(nums, 9)));
        System.out.println(Arrays.toString(twoSum2(nums, 9)));
    }



    public static int[] twoSum(int[] nums, int targ){
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            
            if(map.containsKey(targ-nums[i])){
                return new int[] {map.get(targ-nums[i]), i};
            }

            map.put(nums[i], i);
        }
        return new int[] {-1, -1};
    }



    public static int[] twoSum2(int[] nums, int targ){ // given array is sorted

        int i = 0, j = nums.length-1;
        while(i<j){
            if(nums[i]+nums[j] == targ) return new int[] {i, j};
            else if(nums[i]+nums[j] > targ) j--;
            else i++;
        }

        return new int[] {-1, -1};
    }



    public static int countFreqOfPairs(int[] nums, int targ){ // given array is sorted

        int i = 0, j = nums.length-1;
        int count = 0;
        while(i<j){
            if(nums[i]+nums[j] == targ) count++;
            else if(nums[i]+nums[j] > targ) j--;
            else i++;
        }

        return count;
    }



    

}
