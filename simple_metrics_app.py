import enum
import random
import time

from prometheus_client import (
    CollectorRegistry,
    Counter,
    Histogram,
    disable_created_metrics,
    start_http_server,
)

# Define metrics port
METRICS_PORT = 11501

# Create registry
registry = CollectorRegistry()


# Prometheus metrics don't properly unregister, so we use a helper function to enforce consistent
# naming conventions rather than relying on Enum inheritance. This prevents duplicate metrics during
# hot reloads or testing while ensuring standardized metric names across the application.
def _prepend_metric_prefix(metric_name: str):
    return f"simple_app_{metric_name}"


class SimpleAppMetrics(enum.Enum):
    # Define two metrics: one counter and one histogram
    REQUEST_COUNT = Counter(
        _prepend_metric_prefix("request_count"),
        "Number of requests received by the application",
        registry=registry,
    )

    REQUEST_DURATION = Histogram(
        _prepend_metric_prefix("request_duration_seconds"),
        "Time spent processing requests",
        registry=registry,
    )


def initialize_metrics_server():
    # Disable the automatic _created metrics (timestamp) to reduce clutter in metrics output
    disable_created_metrics()

    # Start the HTTP server to expose metrics
    start_http_server(METRICS_PORT, registry=registry)
    print(f"Metrics server started on port {METRICS_PORT}")


def simulate_request():
    """Simulate a request and record metrics."""
    # Increment the request counter
    SimpleAppMetrics.REQUEST_COUNT.value.inc()

    # Record the duration using a context manager
    with SimpleAppMetrics.REQUEST_DURATION.value.time():
        # Simulate request processing time
        process_time = random.uniform(0.1, 0.5)
        time.sleep(process_time)

    print(f"Request processed in {process_time:.2f} seconds")


def main():
    # Start the metrics server
    initialize_metrics_server()

    print("Simple app with Prometheus metrics running")
    print(f"Visit http://localhost:{METRICS_PORT}/metrics to see metrics")

    try:
        # Main loop
        request_count = 0
        while True:
            # Simulate requests periodically
            simulate_request()
            request_count += 1
            print(f"Total requests: {request_count}")

            # Wait between requests
            time.sleep(2)
    except KeyboardInterrupt:
        print("Application stopped")


if __name__ == "__main__":
    main()
