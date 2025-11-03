import json, numpy as np
from PIL import Image

def load_image(path):
    return np.array(Image.open(path).convert("RGB"))

def save_image(arr, path):
    Image.fromarray(arr.astype(np.uint8)).save(path)

# === Pixel Operations ===
def op_add(arr, val): 
    return np.clip(arr + val, 0, 255)

def op_subtract(arr, val): 
    return np.clip(arr - val, 0, 255)

def op_swap(arr):
    # simple pixel swap: flip vertically
    return np.flipud(arr)

def op_xor(arr, val):
    # XOR every pixel with the given value
    return np.bitwise_xor(arr, val)

# === Encrypt ===
def encrypt(input_path, output_path, op, val, meta_path):
    arr = load_image(input_path)

    if op == "add":
        out = op_add(arr, val)
        meta = {"op": "subtract", "val": val}

    elif op == "subtract":
        out = op_subtract(arr, val)
        meta = {"op": "add", "val": val}

    elif op == "swap":
        out = op_swap(arr)
        meta = {"op": "swap"}  # swap is symmetric

    elif op == "xor":
        out = op_xor(arr, val)
        meta = {"op": "xor", "val": val}

    else:
        raise ValueError("Unsupported operation")

    save_image(out, output_path)
    with open(meta_path, "w") as f:
        json.dump(meta, f)
    print(f"[✔] Encrypted → {output_path}")

# === Decrypt ===
def decrypt(input_path, output_path, meta_path):
    arr = load_image(input_path)

    with open(meta_path) as f:
        meta = json.load(f)

    if meta["op"] == "add":
        out = op_add(arr, meta["val"])
    elif meta["op"] == "subtract":
        out = op_subtract(arr, meta["val"])
    elif meta["op"] == "swap":
        out = op_swap(arr)  # swap twice restores original
    elif meta["op"] == "xor":
        out = op_xor(arr, meta["val"])  # XOR is symmetric
    else:
        raise ValueError("Unsupported inverse")

    save_image(out, output_path)
    print(f"[✔] Decrypted → {output_path}")

# === Menu ===
def main_menu():
    print("\n=== ImageCrypt Tool ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        input_path = input("Enter input image path: ").strip('"')
        output_path = input("Enter output encrypted image path: ").strip('"')
        op = input("Enter operation (add/subtract/swap/xor): ").strip().lower()
        val = 0
        if op in ["add", "subtract", "xor"]:
            val = int(input("Enter value (e.g., 50 or key for xor): "))
        meta_path = input("Enter metadata filename (e.g., meta.json): ").strip()
        encrypt(input_path, output_path, op, val, meta_path)

    elif choice == "2":
        input_path = input("Enter encrypted image path: ").strip('"')
        output_path = input("Enter output decrypted image path: ").strip('"')
        meta_path = input("Enter metadata filename: ").strip()
        decrypt(input_path, output_path, meta_path)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main_menu()
