public class pe_2 {

    public static void main(String[] args) {

        int a = 1;
        int b = 2;
        int toplam = 0;
        int yeniTerim;

        while (b < 4000000) {

            if (b % 2 == 0) {
                toplam += b;
            }

            yeniTerim = a + b;
            a = b;
            b = yeniTerim;
        }

        System.out.println("Toplam: " + toplam);
    }
}
