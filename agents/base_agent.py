from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.findings = []

    @abstractmethod
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the input data and return findings
        """
        pass

    def add_finding(self, finding: Dict[str, Any]):
        """
        Add a finding to the agent's collection
        """
        self.findings.append(finding)

    def get_findings(self) -> List[Dict[str, Any]]:
        """
        Return all findings from this agent
        """
        return self.findings

    def clear_findings(self):
        """
        Clear all findings
        """
        self.findings = []
