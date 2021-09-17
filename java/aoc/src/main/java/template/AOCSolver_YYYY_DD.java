package template;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;

import com.google.common.base.Splitter;
import com.google.common.collect.ImmutableList;
import com.google.common.io.Files;

public class AOCSolver_YYYY_DD {

    final int YEAR = 2020;
    final int DAY = 1;

    String inputFileString;
    ImmutableList<Integer> inputValues;

    public static void main(String[] args) throws IOException {
        AOCSolver_YYYY_DD aoc = new AOCSolver_YYYY_DD();
        aoc.run();
    }

    public AOCSolver_YYYY_DD() {
        this.readInput();
    }

    public void run() {
        this.convertInput();
        System.out.printf("Part 1 result: %d\n", this.partOne());
        System.out.printf("Part 2 result: %d\n", this.partTwo());
    }

    public int partOne() {
        return -1;
    }

    public int partTwo() {
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
