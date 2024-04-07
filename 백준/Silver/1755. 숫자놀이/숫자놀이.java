import java.io.*;
import java.util.*;


public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        Map<String, Integer> dict = new HashMap();
        Map<Character, String> num_dict = new HashMap();
        ArrayList<String> stringInt = new ArrayList();

        num_dict.put('0', "zero");
        num_dict.put('1', "one");
        num_dict.put('2', "two");
        num_dict.put('3', "three");
        num_dict.put('4', "four");
        num_dict.put('5', "five");
        num_dict.put('6', "six");
        num_dict.put('7', "seven");
        num_dict.put('8', "eight");
        num_dict.put('9', "nine");

        for(int i = M; i <= N; i++){
            String num = Integer.toString(i);
            String tmp = "";
            for(int j = 0; j < num.length(); j++){
                tmp += num_dict.get(num.charAt(j)) + ' ';
            }
            dict.put(tmp, i);
            stringInt.add(tmp);
        }
        Collections.sort(stringInt);
        int a = 0;
        for(String tmp: stringInt){
            a += 1;
            sb.append(dict.get(tmp) + " ");
            if(a % 10 == 0){
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}