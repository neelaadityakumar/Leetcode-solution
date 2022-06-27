The idea of this problem is the following: let us keep 2 dictinoaries:
​
self.long_short to keep links between original long address and encoded short address.
self.short_long to keep the opposit connections.
Why we need to keep both dictionaries? Because we want to do fast encoding and decoding.
​
1.encode(self, longUrl) will work like this: let us try to generate random code, say with 6 symbols, which consists of letters. If this code was not used for some other long link, we are happy: we put connections to our direct and inverse dictionaries. If it happen, that this code was used for some other long link, we are not happy, and we generate one more code and so on.
2.decode(self, shortUrl) is pretty straightforward: we just look at our selfl.short_long dictionary.
​
​