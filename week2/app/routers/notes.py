from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import db


class NoteCreate(BaseModel):
    content: str

class NoteResponse(BaseModel):
    id: int
    content: str
    created_at: str

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteResponse)
def create_note(payload: NoteCreate):
    content = payload.content.strip()
    if not content:
        raise HTTPException(status_code=400, detail="content is required")
    note_id = db.insert_note(content)
    note = db.get_note(note_id)
    return note


@router.get("", response_model=List[NoteResponse])
def get_all_notes():
    """TODO 4: Added endpoint to retrieve all notes"""
    return db.list_notes()


@router.get("/{note_id}", response_model=NoteResponse)
def get_single_note(note_id: int):
    note = db.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


