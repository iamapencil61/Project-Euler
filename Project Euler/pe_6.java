public class pe_6 {
    public static void main(String[] args) {
        int sumOfSquares = 0;
        int sum = 0;

        for (int x = 0; x <= 100; x++) {
            sum += x;
            sumOfSquares += x * x;
        }

        int squareOfSum = sum * sum;
        int difference = squareOfSum - sumOfSquares;
        System.out.println("Difference: " + difference);
    }
}
