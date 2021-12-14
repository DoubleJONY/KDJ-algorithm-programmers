package com.doublejony.backjun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        List<String> input = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String temp;

        while ((temp = br.readLine()) != null && !temp.isEmpty()) {
            input.add(temp);
        }
        String answer = new Main().solution(input.toArray(new String[input.size()]));

        System.out.println(answer);
    }

    public String solution(String[] input) {

        int classSize = Integer.parseInt(input[0]);
        int major = Integer.parseInt(input[2].split(" ")[0]);
        double minor = Integer.parseInt(input[2].split(" ")[1]);

        int answer = 0;

        for (int i = 0; i < classSize; i++) {
            double a = Integer.parseInt(input[1].split(" ")[i]) - major;
            answer += a > 0 ? Math.ceil(a / minor) + 1 : 1;
        }

        return Integer.toString(answer);
    }
}
