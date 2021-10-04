import com.google.common.collect.BiMap;
import com.google.common.collect.HashBiMap;
import java.util.Random;
import java.util.ArrayList;
import java.lang.Math;


public class PlugBoard {
    public static BiMap <Integer, Integer> letterMappings;
    public static final int NUM_PLUGS_PLUGBOARD = 10;
    public static final int NUM_PLUGS_REFLECTOR = 13;

    ArrayList<Integer> unmappedLetters= new ArrayList<>();


    PlugBoard(long seed, int numberOfPlugs){
        for(int i = 0; i < Rotor.ALPHABET_SIZE; i++){
            unmappedLetters.add(i); //later this will be used to ensure no letter is mapped twice.
        }

        letterMappings = HashBiMap.create(26);
        Random rng = new Random(seed);
        for(int i = 0; i < (numberOfPlugs); i++){

            int key = unmappedLetters.remove(Math.abs(rng.nextInt()) % unmappedLetters.size());
            int value = unmappedLetters.remove(Math.abs(rng.nextInt()) % unmappedLetters.size());

            letterMappings.put(key,value);
            letterMappings.put(value, key);
        }
        for(int num:unmappedLetters){
            letterMappings.put(num,num);
        }
    }

    int processInput(int c){
        if(letterMappings.containsKey(c))
            return letterMappings.get(c);
        else
            return c;
    }


    void printConnections() {
        System.out.println("Your plugboard connections are:");
        for(int i = 0; i < Rotor.ALPHABET_SIZE; i++){
                System.out.print((char) (i + Rotor.ASCII_UPPERCASE_CONSTANT) + "<---->" + (char)(letterMappings.get(i) + Rotor.ASCII_UPPERCASE_CONSTANT)); //eg A <---> P
                if(i == letterMappings.get(i)){
                    System.out.print("\t(Wired into itself)");
            }
                System.out.print("\n");
        }
    }
}

