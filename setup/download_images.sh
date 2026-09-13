#!/bin/bash
set -e

mkdir -p images
cd images

BASE_URL="https://github.com/cdrias-empa/ToPNoise/releases/latest/download"

wget -O MultiSleeperModel.sif "$BASE_URL/MultiSleeperModel.sif"
wget -O WheelToolbox.sif "$BASE_URL/WheelToolbox.sif"
wget -O Postprocessing.sif "$BASE_URL/Postprocessing.sif"

wget -O topnoisebem.sif.part1 "$BASE_URL/topnoisebem.sif.part1"
wget -O topnoisebem.sif.part2 "$BASE_URL/topnoisebem.sif.part2"

cat topnoisebem.sif.part1 topnoisebem.sif.part2 > topnoisebem.sif

rm topnoisebem.sif.part1 topnoisebem.sif.part2

echo "ToPNoise container images downloaded successfully."