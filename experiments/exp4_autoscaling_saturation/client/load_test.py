import asyncio
import aiohttp
import time
import json
from statistics import mean, quantiles


URL = ""


CONCURRENCY_LEVELS = [10, 25, 50, 100, 200]
REQUESTS_PER_LEVEL = [200, 300, 500, 800, 1000]
TIMEOUT = 5

OUTPUT_FILE = "experiments/exp4_autoscaling_saturation/results/results.json"


##########################################################################
async def fetch(session, url):
    start = time.time()
    try:
        async with session.get(url, timeout=TIMEOUT) as response:
            latency = time.time() - start
            if response.status != 200:
                return latency, True
            return latency, False
    except:
        latency = time.time() - start
        return latency, True


async def run_test(concurrency, total_requests):
    connector = aiohttp.TCPConnector(limit=concurrency)
    timeout = aiohttp.ClientTimeout(total=TIMEOUT)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = []
        start_time = time.time()

        for _ in range(total_requests):
            task = asyncio.create_task(fetch(session, URL))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        total_time = time.time() - start_time

    latencies = [r[0] for r in results]
    errors = sum(1 for r in results if r[1])

    avg_latency = mean(latencies)
    p95_latency = quantiles(latencies, n=100)[94] if len(latencies) >= 100 else max(latencies)
    throughput = total_requests / total_time

    return {
        "concurrency": concurrency,
        "requests": total_requests,
        "avg_latency": avg_latency,
        "p95_latency": p95_latency,
        "errors": errors,
        "error_rate": errors / total_requests,
        "throughput": throughput
    }

async def main():
    all_results = []

    for concurrency, requests in zip(CONCURRENCY_LEVELS, REQUESTS_PER_LEVEL):
        print(f"\nRunning test: concurrency={concurrency}, requests={requests}")

        result = await run_test(concurrency, requests)
        all_results.append(result)

        print(f"Avg latency: {result['avg_latency']:.3f}s")
        print(f"P95 latency: {result['p95_latency']:.3f}s")
        print(f"Errors: {result['errors']}")
        print(f"Throughput: {result['throughput']:.2f} req/s")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(all_results, f, indent=4)

    print("\nsuccess")


if __name__ == "__main__":
    asyncio.run(main())