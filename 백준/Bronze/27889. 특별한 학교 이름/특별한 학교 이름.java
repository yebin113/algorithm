import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        if (a.equals("NLCS")) {
            System.out.print("North London Collegiate School");
        } else if ( a.equals("BHA")) {
            System.out.print("Branksome Hall Asia");
        } else if ( a.equals("KIS")) {
            System.out.print("Korea International School");
        } else if ( a.equals("SJA")) {
            System.out.print("St. Johnsbury Academy");
        }
    }
}