import unittest

from code import Code
from parser import Parser, C_INSTR

test_file_path_add = "../../tests/Add.asm"
test_file_path_max = "../../tests/Max.asm"

class TestCode(unittest.TestCase):
      def __init__(self, methodName: str = "runTest") -> None:
         super().__init__(methodName)
         self.parser_add = Parser(test_file_path_add)
         self.parser_max = Parser(test_file_path_max)
         self.code = Code()

      def test_destination(self):
         destinations = [
            "010",
            "010",
            "000",
            "010",
            "000",
            "010",
            "001",
            "000",
         ]
         i = 0
         for _ in self.parser_max.lines:
            if self.parser_max.command_type == C_INSTR:
               self.assertEqual(self.code.get_destination_code(self.parser_max.destination), destinations[i])
               i+=1


      def test_jump(self):
         jumps = [
            "000",
            "000",
            "001",
            "000",
            "111",
            "000",
            "000",
            "111",
         ]
         i = 0
         for _ in self.parser_max.lines:
            if self.parser_max.command_type == C_INSTR:
               self.assertEqual(self.code.get_jump_code(self.parser_max.jump), jumps[i])
               i+=1

