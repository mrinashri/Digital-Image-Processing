import cv2

def encode(img, msg):
    msg += '####'  # EOF marker
    data_index = 0
    binary_msg = ''.join([format(ord(i), '08b') for i in msg])
    data_len = len(binary_msg)
    
    for row in img:
        for pixel in row:
            for n in range(3):  # R, G, B
                if data_index < data_len:
                    pixel[n] = int(bin(pixel[n])[2:-1] + binary_msg[data_index], 2)
                    data_index += 1
    return img

def decode(img):
    binary_data = ''
    for row in img:
        for pixel in row:
            for n in range(3):
                binary_data += bin(pixel[n])[-1]
    
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''
    for byte in all_bytes:
        char = chr(int(byte, 2))
        decoded += char
        if decoded[-4:] == '####':
            break
    return decoded[:-4]

img = cv2.imread('pexels6.jpg')
secret = "MJ"
encoded = encode(img.copy(), secret)
cv2.imwrite('encoded.png', encoded)

decoded_msg = decode(cv2.imread('encoded.png'))
print("Decoded:", decoded_msg)