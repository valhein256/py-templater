""" UT for app/main """

import random
import heapq


def test_chk(test_app):
    response = test_app.get("/chk")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_api_v1_nlargest_missing_attritubes_num_list(test_app):
    request_json = {
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_missing_attritubes_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_missing_attritubes_all(test_app):
    request_json = {}
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_wrong_string_num_list(test_app):
    request_json = {
        "num_list": "sddag",
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_wrong_element_in_num_list(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30, "qwr"],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_negative_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": -1
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_characters_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": "1ga"
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_wrong_attritubes_num_list(test_app):
    request_json = {
        "num_list_": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_wrong_attritubes_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n_": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_int_string_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": "5"
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_int_string_in_num_list(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, "44", 15, 33, 10, 30, "40"],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_float_num_list(test_app):
    request_json = {
        "num_list": [10.1, 30.2, 20.3, 21.4, 11.5, 22.6, 33.7, 44.8, 15.9, 33.10, 10.11, 30.12],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_float_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30],
        "top_n": 5.1
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_float_string_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30],
        "top_n": "5.1"
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_with_float_string_in_num_list(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, "44.1", 15, 33, 10, 30, "40.2"],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 400


def test_api_v1_nlargest_basic(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": [44, 33, 33, 30, 30]}


def test_api_v1_nlargest_with_zero_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": 0
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": []}


def test_api_v1_nlargest_with_negative_zero_top_n(test_app):
    request_json = {
        "num_list": [10, 30, 20, 21, 11, 22, 33, 44, 15, 33, 10, 30,],
        "top_n": -0
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": []}


def test_api_v1_nlargest_with_normal_case_1(test_app):
    request_json = {
        "num_list": [100, 100, 100, 100, 4, 100, 100, 100, 100],
        "top_n": 5
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": [100, 100, 100, 100, 100]}


def test_api_v1_nlargest_with_normal_case_2(test_app):
    request_json = {
        "num_list": [100, 100, 100, 100, 999, 100, 100, 100, 100, 101],
        "top_n": 7
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": [999, 101, 100, 100, 100, 100, 100]}


def test_api_v1_nlargest_with_normal_case_3(test_app):
    request_json = {
        # random num list with positice int eero, 0, negative int
        "num_list": [-124, -42, 100, 999, 100, 100, 100, 100, 101, 0, -231, -112142, -41243, -42, -5014124],
        "top_n": 11
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": [999, 101, 100, 100, 100, 100, 100, 0, -42, -42, -124]}


def test_api_v1_nlargest_with_largest_top_n(test_app):
    request_json = {
        "num_list": [100, 100, 100, 100, 999, 100, 100, 100, 100, 101],
        "top_n": 100
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": [999, 101, 100, 100, 100, 100, 100, 100, 100, 100]}


def test_api_v1_nlargest_with_100_nums_in_num_list(test_app):
    test_100_nums = [random.randint(-10_000_000, 10_000_000) for _ in range(100)]
    test_top_n = random.randint(0, 99)
    expect = heapq.nlargest(test_top_n, test_100_nums)

    request_json = {
        "num_list": test_100_nums,
        "top_n": test_top_n
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": expect}


def test_api_v1_nlargest_with_1000_nums_in_num_list(test_app):
    test_1000_nums = [random.randint(-10_000_000, 10_000_000) for _ in range(1_000)]
    test_top_n = random.randint(0, 999)
    expect = heapq.nlargest(test_top_n, test_1000_nums)

    request_json = {
        "num_list": test_1000_nums,
        "top_n": test_top_n
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": expect}


def test_api_v1_nlargest_with_10000_nums_in_num_list(test_app):
    test_10000_nums = [random.randint(-10_000_000, 10_000_000) for _ in range(10_000)]
    test_top_n = random.randint(0, 9_999)
    expect = heapq.nlargest(test_top_n, test_10000_nums)

    request_json = {
        "num_list": test_10000_nums,
        "top_n": test_top_n
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": expect}


def test_api_v1_nlargest_with_100000_nums_in_num_list(test_app):
    test_100000_nums = [random.randint(-10_000_000, 10_000_000) for _ in range(100_000)]
    test_top_n = random.randint(0, 10_000)
    expect = heapq.nlargest(test_top_n, test_100000_nums)

    request_json = {
        "num_list": test_100000_nums,
        "top_n": test_top_n
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": expect}


def test_api_v1_nlargest_with_1000000_nums_in_num_list(test_app):
    test_1000000_nums = [random.randint(-10_000_000, 10_000_000) for _ in range(1_000_000)]
    test_top_n = random.randint(0, 10_000)
    expect = heapq.nlargest(test_top_n, test_1000000_nums)

    request_json = {
        "num_list": test_1000000_nums,
        "top_n": test_top_n
    }
    response = test_app.post("/api/v1/nlargest", json=request_json)
    assert response.status_code == 200
    assert response.json() == {"result": expect}
