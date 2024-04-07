import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> inputData = new ArrayList<>(5);
        int maxSize = 0;
        for(int i = 0; i< 5; i++){
            String tmp = bf.readLine();
            inputData.add(tmp);
            if(maxSize < tmp.length()){
                maxSize = tmp.length();
            }

        }
        String ret = "";
        for(int i = 1; i < maxSize+1; i++){
            for(int j = 0; j < 5; j++){
                if(inputData.get(j).length() >= i ){
                    ret += inputData.get(j).charAt(i-1);
                }
            }
        }
        System.out.println(ret);


    }
}