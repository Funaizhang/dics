import json
import argparse
from PIL import Image
import random
import os

def crop_faces(landmarks, input, output, output_fail, confidence, ratio, min_size, size):
    with open(landmarks, 'r') as f:
        json_file = f.read()
        landmarks = json.loads(json_file)
        for key in landmarks:
            faces = landmarks[key]
            fn = os.path.join(input, key)
            if os.path.exists(fn):
                img = Image.open(fn)
                for j, face in enumerate(faces):
                    if face['score'] >= confidence or output_fail is not None:
                        out_folder = output if face['score'] >= confidence else output_fail
                        box = face['bbox']
                        width = box[2] - box[0]
                        height = box[3] - box[1]
                        m = max(width, height)
                        pad_w = (m - width) / 2
                        pad_h = (m - height) / 2
                        side_coef = (ratio - 1) / 2
                        if width * ratio < min_size or height * ratio < min_size:
                            continue
                        crop = img.crop((box[0] - pad_w - m * side_coef,
                                        box[1] - pad_h - m * side_coef,
                                        box[2] + pad_w + m * side_coef,
                                        box[3] + pad_h + m * side_coef))
                        if size > 0:
                            crop = crop.resize((size, size), Image.ANTIALIAS)
                        save_fn = os.path.join(out_folder, '{}-{}.png'.format(key, j))
                        crop.save(save_fn)
            else:
                print('skip {}'.format(fn))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-output', help='output folder path')
    parser.add_argument('-output-fail', default=None, help='weak likelihood output folder path')
    parser.add_argument('-input', help='input folder path')
    parser.add_argument('-landmarks', help='landmark json path')
    parser.add_argument('-conf', type=float, default=0.1, help='minimum confidence threshold')
    parser.add_argument('-ratio', type=float, default=1.2, help='face cutting ratio')
    parser.add_argument('-min-size', type=int, default=64, help='minimum face size')
    parser.add_argument('-size', type=int, default=-1, help='desired face size')
    args = parser.parse_args()

    crop_faces(args.landmarks, args.input, args.output, args.output_fail, args.conf, args.ratio, args.min_size, args.size)
