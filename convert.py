import sys
import aspose.threed as a3d



def copy_file(filename):
    try:
        scene = a3d.Scene.from_file(filename + ".obj")
        scene.save(filename + ".stl")
        print("OBJ file converted and saved as " + filename + ".stl")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        copy_file(sys.argv[1])