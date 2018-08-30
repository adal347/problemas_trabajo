int arrayPacking(int[] a) {
        String binary = "";
        for (int i = a.length - 1; i >= 0; i--) {
            binary += String.format("%8s", Integer.toBinaryString(a[i])).replace(" ", "0");
        }
        return Integer.parseInt(binary, 2);
    }
