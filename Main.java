
public class Main {
  public static int addNum(int a, int b) {

    int result = a + b;
    return result;
  }

  public static int calcSum() {
    int tmp = 0;
    for (int i = 0; i <= 100; i++) {
      tmp += i;
    }
    return tmp;
  }

  public static void main(String[] args) {
    System.out.println(addNum(1, 2));
    System.out.println(calcSum());
  }
}