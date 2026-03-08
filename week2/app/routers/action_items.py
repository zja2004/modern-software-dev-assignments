from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException

from .. import db
from ..services.extract import extract_action_items, extract_action_items_llm
from pydantic import BaseModel

class ExtractRequest(BaseModel):
    text: str
    save_note: bool = False

class ActionItemResponse(BaseModel):
    id: int
    text: str

class ExtractResponse(BaseModel):
    note_id: Optional[int]
    items: List[ActionItemResponse]

class ActionItemFullResponse(BaseModel):
    id: int
    note_id: Optional[int]
    text: str
    done: bool
    created_at: str

class MarkDoneRequest(BaseModel):
    done: bool = True



router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract", response_model=ExtractResponse)
def extract(payload: ExtractRequest):
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.save_note:
        note_id = db.insert_note(text)

    items = extract_action_items(text)
    ids = db.insert_action_items(items, note_id=note_id)
    return ExtractResponse(note_id=note_id, items=[ActionItemResponse(id=i, text=t) for i, t in zip(ids, items)])


@router.post("/extract-llm", response_model=ExtractResponse)
def extract_llm(payload: ExtractRequest):
    """TODO 4: Added extract-llm endpoint."""
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.save_note:
        note_id = db.insert_note(text)

    items = extract_action_items_llm(text)
    ids = db.insert_action_items(items, note_id=note_id)
    return ExtractResponse(note_id=note_id, items=[ActionItemResponse(id=i, text=t) for i, t in zip(ids, items)])


@router.get("", response_model=List[ActionItemFullResponse])
def list_all(note_id: Optional[int] = None):
    return db.list_action_items(note_id=note_id)


@router.post("/{action_item_id}/done")
def mark_done(action_item_id: int, payload: MarkDoneRequest):
    db.mark_action_item_done(action_item_id, payload.done)
    return {"id": action_item_id, "done": payload.done}


