import numpy as np
import wave
import struct

def convert_to_wav(output_filename='output.wav'):
    with open('data.txt', 'r') as file:
        data = [int(num.strip()) for num in file.read().split(',')]
    header_data = data[:44] 
    num_channels = struct.unpack('<H', bytes(header_data[22:24]))[0]
    sample_rate = struct.unpack('<I', bytes(header_data[24:28]))[0]
    bits_per_sample = struct.unpack('<H', bytes(header_data[34:36]))[0]
    audio_data = data[44:]
    if bits_per_sample == 16:
        audio_array = np.array(audio_data, dtype=np.int16)
    elif bits_per_sample == 8:
        audio_array = np.array(audio_data, dtype=np.uint8)
    else:
        raise ValueError(f"Unsupported bit depth: {bits_per_sample}")
    with wave.open(output_filename, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(bits_per_sample // 8)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_array.tobytes())
    
    print(f"WAV file created with:")
    print(f"Channels: {num_channels}")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Bit Depth: {bits_per_sample} bits")

convert_to_wav()