import sys
import base64
import img.encodedImages

# f = open('img/bg_inara.b64','rb')
# b64img = f.read()
# f.close()

b64img = img.encodedImages.bg_inara

print(b64img)
#sys.exit()

#b64encoded = base64.encodebytes(b64img.encode())
b64encoded = b64img
print(b64encoded)

b64encoded = b64encoded.replace(b'\n',b'')
b64encoded = b64encoded.replace(b'\r',b'')
print(b64encoded)

f = open('img/test.png','wb+')
f.write(base64.decodebytes(b64encoded))
f.close()

print('Done!')
