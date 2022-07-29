import glob
import rawpy
import imageio
import time

print("Starting Now")
start = time.time()
# Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
pathnef = "/path/to/image/folder/*.nef" # KEEP /.nef AFTER PATH
pathNEF = "/path/to/image/folder/*.NEF" # KEEP /.NEF AFTER PATH
for path in glob.glob(pathnef):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(path + '.jpg', rgb)

for path in glob.glob(pathNEF):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(path + '.jpg', rgb)

end = time.time()
print("Elapsed Time:",round(end - start, 2), "seconds")
