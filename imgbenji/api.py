import logging

import responder

from .handlers import upload_handler, read_handler


logger = logging.getLogger(__name__)


def make_api():
    api = responder.API(
        title='Image uploader',
    )

    api.add_route("/", static=True)

    @api.route('/api/files')
    async def upload(req, resp):
        await upload_handler(req, resp)

    @api.route('/i/{file_id}')
    async def read(req, resp, *, file_id):
        await read_handler(req, resp, file_id)
    return api
