import os
import argparse
import ffmpeg

def slice_audio(input_file: str, output_folder: str, L: int, D: int) -> None:
    os.makedirs(output_folder, exist_ok=True)

    for i in range(D):
        start_sample = round(i * L / D)
        end_sample = round((i + 1) * L / D)
        out_filename = os.path.join(output_folder, f"part_{i}.wav")

        (ffmpeg
        .input(filename=input_file)
        .atrim(start_sample=start_sample, end_sample=end_sample)
        .output(filename=out_filename)
        .run(overwrite_output=True))

        print(f"segment {i}: samples {start_sample} to {end_sample} extracted to {out_filename}")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="path to the input audio file")
    parser.add_argument("output_folder", type=str, help="folder to store the output segments")
    parser.add_argument("L", type=int, help="total length of the audio in samples")
    parser.add_argument("D", type=int, help="number of segments to split into")
    args = parser.parse_args()

    slice_audio(args.input_file, args.output_folder, args.L, args.D)

if __name__ == "__main__":
    main()
