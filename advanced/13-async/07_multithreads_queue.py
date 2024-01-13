import threading
import requests
from queue import Queue

def fetch_url(url,q):
    response = requests.get(url)
    q.put(f"URL: {url}, Status Code: {response.status_code}, Length: {len(response.text)}")
    #print(f"URL: {url}, Status Code: {response.status_code}, Length: {len(response.text)}")

def main():
    urls = ["https://www.example.com", "https://www.google.com", "https://www.python.org"]

    threads = []
    queue = Queue()

    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = []

    while not queue.empty():
        results.append(queue.get())

    for result in results:
        print(result)


if __name__ == "__main__":
    main()