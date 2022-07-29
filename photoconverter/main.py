import glob
import rawpy
import imageio
import time

print("Starting Now")
start = time.time()
# Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
pathnef = "/Users/jordyn/Desktop/Jordyn/photoconverter/Single Image/*.nef"
pathNEF = "/Users/jordyn/Desktop/Jordyn/photoconverter/Single Image/*.NEF"
for path in glob.glob(pathnef):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(path + '.jpg', rgb)

for path in glob.glob(pathNEF):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(path + '.jpg', rgb)

end = time.time()
print("Elapsed Time:")
print(round(end - start, 2), "seconds")
