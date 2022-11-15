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
    count = 0
    for path in glob.glob(pathnef):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()

            imageio.imwrite(path.replace('.nef', '') + '.jpg', rgb)
            count = count + 1
            print('image #', count, ' done')

    for path in glob.glob(pathNEF):
        count = +1

        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.NEF', '') + '.jpg', rgb)
            count = count + 1
            print('image #', count, ' done')

    # Timer is optional
    end = time.time()
    minutes = (end - start) / 60
    seconds = (end - start) % 60

    print("Elapsed Time:", round(minutes), "minutes and ", round(seconds), "seconds")


if __name__ == '__main__':
    main()
