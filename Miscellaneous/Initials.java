import java.util.Scanner;

public class Initials {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Type   
 your first initial: ");
        char firstInitial = scanner.next().charAt(0);

        System.out.print("Type your last initial: ");
        char lastInitial = scanner.next().charAt(0);

        System.out.println(firstInitial + " " + lastInitial);
    }
}