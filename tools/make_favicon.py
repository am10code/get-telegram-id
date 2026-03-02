import struct, zlib, binascii, os

BG = (11, 18, 32, 255)      # #0b1220
FG = (255, 255, 255, 255)   # white

def png_from_rgba(width, height, rgba_bytes):
    # Each scanline: filter byte 0 + RGBA pixels
    stride = width * 4
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        raw.extend(rgba_bytes[y*stride:(y+1)*stride])
    comp = zlib.compress(bytes(raw), level=9)

    def chunk(typ, data):
        crc = binascii.crc32(typ + data) & 0xffffffff
        return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", crc)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)  # 8-bit, RGBA
    return sig + chunk(b'IHDR', ihdr) + chunk(b'IDAT', comp) + chunk(b'IEND', b'')

def ico_with_png(png_bytes, width, height):
    icondir = struct.pack("<HHH", 0, 1, 1)  # reserved, type=icon, count=1
    w = width if width < 256 else 0
    h = height if height < 256 else 0
    entry = struct.pack("<BBBBHHII", w, h, 0, 0, 1, 32, len(png_bytes), 6 + 16)
    return icondir + entry + png_bytes

def put_rect(buf, w, h, x0, y0, rw, rh, color):
    r,g,b,a = color
    for y in range(max(0, y0), min(h, y0+rh)):
        for x in range(max(0, x0), min(w, x0+rw)):
            i = (y*w + x) * 4
            buf[i:i+4] = bytes([r,g,b,a])

def main():
    os.makedirs("static", exist_ok=True)
    w = h = 64
    buf = bytearray(bytes(BG) * (w*h))

    # Simple pixel-font glyphs (5x7) for "I" and "D"
    I = [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11111",
    ]
    D = [
        "11110",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11110",
    ]

    scale = 6  # 5*6=30 width per glyph
    gap = 4
    glyph_h = 7 * scale
    total_w = (5*scale) + gap + (5*scale)
    x_start = (w - total_w) // 2
    y_start = (h - glyph_h) // 2

    def draw_glyph(glyph, xoff):
        for gy, row in enumerate(glyph):
            for gx, ch in enumerate(row):
                if ch == "1":
                    put_rect(buf, w, h, xoff + gx*scale, y_start + gy*scale, scale, scale, FG)

    draw_glyph(I, x_start)
    draw_glyph(D, x_start + 5*scale + gap)

    png = png_from_rgba(w, h, bytes(buf))
    ico = ico_with_png(png, w, h)

    out = "static/favicon.ico"
    with open(out, "wb") as f:
        f.write(ico)
    print(f"Generated {out} with 'ID' mark")

if __name__ == "__main__":
    main()
