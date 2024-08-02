#!/bin/bash
set -eu

# Create out directory
mkdir -p bin

# Build
iverilog -o bin/uart uart.v uart_tb.v

# Simulate
vvp bin/uart

# Visualize
gtkwave bin/uart_tb.vcd