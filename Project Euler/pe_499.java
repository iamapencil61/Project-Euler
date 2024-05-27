public class pe_499 {
    public static void main(String[] args) {
        System.out.printf("%.7f%n", f(15, (int) Math.pow(10, 9)));
    }

    public static double f(int m, int s) {
        double hi = 1.0;
        double lo = 0.0;
        double diff = 0.0;

        while (true) {
            double mid = (hi + lo) / 2;
            if (g(m, mid) < 0) {
                hi = mid;
            } else {
                lo = mid;
            }
            if ((hi - lo) == diff) {
                break;
            }
            diff = hi - lo;
        }
        return 1 - Math.pow(lo, s - m + 1);
    }

    public static double g(int m, double mid) {
        double n = -1.0;
        double x = 1.0;
        while (true) {
            double d = Math.pow(mid, x - m) / x / 2;
            if (d == 0) {
                break;
            }
            n += d;
            x *= 2;
        }
        return n;
    }
}
