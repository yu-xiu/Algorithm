class zigzag {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        ArrayList<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < Math.min(numRows, s.length()); i++) {
            rows.add(new StringBuilder());
        }
        int currRow = 0;
        boolean goesDown = false;
        for (char c : s.toCharArray()) {
            rows.get(currRow).append(c);
            //betwee first and last row; goes down, else goes up
            if (currRow == 0 || currRow == numRows - 1) {
                goesDown = !goesDown;
            }
            // goesDown is true, currRow + 1; goesDown is false, currRow - 1;
            currRow += goesDown ? 1 : -1;
        }
        String res = "";
        for (StringBuilder row : rows) {
            res += row.toString();
        }
        return res;
    }
}