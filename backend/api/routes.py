from fastapi import APIRouter, HTTPException
from models.request import AnalyzeRequest
from models.response import AnalyzeResponse
from workflow.graph import workflow

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(body: AnalyzeRequest):
    try:
        # 첫 번째 참여자 = 발화자, 나머지 = 수신자
        sender_role = body.participants[0].role
        receiver_roles = [p.role for p in body.participants[1:]]

        result = await workflow.ainvoke({
            "input_text": body.text,
            "sender_role": sender_role,
            "receiver_roles": receiver_roles,
            "communication_type": body.communicationType,
            "role_interpretations": [],
        })
        return result["final_report"]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="분석 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.",
        )
