import os
import argparse
import random
import shutil

def format_data(name, samples, input, output):
    fn = os.path.join(output, 'list_{}.txt'.format(name))
    out_folder = os.path.join(output, name)
    print(out_folder)
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    with open(fn, 'w+') as f:
        print('open {}'.format(fn))
        for sample in samples:
            f.write('./{}\n'.format(sample))
            shutil.copy(os.path.join(input, sample), out_folder)

def prepare_data(input, output, max_size, name, test_ratio):
    samples = os.listdir(input)
    random.shuffle(samples)
    samples = samples[:max_size]
    threshold = int(test_ratio * len(samples))
    test_samples = samples[:threshold]
    train_samples = samples[threshold:]
    format_data('test{}'.format(name), test_samples, input, output)
    format_data('train{}'.format(name), train_samples, input, output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='input folder path')
    parser.add_argument('-output', help='output folder path')
    parser.add_argument('-name', help='dataset name')
    parser.add_argument('-max-size', default=None, help='maximum number of samples')
    parser.add_argument('-test-ratio', default=0.3, help='maximum number of samples')
    args = parser.parse_args()

    prepare_data(args.input, args.output, args.max_size, args.name, args.test_ratio)
