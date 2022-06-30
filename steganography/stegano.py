from PIL import Image
from pprint import pprint as pp


def compare_images(firstImg, secondImg):
    img1 = Image.open(firstImg)
    img2 = Image.open(secondImg)
    
    print_pixels(img1, img2)
    
    print("kahjuks samad pildid :(") if img1.load()==img2.load() else print("erinevad pildid!")


def print_pixels(img1, img2):
    pixels = img1.load()
    list_of_pixels = []
    
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            list_of_pixels.append(pixels[i,j])
    
    pp(list_of_pixels)
    
    pixels = img2.load()
    list_of_pixels = []
    
    for i in range(img2.size[0]):
        for j in range(img2.size[1]):
            list_of_pixels.append(pixels[i,j])
    
    pp(list_of_pixels)


def generate_binary(message):
    return ["".join('0'+b[2:]) for b in list(map(lambda item: bin(ord(item)), message))]


def encode_data(inputImg, outputImg, msg):
    img = Image.open(inputImg)
    pixels = img.load()

    #just a debugging variable
    d = 1

    binaries = generate_binary(msg)
    #print("binary for message: ", binaries)
        
    vertical = 0 #currently only encodes in vertical
    horizontal = 0 #just for future reference, doesn't do anything rn
    
    #loop through each binary
    for n in range(len(binaries)):

        letter = binaries[n]
        valueIndex = 0
        
        #loop through 3 pixels
        for i in range(3):

            current = list(pixels[horizontal, vertical]) #current RGB values
            #print("starter pixel: ", current)
            vertical += 1
            
            #loop through binary values
            for j in range(3):
          
                cpixel = current[j] #current value
                #print("current pixel: ", cpixel)
                
                #change last value to even if more, odd if no more.
                #important for the decoder
                if valueIndex==8 and j==2:
                
                    if n+1==len(binaries):
                       
                        if cpixel%2==0:
                            cpixel += 1
                        
                    else:
                        
                        if cpixel%2!=0:
                            cpixel -= 1
                    
                    current[j] = cpixel
                    break    
                    
                cbinvalue = int(letter[valueIndex]) #current binary value in the letter
                
                #nested if statements
                if cpixel%2==0 and cbinvalue==0:
                    cpixel += d
                elif cpixel%2!=0 and cbinvalue==1:
                    cpixel -= d
                
                valueIndex += 1
                current[j] = cpixel
            
            pixels[horizontal, vertical-1] = tuple(current) #sõnum
            #pixels[horizontal, vertical-1] = (225, 0, 0) #värv
            
    img.save(outputImg)

    
def find_message(inputImg):
    img = Image.open(inputImg)
    pixels = img.load()
        
    vertical = 1 #currently only encodes in vertical
    horizontal = 0 #just for future reference, doesn't do anything rn
    binaries = [] #for storing found binary values
    flag = False #for dealing with the nested for-loop
    
    #while more data is encoded aka 3rd pixel 3rd value is even
    while True:
        
        newBinary = ""
        
        #loop through 3 pixels
        for i in range(3):
            
            currentPixel = list(pixels[horizontal, vertical-1])
            
            #loop through RGB values
            for j in range(3):
                
                value = currentPixel[j]
                
                #check if there's more data
                #even if more, odd if no more
                if vertical%3==0 and j==2 and value%2!=0:
                    binaries.append(newBinary)
                    return binaries
                elif vertical%3==0 and j==2 and value%2==0:
                    #need this part because we want to avoid reading the info as data
                    continue
                
                #nested if statements for assignment
                if value%2==0:
                    newBinary += "1"
                elif value%2!=0:
                    newBinary += "0"
                         
            vertical += 1
        
        binaries.append(newBinary)


def decode_data(binaries):
    message = ""
    
    for binary in binaries:
        code = int(binary, 2)
        message += str(code.to_bytes((code.bit_length() + 7) // 8, 'big').decode())

    return message


def main():
    message = "".join("hi".split(" "))
    encode_data("image.jpg", "muudetud_image.png", message)

    print(decode_data(find_message("muudetud_image.png")))


main()