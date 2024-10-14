package book.정렬;

public class P50_계수정렬 {
    public static void main(String[] args) {
        System.out.println(solution("hello"));
        System.out.println(solution("algorithm"));
    }

    private static String solution(String s) {
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (counts[i] > 0) {
                for (int j = 0; j < counts[i]; j++) {
                    sb.append((char) (i + 'a'));
                }
            }
        }
        return sb.toString();
    }
}
