from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class SheetRange:
    sheet_name: str
    start_cell: str
    end_cell: Optional[str] = None

@dataclass
class SheetReadRequest:
    spreadsheet_id: str
    range: SheetRange
    major_dimension: str = "ROWS"

@dataclass
class SheetReadResponse:
    values: List[List[str]]
    timestamp: datetime
    range: str

@dataclass
class SheetWriteRequest:
    spreadsheet_id: str
    range: SheetRange
    values: List[List[str]]
    major_dimension: str = "ROWS"

@dataclass
class SheetWriteResponse:
    updated_range: str
    updated_rows: int
    updated_columns: int
    updated_cells: int
    timestamp: datetime
