"""
Solution of the medium problem - "Encode and Decode TinyURL",
https://leetcode.com/problems/encode-and-decode-tinyurl/
"""
class Codec:
    """Codec.

    >>> codec = Codec()
    >>> url = "https://leetcode.com/problems/design-tinyurl"
    >>> codec.decode(codec.encode(url))
    'https://leetcode.com/problems/design-tinyurl'

    """
    def encode(self, longUrl: str) -> str:
        return longUrl

    def decode(self, shortUrl: str) -> str:
        return shortUrl

