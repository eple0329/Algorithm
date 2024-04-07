import java.util.*;
import java.io.*;

public class Main{
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        ArrayList<Integer> inputList = new ArrayList<>(N);
        ArrayList<Integer> dp = new ArrayList<>(N);
        for(int i = 0; i< N; i++){
            inputList.add(Integer.parseInt(br.readLine()));
            dp.add(0);
        }
        if(N == 1){
            System.out.println(inputList.get(0));
            return;
        }
        else if(N == 2){
            System.out.println(inputList.get(0) + inputList.get(1));
            return;
        }
        else if(N == 3){
            System.out.println(Math.max(inputList.get(1) + inputList.get(2), inputList.get(0) + inputList.get(2)));
            return;
        }
        dp.set(0, inputList.get(0));
        dp.set(1, dp.get(0) + inputList.get(1));
        dp.set(2, Math.max(inputList.get(1) + inputList.get(2), dp.get(0) + inputList.get(2)));
        for(int i = 3; i < N; i++) {
            dp.set(i, Math.max(inputList.get(i-1) + dp.get(i-3) + inputList.get(i), dp.get(i-2) + inputList.get(i)));
        }
        System.out.println(dp.get(N-1));
    }
}