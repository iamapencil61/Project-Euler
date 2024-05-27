import java.util.Scanner;

public class pe_7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int istenenAsalSayi;
        int kontrolEdilenSayi = 2;
        int x;
        int asalKontrol;
        int bulunanAsalSayi = 0;

        System.out.println("Kaç tane asal bulacaksın ?: ");
        istenenAsalSayi = scanner.nextInt();

        while (istenenAsalSayi > bulunanAsalSayi) {

            asalKontrol = 0;
            for (x = 2; x < kontrolEdilenSayi; x++) {

                if (kontrolEdilenSayi % x == 0) {
                    asalKontrol = 1;
                }
            }

            if (asalKontrol == 0) {
                System.out.println(kontrolEdilenSayi);
                bulunanAsalSayi += 1;
            }

            kontrolEdilenSayi += 1;
        }
    }
}
