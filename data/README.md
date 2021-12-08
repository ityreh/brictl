# Data

The data process is *raw -> generated -> labeled*. Original images are stored in raw and with data augmentation more versions of the original images are sotred in generated. The labeled files are then stored in labeled.

## raw > generated

Apply data augmentation to the raw images using the script `imgaug.py`:

    ./scripts/imgaug.py ./data/raw ./data/generated

## generated > labeled

To label the images we use [labelImg](https://pypi.org/project/labelImg/). The images are stored in generated and the labels are defined in [classes.txt](./classes.txt):

    labelImg ./generated ./classes.txt

To make labeling easier, use the following shortcuts:

| Shortcuts | Action                            |
| -         | -                                 |
| Ctrl + U  | loads all images from a folder    |
| Ctrl + R  | change folder for annotations     |
| Ctrl + S  | save current image                |
| Ctrl + D  | copy label and bounding box       |
| Space     | mark image as prooved             |
| W         | create a bounding box             |
| D         | next image                        |
| A         | previous image                    |
| Del       | delete a bounding box             |
| Ctrl + +  | zoom in                           |
| Ctrl + -  | zoom out                          |
| Arrows    | move bounding box                 |
