import sys
from PIL import Image

def resize_gif(input_path, output_path, width, height):
    img = Image.open(input_path)
    frames = []
    durations = []
    
    transparency = img.info.get('transparency', None)
    disposal = img.info.get("disposal", 2)
    last_frame = Image.new("RGBA", img.size)

    try:
        while True:
            frame = img.convert("RGBA")
            
            if disposal == 2:
                combined = frame
            else:
                combined = Image.alpha_composite(last_frame, frame)
            
            resized_frame = combined.resize((width, height), Image.LANCZOS)
            frames.append(resized_frame.convert("P", palette=Image.ADAPTIVE))
            
            durations.append(img.info['duration'])
            last_frame = combined if disposal != 2 else frame.copy()
            
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    save_kwargs = {
        "save_all": True,
        "append_images": frames[1:],
        "loop": 0,
        "duration": durations,
        "disposal": disposal,
    }

    if transparency is not None:
        save_kwargs["transparency"] = transparency

    frames[0].save(output_path, **save_kwargs)

def main():
    if len(sys.argv) != 5:
        print("Usage: gif-resizer <input_path> <output_path> <width> <height>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])

    resize_gif(input_path, output_path, width, height)
    print(f"Resized GIF saved as {output_path}")

if __name__ == "__main__":
    main()
