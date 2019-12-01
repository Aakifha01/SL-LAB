function oddRange(a, b) {
    for (i = a + 1; i < b; i++) {
        if (i % 2 != 0)
            console.log(i);
    }
}

oddRange(1, 7);