import snappy

s = "this is a very very basic correctness test"
assert snappy.uncompress(snappy.compress(s)) == s
