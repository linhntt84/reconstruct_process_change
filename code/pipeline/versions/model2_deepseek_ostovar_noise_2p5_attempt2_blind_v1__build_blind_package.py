#!/usr/bin/env python3
"""Build a fresh blind-grading package for Ostovar 2.5% Attempt 2.

The implementation reuses the validated v1 packager but replaces every input,
output, and ID-seed constant.  Consequently, Attempt 2 receives a completely
new opaque ID namespace and cannot be linked to Attempt 1 by grading ID.
"""

from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = Path(__file__).resolve().parents[4]
V1_PACKAGE = (
    WORKSPACE
    / "Latex/Kết quả thực nghiệm/model2_deepseek_ostovar_noise_2p5_blind_v1"
)
V1_BUILDER = V1_PACKAGE / "scripts/build_blind_package.py"


def load_v1_builder():
    spec = importlib.util.spec_from_file_location("noise2p5_v1_builder", V1_BUILDER)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot load validated builder: {V1_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_v1_builder()
    module.PACKAGE = PACKAGE
    module.WORKSPACE = WORKSPACE
    module.MANIFEST = (
        WORKSPACE
        / "Experiments/IEEE_ACCESS/manifests/model2_deepseek_v4_flash/"
        "ostovar_noise_2p5_integrated_26_attempt2.csv"
    )
    module.RUN = (
        WORKSPACE
        / "Experiments/IEEE_ACCESS/runs/"
        "model2_deepseek_v4_flash_ostovar_noise_2p5_integrated_26_attempt2"
    )
    module.TRUTH = (
        WORKSPACE
        / "Experiments/IEEE_ACCESS/ground_truth/"
        "ostovar_size3_atomic_noise_2p5_object_ground_truth_v1.csv"
    )
    module.PUBLIC = PACKAGE / "for_claude/blind_items.csv"
    module.PRIVATE = PACKAGE / "internal_after_grading/private_blind_key.csv"
    module.AUDIT = PACKAGE / "provenance/run_audit.csv"
    module.SUMMARY = PACKAGE / "provenance/run_summary.json"
    module.BATCH_DIR = PACKAGE / "for_claude/batches"
    module.CHECKSUMS = PACKAGE / "SHA256SUMS"
    module.SEED = "noise-2p5-deepseek-attempt2-blind-v1-20260920-5e37c9"

    public_dir = PACKAGE / "for_claude"
    public_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(
        V1_PACKAGE / "for_claude/RUBRIC_BLIND_V1_VI.md",
        public_dir / "RUBRIC_BLIND_V1_VI.md",
    )
    shutil.copyfile(
        V1_PACKAGE / "for_claude/PROMPT_FOR_GRADER.md",
        public_dir / "PROMPT_FOR_GRADER.md",
    )
    module.main()


if __name__ == "__main__":
    main()
