import cv2
import argparse
import os

DEFAULT_OUT_DIRECTORY = 'out'

def save_dimension(img, h: int, w: int, dir_name, file_name):
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    print(f'Resizing {file_name} to {w}x{h}...')

    dim = (w , h)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f"{dir_name}/{file_name}.png", resized)

def process_file(path, out_file_name):
    print('Open image...')
    cv_image = cv2.imread(path, cv2.INTER_AREA)
    original_h, original_w, original_d = cv_image.shape
    if original_h != original_w:
        raise Exception('Orginal image must be square')
    if original_h < 192:
        raise Exception('Original dimensions must be >= 192px')

    save_dimension(cv_image, 192, 192, f'{out_dir}/mipmap-xxxhdpi', out_file_name)
    save_dimension(cv_image, 144, 144, f'{out_dir}/mipmap-xxhdpi', out_file_name)
    save_dimension(cv_image, 96, 96, f'{out_dir}/mipmap-xhdpi', out_file_name)
    save_dimension(cv_image, 72, 72, f'{out_dir}/mipmap-hdpi', out_file_name)
    save_dimension(cv_image, 48, 48, f'{out_dir}/mipmap-mdpi', out_file_name)

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str, help="Input images file")
parser.add_argument('rounded', type=str, help="Input rounded image file")
parser.add_argument('--out','-o', type=str, help="Output directory")

args = parser.parse_args()
print(args.input)

out_dir = args.out

try:
    if not out_dir:
        if not os.path.isdir(DEFAULT_OUT_DIRECTORY):
            os.makedirs(DEFAULT_OUT_DIRECTORY)
        out_dir = DEFAULT_OUT_DIRECTORY
    else:
        if not os.path.isdir(out_dir):
            raise Exception('Out directory is not exist')


    if not os.path.isfile(args.input):
        raise Exception('Input file is not exist')
    if not os.path.isfile(args.rounded):
        raise Exception('Input rounded file is not exist')

    process_file(args.input, 'ic_launcher')
    process_file(args.rounded, 'ic_launcher_round')

    print('Done.')
except Exception as e:
    print(e)