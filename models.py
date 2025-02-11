
# models.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Project:
    id: int
    name: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime

@dataclass
class Task:
    id: int
    project_id: int
    title: str
    description: str
    assignee: str
    status: str
    created_at: datetime
    updated_at: datetime