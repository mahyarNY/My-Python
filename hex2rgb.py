def rgb_hex():
  invalid_msg = "Invalid message!"
  red = int(raw_input("Enter a red value: "))
  if red < 0 and red > 255:
    print "You've entered an invalid red number"
    return
  green = int(raw_input("Enter a green value: "))
  if green < 0 and green > 255:
    print "You've entered an invalid green number"
    return
  blue = int(raw_input("Enter a blue value: "))
  if blue < 0 and blue > 255:
    print "You've entered an invalid blue number"
    return
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:].upper())
def hex_rgb():
  hex_val = raw_input("Enter the color(six hexadecimal digits): ")
  if len(hex_val) != 6:
    print "You've entered an invalid number!"
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_va3 >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s " %(red,green,blue)
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to HEX ..."
      rgb_hex()
    elif option == "2":
      print "HEX to RGB ..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Error."
      
      
convert()      
      
      
      
      
      
      
      
      
