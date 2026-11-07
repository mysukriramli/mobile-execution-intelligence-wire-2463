"""
Pydantic Data Schemas for Mobile Execution Intelligence Wire.
Global Edge Device, Connectivity, and Autonomous Execution Readiness Intelligence.
"""

from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from pydantic import BaseModel, Field


# ==========================================
# Domain Enums
# ==========================================

class WorkloadPlacement(str, Enum):
    EDGE_EXECUTION = "EDGE_EXECUTION"
    HYBRID_EXECUTION = "HYBRID_EXECUTION"
    CLOUD_ASSISTED = "CLOUD_ASSISTED"
    REMOTE_ONLY = "REMOTE_ONLY"


class MobileExecutionReadiness(str, Enum):
    UNUSABLE = "UNUSABLE"
    DEGRADED = "DEGRADED"
    LIMITED = "LIMITED"
    OPERATIONAL = "OPERATIONAL"
    OPTIMAL = "OPTIMAL"


class InfrastructureState(str, Enum):
    SPARSE = "SPARSE"
    BASIC = "BASIC"
    DEVELOPING = "DEVELOPING"
    ADVANCED = "ADVANCED"
    DENSE = "DENSE"


class ConnectivityState(str, Enum):
    POOR = "POOR"
    WEAK = "WEAK"
    STABLE = "STABLE"
    STRONG = "STRONG"
    EXCELLENT = "EXCELLENT"


# class AgentReadiness(str, Enum):
