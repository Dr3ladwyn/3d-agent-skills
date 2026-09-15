#!/usr/bin/env bash

set -e

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)

TARGET=${1:-"$HOME/.agent-skills/3d-agent-skills"}

mkdir -p "$TARGET"
cp -R "$ROOT_DIR"/* "$TARGET"/

echo "Installed 3D Agent Skills to $TARGET"
echo "Configure your AI harness to load skills from this directory."
