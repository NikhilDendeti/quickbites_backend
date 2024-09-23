import typing
from qb_users.constants import *




class SpreadSheetUtil:

    def fetch_data_from_spreadsheet(
            self, SPREAD_SHEET_NAME: str, STUDENT_SUB_SHEET_NAME: str
    ) -> typing.List[typing.Dict]:
        return [
            {
                "student_id": "N23B1003",
                "name": "NIKHIL"
            },
            {
                "employee_id": "NW0001606",
                "name": "HARSH"
            }
        ]

