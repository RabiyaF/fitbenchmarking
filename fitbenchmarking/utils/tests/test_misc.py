"""
Tests for misc.py
"""

import inspect
import os
import shutil
import time
import unittest

from fitbenchmarking import test_files
from fitbenchmarking.utils.misc import get_css, get_js, get_problem_files
from fitbenchmarking.utils.options import Options


class CreateDirsTests(unittest.TestCase):
    """
    Tests for the file and directory setting in misc.py
    """

    def setUp(self):
        """
        Create some datafiles to look for.
        """
        base_path = os.path.dirname(inspect.getfile(test_files))
        self.dirname = os.path.join(base_path, f"mock_datasets_{time.time()}")
        os.mkdir(self.dirname)

        expected = []
        for i in range(10):
            filename = f"file_{i}.txt"
            filepath = os.path.join(self.dirname, filename)
            expected.append(filepath)

            with open(filepath, "w+", encoding="utf-8") as f:
                f.write(
                    "This is a mock data file to check "
                    "that finding files is correct"
                )

        self.expected = sorted(expected)

    def tearDown(self):
        """
        Clean up created datafiles.
        """
        shutil.rmtree(self.dirname)

    def test_getProblemFiles_get_correct_probs(self):
        """
        Test that the correct files are found
        """

        problems = get_problem_files(self.dirname)

        self.assertIsInstance(problems, list)
        self.assertEqual(self.expected, sorted(problems))

    def test_get_css(self):
        """
        Test that the right css files are returned
        """
        options = Options()
        print(options.results_dir)
        test_dir = os.path.join(options.results_dir, "foo")

        expected_css_dir = os.path.join("..", "css")
        expected_main_css = os.path.join(expected_css_dir, "main_style.css")
        expected_table_css = os.path.join(expected_css_dir, "table_style.css")
        expected_custom_css = os.path.join(
            expected_css_dir, "custom_style.css"
        )
        css = get_css(options, test_dir)

        self.assertEqual(css["main"], expected_main_css)
        self.assertEqual(css["table"], expected_table_css)
        self.assertEqual(css["custom"], expected_custom_css)

    def test_get_js(self):
        """
        Test that the right js files are returned
        """
        options = Options()
        print(options.results_dir)
        test_dir = os.path.join(options.results_dir, "foo")

        expected_js_dir = os.path.join("..", "js")
        expected_mathjax_js = os.path.join(expected_js_dir, "tex-mml-chtml.js")
        js = get_js(options, test_dir)

        self.assertEqual(js["mathjax"], expected_mathjax_js)


if __name__ == "__main__":
    unittest.main()
