def gem():
    yield "first"
    yield "second"
    yield "third"

for res in gem():
    print res
