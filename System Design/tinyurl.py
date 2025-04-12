
# Super naive solution, just count it
class Codec:
    def __init__(self):
        self.count = 0
        self.longToShort = {}
        self.shortToLong = {}
        self.base = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.longToShort:
            return self.base + self.longToShort[longUrl]
        else:
            self.count += 1
            shortUrl = self.base + str(self.count)
            self.longToShort[longUrl] = shortUrl
            self.shortToLong[shortUrl] = longUrl
            return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortToLong[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
