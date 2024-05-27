public class LargestPrimeFactor {
    public static void main(String[] args) {
        long number = 600851475143L;
        long largestPrimeFactor = 0;

        for (long x = 2; x <= Math.sqrt(number); x++) {
            if (number % x == 0) {
                largestPrimeFactor = x;
                number /= x;
            }
        }

        if (number > 1) {
            largestPrimeFactor = number;
        }

        System.out.println("The largest prime factor is: " + largestPrimeFactor);
    }
}
