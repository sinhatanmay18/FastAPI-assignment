from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from middleware import log_requests_middleware
from database import engine, Base
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.middleware("http")(log_requests_middleware)


class MatrixInput(BaseModel):
    matrix: List[List[int]]


@app.post("/input-rectangle")
def largest_rectangle(matrix_request: MatrixInput) -> tuple:
    matrix = matrix_request.matrix
    return find_largest_rectange(matrix)


def find_largest_rectange(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        return 0, None

    rows, cols = len(matrix), len(matrix[0])

    max_area = 0
    max_number = None
    current_area = 0

    height = [[0] * cols for _ in range(rows)]
    left = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -9:
                continue

            if i == 0:
                height[i][j] = 1
            else:
                height[i][j] = height[i - 1][j] + 1 if matrix[i][j] == matrix[i - 1][j] else 1

            left[i][j] = j if j == 0 or matrix[i][j] != matrix[i][j - 1] else left[i][j - 1]

            for k in range(j, left[i][j] - 1, -1):
                current_width = j - k + 1
                current_height = min(height[i][k:j + 1])
                if current_width != current_height:
                    current_area = current_width * current_height

                if current_area > max_area:
                    max_area = current_area
                    max_number = matrix[i][j]
    if max_area == 0:
        return -1, -1

    return max_number, max_area
