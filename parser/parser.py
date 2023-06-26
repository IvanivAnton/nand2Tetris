import os
import re

A_INSTR = 0
C_INSTR = 1
L_INSTR = 2

class Parser:
    def __init__(self, input_file_path: os.PathLike) -> None:
        try:
            self.input_file_path = input_file_path
            self.pattern_whitespaces = re.compile(r"\s+")
            self.pattern_comments = re.compile(r"\/\/.+$")
            self.pattern_a_instruction = re.compile(r"@(?:[A-z\.$:]+|\d+)")
            self.pattern_l_instruction = re.compile(r"\([A-z\.$:\d]+\)")
            self.pattern_c_instruction = re.compile(r"^(?:(A?M?D?)=)?([DAM][\-+|&](?:[DAM]|\-?1)|[!-]?[DAM]|0|-?1)(?:;(J(?:GT|EQ|GE|LT|NE|LE|MP)))?")
        except Exception as e:
            print(str(e))
            return

        self.__line__ = None
        self.command_type = -1

    @property
    def lines(self):
        return self.__iter__()

    def __command_type__(self) -> int:
        if re.match(self.pattern_a_instruction, self.__line__):
            return A_INSTR
        elif re.match(self.pattern_c_instruction, self.__line__):
            return C_INSTR
        elif re.match(self.pattern_l_instruction, self.__line__):
            return L_INSTR
        else:
            raise ValueError(f"Unknown instruction \"{self.__line__}\"")

    @property
    def symbol(self) -> str:
        if self.command_type == A_INSTR:
            return self.__line__.replace("@", "")
        elif self.command_type == L_INSTR:
            return self.__line__.replace("(", "").replace(")", "")

        raise ValueError(f"command_type \"{self.command_type}\" is incorrect")

    @property
    def destination(self) -> str:
        if self.command_type == C_INSTR:
            return re.search(self.pattern_c_instruction, self.__line__).group(1)

        raise ValueError(f"command_type \"{self.command_type}\" is incorrect")

    @property
    def compute(self) -> str:
        if self.command_type == C_INSTR:
            return re.search(self.pattern_c_instruction, self.__line__).group(2)

        raise ValueError(f"command_type \"{self.command_type}\" is incorrect")

    @property
    def jump(self) -> str:
        if self.command_type == C_INSTR:
            return re.search(self.pattern_c_instruction, self.__line__).group(3)

        raise ValueError(f"command_type \"{self.command_type}\" is incorrect")

    def __iter__(self):
        with open(self.input_file_path) as file:
            for line in file:
                if line[0:2] == "//":
                    continue

                line = re.sub(self.pattern_whitespaces, "", line)
                if len(line) == 0:
                    continue

                line = re.sub(self.pattern_comments, "", line)
                if len(line) == 0:
                    continue

                self.__line__ = line
                self.command_type = self.__command_type__()
                yield line
