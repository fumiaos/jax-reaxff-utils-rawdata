import argparse
from pathlib import Path
from format_bracket import *
from format_th import convert_text
from togeo import convert_to_pdb
from totrain import to_train

def main():
    parser = argparse.ArgumentParser(description="JAX-REAXFF format converter")
    parser.add_argument("--input", "-i", required=True, help="input .xyz file")
    parser.add_argument("--output", "-o", required=True,
                        help="output prefix (will create <prefix>.geo and <prefix>.train.in)")
    args = parser.parse_args()

    in_file = Path(args.input)
    out_prefix = Path(args.output).with_suffix("")

    # read
    data = in_file.read_text(encoding="utf-8")
    data_lines = data.strip().split("\n")

    # process
    processed_lines = add_empty_line(data_lines)
    num = int(get_num(data_lines))
    processed_data = "\n".join(processed_lines)

    output_text = convert_text(processed_data)
    pdb_output = convert_to_pdb(output_text)
    train_output = to_train(output_text, num)

    # write
    (out_prefix.with_suffix(".geo")).write_text(pdb_output, encoding="utf-8")
    (out_prefix.with_suffix(".train.in")).write_text(train_output, encoding="utf-8")

    print("done：")
    print(f"  geo_file -> {out_prefix}.geo")
    print(f"  training_file -> {out_prefix}.train.in")

if __name__ == "__main__":
    main()

