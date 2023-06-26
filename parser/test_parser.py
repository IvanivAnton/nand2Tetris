
import unittest

from parser import Parser, A_INSTR, L_INSTR, C_INSTR

test_file_path_add = "../../tests/Add.asm"
test_file_path_max = "../../tests/Max.asm"

class TestParser(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.parser_add = Parser(test_file_path_add)
        self.parser_max = Parser(test_file_path_max)

    def test_init(self):
        self.assertEqual(self.parser_add.__line__, None)
        self.assertEqual(self.parser_add.command_type, -1)

    def test_iter(self):
        i = 0
        lines: list = [
            "@2",
            "D=A",
            "@3",
            "D=D+A",
            "@0",
            "M=D",
        ]
        for line in self.parser_add.lines:
            self.assertEqual(line, lines[i])
            i +=1

    def test_command_type(self):
        i = 0
        types = [
            A_INSTR,
            C_INSTR,
            A_INSTR,
            C_INSTR,
            A_INSTR,
            C_INSTR,
        ]
        for _ in self.parser_add.lines:
            self.assertEqual(self.parser_add.command_type, types[i])
            i += 1

    def test_symbol(self):
        i = 0
        symbols = [
            "R0",
            "R1",
            "OUTPUT_FIRST",
            "R1",
            "OUTPUT_D",
            "OUTPUT_FIRST",
            "R0",
            "OUTPUT_D",
            "R2",
            "INFINITE_LOOP",
            "INFINITE_LOOP",
        ]
        for _ in self.parser_max.lines:
            if self.parser_max.command_type in [A_INSTR, L_INSTR]:
                self.assertEqual(self.parser_max.symbol, symbols[i])
                i+=1
            else:
                with self.assertRaises(ValueError):
                    self.parser_max.symbol

    def test_compute(self):
        i = 0
        destinations = [
            "D",
            "D",
            "M",
        ]
        for _ in self.parser_add.lines:
            if self.parser_add.command_type == C_INSTR:
                self.assertEqual(self.parser_add.destination, destinations[i])
                i+=1
            else:
                with self.assertRaises(ValueError):
                    self.parser_max.destination

    def test_destination(self):
        i = 0
        destinations = [
            "D",
            "D",
            "M",
        ]
        for _ in self.parser_add.lines:
            if self.parser_add.command_type == C_INSTR:
                self.assertEqual(self.parser_add.destination, destinations[i])
                i+=1
            else:
                with self.assertRaises(ValueError):
                    self.parser_max.destination

    def test_compute(self):
        i = 0
        computes = [
            "A",
            "D+A",
            "D",
        ]
        for _ in self.parser_add.lines:
            if self.parser_add.command_type == C_INSTR:
                self.assertEqual(self.parser_add.compute, computes[i])
                i+=1
            else:
                with self.assertRaises(ValueError):
                    self.parser_add.compute

    def test_jump(self):
        i = 0
        jumps = [
            None,
            None,
            "JGT",
            None,
            "JMP",
            None,
            None,
            "JMP"
        ]
        for _ in self.parser_max.lines:
            if self.parser_max.command_type == C_INSTR:
                self.assertEqual(self.parser_max.jump, jumps[i])
                i+=1
            else:
                with self.assertRaises(ValueError):
                    self.parser_max.compute

if __name__ == "__main__":
    unittest.main()
