import java.util.Scanner;

class Nuklir {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int securityNum = 85381;
        System.out.println("Masukkan kode nuklir:");
        int nuklir = input.nextInt();
        securityNum = securityNum * 2;
        securityNum = securityNum * 2;
        if (securityNum == nuklir) {
            System.out.println("LKS2021{" + nuklir + "}");
        } else {
            System.out.println("Kode nuklir salah komandan!");
        }
    }
}