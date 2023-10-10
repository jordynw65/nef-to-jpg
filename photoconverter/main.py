import glob
import rawpy
import imageio


def main():
    # sometimes the file ending can be .nef or .NEF, therefore I included both possibilities to save extra work.
    directory = "/path/to/image/directory"
    pathnef = glob.glob(f"{directory}/*.nef")
    pathNEF = glob.glob(f"{directory}/*.NEF")
    count = 0

    # check the total number of images to begin with
    number_files = len(pathnef) + len(pathNEF)
    print("Total Number of Images: ", number_files)
    for path in pathnef:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.nef', '') + '.jpg', rgb)
            count = count + 1
        print(count, '/', number_files)
    for path in pathNEF:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imwrite(path.replace('.NEF', '') + '.jpg', rgb)
            count = count + 1
        print(count, '/', number_files)


if __name__ == '__main__':
    main()
