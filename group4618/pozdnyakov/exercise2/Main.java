package group4618.pozdnyakov.exercise2;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ShopToy shopToy = new ShopToy();
        shopToy.put(1, "Конструктор", 0.2);
        shopToy.put(2, "Робот", 0.2);
        shopToy.put(3, "Кукла", 0.6);
        shopToy.put(4, "Мяч", 0.3);
        shopToy.put(5, "Машинка", 0.4);
        shopToy.put(6, "Меч", 0.1);
        shopToy.put(1, "Конструктор", 0.2);
        shopToy.put(2, "Робот", 0.2);
        shopToy.put(3, "Кукла", 0.6);
        shopToy.put(4, "Мяч", 0.3);
        shopToy.put(5, "Машинка", 0.4);
        shopToy.put(6, "Меч", 0.1);

        String fileName = "result.txt";
        ArrayList<Toy> lotteryIssueList = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            lotteryIssueList.add(shopToy.get());
        }
        shopToy.saveArrayToFile(fileName, lotteryIssueList);
        shopToy.saveToFile(fileName, shopToy.get());
    }

}
