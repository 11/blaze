import sys
import json
import httpx
import asyncio
from pathlib import Path


def batch_download(urls):
    async def fetch(url):
        async with httpx.AsyncClient() as client:
            return await client.get(url) 

    async def download():
        return await asyncio.gather(*[fetch(url=url) for url in urls]) 

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(download())
    loop.close() 

    return results


def find_project_root():
    parent_dirs = list(Path.cwd().parents)
    parent_dirs.insert(0, Path.cwd()) 
    for folder in parent_dirs:
        settings_file = folder / Path('blaze.json')
        if settings_file.exists():
            return folder

    sys.exit('Could not find root project. Try placing a `blaze.json` file in the root of your project.')

            
def fill_dir(parent, file_descriptors):
    for fd in file_descriptors:
        descriptor = parent / Path(fd)
        if descriptor.exists() == False:
            if fd[-1] == '/':
                descriptor.mkdir()
            else:
                descriptor.touch()
