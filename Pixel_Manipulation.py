from PIL import Image

def apply_xor(image, key):
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    return image

def encrypt(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    encrypted = apply_xor(image, key)
    encrypted.save(output_path)
    print(f"Encrypted image saved to: {output_path}")

def decrypt(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    decrypted = apply_xor(image, key)
    decrypted.save(output_path)
    print(f"Decrypted image saved to: {output_path}")

def main():
    print("=== Simple Image Encryptor ===")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter 1 or 2: ")
    input_path = input("Enter input image filename (e.g. photo.png): ")
    output_path = input("Enter output image filename (e.g. output.png): ")
    key = int(input("Enter secret key (1 to 255): "))

    if choice == "1":
        encrypt(input_path, output_path, key)
    elif choice == "2":
        decrypt(input_path, output_path, key)
    else:
        print("Invalid choice.")

main()
