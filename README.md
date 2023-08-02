# Python Project Templater

## Descriptions

This project is a web service that provides an API to find the top N elements in a list without sorting the list.
It has been developed using the Python web framework [Fastapi.](https://fastapi.tiangolo.com/lo/)

### APIs

The web service offers two APIs.

| API | Method | Path | Descriptions |
| --- | --- | --- | --- |
| Health Check | GET | /health | This is a health check endpoint that can be used to verify the status and availability of the service. |
| Top N Elements Search | POST | /api/v1/nlargest | It requires two inputs: a list of integers and a positive integer N. It returns a list that contains the top N elements, which refers to the N largest elements in the input list. |

### Request & Response

#### Health Check

| Request | Response |
| --- | --- |
| N/A | {"status": "ok"} |

#### Top N Elements Search

| Request | Response |
| --- | --- |
| {"num_list": [11, 2, 23, 44, 5], "top_n": 3} | {"result": [44, 23, 11]} |

### Http Status Code

#### Health Check

| Status Code | Descriptions |
| --- | --- |
| 200 | OK |

#### Top N Elements Search

| Status Code | Descriptions |
| --- | --- |
| 200 | OK |
| 400 | Bad Request |
| 500 | Internal Server Error |

Note: After running the service locally, you can browser `http://localhost:8000/docs` to see Swagger UI of this service for more details.

### Problem: How to find the top N elements in a list without sorting the list?

To solve this problem, I use the python standard library heapq to implement a min-heap.

The min-heap is a binary tree that satisfies the following properties:

- The root node is the smallest element in the tree.
- The left and right subtrees are also min-heaps.

The following steps outline the solution:

1. Check if the input list is empty or if the value of N is less than or equal to 0. If either of these conditions is true, return an empty list as the result. Otherwise, continue to the next step.
2. Create a list to serve as a min-heap, which will store the N largest numbers.
3. Iterate through the elements of the input list:
a. If the number of elements in the min-heap is less than N, push the current element directly into the list using heapq.heappush(). This action automatically adjusts the list as a min-heap.
b. Once the number of elements in the min-heap reaches N, follow these steps:
    - If the current element is greater than the root node of the min-heap:
        - Pop the root node of the min-heap, removing the smallest element.
        - Push the current element into the min-heap using heapq.heappush(). This maintains the min-heap property.
4. After iterating through all the elements in the input list, the min-heap will contain the top N elements.
5. Extract all elements from the min-heap by repeatedly using heapq.heappop(), and save them in a list. Then, reverse the list.
6. Finally, return the reversed list as the result.

### Complexity Analysis
- The time complexity of this algorithm is O(nlogk), n is the length of the input list: num_list, k is the value of top_n.
- The space complexity of this algorithm is O(k), k is the value of top_n.

In next section, I will show how to run this service locally.

## Build Service Locally

For your convenience, I have provided a set of Makefile commands that you can use during development. To view the available commands and their descriptions, you can run "make" or "make help" in your terminal. you can also open the Makefile to explore the details further.

    $ make
    or
    $ make help

The Makefile provides the following commands to help you to quick start the project setup and development, including:

Main:
- Build service docker images
- Run service locally via docker containers
- Run unit tests
	- pytest

Others:
- Run benchmark
	- locust
- Run Profiling
	- fastapi-profiler
	- memory-profiler
- Run pylint
	- pylint

### Build Development Docker Images

In this step, you can build Docker images for development purposes. The following command will build Docker images with the specified TARGET_TAGS:

    $ make devs

Then, run "docker images" to view the images you just built. Example:

    $ docker images
    REPOSITORY            TAG              IMAGE ID       CREATED          SIZE
    py-web-apps-develop   latest           f4648d1a7451   8 minutes ago    578MB
    py-web-apps-base      latest           d750fb61a723   26 minutes ago   559MB

By running this command, you initiate the build process for Docker images, specifically targeting the tags: `base` and `develop`.
- The `base` tag refer to the base image with essential dependencies.
- The `develop` tag include additional tools, 3rd-party python packages and configurations required for development.

#### Others

You can run the following command to start a container for development.

    # TARGET_TAG = base, develop
    $ make container-bash TARGET_TAG=base

In this project, I use poetry to manage python libs. You can use poetry commands to add/remove/update python libs in docker image with tag: `base`.
Following is a sample commands:

    $ make container-bash TARGET_TAG=base
    (container)$ pwd # Make sure you are in /opt/dev
    /opt/dev

    (container)$ cd src
    (container)$ poetry update
    (container)$ poetry add <package_name>
    (container)$ poetry remove <package_name>
    (container)$ poetry export -f requirements.txt --output requirements.txt
    (container)$ exit

### Deploy / Launch Service Locally

To launch this service locally, you can run the following make commands:

    # Launch a container for development
    $ make run-dev
    [+] Running 2/2
     ⠿ Network offsite-assignment-4hi4nbra_default      Created
     ⠿ Container py-web-apps-dev                        Started

After running the previously mentioned commands and successfully deploying the service locally, you can open a web browser and navigate to `http://localhost:8000/docs`. This URL will direct you to the Swagger UI of the service.

If you want to stop the service, you can run the following command:

    # Down the running container
    $ make down-dev
    [+] Running 1/1
     ⠿ Container py-web-apps-dev                        Stopped
     ⠿ Network offsite-assignment-4hi4nbra_default      Removed

## Release

In this project, I package the service into a Docker image with tag: `release`. You can run the following command to build the release image:

    $ make release

Then, run "docker images" to view the images you just built. Example:

    $ docker images
    REPOSITORY                        TAG              IMAGE ID       CREATED        SIZE
    py-web-apps-release               latest           19675cc37260   2 hours ago    588MB
    py-web-apps-develop               latest           30a4baa29311   3 hours ago    849MB
    py-web-apps-base                  latest           d46652737f47   2 hours ago    562MB

Once the release image is built, you can run the following command to start a container for the release service locally:

    $ make run
    [+] Running 2/2
    ⠿ Network offsite-assignment-4hi4nbra_default  Created
    ⠿ Container py-web-apps                        Started

Same as the development service, you can open a web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI of the service.

To stop the service, you can run the following command:

    $ make down
    [+] Running 2/2
    ⠿ Container py-web-apps                        Stopped
    ⠿ Network offsite-assignment-4hi4nbra_default  Removed

## Development

Once you have built the necessary Docker images for the project, you can run the following command to start a container specifically for:

### Testing

To run the unit tests in the project, you can run the following command:

    $ make test

### Linting

To check the code quality in the project using pylint, you can run the following command:

    $ make lint

### Benchmark

In this project, I use the Python library Locust to build the benchmark. You can initiate the benchmark by executing the following command:

    $ make benchmark

Once the benchmark is running, you can open a web browser and visit `http://localhost:8089/` to begin the benchmarking process.

I prepared a sample benchmark script in the project: `./scripts/benchmark/locustfile.py`. You can modify the script to customize the benchmarking process.

Following is a sample output:

    $ make benchmark
    [+] Running 1/1
     ⠿ Container py-web-apps-dev  Started
    [2023-05-24 16:42:32,790] 81b90d8147ff/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
    [2023-05-24 16:42:32,807] 81b90d8147ff/INFO/locust.main: Starting Locust 2.15.1
    [2023-05-24 16:42:49,186] 81b90d8147ff/INFO/locust.runners: Ramping to 10 users at a rate of 1.00 per second
    [2023-05-24 16:42:58,198] 81b90d8147ff/INFO/locust.runners: All users spawned: {"WebsiteUser": 10} (10 total users)
    KeyboardInterrupt
    2023-05-24T16:46:07Z
    [2023-05-24 16:46:07,011] 81b90d8147ff/INFO/locust.main: Shutting down (exit code 0)
    Type     Name                                       # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
    --------|-----------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
    POST     /api/v1/nlargest                              198     0(0.00%) |    271     121    3062    180 |    1.00        0.00
    --------|-----------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
             Aggregated                                    198     0(0.00%) |    271     121    3062    180 |    1.00        0.00

    Response time percentiles (approximated)
    Type     Name                                       50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
    --------|-------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    POST     /api/v1/nlargest                           180    200    220    260    340    510   2300   2500   3100   3100   3100    198
    --------|-------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
             Aggregated                                 180    200    220    260    340    510   2300   2500   3100   3100   3100    198

### Profiling

In this project, I use the Python library fastapi-profiler and memory-profiler to build the profiling.

#### FastAPI Profiler: For profiling the execution time of FastAPI

FastAPI offers a middleware that allows to configure and set up FastAPI-Profile. This middleware simplifies the integration of FastAPI-Profile into FastAPI application.
To profile the execution time of FastAPI, I have added a profile_enable flag to determine whether to run the code in profiling mode or not.
The profile_enable flag is set to "false" by default. If you want to enable the profiling mode, you can set the profile_enable flag to True in the `src/config/env` file.

If you want to deploy the service locally with profiling mode, you can following the steps below.
Note that the final profiling result will be saved in the ./outputs/profiles/profile.html file. If the outputs folder already exists in the project, please delete it first.

1. Modify the `profile_enable` flag to "true" in the `src/config/env` file. (You may need to rebuild the docker image if you have already built the image before)
2. Run makefile command: "make benchmark" to launch the service and start the benchmark. (If you want to modify the benchmark script, you can modify the script in the `./scripts/benchmark/locustfile.py` file.)
3. Go to `http://localhost:8089/` to start the benchmarking process.
4. Wait for a while to let the benchmark process run for some time.
5. Shutdown the service by running the makefile command: "make down-dev".
6. Then, you can find the profiling result in `./outputs/profiles/profile.html`, you can open the html file to check the profiling result.

#### Profiler: For profiling the memory usage and execution time of function

In order to profile the memory usage and execution time of function, I import the memory_profiler library in the project.
I prepare a sample script in the project: `./scripts/profiler/profiler.py`. You can modify the script to customize the profiling process.
To run the profiling script, you can run the following command:

    # Run the profiling script
    $ make profiling

    # Or, with arguments:
    $ make profiling LIST_SIZE=1000 TOP_N=10 ITERATION=1000

Sample output:

    ---------Memory Profiling---------
    Size of num_list: 10000
    Top n: 1000

    Test case: the size of num_list: 10000 and top_n: 1000
    Memory usage for sort
    Filename: /opt/dev/scripts/profile/profiler.py

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        20     22.4 MiB     22.4 MiB           1   @profile
        21                                         def _function(f, *args, **kwargs):
        22     22.4 MiB      0.0 MiB           1       return f(*args, **kwargs)


    Memory usage for heapq
    Filename: /opt/dev/scripts/profile/profiler.py

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        20     22.4 MiB     22.4 MiB           1   @profile
        21                                         def _function(f, *args, **kwargs):
        22     22.4 MiB      0.0 MiB           1       return f(*args, **kwargs)


    Memory usage for minheap
    Filename: /opt/dev/scripts/profile/profiler.py

    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        20     22.4 MiB     22.4 MiB           1   @profile
        21                                         def _function(f, *args, **kwargs):
        22     22.4 MiB      0.0 MiB           1       return f(*args, **kwargs)


    ----------------------------------

    ------Execute Time Profiling------
    Size of num_list: 10000
    Top n: 1000
    Iteration: 10

    Average times:
    Total average times for sort 0.3611016035079956
    Total average times for heapq 0.11291768550872802
    Total average times for minheap 0.17045238018035888
    ----------------------------------
