import snappy

s = u"this is a very very basic correctness test".encode('utf-8')
assert snappy.uncompress(snappy.compress(s)) == s
