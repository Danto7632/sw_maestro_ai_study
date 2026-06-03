from fastapi import APIRouter, HTTPException
from models.request import AnalyzeRequest
from models.response import AnalyzeResponse
from workflow.graph import workflow

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(body: AnalyzeRequest):
    try:
        # receiverRole을 콤마로 분리해 리스트로 변환
        receiver_roles = [r.strip() for r in body.receiverRole.split(",") if r.strip()]

        result = await workflow.ainvoke({
            "input_text": body.text,
            "sender_role": body.senderRole,
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
