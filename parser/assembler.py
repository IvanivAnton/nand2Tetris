import os
from symbol_table import SymbolTable
from parser import Parser, A_INSTR, L_INSTR, C_INSTR
from code import Code

class Assembler:
    def __init__(self) -> None:
        symbol_table = SymbolTable()
        self.code = Code()

        # predefined symbols
        symbol_table.add("SP", 0)
        symbol_table.add("LCL", 1)
        symbol_table.add("ARG", 2)
        symbol_table.add("THIS", 3)
        symbol_table.add("THAT", 4)

        self.__variables_start_address__ = 16
        for i in range(0, self.__variables_start_address__):
            symbol_table.add(f"R{i}", i)

        symbol_table.add("SCREEN", 16384)
        symbol_table.add("KBD", 24576)
        self.__symbol_table__ = symbol_table

    def assemble(self, input_file_path: os.PathLike) -> None:
        self.__parser__ = Parser(input_file_path)
        output_file_path = str(input_file_path).replace(".asm", ".hack")

        with open(output_file_path, 'w') as output_file:
            self.__add_labels_to_symbol_table__()
            self.__add_variables_and_generate_code__(output_file)

    def __add_labels_to_symbol_table__(self) -> None:
        label_address = 0
        for _ in self.__parser__.lines:
            if self.__parser__.command_type == L_INSTR:
                self.__symbol_table__.add(self.__parser__.symbol, label_address)
            else:
                label_address += 1

    @staticmethod
    def __format_to_16_bit__(number: str) -> str:
        return "{0:016b}".format(int(number))

    def __add_variables_and_generate_code__(self, output_file) -> None:
        variable_address = self.__variables_start_address__
        for _ in self.__parser__.lines:
            command_type = self.__parser__.command_type
            if command_type == A_INSTR:
                symbol = self.__parser__.symbol
                if not symbol.isnumeric():
                    if not self.__symbol_table__.contains(symbol):
                        self.__symbol_table__.add(symbol, variable_address)
                        address = Assembler.__format_to_16_bit__(variable_address)
                        variable_address += 1
                    else:
                        address = Assembler.__format_to_16_bit__(self.__symbol_table__.get(symbol))
                else:
                    address = Assembler.__format_to_16_bit__(symbol)

                instruction_binary = address
            elif command_type == L_INSTR:
                continue
            elif command_type == C_INSTR:
                comp = self.__parser__.compute
                dest = self.__parser__.destination
                jump = self.__parser__.jump

                instruction_binary = f"111" + \
                    self.code.get_comp_code(comp) + \
                    self.code.get_destination_code(dest) + \
                    self.code.get_jump_code(jump)

            output_file.write(instruction_binary + "\n")




