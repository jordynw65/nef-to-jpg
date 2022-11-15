import glob
import rawpy
import imageio
import time


def main():
    # Timer is optional
    print("Starting Now")
    start = time.time()

    # Sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    pathnef = "/path/to/*.nef"
    pathNEF = "/path/to/*.NEF"
    for path in glob.glob(pathnef):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()

            imageio.imwrite(path.replace('.nef', '') + '.jpg', rgb)

    for path in glob.glob(pathNEF):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.NEF', '') + '.jpg', rgb)

    # Timer is optional
    end = time.time()
    minutes = (end - start) / 60
    seconds = (end - start) % 60

    print("Elapsed Time:", round(minutes), "minutes and ", round(seconds), "seconds")


if __name__ == '__main__':
    main()
