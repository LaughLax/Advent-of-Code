package y2020;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;

import com.google.common.base.Splitter;
import com.google.common.collect.ImmutableList;
import com.google.common.io.Files;

public class AOCSolver_2020_01 {

    final int YEAR = 2020;
    final int DAY = 1;

    String inputFileString;
    ImmutableList<Integer> inputValues;

    public static void main(String[] args) throws IOException {
        AOCSolver_2020_01 aoc = new AOCSolver_2020_01();
        aoc.run();
    }

    public AOCSolver_2020_01() {
        this.readInput();
    }

    public void run() {
        this.convertInput();
        System.out.printf("Part 1 result: %d\n", this.partOne());
        System.out.printf("Part 2 result: %d\n", this.partTwo());
    }

    public int partOne() {
        Integer[] sortedInputValues = ImmutableList.sortedCopyOf(inputValues).toArray(new Integer[0]);

        for (int i = 0; i < sortedInputValues.length; i++) {
            for (int j = 0; j < sortedInputValues.length; j++) {
                if (sortedInputValues[i] + sortedInputValues[j] > 2020) {
                    break;
                } else if (sortedInputValues[i] + sortedInputValues[j] == 2020) {
                    return sortedInputValues[i] * sortedInputValues[j];
                }
            }
        }
        return -1;
    }

    public int partTwo() {
        Integer[] sortedInputValues = ImmutableList.sortedCopyOf(inputValues).toArray(new Integer[0]);

        for (int i = 0; i < sortedInputValues.length; i++) {
            for (int j = i+1; j < sortedInputValues.length; j++) {
                if (sortedInputValues[i] + sortedInputValues[j] > 2020) {
                    break;
                }
                for (int k = j+1; k < sortedInputValues.length; k++) {
                    if (sortedInputValues[i] + sortedInputValues[j] + sortedInputValues[k] > 2020) {
                        break;
                    }
                    if (sortedInputValues[i] + sortedInputValues[j] + sortedInputValues[k] == 2020) {
                        return sortedInputValues[i] * sortedInputValues[j] * sortedInputValues[k];
                    }
                }
            }
        }
        return -1;
    }

    private void readInput() {
        String filePath = String.format("input\\%d\\%02d.txt", YEAR, DAY);
        File file = new File(filePath);
        Charset charset = Charset.defaultCharset();
        try {
            inputFileString = Files.asCharSource(file, charset).read();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void convertInput() {
        Splitter splitter = Splitter.on('\n').omitEmptyStrings().trimResults();
        
        ImmutableList.Builder<Integer> inputValueBuilder = new ImmutableList.Builder<Integer>();
        splitter.split(inputFileString).forEach(
            line -> { inputValueBuilder.add(Integer.valueOf(line));
        });
        inputValues = inputValueBuilder.build();
    }
}
