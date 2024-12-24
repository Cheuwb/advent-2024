package day14;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

/*
 * Track # of robots per quadrant after 100 units of movement
 * For 0...100, update all robots from starting position using velocity & modulo for cycling
 * Grid is 101 columns and 103 rows
 */

public class Day14 {

    public static void main(String[] args) throws Exception {
        Grid grid = new Grid("input");
        // Sample grid
        // for (int i=0; i<7; i++) {
        //     for (int j=0; j<11; j++) {
        //         System.out.print(Grid.sampleGrid[i][j]);
        //     }
        //     System.out.println();
        // }
        // System.out.println(Grid.VERTICAL_LINE);
        // System.out.println(Grid.HORIZONTAL_LINE);
        System.out.println(grid.calcaulteP1());
    }

    static class Grid {
        //input: x = width = columns, y = height/tall = rows
        static final int cols = 101;
        static final int rows = 103;
        //sample
        // static final int cols = 11;
        // static final int rows = 7;

        static final int VERTICAL_LINE = cols / 2;
        static final int HORIZONTAL_LINE = rows / 2;

        // static int[][] sampleGrid = new int[7][11];

        static Map<String, Integer> quadrant = new HashMap<>();

        Grid(String filename) throws IOException, URISyntaxException {
            InputStream input = Objects.requireNonNull(getClass().getResourceAsStream(filename));
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            Stream<String> lines = reader.lines();
            lines.forEach(Robot::processLine);
        }

        int calcaulteP1() {
            //safety value for P1
            int res = 1;
            Set<String> Q = Grid.quadrant.keySet();
            for (String q : Q) {
                int countInQuadrant = Grid.quadrant.get(q);
                res *= countInQuadrant;
                System.out.println(String.format("Quadrant: %s Count: %d", q, countInQuadrant));
            }
            return res;
        }
    }

    record Coordinate(int col, int row) {
        static Coordinate from(String col, String row) {
            return new Coordinate(Integer.parseInt(col), Integer.parseInt(row));
        }
    }

    static class Robot {
        static final Pattern ROBOT_PROPERTIES = Pattern.compile("(?<=p=)(\\d+),(\\d+).*?v=(-?\\d+),(-?\\d+)");
        Coordinate position;
        Coordinate movement;

        Robot(String line) {
            Matcher matcher = ROBOT_PROPERTIES.matcher(line);
            if (matcher.find()) {
                // System.out.println(matcher.group(1) + matcher.group(2) + matcher.group(3) + matcher.group(4));
                // starting coordinates
                this.position = Coordinate.from(matcher.group(1), matcher.group(2));
                // movement 
                this.movement = Coordinate.from(matcher.group(3), matcher.group(4));
            }
        }

        static void processLine(String line) {
            Robot robot = new Robot(line);
            robot.move();
        }

        static int mod(int a, int b) {
            // System.out.println(a + " " + b);
            int c = a % b;
            return c >= 0 ? c : c + b;
        }

        void move() {
            int endColPosition = mod((position.col() + (movement.col() * 100)), Grid.cols);
            int endRowPosition = mod((position.row() + (movement.row() * 100)), Grid.rows);

            // Grid.sampleGrid[endRowPosition][endColPosition] += 1;

            // System.out.print(px + " ");
            // System.out.print(py);
            // System.out.println();

            if (endRowPosition == Grid.HORIZONTAL_LINE || endColPosition == Grid.VERTICAL_LINE) {
                // discarded robots
            } else {
                if (endRowPosition < Grid.HORIZONTAL_LINE) {
                    // Top Quadrants
                    if (endColPosition < Grid.VERTICAL_LINE) {
                        //Top Left
                        Grid.quadrant.merge("TopLeft", 1, Integer::sum);
                    } else {
                        // Top Right
                        Grid.quadrant.merge("TopRight", 1, Integer::sum);
                    }
                }
                if (endRowPosition > Grid.HORIZONTAL_LINE) {
                    // Bottom Quadrants
                    if (endColPosition < Grid.VERTICAL_LINE) {
                        //Bottom Left
                        Grid.quadrant.merge("BottomLeft", 1, Integer::sum);
                    } else {
                        // Bottom Right
                        Grid.quadrant.merge("BottomRight", 1, Integer::sum);
                    }
                }
            }
        }
    }
}
