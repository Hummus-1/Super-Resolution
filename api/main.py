"""REST API module.

Implements a RESTful API server which exposes several endpoints that
handle client requests and perform image enhancement operations.
"""

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image

from .models import super_resolution


API_VERSION = "0.2.0"
TITLE = "Super-Resolution API"
DESCRIPTION = """
**Super-Resolution API** allows you to enhance the quality of your images.

## Features

You can improve on several parameters:

- **Resolution**: (*not yet implemented*).
- **Light**: (*not yet implemented*).

Feel free to explore the interactive examples provided below.
"""

app = FastAPI(title=TITLE, description=DESCRIPTION, version=API_VERSION)


@app.get("/")
def root():
    return {"health_check": "OK", "version": API_VERSION}


@app.post("/enhance/resolution")
def enhance_resolution(image: UploadFile):
    low_image = Image.open(image.file)
    high_image = super_resolution.enhance(low_image)

    stream = BytesIO()
    high_image.save(stream, "JPEG")
    stream.seek(0)
    return StreamingResponse(stream, media_type="image/jpeg")
