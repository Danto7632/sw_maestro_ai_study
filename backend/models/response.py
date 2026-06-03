from pydantic import BaseModel


class TermAnalysis(BaseModel):
    term: str
    context: str
    currentMeaning: str
    plannerView: str | None = None
    developerView: str | None = None
    designerView: str | None = None
    pmView: str | None = None
    riskLevel: str
    riskReason: str
    confirmationQuestion: str


class AnalyzeResponse(BaseModel):
    summary: str
    keyRequest: str
    terms: list[TermAnalysis]
    agreementQuestions: list[str]
    checklist: list[str]
