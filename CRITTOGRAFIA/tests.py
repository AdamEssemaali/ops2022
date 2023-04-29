from functions import *
from rich.console import Console
import subprocess
import pytest

console = Console()

class TestChiper:
    def test_splitter(self):
        assert split_vocabulary() != None
    def test_encrypt(self):
        assert encrypt("ciao", 3) == "fldr"
    def test_decrypt(self):
        assert decrypt("fldr", 3) == "ciao"
    def test_adjust_key(self):
        assert adjust_key(27) == 1
    def test_find_in_dict(self):
        assert find_in_dict("ciao", split_vocabulary()) == "c"
    def test_reconstruct_vocabulary_from_cifrated(self):
        assert reconstruct_vocabulary_from_cifrated([("ciao", "ciao")]) == {"c": ["ciao"]}
    def test_deduct(self):
        assert deduct([("ciao", "ciao")], "ciao") == 0
    def test_brute(self):
        assert brute("ciao") == 0
    def brute_direct_test(self):
        for i in range(1, 27):
            print(brute(encrypt("ciao", i)))
            assert brute(encrypt("ciao", i)) == i


if __name__ == "__main__":
    tester = TestChiper()
    console.print("Test started")
    tester.brute_direct_test()

    console.print("Test ended")