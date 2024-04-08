import java.util.*;
import java.io.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int[][] giftMap = new int[friends.length][friends.length];
        int[] giveSum = new int[friends.length];
        int[] givenSum = new int[friends.length];
        int[] totalGift = new int[friends.length];
        for(int i = 0; i< giftMap.length; i++){
            for(int j = 0; j < giftMap[i].length; j++){
                giftMap[i][j] = 0;
            }
        }
        for(int i = 0; i< gifts.length; i++){
            StringTokenizer st = new StringTokenizer(gifts[i]);
            String A = st.nextToken();
            String B = st.nextToken();
            int idxA = -1;
            int idxB = -1;
            for(int j = 0; j < friends.length; j++){
                if(friends[j].equals(A)){
                    idxA = j;
                }
                if(friends[j].equals(B)){
                    idxB = j;
                }
            }
            giftMap[idxA][idxB] += 1;
        }
        for(int i = 0; i< giftMap.length; i++){
            giveSum[i] = Arrays.stream(giftMap[i]).sum();
            
            int tmp = 0;
            for(int j = 0; j < giftMap.length; j++){
                tmp += giftMap[j][i];
            }
            givenSum[i] = tmp;
        }
        
        for(int A = 0; A < friends.length; A++){
            for(int B = 0; B < A; B++){
                if(A == B) continue;
                int giftScoreA = giveSum[A] - givenSum[A];
                int giftScoreB = giveSum[B] - givenSum[B];
                
                
                // 주고받은 기록이 있는데 같지 않을 때
                if(giftMap[A][B] != giftMap[B][A]){
                    if(giftMap[A][B] > giftMap[B][A]){
                        totalGift[A] += 1;
                        System.out.println(B + " " + A);
                    }
                    else{
                        totalGift[B] += 1;
                    }
                }
                
                // 주고받은 기록이 없거나 같을 때
                else{
                // 선물 지수가 다를 때
                    if(giftScoreA > giftScoreB){
                        totalGift[A] += 1;
                        System.out.println(B + " " + A);
                    }
                    else if(giftScoreA < giftScoreB){
                        totalGift[B] += 1;
                        System.out.println(A + " " + B);
                    }
                
                // 선물 지수가 같을 때 (Pass)
                }
            }
        }
        System.out.println(Arrays.toString(totalGift));
        int answer = Arrays.stream(totalGift).max().orElseThrow(null);
        return answer;
    }
}