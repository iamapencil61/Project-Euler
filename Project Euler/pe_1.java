public class pe_1 {

    public static void main(String[] args) {

        int toplam = 0;

        for (int x = 1; x < 1000; x++) {
            if (x % 3 == 0 || x % 5 == 0) {
                toplam += x;
            }
        }

        System.out.println("İstenen sayıların toplamı: " + toplam);

    }
}
