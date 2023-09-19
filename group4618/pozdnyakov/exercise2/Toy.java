package group4618.pozdnyakov.exercise2;

/**
 * Toy
 */
public class Toy {

    private int id;
    private String name;
    private double frequency;

    public Toy(int id, String name, double frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getFrequency() {
        return frequency;
    }

    public void setFrequency(double frequency) {
        this.frequency = frequency;
    }

    @Override
    public String toString() {
        return "Toy [id=" + id + ", name=" + name + ", frequency=" + frequency + "]";
    }

}