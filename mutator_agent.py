from typing import List, Dict
from pathlib import Path
from dataclasses import dataclass
from verifier import Referee, VerificationResult
from red_agent import VulnerabilityFinding

@dataclass
class MutatorResult:
    total_payloads: int
    blocked_payloads: int
    bypasses: List[str]

class MutatorAgent:
    """
    Deterministic MUTATOR Battery.
    Runs a fixed, curated list of payloads per vulnerability class to ensure
    the patch wasn't just overfitted to the specific payload used in the initial attack.
    """
    
    PAYLOADS = {
        "Hardcoded Secret": [], # Skip entirely, it's a presence check
        "SQL Injection": [
            "' OR '1'='1' -- ",
            "' OR 1=1#",
            "'/**/OR/**/1=1--"
        ],
        "Command Injection": [
            "; whoami",
            "$(whoami)",
            "`whoami`"
        ],
        "Path Traversal": [
            "../../etc/passwd",
            "../../../../etc/passwd",
            "..\\..\\windows\\system32\\drivers\\etc\\hosts",
            "%2e%2e%2fetc%2fpasswd",
            "....//....//etc/passwd",
            "/etc/passwd",
            "../../etc/passwd%00.png"
        ]
    }

    def __init__(self, referee: Referee):
        self.referee = referee

    def run_battery(self, patched_root: Path, finding: VulnerabilityFinding) -> MutatorResult:
        payloads = self.PAYLOADS.get(finding.vulnerability_type, [])
        if not payloads:
            return MutatorResult(total_payloads=0, blocked_payloads=0, bypasses=[])

        total = len(payloads)
        bypasses = []
        
        for payload in payloads:
            check = self.referee.verify_exploit(patched_root, finding, payload)
            if check.attack_succeeded:
                bypasses.append(payload)
                
        blocked = total - len(bypasses)
        return MutatorResult(total_payloads=total, blocked_payloads=blocked, bypasses=bypasses)
