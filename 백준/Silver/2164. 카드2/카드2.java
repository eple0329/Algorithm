import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 1; i<= N; i++) {
            queue.add(i);
        }
        while(true){
            int num = queue.poll();
            if(queue.isEmpty()){
                System.out.println(num);
                break;
            }
            queue.add(queue.poll());
        }

    }
}