"""the main code for Img Benji"""
import logging
import os
import string
import random

import aiofiles

DATA_DIRECTORY = os.getenv('DATA_DIRECTORY')
logger = logging.getLogger(__name__)


def _get_filepath(file_id):
    filepath = f'{DATA_DIRECTORY}/{file_id}.png'
    return filepath


async def _ensure_data_directory():
    """make sure the data directory works"""
    if not DATA_DIRECTORY:
        raise ValueError('DATA_DIRECTORY environment variable is not set')
    try:
        async with aiofiles.open(f'{DATA_DIRECTORY}/_scratch.txt', 'w') as f:
            await f.write('delete me')
    except FileNotFoundError:
        # we need to create #DATA_DIRECTORY
        logger.info('creating directory %s...', DATA_DIRECTORY)
        os.makedirs(DATA_DIRECTORY)


def _create_new_id():
    while True:
        file_id = ''.join([random.choice(string.ascii_letters) for _ in range(7)])
        filepath = f'{DATA_DIRECTORY}/{file_id}'
        try:
            os.stat(filepath)
        except FileNotFoundError:
            logger.debug('found a valid id')
            break
    return file_id


async def upload(req):
    await _ensure_data_directory()
    file_id = _create_new_id()
    logger.info('file_id = %s', file_id)
    filepath = _get_filepath(file_id)
    logger.info('creating %s...', filepath)
    async with aiofiles.open(filepath, 'wb') as f:
        file_contents = await req.content
        await f.write(file_contents)
    return file_id


async def read(file_id) -> bytes:
    filepath = _get_filepath(file_id)
    async with aiofiles.open(filepath) as f:
        file_contents = await f.read()
        return file_contents
