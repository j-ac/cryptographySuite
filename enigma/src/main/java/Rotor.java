import com.google.common.collect.BiMap;
import com.google.common.collect.HashBiMap;
import java.util.ArrayList;
import java.util.Random;
import java.lang.Math;

public class Rotor {
    public static final int ALPHABET_SIZE = 26;
    public static final int ASCII_UPPERCASE_CONSTANT = 65; //for converting numbers 0 -> A, 1 -> B ... 25 -> Z
    public static final int WHEEL_0_SEED = 1066;
    public static final int WHEEL_1_SEED = 1945;
    public static final int WHEEL_2_SEED = 745228;
    public static final int WHEEL_3_SEED = 999597;
    public static final int WHEEL_4_SEED = 9223997;
    public static final int[] seeds = {Rotor.WHEEL_0_SEED, Rotor.WHEEL_1_SEED, Rotor.WHEEL_2_SEED, Rotor.WHEEL_3_SEED, Rotor.WHEEL_4_SEED};

    public final int rotationPoint; //The value which causes subsequent wheels to rotate

    public int offset; //the wheel's rotation which changes during runtime
    Rotor previous;
    Rotor next;
    BiMap<Integer, Integer> connections, connectionsInverse;

    Rotor(Rotor previous, Rotor next, int seed) {
        this.previous = previous;
        this.next = next;

        Random rng = new Random(seed);
        this.rotationPoint = rng.nextInt(ALPHABET_SIZE);
        connections = HashBiMap.create(ALPHABET_SIZE);

        //create an array list with all values 0 - 25
        ArrayList<Integer> valueSpace = new ArrayList<>();
        for(int i = 0; i < ALPHABET_SIZE; i++)
        {
            valueSpace.add(i);
        }
        int value;
        for (int i = 0; i < ALPHABET_SIZE; i++)
        {
            int indexSelection = Math.abs(rng.nextInt()) % valueSpace.size();
            value = valueSpace.remove(indexSelection);
            connections.put(i,value);
        }
        connectionsInverse = HashBiMap.create(ALPHABET_SIZE);
        connectionsInverse = connections.inverse();
        System.out.println(this);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < ALPHABET_SIZE; i++){
            sb.append((char) (i + ASCII_UPPERCASE_CONSTANT))
                    .append("---->")
                    .append((char) (connections.get(i) + ASCII_UPPERCASE_CONSTANT))
                    .append("\n");
        }
        return sb.toString();
    }

    void rotate() { //rotate the wheel, and if necessary, rotate subsequent wheels.
        offset = (offset + 1) % ALPHABET_SIZE;
        if (this.offset == rotationPoint)
            next.rotate();
    }

    //Can encrypt OR decrypt with no change in usage.
    //Eg. If ABC generates DEF that implies DEF generates ABC.
    //Encrypts or decrypts a single character. Should be called once per letter in the original string.
    int performCypherSingleChar(int c) {
        if(next == null){ //if this is the last rotor
            return connections.get((c + this.offset) % ALPHABET_SIZE);
        }
        else {
            c = connections.get((c + this.offset) % ALPHABET_SIZE);
            return next.performCypherSingleChar(c);
        }
    }

    //sends the input through more transformations, travelling through all rotors in reverse. Not strictly necessary, and actually introduces its key weakness, but the real Enigma does it, so I will too.
    int performReverseCypherSingleChar(int c)
    {
        if(previous == null){ //When the signal reaches the first rotor again.
            c = (connectionsInverse.get(c) - offset + ALPHABET_SIZE) % ALPHABET_SIZE; //Adding alphabet_size Ensures bracket will always resolve positive w/o affecting answer
            return c;
        }
        else{
            c = (connectionsInverse.get(c) - offset + ALPHABET_SIZE) % ALPHABET_SIZE;
            return previous.performReverseCypherSingleChar(c);
        }
    }


}
