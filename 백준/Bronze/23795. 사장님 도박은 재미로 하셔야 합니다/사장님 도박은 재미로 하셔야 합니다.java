import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        for (int i = 0; i < 2000;i++){
            int n = sc.nextInt();
            if (n==-1){
                break;
            }
            sum += n;    
        }
        
        System.out.print(sum);
    }
}