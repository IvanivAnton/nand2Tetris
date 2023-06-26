import unittest

from assembler import Assembler

class TestCode(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_files_files = [
            ["Add.asm", "AddResult.hack"],
            ["Max.asm", "MaxResult.hack"],
            ["MaxL.asm", "MaxLResult.hack"],
            ["Rect.asm", "RectResult.hack"],
            ["RectL.asm", "RectLResult.hack"],
            ["RectL.asm", "RectLResult.hack"],
            ["Pong.asm", "PongResult.hack"],
        ]
        self.dir_path = "/home/ivanivanton/Documents/nand2tetris/projects/06/tests/"
        self.assembler = Assembler()

    def test(self):
        for file, result_file in self.test_files_files:
            file_path = f"{self.dir_path}{file}"
            compare_path = f"{self.dir_path}{result_file}"

            self.assembler.assemble(file_path)
            output_file_path = file_path.replace('asm', 'hack')
            with open(output_file_path) as output_file, open(compare_path) as compare_file:
                for line1, line2 in zip(output_file, compare_file):
                    self.assertEqual(line1, line2)

