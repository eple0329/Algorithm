import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        HashMap<Integer, Integer> countByNum = new HashMap<>();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if(countByNum.get(arr[i]) == null){
                countByNum.put(arr[i], 1);
            }
            else{
                countByNum.put(arr[i], countByNum.get(arr[i])+1);
            }
        }
        int[] queries = new int[m];
        for (int i = 0; i < m; i++) {
            queries[i] = sc.nextInt();
            if(countByNum.get(queries[i]) == null){
                System.out.print("0 ");
            }
            else{
                System.out.print(countByNum.get(queries[i]) + " ");
            }
        }

    }
}