import java.util.Scanner;

public class BitPlusPlus{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tests = sc.nextInt();

        int ans = 0;
        for(int i=0; i<tests; i++){
            String x = sc.next();
            if(x.contains("++")) ans++;
            else ans--;
        }
        sc.close();
        System.out.println(ans);
    }
}



