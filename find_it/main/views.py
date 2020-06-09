
from . import main
from ..utils.helpers import Helpers


@main.route('/', methods=['GET'])
def index():
    return Helpers.format_response(200)
