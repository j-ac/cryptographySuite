import java.util.Scanner;

public class EnigmaMachine {

    public Rotor head;
    public Rotor tail;
    public PlugBoard letterMaps, reflector;
    public static final Scanner sc = new Scanner(System.in);
    public static final int REFLECTOR_SEED = 777;
    EnigmaMachine(){
        int numRotors = -1;
        while(!(numRotors <= 5 && numRotors >= 1)){
            System.out.println("How many rotors? (Choose a number between 1-5)");
            numRotors = sc.nextInt();
        }

        System.out.println("Which rotor type is the first rotor?, single number, (0-4)");
        int rotorType = sc.nextInt();
        head = new Rotor(null, null, Rotor.seeds[rotorType]);
        createLinkedListOfRotors(head, head, numRotors);

        int PlugBoardSeed = -1;
        while(!(PlugBoardSeed >= 0)){
            System.out.println("enter a seed for generating a plugboard.");
            PlugBoardSeed = sc.nextInt();
        }
        letterMaps = new PlugBoard(PlugBoardSeed, PlugBoard.NUM_PLUGS_PLUGBOARD);
        letterMaps.printConnections();
        reflector = new PlugBoard(REFLECTOR_SEED, PlugBoard.NUM_PLUGS_REFLECTOR);
        reflector.printConnections();
    }

    Rotor createLinkedListOfRotors(Rotor firstRotor, Rotor r, int numRotors){

        if (numRotors <= 1) {
            this.tail = r;
            return firstRotor;
        }
        else {
            System.out.println("Which rotor type would you like for this rotor?, (0-4)");
            int rotorType = sc.nextInt();
            Rotor rotor = new Rotor(r, null, Rotor.seeds[rotorType]);
            r.next = rotor;
            numRotors--;

            return createLinkedListOfRotors(firstRotor, rotor, numRotors);
        }
    }


    void performCypher() {
        System.out.println("Enter the message you would like encrypted or decrypted.");
        sc.nextLine();
        String message = sc.nextLine();
        message = message.toUpperCase();

        for(int i = 0; i < message.length(); i++){

            int intAfterFirstPlugBoard = letterMaps.processInput(message.charAt(i) - Rotor.ASCII_UPPERCASE_CONSTANT);
            int intAfterForwardCypher = head.performCypherSingleChar(intAfterFirstPlugBoard);
            int intAfterReflector = reflector.processInput(intAfterForwardCypher);
            int intAfterReverseCypher = tail.performReverseCypherSingleChar(intAfterReflector);
            int intAfterSecondPlugBoard = letterMaps.processInput(intAfterReverseCypher);
            char charAfterCypher = (char)(intAfterSecondPlugBoard + Rotor.ASCII_UPPERCASE_CONSTANT);
            System.out.print(charAfterCypher);
            head.rotate();
        }
            System.out.print("\n");
    }
}