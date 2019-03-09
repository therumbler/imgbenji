"""a bunch of responder handlers"""
import logging

from responder import Request, Response

from .imgbenji import upload

logger = logging.getLogger(__name__)


async def upload_handler(req: Request, resp: Response) -> None:
    """let's upload a file"""
    id_ = await upload(req)

    resp.media = {
        'data': {
            'id': id_,
        }
    }


async def read_handler(req: Request, resp: Request, file_id) -> None:
    """let's fetch a file"""
    logger.debug('in read handler for file_id %s', file_id)
    resp.text = f'''<html>
    <h1>hi {file_id}</h1>
    <img src="/static/images/{file_id}.png" alt="{file_id}" />
    </html>
    '''.strip()
