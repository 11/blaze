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


def read_settings():
    project_dir = find_project_dir()
    settings_file = project_dir / Path('blaze.json')
    if settings_file.exists():
        try:
            settings = json \
                .loads(settings_file) \
                .decode('utf-8')

            return settings
        except json.JSONDecodeError:
            sys.exit('Error while decoding `blaze.json`')

    sys.exit('Could not find blaze.json file. Try running `blaze init`')

def find_project_root():
    for folder in Path.cwd().parents:
        settings_file = folder / Path('blaze.json')
        if settings_file.exists():
            return folder

            
def fill_dir(parent, file_descriptors):
    for fd in file_descriptors:
        descriptor = parent / Path(fd)
        if descriptor.exists() == False:
            if fd[-1] == '/':
                descriptor.mkdir()
            else:
                descriptor.touch()
