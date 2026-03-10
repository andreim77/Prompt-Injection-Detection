PROMPT INJECTION DETECTION WITH TOOL BOUNDARY

== Overview

This project demonstrates a simple mitigation for prompt injection attacks in Retrieval-Augmented Generation (RAG) systems.

In RAG systems, an AI agent retrieves documents from a knowledge base (KB) to help answer user queries. However, retrieved documents may contain malicious instructions designed to manipulate the agent.

This demo shows how to treat retrieved KB content as untrusted data, detect potential prompt injection, and prevent unsafe tool execution.

---

== Approach and Reasoning

The key design principle is enforcing a trust hierarchy:

System / Agent Logic (trusted) >
User Input (semi-trusted) >
Retrieved KB Content (untrusted)

Retrieved KB content is treated strictly as data, not instructions.

## Security Principle

Privileged actions must never be triggered by untrusted data.
The source of the instruction determines whether an action is allowed, not the severity of the action itself.
---

== Detection Strategy

To keep the solution simple and intentional, the implementation uses 'rule-based detection' of suspicious phrases commonly used in prompt injection attacks, such as:

- "ignore prior instructions"
- "call create_ticket"

If such patterns appear in retrieved content:

1. A security event is logged.
2. Tool execution is blocked.

This prevents untrusted KB data from triggering privileged actions.

---

== Implementation

The project consists of three small components:

## agent.py

Contains:

- agent logic
- prompt injection detection
- security event logging
- enforcement of the tool boundary

## tools.py

Defines the privileged tool used in the demo:

- create_ticket(priority)

### kb.py

Simulates knowledge base retrieval results with two documents:

- a benign document
- a malicious document containing a prompt injection

---
== Tradeoffs

This implementation intentionally keeps the solution minimal and easy to reason about.
- Rule-based detection: The agent detects prompt injection using simple pattern matching. This keeps the implementation clear, but it would not catch all possible attack variations.
- Limited KB simulation: The knowledge base is simulated with two documents for clarity rather than a full retrieval pipeline.
- Single tool example: Only one privileged tool (`create_ticket`) is implemented to demonstrate the tool boundary principle.
The goal of this demo is to clearly illustrate the security reasoning and tool boundary principle, rather than build a full production defense system.

---

== Running the Demo

Run the script with:

python agent.py

The agent will demonstrate both:

1. a benign KB scenario
2. a malicious prompt injection scenario
