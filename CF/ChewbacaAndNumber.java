
import java.util.Scanner;

public class ChewbacaAndNumber {
    public static void main(String[] args) {
        String ans;
        try (Scanner sc = new Scanner(System.in)) {
            String num = sc.next();
            int len = num.length();
            ans = "";
            for(int i=0; i<len; i++){
                int d = num.charAt(i)-'0';
                int invt = 9-d;
                
                if(i == 0 && invt == 0) ans = ans + d;
                else ans = ans + Math.min(d, invt);
            }
        }
        System.out.println(ans);
    }
}
