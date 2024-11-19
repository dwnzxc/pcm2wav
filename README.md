# PCMtoWAV: Convert Raw PCM Data to Standard WAV Files

PCMtoWAV is a simple tool designed to convert raw PCM (Pulse Code Modulation) audio data stored in a text file into a playable WAV (Waveform Audio) file.

### Features
- Reads audio data and metadata from a text file.
- Supports 8-bit and 16-bit PCM audio formats.
- Automatically extracts key WAV file attributes:
  - Number of channels
  - Sample rate
  - Bit depth
- Creates a standard WAV file compatible with most media players and audio software.
- Easy-to-use Python implementation with detailed logs.

### How It Works
1. Provide a text file (`data.txt`) containing:
   - A 44-integer WAV header.
   - Raw PCM audio data.
2. Run the script to generate an output WAV file (`output.wav`).
3. Play your audio in any WAV-compatible player or tool.
