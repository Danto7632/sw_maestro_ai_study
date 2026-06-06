export type RouteType =
  | "consensus_report"
  | "need_more_context"
  | "definition_enrichment";

export type AnalyzeRequest = {
  text: string;
  senderRole: string;
  receiverRole: string;
  communicationType: string;
};

export type TermAnalysis = {
  term: string;
  context: string;
  currentMeaning: string;
  plannerView: string | null;
  developerView: string | null;
  designerView: string | null;
  pmView: string | null;
  riskLevel: "낮음" | "보통" | "높음" | string;
  riskReason: string;
  confirmationQuestion: string;
};

export type AnalyzeResponse = {
  summary: string;
  keyRequest: string;
  terms: TermAnalysis[];
  agreementQuestions: string[];
  checklist: string[];
  route?: RouteType;
  message?: string;
};

export type AnalysisHistoryItem = {
  id: string;
  summary: string;
  keyRequest: string;
  senderRole: string;
  createdAt: string;
};

export type TestCase = {
  id: string;
  scenarioName: string;
  primaryUser: string;
  route: RouteType;
  request: AnalyzeRequest;
  response: AnalyzeResponse;
};

export type AnalyzeState = "idle" | "loading" | "success" | "error";

export type AppPage = "analyze" | "history";
