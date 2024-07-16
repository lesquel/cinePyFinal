from concurrent.futures import ThreadPoolExecutor
def ModelRequest(func, *args):
    with ThreadPoolExecutor() as executor:
        return executor.submit(func, *args).result()