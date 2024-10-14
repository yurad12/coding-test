package book.정렬;

import java.util.Arrays;
import java.util.stream.IntStream;

public class P51_병합정렬 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1,3,5}, new int[]{2,4,6})));
        System.out.println(Arrays.toString(solution2(new int[]{1,3,5}, new int[]{2,4,6})));
    }

    private static int[] solution(int[] arr1, int[] arr2) {
        int[] merged = new int[arr1.length + arr2.length];
        int k = 0, i = 0, j = 0;

        while (i < arr1.length && j < arr2.length) {
            merged[k++] = arr1[i] <= arr2[j] ? arr1[i++] : arr2[j++];
        }

        while (i < arr1.length) {
            merged[k++] = arr1[i++];
        }
        while (j < arr2.length) {
            merged[k++] = arr2[j++];
        }

        return merged;
    }

    // Stream 이용
    private static int[] solution2(int[] arr1, int[] arr2) {
        // return IntStream.concat(Arrays.stream(arr1), Arrays.stream(arr2))
        //     .sorted().toArray();
        return IntStream.concat(IntStream.of(arr1), IntStream.of(arr2)).sorted().toArray();
    }
}
