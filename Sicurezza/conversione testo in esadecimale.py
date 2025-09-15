n= "00a5cae65abe0b036c27b740326e37"+\
    "a9e2a3e5963b0cf64b8f2d1aaab751"+\
    "d6d1aad3090ab0c81ce28e4a16e733"+\
    "0ef0fb41a3f027e450ac398daebc57"+\
    "080e7ae8b330f69e0e954543dbcf79"+\
    "ee0edfeb0d80d13dfaf31279bb18b6"+\
    "3517ca931149a90ad05262d360a257"+\
    "4b79f77f48e968d8a33f64cf9c613b"+\
    "4fc8a6e85892634796c98e3cffbf07"+\
    "ff4dcd55387aa712845da593449a98"+\
    "3be4e54bf72b742534387993912473"+\
    "94eefec7e271e68e4bba85b657d9d3"+\
    "e3e2d17ab79fd30fac61f41af664c6"+\
    "ec36e80ce0931f33f95ac929604a7b"+\
    "4b2192e609aab63cd434895d850661"+\
    "dc5808a8a5025bb03f05605e51c738"+\
    "32801449caccff8aac0f4eccc4b970"+\
    "f63b"

decimale = int(n,16) # trasformazione del numero esadecimale a decimale 
M="Ciao come va?.."
Mi=int(M.encode("utf-8").hex(), 16)
print(Mi)
e=3

c=pow(Mi,e,decimale) # cifratura del messaggio

print(c)

d="1ba1d10f1fac8092069e8ab3125e9c"+\
    "5070a643b482290c97dcd9c71e8da3"+\
    "cd9c788181c8215a25c261ae7bddd7"+\
    "d2d48af0a806a60d7209979d1f63d6"+\
    "ad147c1ddd7e6fad18e0e0a4a29452"+\
    "57cffc824022dfa9d32dbef4841e5e"+\
    "2ea1c32d8c46d722b865cde57063e1"+\
    "e9a93fe17c3c241b353b77ef6589e2"+\
    "a17126b96dbb3698dc64d7e5f11357"+\
    "0e33b083f3d3f0f628e8467942e8a2"+\
    "906f62303fbaba45339ddc43a8e7c2"+\
    "a559fe219cc5a4bb7a3eeb39ffe9f4"+\
    "122b93ba299f27709654f1e0efa38c"+\
    "1169583115250e66d4dbb972d66aee"+\
    "00dd214303a17b5060ab79da19d338"+\
    "b0e7d1debfca2973b9069ba129a503"+\
    "ccccde926e7ac9fe69e20f520990f00b"
d = int(d,16) # trasformazione esadecimale decimale 
decifrato= pow(c,d,decimale) #decifratura del messaggio 
print(decifrato)