package book.배열;

import java.util.Arrays;

public class P01_배열_정렬하기 {
    public static void main(String[] args) {
        int[] numbers = {4, 2, 3, 1, 5};
        int[] answer = solution1(numbers);
        System.out.println(Arrays.toString(answer));
    }

    // 원본 배열 정렬
    public static int[] solution1(int[] arr) {
        Arrays.sort(arr);
        return arr;
    }

    // 새로운 배열 생성하여 정렬
    private static int[] solution2(int[] arr) {
        int[] copyArr = arr.clone();
        Arrays.sort(copyArr);
        return copyArr;
    }
}
