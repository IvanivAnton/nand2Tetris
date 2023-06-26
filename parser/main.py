import sys
from assembler import Assembler

assembler = Assembler()

if __name__ == "__main__":
    input_file_path = sys.argv[1]

    assembler.assemble(input_file_path)