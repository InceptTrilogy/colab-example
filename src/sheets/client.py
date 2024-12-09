from datetime import datetime
from typing import Any, Dict, List

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from .models import (
    SheetRange,
    SheetReadRequest,
    SheetReadResponse,
    SheetWriteRequest,
    SheetWriteResponse,
)

class GoogleSheetsClient:
    def __init__(self, credentials: Credentials) -> None:
        # Type hint as Any since the service object structure is dynamic
        self.service: Any = build("sheets", "v4", credentials=credentials)

    def _format_range(self, range_obj: SheetRange) -> str:
        if range_obj.end_cell:
            return f"'{range_obj.sheet_name}'!{range_obj.start_cell}:{range_obj.end_cell}"
        return f"'{range_obj.sheet_name}'!{range_obj.start_cell}"

    def read(self, request: SheetReadRequest) -> SheetReadResponse:
        range_str = self._format_range(request.range)
        result: Dict[str, Any] = self.service.spreadsheets().values().get(
            spreadsheetId=request.spreadsheet_id,
            range=range_str,
            majorDimension=request.major_dimension,
        ).execute()

        return SheetReadResponse(
            values=result.get("values", []),
            timestamp=datetime.now(),
            range=result["range"],
        )

    def write(self, request: SheetWriteRequest) -> SheetWriteResponse:
        range_str = self._format_range(request.range)
        body = {
            "values": request.values,
            "majorDimension": request.major_dimension,
        }
        
        result: Dict[str, Any] = self.service.spreadsheets().values().update(
            spreadsheetId=request.spreadsheet_id,
            range=range_str,
            valueInputOption="RAW",
            body=body,
        ).execute()

        return SheetWriteResponse(
            updated_range=result["updatedRange"],
            updated_rows=result["updatedRows"],
            updated_columns=result["updatedColumns"],
            updated_cells=result["updatedCells"],
            timestamp=datetime.now(),
        )
