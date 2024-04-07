import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        // 데이터 입력 방식 -> System.in 보다 엄청난 시간차이가 존재한다고 한다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 데이터 전처리 방식 -> StringTokenizer가 입력된 값을 잘라주는 역할을 한다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 데이터 출력 방식 -> 이 방식으로 한번에 출력하는게 시간적으로 좋다고 한다.
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // Key, Value 값으로 저장하기 위해서 해당 방식으로 선언했다. HashMap을 기억하자
        Map<String, String> data = new HashMap<>();
        for(int i = 0; i< N; i++){
            st = new StringTokenizer(br.readLine());
            String key = st.nextToken();
            String value = st.nextToken();
            data.put(key, value);
        }

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            String key = st.nextToken();
            sb.append(data.get(key) + '\n');
        }
        System.out.print(sb);
    }

}
