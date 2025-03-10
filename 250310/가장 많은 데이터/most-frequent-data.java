import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String[] arr = new String[n];
        HashMap<String, Integer> stringCount = new HashMap<>();
        
        int maxCount = -1;
        String maxIndex = null;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
            if(stringCount.get(arr[i]) == null){
                stringCount.put(arr[i], 1);
                if(maxIndex == null){
                    maxIndex = arr[i];
                    maxCount = 1;
                }
            }
            else{
                stringCount.put(arr[i], stringCount.get(arr[i]) + 1);
                if(stringCount.get(arr[i]) > maxCount){
                    maxCount = stringCount.get(arr[i]);
                    maxIndex = arr[i];
                }
            }
        }
        System.out.println(stringCount.get(maxIndex));



    }
}