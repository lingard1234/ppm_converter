def p6_to_p3(input_path, output_path):
    with open(input_path, "rb") as f:
        header = []
        while len(header) < 4:
            line = f.readline()
            if line.startswith(b'#'):
                continue
            header += line.strip().split()
        width, height, maxval = map(int, header[1:4])
        pixels = f.read()

    with open(output_path, "w") as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n{maxval}\n")
        for i in range(0, len(pixels), 3):
            f.write(f"{pixels[i]} {pixels[i+1]} {pixels[i+2]}\n")

# 실행
p6_to_p3("colorP6File.ppm", "colorP3File.ppm")
