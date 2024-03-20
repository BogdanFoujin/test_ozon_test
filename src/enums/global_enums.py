from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recived status code is not equal to excepted."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to excepted."