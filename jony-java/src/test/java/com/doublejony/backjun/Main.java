package com.doublejony.backjun;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        int count = 5;
        String[] input = new String[count];
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < count; i++) {
            input[i] = scanner.next();
        }

        String answer = solution(input);

        System.out.println(answer);
    }

    public static String solution(String[] input) {
        return input[0];
    }
}