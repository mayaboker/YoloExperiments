# YoloExperiments

A Hydra-based project for visually comparing pretrained YOLO26 model sizes on your own images and videos.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -e '.[dev]'
```

The explicit PyTorch command installs the CPU build. Use the appropriate PyTorch
CUDA installation command instead when running on an NVIDIA system.

## Run

```bash
.venv/bin/python main.py
```

Put one or more images or videos in `data/raw/`. The first run downloads the official
pretrained YOLO26 weights automatically. By default, it compares the nano,
small, medium, large, and extra-large models and displays bounding boxes, class
names, and confidence for car, person, motorcycle, bus, and animals.

Run on specific COCO classes by name:

```bash
.venv/bin/python main.py 'comparison.classes=[person,car]'
```

Choose fewer model sizes for a quicker comparison:

```bash
.venv/bin/python main.py 'comparison.models=[yolo26n.pt,yolo26s.pt]'
```

Use another input directory or adjust inference settings:

```bash
.venv/bin/python main.py data.source=/path/to/images comparison.confidence=0.4
```

Each Hydra run creates a directory under `outputs/` containing:

```text
comparisons/                 side-by-side images and MP4 videos
models/yolo26n/              annotated output from each model
models/yolo26s/
predictions.json             detected classes, confidence, and boxes
timings.csv                  load time, processing time, and effective FPS
.hydra/                      complete resolved run configuration
```

`animal` is a project class group that includes bird, cat, dog, horse, sheep,
cow, elephant, bear, zebra, and giraffe from the pretrained COCO classes.

Supported video formats include MP4, MOV, MKV, AVI, WebM, MPEG, MPG, and M4V.
Annotated video output uses MP4 with the `mp4v` codec. Quantitative metrics,
matrices, formal benchmarks, ONNX evaluation, and tracker evaluation are
reserved for later phases.

## Phase 2

Phase 2 exports selected pretrained models to ONNX and evaluates PyTorch and
ONNX runtimes against a labeled YOLO detection dataset. It produces latency
percentiles, effective FPS, per-object normalized box size, confidence,
confidence multiplied by normalized area, recall and precision by size bin,
and the minimum size bin meeting the configured reliable-recall threshold.

The benchmark is guarded and cannot run with the default configuration:

```bash
.venv/bin/python main.py task=benchmark
```

A valid dataset must be placed in `data/benchmarks/phase2/` and configured in
`configs/dataset/`. After reviewing the dataset and configuration, an explicit
run uses:

```bash
.venv/bin/python main.py task=benchmark dataset=<valid_config> task.confirm=true
```

The benchmark initializes a ClearML testing task with project
`YOLO_benchmark` and task name `diff_size_yolo_compare`. Phase 2 has not been
executed yet.

The configured dataset is a 210-frame official validation split from the
traffic-camera dataset linked in `configs/dataset/phase2.yaml`. It includes
bounding boxes and persistent track IDs. The source license is CC BY-NC-ND 4.0,
which restricts it to non-commercial use and prohibits distributing modified
versions.
