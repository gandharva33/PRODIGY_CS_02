# 🔐 PixelCrypt

A lightweight, browser-based image encryption tool that scrambles image pixels using a numeric key — no server, no uploads, no dependencies.

![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES5-yellow?logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## ✨ Features

- **Client-side only** — all processing happens in your browser; images never leave your device
- **XOR-based pixel encryption** — each pixel's RGB channels are scrambled using a seeded pseudo-random key stream
- **Encrypt & decrypt** — toggle between encrypted and original with the same key
- **Save output** — download the encrypted (or decrypted) image as a PNG
- **Zero dependencies** — pure HTML + vanilla JavaScript, no frameworks or libraries needed

---

## 🚀 Getting Started

No build step required. Just open the file in a browser.

```bash
# Clone the repo
git clone https://github.com/gandharva33/pixelcrypt.git
cd pixelcrypt

# Open directly in your browser
open index.html
```

Or simply drag `index.html` into any modern browser window.

---

## 🛠️ How to Use

1. **Load an image** — click the file input and select any image (PNG, JPG, WebP, etc.)
2. **Set a key** — enter a numeric key between `1` and `999999` (default: `42`)
3. **Encrypt** — click **🔒 Encrypt** to scramble the image; the result appears on the right canvas
4. **Decrypt** — with the same key loaded, click **🔓 Decrypt** to restore the original
5. **Save** — click **💾 Save** to download the output canvas as `output.png`

> ⚠️ **Important:** You must use the exact same key to decrypt an image that was encrypted with it. There is no key recovery mechanism.

---

## 🔬 How It Works

PixelCrypt uses a seeded linear congruential generator (LCG) to produce a deterministic pseudo-random key stream, then XORs each pixel's RGB channels against it.

```
seed  = (key × 9973) mod 2147483647
per pixel:
  seed  = (seed × 16807) mod 2147483647
  pk    = floor((seed − 1) / 2147483646 × 256)

  R  ^= (key       XOR pk XOR (pixelIndex mod 251))
  G  ^= ((key>>3)  XOR pk XOR ((pixelIndex × 3) mod 251))
  B  ^= ((key>>5)  XOR pk XOR ((pixelIndex × 7) mod 251))
```

Because XOR is its own inverse, the same function encrypts and decrypts — applying it twice with the same key returns the original data.

> **Note:** This is a demonstration of pixel-level obfuscation, not cryptographic-grade encryption. Do not use it to protect sensitive data.

---

## 📁 Project Structure

```
pixelcrypt/
└── index.html   # The entire app — HTML, CSS, and JS in one file
```

---

## 🌐 Browser Compatibility

Works in any modern browser that supports the [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) and `getImageData`.

| Browser | Support |
|---------|---------|
| Chrome  | ✅ |
| Firefox | ✅ |
| Safari  | ✅ |
| Edge    | ✅ |

---

## 📄 License

MIT — free to use, modify, and distribute.
