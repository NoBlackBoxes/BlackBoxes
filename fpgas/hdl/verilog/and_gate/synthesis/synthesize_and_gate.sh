#!/bin/bash
set -eu

# Set Roots
NBB_ROOT="/home/${USER}/NoBlackBoxes"
LBB_ROOT=$NBB_ROOT"/LastBlackBox"

# Create out directory
mkdir -p bin

# Copy verilog module(s)
cp ../and_gate.v bin/.

# Copy constraints file
cp upduino.pcf bin/.

# Verify Verilog
apio verify --project-dir=bin --board upduino3 --verbose

# Synthesize
apio build --project-dir=bin --board upduino3 --verbose

# Upload
#apio upload --project-dir=bin --board upduino3 --verbose

# FIN