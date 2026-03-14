# -*- coding: utf-8 -*-
"""
core/paths.py -- Centralized path registry for Mega Brain
==========================================================

All intelligence scripts import path constants from here.
Paths resolve relative to the repository root (auto-detected).

Created during upstream sync smoke-test (2026-03-14).
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# Repository root (two levels up from core/paths.py)
# ---------------------------------------------------------------------------
WORKSPACE: Path = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Top-level directories
# ---------------------------------------------------------------------------
INBOX: Path = WORKSPACE / "inbox"
LOGS: Path = WORKSPACE / "logs"
DATA: Path = WORKSPACE / ".data"
ARTIFACTS: Path = WORKSPACE / "artifacts"
COMMANDS: Path = WORKSPACE / ".claude" / "commands"
MISSION_CONTROL: Path = WORKSPACE / ".claude" / "mission-control"

# ---------------------------------------------------------------------------
# Aliases
# ---------------------------------------------------------------------------
ROOT: Path = WORKSPACE  # alias used by some scripts

# ---------------------------------------------------------------------------
# Knowledge paths
# ---------------------------------------------------------------------------
KNOWLEDGE_EXTERNAL: Path = WORKSPACE / "knowledge"
KNOWLEDGE_PERSONAL: Path = WORKSPACE / "knowledge" / "personal"
KNOWLEDGE_BUSINESS: Path = KNOWLEDGE_EXTERNAL / "business"

# ---------------------------------------------------------------------------
# Personal sub-paths (bucket_processor)
# ---------------------------------------------------------------------------
PERSONAL_CALLS: Path = KNOWLEDGE_PERSONAL / "calls"
PERSONAL_COGNITIVE: Path = KNOWLEDGE_PERSONAL / "cognitive"
PERSONAL_EMAIL: Path = KNOWLEDGE_PERSONAL / "email"
PERSONAL_MESSAGES: Path = KNOWLEDGE_PERSONAL / "messages"

# ---------------------------------------------------------------------------
# Workspace sub-paths (bucket_processor)
# ---------------------------------------------------------------------------
WORKSPACE_AUTOMATIONS: Path = WORKSPACE / "workspace" / "automations"
WORKSPACE_FINANCE: Path = WORKSPACE / "workspace" / "finance"
WORKSPACE_MEETINGS: Path = WORKSPACE / "workspace" / "meetings"
WORKSPACE_ORG: Path = WORKSPACE / "workspace" / "org"
WORKSPACE_TEAM: Path = WORKSPACE / "workspace" / "team"
WORKSPACE_TOOLS: Path = WORKSPACE / "workspace" / "tools"

# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------
AGENTS: Path = WORKSPACE / "agents"
AGENTS_EXTERNAL: Path = WORKSPACE / "agents"
AGENTS_CARGO: Path = WORKSPACE / "agents" / "cargo"
AGENTS_BUSINESS: Path = WORKSPACE / "agents" / "business"

# ---------------------------------------------------------------------------
# RAG
# ---------------------------------------------------------------------------
RAG_INDEX: Path = DATA / "rag" / "index"
RAG_BUSINESS: Path = DATA / "rag" / "business"

# ---------------------------------------------------------------------------
# Business-specific
# ---------------------------------------------------------------------------
BUSINESS_INSIGHTS: Path = KNOWLEDGE_EXTERNAL / "insights"
BUSINESS_SOPS: Path = KNOWLEDGE_EXTERNAL / "sops"
BUSINESS_DECISIONS: Path = KNOWLEDGE_EXTERNAL / "business" / "decisions"
BUSINESS_DOSSIERS: Path = KNOWLEDGE_EXTERNAL / "business" / "dossiers"
BUSINESS_DRIVE: Path = KNOWLEDGE_EXTERNAL / "business" / "drive"
WORKSPACE_BUSINESSES: Path = WORKSPACE / "workspace" / "businesses"
WORKSPACE_STRATEGY: Path = WORKSPACE / "workspace" / "strategy"
WORKSPACE_TEMPLATES: Path = WORKSPACE / "workspace" / "templates"

# ---------------------------------------------------------------------------
# ROUTING: path registry for scripts that need configurable destinations.
# Scripts use ROUTING.get("key", fallback) so missing keys are non-fatal.
# ---------------------------------------------------------------------------
ROUTING: dict[str, Path] = {
    # Inbox variants
    "external_inbox": KNOWLEDGE_EXTERNAL / "external" / "inbox",
    "personal_inbox": KNOWLEDGE_PERSONAL / "inbox" if KNOWLEDGE_PERSONAL.exists() else DATA / "personal-inbox",
    "business_inbox": KNOWLEDGE_EXTERNAL / "business" / "inbox",
    "business_people": KNOWLEDGE_EXTERNAL / "business" / "people",
    "workspace_inbox": INBOX,

    # Batch / pipeline
    "batch_log": LOGS / "batches",
    "batch_registry": MISSION_CONTROL / "BATCH-REGISTRY.json",
    "batch_auto_creator_log": LOGS / "batch-auto-creator.jsonl",

    # MCE Pipeline
    "mce_state": MISSION_CONTROL / "mce",
    "mce_cache": DATA / "mce_cache",
    "mce_metrics_log": LOGS / "mce-metrics.jsonl",

    # Read AI
    "read_ai_log": LOGS / "read-ai.jsonl",
    "read_ai_state": MISSION_CONTROL / "read-ai-state.json",
    "read_ai_staging": DATA / "read-ai-staging",

    # Inbox watcher
    "watcher_state": MISSION_CONTROL / "watcher-state.json",
    "watcher_log": LOGS / "watcher.jsonl",

    # Workspace sync
    "workspace_sync_log": LOGS / "workspace-sync.jsonl",
}
