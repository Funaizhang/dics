# DICS - Deep Image-to-Comic Synthesis

## Usage

### Create your own manga dataset

1. Scraping Manga

List of compatible mangas can be found on this [page](https://ww1.animecruzers.io/read-manga/)

```
python MangaScraper.py "https://ww4.readonepiece.com/chapter/one-piece-digital-colored-comics-chapter-001/" "path/to/output"
```

2. Export landmarks

Follow instruction from 1 to 3 of this [README](https://github.com/couver-v/anime-face-detector/blob/master/README.md) to setup the project

Then run:
```
python anime-face-detector/main.py -i path/to/dir -o path/to/landmarks.json -model path/to/model.ckpt -conf 0.1
```

3. Crop faces

```
python crop_faces.py --landmarks=path/to/landmarks.json --input=path/to/input/dir --output=path/to/output --ratio=1.2 --min-size=64 --conf=0.1
```

### Download datasets
- [CelebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html): [Google Drive](https://drive.google.com/open?id=0B7EVK8r0v71pWEZsZE9oNnFzTm8)
- One Piece Face: [Google Drive](https://drive.google.com/open?id=1HHicP1ZgcL0VeuZA41P57R4ag_KKAX-B)

```
python download_datasets.py -output path/to/output
```

### Format dataset for MUNIT

for each dataset run:
```
prepare_data.py -input path/to/dir -output path/to/output -name dataset_name
```

## Main sites
* [Deeppomf's anime papers](https://github.com/deeppomf/DeepLearningAnimePapers)
* [Overleaf](https://www.overleaf.com/project/5cca6bb602327479035358ae)

## Main papers
* [MUNIT](https://github.com/NVlabs/MUNIT)
* [StyleGAN](https://github.com/NVlabs/stylegan)

## Misc papers
* [FUNIT](https://nvlabs.github.io/FUNIT/)
* [Paper - Improving Shape Deformation in Unsupervised Image-to-Image Translation](https://arxiv.org/pdf/1808.04325.pdf)
* [Paper - Towards the Automatic Anime Characters Creation with Generative Adversarial Networks](https://arxiv.org/pdf/1708.05509.pdf)

## Misc sites
* [Waifu dataset](https://www.thiswaifudoesnotexist.net/example-30.jpg)
* [Deeppomf's anime papers](https://github.com/deeppomf/DeepLearningAnimePapers)
* [Overleaf](https://www.overleaf.com/project/5cca6bb602327479035358ae)