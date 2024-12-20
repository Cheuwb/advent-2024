package day13;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

//29201
public class Day13 {
    public static void main(String[] args) throws Exception {
        new ReadFile().calculate();
    }

    static class ReadFile {
        List<ClawMachine> clawMachines = new ArrayList<>();
        static final Pattern MACHINE_PROPERTIES = Pattern.compile("(?<=X[+=])(\\d+).*?(?<=Y[+=])(\\d+)");

        ReadFile() throws Exception {
            String fileName = "input";
            String input = Files.readString(Paths.get(Objects.requireNonNull(getClass().getResource(fileName)).toURI()));
            input = input.replace("\r\n", "\n");
            for (String build : input.split("\\n\\n")) {
                Matcher matcher = MACHINE_PROPERTIES.matcher(build);
                List<Point> machineParts = new ArrayList<>();
                while (matcher.find()) {
                    Point p = new Point(Long.parseLong(matcher.group(1)), Long.parseLong(matcher.group(2)));
                    machineParts.add(p);
                }
                ClawMachine clawMachine = new ClawMachine(machineParts.get(0), machineParts.get(1), machineParts.get(2));
                clawMachines.add(clawMachine);
            }
        }

        void calculate() {
            Long part1 = clawMachines.stream()
                            .mapToLong(cm -> cm.cramerRule(0))
                            // .forEach(total -> System.out.println(total))
                            .sum();
            Long part2 = 
            clawMachines.stream()
                            .mapToLong(cm -> cm.cramerRule(10000000000000L))
                            .sum();
            System.out.println(part1);
            System.out.println(part2);
        }
    }

    static class ClawMachine{
        static final long BUTTON_COST_A = 3;
        static final long BUTTON_COST_B = 1;

        Point buttonA;
        Point buttonB;
        Point prize;
        
        ClawMachine(Point a, Point b, Point prize) {
            this.buttonA = a;
            this.buttonB = b;
            this.prize = prize;
        }

        long determinant(long ax, long ay, long bx, long by) {
            return (ax * by) - (ay * bx);
        }
        
        long cramerRule(long prizeModifier) {
            long prizeX = prize.X + prizeModifier;
            long prizeY = prize.Y + prizeModifier;

            long detM = determinant(buttonA.X, buttonA.Y, buttonB.X, buttonB.Y);
            if (detM == 0) {
                return 0;
            }
            long detA = determinant(prizeX, prizeY, buttonB.X, buttonB.Y);
            long detB = determinant(buttonA.X, buttonA.Y, prizeX, prizeY);

            //only accept full button presses
            if (detA % detM == 0 && detB % detM == 0) {
                long a = detA/detM;
                long b = detB/detM;
                // Button A or B cannot be pushed more than 100 tries
                // if (a > 100 || b > 100) {
                //     return 0;
                // }
                //3a + 1b = tokens
                return BUTTON_COST_A * a + BUTTON_COST_B * b;
            }
            return 0;
        }
    }
    static class Point {
        long X;
        long Y;

        Point(long x, long y) {
            this.X = x;
            this.Y =y;
        }
    }
}