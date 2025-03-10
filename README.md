# 🚀 Simple Prometheus Metrics Demo App 📊

## What does this demo app do? 🤔

This is a simple PoC application that demonstrates how to implement Prometheus metrics in a Python application. It creates two metrics:

- 🔢 **Counter**: Tracks the number of requests processed
- ⏱️ **Histogram**: Measures the processing time of each request

The app simulates processing requests and exposes these metrics for Prometheus to scrape.

## Requirements 📋

- 🐍 Python 3.6+
- 📦 prometheus_client==0.21.1

## Installation 💻

1. Clone this repository:

```bash
git clone https://github.com/sfc-gh-svishnu/simple-python-prometheus-app.git
cd simple-python-prometheus-app
```

2. Create a virtual environment:

```bash
python -m venv prometheus_app_env
source prometheus_app_env/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the App 🏃‍♂️

```bash
python simple_metrics_app.py
```

You'll see output like this:

```
Metrics server started on port 11501
Simple app with Prometheus metrics running
Visit http://localhost:11501/metrics to see metrics
Request processed in 0.32 seconds
Total requests: 1
Request processed in 0.17 seconds
Total requests: 2
...
```

## Viewing Metrics 👀

Open your browser or use curl to view the metrics:

```bash
curl http://localhost:11501/metrics
```

Sample output:

```shell
❯ curl http://localhost:11501/metrics
# HELP simple_app_request_count_total Number of requests received by the application
# TYPE simple_app_request_count_total counter
simple_app_request_count_total 32.0
# HELP simple_app_request_duration_seconds Time spent processing requests
# TYPE simple_app_request_duration_seconds histogram
simple_app_request_duration_seconds_bucket{le="0.005"} 0.0
simple_app_request_duration_seconds_bucket{le="0.01"} 0.0
simple_app_request_duration_seconds_bucket{le="0.025"} 0.0
simple_app_request_duration_seconds_bucket{le="0.05"} 0.0
simple_app_request_duration_seconds_bucket{le="0.075"} 0.0
simple_app_request_duration_seconds_bucket{le="0.1"} 0.0
simple_app_request_duration_seconds_bucket{le="0.25"} 15.0
simple_app_request_duration_seconds_bucket{le="0.5"} 31.0
simple_app_request_duration_seconds_bucket{le="0.75"} 32.0
simple_app_request_duration_seconds_bucket{le="1.0"} 32.0
simple_app_request_duration_seconds_bucket{le="2.5"} 32.0
simple_app_request_duration_seconds_bucket{le="5.0"} 32.0
simple_app_request_duration_seconds_bucket{le="7.5"} 32.0
simple_app_request_duration_seconds_bucket{le="10.0"} 32.0
simple_app_request_duration_seconds_bucket{le="+Inf"} 32.0
simple_app_request_duration_seconds_count 32.0
simple_app_request_duration_seconds_sum 9.58327141427435
```

## How It Works 🧠

1. 🏗️ Creates a custom registry and defines metrics using an Enum
2. 🚦 Starts an HTTP server on port 11501 to expose metrics
3. 🔄 Simulates processing requests in a loop
4. 📝 Records request count and duration as metrics
5. 🌐 Exposes metrics at the `/metrics` endpoint
