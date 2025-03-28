from fastapi import HTTPException, status, UploadFile
from typing import Optional
from PIL import Image

import xml.etree.ElementTree as ET

from app.core.config import settings


def validate_positive_int64(value: int) -> int:
    if value < 0 or value > 9223372036854775807:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Value must be a positive int64.',
        )

    return value


def validate_positive_int32(value: int) -> int:
    if value < 0 or value > 2147483647:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Value must be a positive int32.',
        )

    return value


def validate_positive_smallint(value: int) -> int:
    if value < 0 or value > 32767:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Value must be a positive smallint.',
        )

    return value


def validate_not_none(value):
    if value is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{value} must not be None.',
        )

    return value


def validate_image(file: Optional[UploadFile] = None):
    if file is None:
        return None

    ext = file.filename.split('.')[-1].lower()
    print(ext)

    if ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid file type'
        )

    try:
        if ext == 'svg':
            # Validate SVG by parsing it as XML
            file.file.seek(0)
            ET.parse(file.file)
            file.file.seek(0)
        else:
            Image.open(file.file).verify()
            file.file.seek(0)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Corrupted or invalid image file'
        )

    return ext
