import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{

        Scanner sc = new Scanner(System.in);
        String[] splited = sc.nextLine().split(" ");
        // 각 숫자를 비트 번호로 설정해서 저장
        BitSet bitSet = new BitSet();
        StringBuilder answer = new StringBuilder();

        // 반복문을 돌면서
        for (String str : splited) {
            int num = Integer.parseInt(str);
            // 세트에 숫자가 있으면 넘기기
            if (bitSet.get(num)) continue;
            // 없으면 정답에 추가
            bitSet.set(num);
            answer.append(num + " ");
        }

        System.out.println(answer);
    }
}
