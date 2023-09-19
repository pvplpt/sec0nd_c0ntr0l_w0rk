package group4618.pozdnyakov.exercise2;

import java.util.Comparator;

public class ToyComparator implements Comparator<Toy> {

    @Override
    public int compare(Toy arg0, Toy arg1) {
        return Double.compare(arg1.getFrequency(), arg0.getFrequency());
    }

}
