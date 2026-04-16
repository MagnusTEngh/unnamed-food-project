from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["test"])

TEST_MESSAGES = [
    {"message": "This is first message yes yes"},
    {"message": "This is the second message yes yes"},
]


@router.get("/")
def test_root():
    """This message is found at /api/test"""
    return {"message": "Test endpoint functional."}


@router.get("/message")
def get_test_messages():
    """This message is found at /api/test/message"""
    return {"content": TEST_MESSAGES}


@router.get("/message/{message_no}")
def get_specific_test_message(message_no):
    """This message is found at /api/test/message/your-int-here"""
    if message_no:
        return {"content": TEST_MESSAGES[int(message_no)]}

@router.get("/message/from")
def get_message_from():
    """This should be found at /api/test/message/from"""
    return {"Listen": "Someone wants to talk"}

@router.get("/message/from/thedan")
def get_message_from_daniel():
    """This should be found at /api/test/message/from/thedan"""
    return {"thedan": "You shall be doomed"}