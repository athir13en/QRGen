# Importing library
import qrcode
 
# Data to be encoded
data = 'www.google.com'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode.png')