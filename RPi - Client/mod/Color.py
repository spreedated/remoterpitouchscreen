class ColorConversion():
	def RGBA_to_Float(R, G, B, A=255):
		R = float("{0:.2f}".format(R/255))
		G = float("{0:.2f}".format(G/255))
		B = float("{0:.2f}".format(B/255))
		A = float("{0:.2f}".format(A/255))

		return (R,G,B,A)

class Colors():
	#Fonts
	standardFont = (0.99,0.61,0,1)
	#Elements
	black = ColorConversion.RGBA_to_Float(0,0,0)
	white = ColorConversion.RGBA_to_Float(255,255,255)
	lightyellow = ColorConversion.RGBA_to_Float(241,223,111)
	yellow = ColorConversion.RGBA_to_Float(255,255,51)
	orange = ColorConversion.RGBA_to_Float(254,154,0)
	darkRed = ColorConversion.RGBA_to_Float(181,0,6)
	neonRed = ColorConversion.RGBA_to_Float(237,26,33)
	skyBlue = ColorConversion.RGBA_to_Float(156,160,255)
	lightBlue = ColorConversion.RGBA_to_Float(153,205,255)
	green = ColorConversion.RGBA_to_Float(0,168,89)
