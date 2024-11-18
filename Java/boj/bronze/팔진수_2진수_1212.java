package boj.bronze;

import java.util.Scanner;

public class 팔진수_2진수_1212 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String octal = sc.nextLine();

        StringBuilder bianry = new StringBuilder();

        bianry.append(Integer.toBinaryString(octal.charAt(0) - '0'));
        for (int i = 1; i < octal.length(); i++) {
            String x = Integer.toBinaryString(octal.charAt(i) - '0');

            while (x.length() < 3) {
                x = "0" + x;
            }
            bianry.append(x);
        }

        System.out.println(bianry.toString());
        sc.close();
    }
}