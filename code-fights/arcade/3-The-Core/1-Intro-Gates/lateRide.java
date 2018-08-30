int lateRide(int n) {
    int hours = n/60;
    int minutes = n%60;
    int theTime = 0;
    String timing = Integer.toString(hours) + Integer.toString(minutes);
    for (int i = 0; i < timing.length(); i++) {
        char number = timing.charAt(i);
        System.out.println(theTime);
        theTime += Integer.parseInt(String.valueOf(number));
    }
    return theTime;
}
