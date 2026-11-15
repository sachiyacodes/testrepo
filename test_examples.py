from pathlib import Path
import subprocess
import sys
import unittest


class ExampleTests(unittest.TestCase):
    def test_expected_outputs(self):
        for name, expected in [("firstpython.py", ["New python file"]),
                               ("abc.py", ["pass", "fail", "fail"])]:
            with self.subTest(name=name):
                result = subprocess.run([sys.executable, str(Path(__file__).with_name(name))],
                                        text=True, capture_output=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.splitlines(), expected)


if __name__ == "__main__":
    unittest.main()
