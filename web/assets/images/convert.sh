#!/bin/bash

#finally convert all images to Webp format
for f in *.jpg; do cwebp -q 90 "$f" -o "${f}".webp; done


for f in *.png; do cwebp -q 90 "$f" -o "${f}".webp; done
