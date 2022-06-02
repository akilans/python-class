import concurrent.futures
import time
from itertools import repeat
import requests

image_urls = [
    "https://images.pexels.com/photos/15286/pexels-photo.jpg",
    "https://images.pexels.com/photos/1761279/pexels-photo-1761279.jpeg",
    "https://images.pexels.com/photos/1402850/pexels-photo-1402850.jpeg",
    "https://images.pexels.com/photos/1671325/pexels-photo-1671325.jpeg",
    "https://images.pexels.com/photos/3225529/pexels-photo-3225529.jpeg",
    "https://images.pexels.com/photos/4534200/pexels-photo-4534200.jpeg",
    "https://images.pexels.com/photos/4064432/pexels-photo-4064432.jpeg",
    "https://images.pexels.com/photos/5187131/pexels-photo-5187131.jpeg",
    "https://images.pexels.com/photos/4215113/pexels-photo-4215113.jpeg"
]


def download_image(url, image_path):

    image_name = url.split("/")[5]
    image_bytes = requests.get(url).content
    print(f"Started downloading {image_name}")

    with open(image_path+image_name, "wb") as image_file:
        image_file.write(image_bytes)

    print(f"Downloaded {image_name}")


# normal way to download images
before = time.perf_counter()
for url in image_urls:
    continue
    #download_image(url, "./normal-images/")
after = time.perf_counter()
print(f"Normal synchronus way took {round(after - before,2)} seconds")


# efficient way to download images using threadpools
before = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, image_urls, repeat("./thread-images/"))

    '''
    # This also works
        results = [executor.submit(
        download_image, url, "./thread-images/") for url in image_urls]
    for f in concurrent.futures.as_completed(results):
        f.result()
    '''


after = time.perf_counter()
print(f"Normal synchronus way took {round(after - before,2)} seconds")
