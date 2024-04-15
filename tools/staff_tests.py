import math

from framework import Test, TestSpec, Task, Matrix, randint
import filters


@Test()
def test_tiny(test: TestSpec):
    test.add_task(Task(Matrix.random(2, 2, min_value=1, max_value=10),
                  Matrix.random(2, 2, min_value=1, max_value=10)))
    test.add_task(Task(Matrix.random(4, 4, min_value=1, max_value=10),
                  Matrix.random(2, 2, min_value=1, max_value=10)))
    test.add_task(Task(Matrix.random(5, 3, min_value=1, max_value=10),
                  Matrix.random(4, 2, min_value=1, max_value=10)))
    test.add_task(Task(Matrix.random(5, 4, min_value=1, max_value=10),
                  Matrix.random(4, 3, min_value=1, max_value=10)))


@Test()
def test_small(test: TestSpec):
    for _ in range(10):
        rows_a = randint(15, 25)
        cols_a = randint(15, 25)
        rows_b = randint(5, 15)
        cols_b = randint(5, 15)
        test.add_task(
            Task(Matrix.random(rows_a, cols_a), Matrix.random(rows_b, cols_b))
        )


@Test()
def test_large(test: TestSpec):
    for _ in range(50):
        rows_a = randint(100, 100)
        cols_a = randint(100, 100)
        rows_b = randint(20, 40)
        cols_b = randint(20, 40)
        test.add_task(
            Task(Matrix.random(rows_a, cols_a, min_value=-(2 ** 30), max_value=2 ** 30),
                 Matrix.random(rows_b, cols_b, min_value=-(2 ** 30), max_value=2 ** 30))
        )


@Test()
def test_gif_kachow_blur(test: TestSpec):
    test.add_gif("/home/ff/cs61c/sp24/proj4/gifs/kachow.gif",
                 filters.BlurFilter.create(size=17, sigma=7))


@Test()
def test_gif_kachow_sharpen(test: TestSpec):
    test.add_gif("/home/ff/cs61c/sp24/proj4/gifs/kachow.gif",
                 filters.SharpenFilter.create(size=3, sigma=1))
