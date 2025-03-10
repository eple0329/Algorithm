import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        HashMap<String, Integer> StringToInteger = new HashMap<>();
        HashMap<Integer, String> IntegerToString = new HashMap<>();

        String[] words = new String[n + 1];
        for (int i = 1; i <= n; i++) {
            words[i] = sc.next();
            StringToInteger.put(words[i], i);
            IntegerToString.put(i, words[i]);
        }
        // Please write your code here.

        for (int i = 0; i < m; i++){
            String tmp = sc.next();
            if(tmp.chars().allMatch(Character::isDigit)){
                System.out.println(IntegerToString.get(Integer.parseInt(tmp)));
            }
            else{
                System.out.println(StringToInteger.get(tmp));
            }
            
        }
    }
}